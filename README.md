# band_calc
---

- ### How to settup the git environment
    1. First, register to git.
        ```
        git config --global user.name "ユーザー名"
        git config --global user.email メールアドレス
        ```
        See here →  [Git でユーザー名とメールアドレスを設定する方法（全体用とプロジェクト用）](https://laboradian.com/set-git-user-and-email/#:~:text=Git%20%E3%81%A7%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E5%90%8D%E3%81%A8%E3%83%A1%E3%83%BC%E3%83%AB%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9%E3%82%92%E8%A8%AD%E5%AE%9A%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95%EF%BC%88%E5%85%A8%E4%BD%93%E7%94%A8%E3%81%A8%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E7%94%A8%EF%BC%89%201%201.%20%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%82%92%E3%81%BE%E3%81%9F%E3%81%84%E3%81%A0%E5%85%A8%E4%BD%93%E3%81%AE%E8%A8%AD%E5%AE%9A%EF%BC%88%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%2C%20global%EF%BC%89%20%E3%81%9D%E3%81%AE%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%20git,%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E3%81%AB%E7%A7%BB%E5%8B%95%E3%81%97%E3%81%BE%E3%81%99%E3%80%82%20cd%20path%2Fto%2Fproject%20...%203%203.%20%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E5%90%8D%E3%81%A8%E3%83%A1%E3%83%BC%E3%83%AB%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9%E3%81%8C%E4%BD%BF%E3%82%8F%E3%82%8C%E3%82%8B%E3%81%A8%E3%81%93%E3%82%8D%20)
    2. Afterwards, you create an SSH key and register it on GitHub to perform authentication.
        See here:
        - [【WSL環境】sshを作成してgithubにアクセスするまでの道のり](https://qiita.com/uta3chame/items/ae1291191122d75de718)
        - [SSH を使用した GitHub への接続](https://docs.github.com/ja/authentication/connecting-to-github-with-ssh)
        
- ### clone repository 
  this is a command to clone the remote repository into local environment.
    ```
    ~$ git clone git@github.com:OU-QMP-students/band_calc.git
    ```
- ### Other commands
  - git add
  - git commit 
  - git push         ...etc.

- ### REFERENCE
  - [【Git】基本コマンド](https://qiita.com/konweb/items/621722f67fdd8f86a017)
  - [仕組みから理解するGit 入門 〜ひとり開発でも便利〜](https://www.youtube.com/watch?v=qerW4vBftNA)
  - [git入門(全22回)-プログラミングならドットインストール](https://dotinstall.com/lessons/basic_git)
