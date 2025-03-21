import os
import re
from collections import defaultdict

def extract_record_errors_from_txt(file_path):
    """テキストファイルからレコードエラーのパターンを抽出する関数"""
    patterns = []
    
    try:
        # まずShift-JISで試し、エラーならUTF-8で開く
        try:
            with open(file_path, 'r', encoding='shift_jis') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        
        # テキストを「■ 該当アイテムのURL」でブロックに分割
        blocks = content.split("■ 該当アイテムのURL")
        
        # ブロックごとに処理（最初のブロックは空またはヘッダーなのでスキップ）
        for block in blocks[1:]:
            if "　● レコードエラー：" in block:
                # レコードエラー行を抽出
                for line in block.split('\n'):
                    if "[" in line and "]" in line:
                        # [...] パターンを探す
                        pattern_match = re.search(r'\[(.*?)\](.*?)(?:\(|$)', line)
                        if pattern_match:
                            category = pattern_match.group(1).strip()
                            desc = pattern_match.group(2).strip()
                            patterns.append((category, desc))
        
        return patterns
    
    except Exception as e:
        print(f"ファイル {file_path} の処理中にエラーが発生しました: {e}")
        return []

def get_script_path():
    """実行環境に応じて適切なスクリプトパスを取得する関数"""
    try:
        # 通常のPythonスクリプト実行時
        return os.path.dirname(os.path.abspath(__file__))
    except NameError:
        # Jupyter Notebook等の対話型環境での実行時
        return os.path.abspath('')

def main():
    # スクリプトと同じディレクトリを使用
    script_dir = get_script_path()
    
    print(f"{script_dir} からレコードエラーを収集中...")
    
    # スクリプトと同じディレクトリ内のテキストファイルを処理
    txt_files = [f for f in os.listdir(script_dir) if f.endswith('.txt') and f != "error_analysis_result_recorderror.txt"]
    
    if not txt_files:
        print("テキストファイルが見つかりませんでした。")
        return
    
    # レコードエラーパターンをカウント
    error_counts = defaultdict(int)
    
    # テキストファイルの処理
    for filename in txt_files:
        filepath = os.path.join(script_dir, filename)
        print(f"処理中: {filename}")
        
        # ファイルからレコードエラーを抽出
        patterns = extract_record_errors_from_txt(filepath)
        print(f"  {len(patterns)} 件のレコードエラーパターンを抽出しました。")
        
        # エラーパターンをカウント
        for category, desc in patterns:
            error_key = f"[{category}] {desc}"
            error_counts[error_key] += 1
    
    # 結果をファイルに出力
    output_file = os.path.join(script_dir, "error_analysis_result_recorderror.txt")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("===== レコードエラーパターン別の集計 =====\n\n")
        
        if error_counts:
            # 件数順に並べ替えてから出力
            sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))
            for error_key, count in sorted_errors:
                f.write(f"レコードエラー - {error_key}: {count}件\n")
        else:
            f.write("レコードエラーは見つかりませんでした。\n")
    
    print(f"レコードエラー解析が完了しました。結果は {output_file} に保存されました。")
    print(f"合計 {len(txt_files)} 個のファイルから {sum(error_counts.values())} 件のレコードエラーパターンを集計しました。")

if __name__ == "__main__":
    main()