# Mona Transactions Investigate Tools

### How To Use
`python3 mona_researcher.py [address]`  
  
特定のアドレスに関するトランザクションを全部取得し、全トランザクションの保存、関連するアドレスのリスト作成、マネーフローグラフの作成をすべて一気に行います。  
調査結果はResearchResult/[address]に保存されます。  
  
### Requirements
* requests
* pydot