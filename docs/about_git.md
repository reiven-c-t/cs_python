# Git&Githubについて

こちらのページの入門編/発展編/プルリクエスト編を一通り見ておいてください。
流し見で十分です。
Git/Githubに関しては、インストールの時に一緒に少しやりますが、少し目を通しておいていただければ
理解が深まるかと思いますので、時間があれば見ておいてください。


- <https://www.backlog.jp/git-guide/intro/intro1_1.html>

- repository: gitのバージョンコントロールデータそのもの
- branch: 自分の変更(バージョン)を記録するrepositoryの一部
- commit: 自分の変更を自分のパソコン内の自分のbranchに記録する方法
- pull: ネットワーク上のgit repositoryのmasterブランチ(メインブランチ)の内容を自分のPCに取り込むこと
- push: 自分のパソコンのgit repositoryの変更ををネットワーク上のgitに反映させること
- pull request: ネットワーク上のgitにて、自分のbranchの変更をmaster branchに反映させること
- coflict: 衝突。
- (merge)

## おまじない

PyCharmを立ち上げたらgit pull!
push(またはcommit and push)前にはgit pull!
pull request前にはgit pull!
三度の飯よりgit pull!


### おすすめアプリ

iPhone/iPadで使えるgithubクライアントがあったので紹介します。

何度も言うように、人がorigin/masterを更新した際はできるだけ早く、pullするべき。
そのためには、常に(特に作業開始から作業中)githubのリポジトリのコミット履歴を追跡しておきたい。

なので、作業時に、PCの側に携帯を置いといて、そこにgithubのブランチ状況を常に表示しておくと
PCの画面を割くことが減って便利かと思います。
後、多分、iPhone/iPadからPull request処理ができると便利じゃね?とも思います(試してないけど)

- iPhone/iPad: <http://codehub-app.com/>
- Androidはググって: <https://www.google.com/search?q=github+android+アプリ> 
