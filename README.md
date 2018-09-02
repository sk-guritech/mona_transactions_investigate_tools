# Mona Transactions Investigate Tools

### Files
- get_specific_address_transactions.py  
  特定のアドレスのトランザクションを取得しファイルに保存。
- analyzer.py  
  トランザクションを保存したファイルから、記載されているアドレスのリストと簡易的なマネーフローのリストを出力してくれる。
---
### How To Use
`python3 get_specific_address_transactions.py [address] [max_page_num]`  
（max_page_numを省略した場合は100に設定）  
  
`python3 analyzer.py [address]`  
（先にget_specific_address_transactions.pyでトランザクションのJSONを取得してから）  
