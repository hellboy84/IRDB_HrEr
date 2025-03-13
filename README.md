# IRDB_HrEr
IRDBのハーベストエラーの結果ファイル(デフォルト：contents.csv)に含まれるエラーパターン種類と各エラーパターン件数のカウント用のPythonファイルです。

- 「IRDB_error_analysis.py」と同じフォルダにエラーファイルをおいて，pyを実行してください。
- エラーファイルは複数あっても大丈夫です。名前を変更しても大丈夫です。
- 結果は以下のような内容で「error_analysis_result.txt」として同じフォルダに出力されます。
- 以下のエラーは例です。これ以外のエラーも抽出されます。
- このコードのエラーパターンの抽出やカウントが完璧であることを保証するものではありません。
- このコードの作成は生成AIのサポートを受けています。

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

