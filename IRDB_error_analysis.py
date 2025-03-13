import os
import csv
import re
from collections import defaultdict

def extract_error_patterns(message):
    """エラーメッセージからエラーパターンを抽出する関数"""
    patterns = []
    
    # 項目登録エラー、ワーニング、項目変換のマーカーを定義
    markers = [
        "　● 項目登録エラー：",
        "　● ワーニング：",
        "　● 項目変換："
    ]
    
    # 各マーカーごとにパターンを抽出
    for marker in markers:
        if marker in message:
            # マーカーがある行を特定
            marker_lines = [line.strip() for line in message.split('\n') if marker in line]
            
            for line in marker_lines:
                # その行以降の行（エラー詳細）を取得
                start_idx = message.find(line)
                next_marker_idx = float('inf')
                for m in markers:
                    next_m_idx = message.find(m, start_idx + len(line))
                    if next_m_idx > -1 and next_m_idx < next_marker_idx:
                        next_marker_idx = next_m_idx
                
                if next_marker_idx == float('inf'):
                    detail_text = message[start_idx + len(line):].strip()
                else:
                    detail_text = message[start_idx + len(line):next_marker_idx].strip()
                
                # 空行を削除し、各行を分析
                detail_lines = [l.strip() for l in detail_text.split('\n') if l.strip()]
                for detail in detail_lines:
                    # [...] パターンを探す
                    pattern_match = re.search(r'\[(.*?)\](.*?)(?:\(|$)', detail)
                    if pattern_match:
                        category = pattern_match.group(1).strip()
                        desc = pattern_match.group(2).strip()
                        error_type = marker.replace("　● ", "").replace("：", "")
                        # エラータイプ、カテゴリ、詳細説明をパターンとして格納
                        # 括弧内の情報は無視する
                        patterns.append((error_type, category, desc))
    
    return patterns

def get_script_path():
    """実行環境に応じて適切なスクリプトパスを取得する関数"""
    try:
        # 通常のPythonスクリプト実行時
        return os.path.dirname(os.path.abspath(__file__))
    except NameError:
        # Jupyter Notebook等の対話型環境での実行時
        return os.path.abspath('')

def collect_errors_data():
    """スクリプトと同じディレクトリからエラーデータを収集する関数"""
    # スクリプトファイルのディレクトリを使用
    script_dir = get_script_path()
    
    # OAI-IDごとのエラーパターンを記録
    oai_id_patterns = defaultdict(set)
    
    print(f"{script_dir} からデータを収集中...")
    
    # ディレクトリ内のすべてのCSVファイルを処理
    csv_files = [f for f in os.listdir(script_dir) if f.endswith('.csv')]
    
    if not csv_files:
        print("CSVファイルが見つかりませんでした。")
        return oai_id_patterns
    
    for filename in csv_files:
        filepath = os.path.join(script_dir, filename)
        print(f"処理中: {filename}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                csv_reader = csv.reader(f)
                try:
                    next(csv_reader)  # ヘッダー行をスキップ
                except StopIteration:
                    continue  # 空のファイルの場合はスキップ
                
                for row in csv_reader:
                    if len(row) >= 6:  # 少なくとも6列あるか確認
                        oai_id = row[0]
                        message = row[5]
                        
                        # エラーパターンを抽出
                        patterns = extract_error_patterns(message)
                        for pattern in patterns:
                            error_key = f"{pattern[0]} - [{pattern[1]}] {pattern[2]}"
                            # OAI-IDごとにユニークなエラーパターンを記録
                            # setを使用しているので自動的に重複は排除される
                            oai_id_patterns[oai_id].add(error_key)
        except Exception as e:
            print(f"ファイル {filename} の処理中にエラーが発生しました: {e}")
    
    print(f"合計 {len(csv_files)} 個のCSVファイルから {len(oai_id_patterns)} 個のユニークなOAI-IDを抽出しました。")
    return oai_id_patterns

def main():
    # OAI-IDごとのエラーパターンを収集
    oai_id_patterns = collect_errors_data()
    
    # 重複を排除してエラーパターンをカウント
    error_counts = defaultdict(int)
    
    # 各OAI-IDのユニークなエラーパターンを集計
    for oai_id, patterns in oai_id_patterns.items():
        for error_key in patterns:
            error_counts[error_key] += 1
    
    # 結果をファイルに出力
    script_dir = get_script_path()
    output_file = os.path.join(script_dir, "error_analysis_result.txt")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("===== エラーパターン別の集計 =====\n\n")
        
        # エラーカテゴリーごとのグループ分け
        categories = {
            "項目登録エラー": [],
            "ワーニング": [],
            "項目変換": []
        }
        
        # エラーをカテゴリー別に分類
        for error_key, count in error_counts.items():
            for category in categories.keys():
                if error_key.startswith(category):
                    categories[category].append((error_key, count))
        
        # カテゴリーごとに出力
        for category_name, errors in categories.items():
            if errors:
                f.write(f"■ {category_name}\n")
                sorted_errors = sorted(errors, key=lambda x: (-x[1], x[0]))
                for error_key, count in sorted_errors:
                    f.write(f"{error_key}: {count}件\n")
                f.write("\n")
    
    print(f"エラー解析が完了しました。結果は {output_file} に保存されました。")
    print(f"合計 {len(oai_id_patterns)} 個のユニークなOAI-IDから {sum(error_counts.values())} 件のエラーパターンを集計しました。")

if __name__ == "__main__":
    main()
