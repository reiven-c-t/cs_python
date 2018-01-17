# Git&Githubについて

こちらのページの入門編/発展編/プルリクエスト編を一通り見ておいてください。
流し見で十分です。
Git/Githubに関しては、インストールの時に一緒に少しやりますが、少し目を通しておいていただければ
理解が深まるかと思いますので、時間があれば見ておいてください。


- <https://www.backlog.jp/git-guide/intro/intro1_1.html>

## 基本用語

- repository: gitのバージョンコントロールデータそのもの
- branch: 自分の変更(バージョン)を記録するrepositoryの一部
- commit: 自分の変更を自分のパソコン内の自分のbranchに記録する方法
- pull: ネットワーク上のgit repositoryのmasterブランチ(メインブランチ)の内容を自分のPCに取り込むこと
- push: 自分のパソコンのgit repositoryの変更ををネットワーク上のgitに反映させること
- pull request: ネットワーク上のgitにて、自分のbranchの変更をmaster branchに反映させること
- coflict: 衝突。githubのorigin/masterと自分のコードが重複するとおこる。
- (merge)

## おまじない

PyCharmを立ち上げたらgit pull!
push(またはcommit and push)前にはgit pull!
pull request前にはgit pull!
三度の飯よりgit pull!


## おすすめアプリ

iPhone/iPadで使えるgithubクライアントがあったので紹介します。

何度も言うように、人がorigin/masterを更新した際はできるだけ早く、pullするべき。
そのためには、常に(特に作業開始から作業中)githubのリポジトリのコミット履歴を追跡しておきたい。

なので、作業時に、PCの側に携帯を置いといて、そこにgithubのブランチ状況を常に表示しておくと
PCの画面を割くことが減って便利かと思います。
後、多分、iPhone/iPadからPull request処理ができると便利じゃね?とも思います(試してないけど)

- iPhone/iPad: <http://codehub-app.com/>
- Androidはググって: <https://www.google.com/search?q=github+android+アプリ> 

## Gitの作業フローについての基本事項

- gitは作業履歴を保存(&共有)する、バージョン管理システムというツールである。
- gitはリポジトリという単位でプロジェクト(cs_pythonみたいな企画とか)を管理する
- リポジトリは木構造である。自分の記録のための枝(branch)を作り、そこに変更を記録していく。
- ファイルをgitリポジトリにaddすることでリポジトリに登録できる
- gitはリポジトリに登録されたファイルの履歴を管理する(**重要:リポジトリに登録されてないファイルは記録しない**)
- gitにリポジトリにファイルの変更をcommitすることでファイルの変更を記録できる
- githubはネットワーク上でgitのリポジトリを管理・共有するためのサービスである
- github上のリポジトリと自分のPC内のリポジトリをpullなどで同期できる。同期することで、作業状況の記録を共有できる。
- github上で、自分のbranchでの変更を本流のbranchに結合(merge)することで、作業内容を全員と共有できる
- github上でmergeするためにpull requestをする。

## 作業についての基本事項(再確認)

1. 作業前には必ずpull!
2. commit/push、pull requestをする前に必ずpull!
3. ある程度目処がたったら(関数を1つ定義し終えたとか、全ての関数の名前を決めたくらいでも良い)とりあえずcommit & push
4. 3のとき、commit/pushする前にpull!(大事なので2度言います)
5. 3のとき、commit/pushする前にpull!(大事なので2度言った)
6. commit/pushのコメントは後述する規則に従う。

## commit/pushコメントの規則

>人はなぜ、commit/pushをするのか。それは、争いをなくすためである。
Akifumi Nakamachi(1994~)

さて、commit/pushについてだけども、commit/pushをする理由は、
コードに履歴をつけながらコードを保存し、その履歴を皆で共有するためである。

commit/pushをする時点で、日付や保存した人の情報は登録されるので、
commit/pushのコメントに日付や作業者を書く必要はない。

では、何をコメントに書くか。
それは、そのcommit/pushがどういう作業を保存するためのcommit/pushなのか、
そのcommit/pushをその時点でcommit/pushした理由はなんなのか、
これを書くべきである。

プログラム(ソフトウェア)作成において、代表的な作業例として、

- 作成(create)
- 更新(update)
- 修正(fix)
- 削除(delete)
- コメント添付(comment)
- そのた追加(add)

が考えられる。これらをコメントとして明示ことでcommit/pushが
コードの履歴としてわかりやすくなるだろう。
cs_pythonにおいては、これらの作業例のラベルを用いる。

### 何かファイルを作ったとき

[create] 作業についてのコメント

と書く。必ず[create] と書くことをを忘れない。

例:(例:足し算のコードを確認するためのtest.pyをakiフォルダに作成したとき)

[create] コード確認のためのaki/test.py

のようにかく。大事なことは、[create] コメント!

### ファイルに内容を追加したとき

[update] 作業についてのコメント

と書く。必ず[update] と書くことをを忘れない。

### ファイルの内容を修正したとき

[fix] 作業についてのコメント

と書く。必ず[fix] と書くことをを忘れない。

### ファイルを削除したとき

[delete] 作業についてのコメント

と書く。必ず[delete] と書くことをを忘れない。

### ファイルにコメントなどの、実行に関係ないメモを添付したとき

[comment] 作業についてのコメント

と書く。必ず[comment] と書くことをを忘れない。


### 上の分類に当てはまらないような追加をしたとき

[add] 作業についてのコメント

と書く。必ず[add] と書くことをを忘れない。


## その他PyCharmでのgit利用について

困ったらメニューバーのVCSのgit項目に基本的なのは全部ある。
(add/pull/push/pull request)

あるいは、shift3連打で検索検索ぅ
