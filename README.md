# sample_docker-vpn

このリポジトリは、Docker Composeを用いてVPN経由でアクセスを行うサンプルです。

## 概要
複数のDockerコンテナ（アプリケーション、Selenium、VPN）を連携させ、VPN経由でWebアクセスを実現します。

## 構成
- **app**: Pythonアプリケーション（例: requestsやSeleniumでWebアクセス）
- **selenium**: Selenium Standalone（Chrome）
- **gluetun**: VPN接続用コンテナ
- **autoheal**: ヘルスチェック失敗時に自動再起動するユーティリティ

## VPNを利用しない接続サンプル

VPNコンテナ（gluetun）を使わず、通常のネットワーク経由で外部サイトにアクセスした場合の挙動例です。

### 実行例
```
$ docker compose -f docker-compose.yml up --build
...
app-1       | [Selenium] Your IP address is: <ホストのグローバルIPアドレス>
app-1       | [Requests] Your IP address is: <ホストのグローバルIPアドレス>
```

Selenium経由・requests経由ともにホストのグローバルIPアドレスが表示されます。
VPNを使わない場合、全ての通信は通常のネットワーク経由となります。


## 想定ユースケース
- VPN経由でのWebスクレイピングや自動テスト
- Seleniumを使ったブラウザ操作のVPNトンネリング

---
ご質問・要望があればIssueやPRでご連絡ください。
