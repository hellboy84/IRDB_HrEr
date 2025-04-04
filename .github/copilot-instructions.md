## Premise
- CSV files containing error messages returned from a target database during the harvesting of institutional repository data are available.
- The error messages are not strictly structured, making it difficult to understand the patterns and frequencies of occurrences.
- Therefore, we would like to extract the content using Python, analyze the error patterns, and understand the frequency of each occurrence.
## Error File Content Description
- The CSV file is delimited by commas ",".
- The error messages to be extracted and analyzed are described in the 6th column "メッセージ(Message)" of each data entry.
- Error messages can be broadly classified into three categories: "項目登録エラー(Item Registration Error)", "ワーニング(Warning)", and "項目変換(Item Conversion)".
- Within these categories, there are more specific error patterns that follow in brackets [...]. The examples below are just excerpts.
- Error message patterns include but are not limited to:
    - 項目登録エラー：対象項目のみ削除されてアイテムがIRDBに登録されています。
        - [出版者] 言語に規定値以外の値が設定されています。 (ja-Latn)
        - [タイトル] 言語に規定値以外の値が設定されています。 (ja-Latn)
    - ワーニング：対象項目のワーニングです。対応項目を含めてアイテムはIRDBに登録されています。
        - [博士論文] 本文URL(全文)がないため、博士論文提出チェックは実行されませんでした。
    - 項目変換：対象項目を置換しました。対応項目を含めてアイテムはIRDBに登録されていますが、データ修正をお願いします。
        - [作成者姓名] 既定の値に変換しました。 (--- -gt; )
## Aggregation Method
- We want to count these error messages by patterns such as [出版者] to understand the frequency of each pattern.
    - Please omit the content in parentheses () in the error messages.
    - Example: For "[主題] subjectSchemeは必須です。(gastric cancer)", the part "(gastric cancer)" is unnecessary.
- The identifier for each data entry is stored in the 1st column as "oai:toho.repo.nii.ac.jp:02003940".
- If the same oai-id appears across multiple files, please count it only once to avoid duplication.
## Output Method
- Please output the error analysis and count results to a text file. There is no specific format requirement for the file.

## 前提
- 機関リポジトリでデータをハーベストさせた際に，ハーベスト先のデータべースから返されたエラーメッセージを含むファイルがcsv形式で用意されています。
- エラーメッセージは厳密に構造化されておらず，パターンや発生数を把握することが難しいです。
- そこでPythonを用いて内容を切り出し，エラーパターンを解析し，各件数を把握したいです。
## エラーファイルの内容説明
- csvファイルはカンマ「,」で区切られています。
- 切り出して解析したいエラーメッセージは各データの6列目の「メッセージ」に記述されています。
- エラーメッセージは大きく分けると，「項目登録エラー」「ワーニング」「項目変換」の3つに分類できます。
- その中に更に[]に続いて以下の例のようにエラーパターンの細部が続きます。これはあくまで抜粋です。
- エラーメッセージのパターンは以下の他にも存在します。
    - 項目登録エラー：対象項目のみ削除されてアイテムがIRDBに登録されています。
        - [出版者] 言語に規定値以外の値が設定されています。 (ja-Latn)
        - [タイトル] 言語に規定値以外の値が設定されています。 (ja-Latn)
    - ワーニング：対象項目のワーニングです。対応項目を含めてアイテムはIRDBに登録されています。
        - [博士論文] 本文URL(全文)がないため、博士論文提出チェックは実行されませんでした。
    - 項目変換：対象項目を置換しました。対応項目を含めてアイテムはIRDBに登録されていますが、データ修正をお願いします。
　　    - [作成者姓名] 既定の値に変換しました。 (--- -gt; )
## 集計方法
- このようなエラーメッセージを，[出版者] などのパターンごとにカウントして，各パターンの発生数を把握したいです。
    - ただしエラーメッセージ内の()は省略して下さい。
    - 例：「[主題] subjectSchemeは必須です。(gastric cancer)」の場合(gastric cancer)部分は不要。
- 各データの番号は1列目に「oai:toho.repo.nii.ac.jp:02003940」として格納されています。
- ファイル間で同じoai-idが出現する場合は，重複しないように1回のみカウントしてください。
## 結果の出力方法
- エラー解析してカウントした結果はtxtファイルに出力してください。ファイル形式に特定の指定はありません。

