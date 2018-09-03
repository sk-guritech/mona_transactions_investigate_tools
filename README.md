# Mona Transactions Investigate Tools

### Useage
`python3 mona_researcher.py [address]`  
  特定のアドレスに関するトランザクションを全部取得し、全トランザクションの保存、関連するアドレスのリスト作成、マネーフローグラフの作成をすべて一気に行います。  調査結果はResearchResult/[address]に保存されます。  
  
`python3 mona_researcher.py [address] -r [recursive_max_time]`  
最初に設定したアドレスの調査が終わったあと、その時取得した関連するアドレスに対して更に調査を行う。そのまた更に取得した関連アドレスに対して調査を行う。recursive_max_time によって再帰回数が決定される（省略時は2(最初のアドレスと、そのアドレスに関連したアドレスに対して)が設定される）。  
  
`python3 mona_researcher.py [address] -f`  
addressは既に調査結果が出力されたものを入力してください。入力したアドレスの関連アドレスリストに対して調査を行います。  
  
`python3 mona_researcher.py [address] -f -r [recursive_max_time]`  
関連アドレスリストに対して調査を行い、更に出力された関連アドレスに対しても調査を行います。設定した再帰回数に到達するまで再帰的に調査を行います。

### Requirements
* requests
* pydot

### Author
https://twitter.com/GuriTech