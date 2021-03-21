# プラグインのトータルダウンロード数を取得する何か

# 事前準備
## ライブラリのインストール
以下の手順で必要なライブラリをインストールする
```
pip install requests
pip install beautifulsoup4
pip install python-dotenv
pip install selenium
pip install chromedriver-binary={Chromeのバージョン}
```
## 環境定数
1. `.env.sample` ファイルをコピーして `.env` ファイルを作成する
1. `TARGET_URL` に WordPress.org のプロフィール(プラグイン)画面のURLを記載する

# 実行
```
python plugin-download-rate.py
```