# IRDB_HrEr
[IRDB](https://irdb.nii.ac.jp/)のハーベストエラーファイルからエラーパターンごとの件数をカウントするPythonコードです。

## 更新
- 20250321：[レコードエラー(登録エラー)のパターンを分析するコード](https://github.com/hellboy84/IRDB_HrEr/blob/main/IRDB_error_analysis_recorderror.py)を追加しました
- 20250313：[項目エラー系のパターンを分析するコード](https://github.com/hellboy84/IRDB_HrEr/blob/main/IRDB_error_analysis.py)をJupyterNotebook等の対話型実行環境でも動くように修正しました

## 使い方
- Python 3.6以上が動作する環境でお使いください。
#### 「レコードエラー(登録エラー)」の場合
- NIIから送られてくる？レコードエラーのファイル(xxx.txt(SJIS))を用意します。
- [「IRDB_error_analysis_recorderror.py」](https://github.com/hellboy84/IRDB_HrEr/blob/main/IRDB_error_analysis_recorderror.py)と同じフォルダにエラーファイル(txt)をおいて，pyを実行してください。
#### 「項目エラー・ワーニング・項目変換」の場合
- [IRDB](https://irdb.nii.ac.jp/)にログインし，[マイコンテンツ](https://irdb.nii.ac.jp/usercontents)からエラーファイル(contents.csv(UTF-8))を取得してください。
- [「IRDB_error_analysis.py」](https://github.com/hellboy84/IRDB_HrEr/blob/main/IRDB_error_analysis.py)と同じフォルダにエラーファイル(csv)をおいて，pyを実行してください。
- エラーファイル(csv)は複数あっても大丈夫です。名前を変更しても大丈夫です。

## 動作内容
- 結果は以下のような内容で「error_analysis_result_recorderror.txt」(レコードエラーの場合)あるいは「error_analysis_result.txt」(項目エラー系の場合)として同じフォルダに出力されます。
- 以下のエラーは例です。これ以外のエラーも抽出されます。
- 項目エラー系でファイル間でoai-idが重複している場合，重複は削除して計算されます。
- このコードは，予め用意したエラーパターンに合致したものを数えるのではなく，ファイルを確認してエラー報告の構造[...]を持っているものを抽出します。
- このコードのエラーパターンの抽出やカウントが完璧であることを保証するものではありません。
- このコードの作成は生成AIのサポートを受けています。
    - initial instruction is at https://github.com/hellboy84/IRDB_HrEr/blob/main/.github/copilot-instructions.md

===== エラーパターン別の集計 =====    
    
■ 項目登録エラー  
項目登録エラー - [タイトル] 言語に規定値以外の値が設定されています。: 件  
項目登録エラー - [主題] subjectSchemeは必須です。: 件  
項目登録エラー - [関連情報] 10桁の数字以外の値が設定されています。: 件  
項目登録エラー - [内容記述] 内容種別が設定されていません。: 件  
項目登録エラー - [作成者姓名] 言語が重複しています: 件  
項目登録エラー - [作成者姓名] 日本語が設定されていません。: 件  
項目登録エラー - [関連情報] prefixの形式が不正です。: 件  
項目登録エラー - [日付] 日付種別が設定されていません。: 件  
  
■ ワーニング  
ワーニング - [博士論文] 本文URL: 件  
ワーニング - [出版タイプ] 出版タイプに値が設定されていません。: 件  
ワーニング - [作成者姓名] 言語が未設定です。: 件  
  
■ 項目変換  
項目変換 - [作成者姓名] 既定の値に変換しました。: 件  

