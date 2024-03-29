# Local Chat Messenger

### この Local Chat Messenger では、クライアントがメッセージを送り、サーバがそれに応答するという形で通信が行われます。

## SOCK_STREAM の通信処理の流れ

![local-chat-messager](https://github.com/takeshi-arihori/video_compressor/assets/83809409/8ca61cec-d416-4578-9556-25bc1d2c67d6)


## 手順の動画
https://github.com/takeshi-arihori/video_compressor/assets/83809409/93a1811a-1202-4c97-8a3c-dfd2d166d44a



## 実行手順

### 前提条件

- 1. Python がインストールされていること。
- 2. サーバーとクライアントのスクリプトが用意されていること。

### 手順

- 1. サーバースクリプトの準備
     サーバースクリプト（例: server.py）が保存されているディレクトリに移動します。
- 2. サーバースクリプトの実行
     ターミナルを開き、以下のコマンドを入力してサーバーを起動します。

`python server.py`

サーバーが起動したら、Starting up on /tmp/socket_file のようなメッセージが表示され、クライアントからの接続を待ち始めます。

- 3. クライアントスクリプトの準備
     新しいターミナルウィンドウを開き、クライアントスクリプト（例: client.py）が保存されているディレクトリに移動します。

- 4. クライアントスクリプトの実行
     以下のコマンドを入力してクライアントを起動します。

`python client.py`

クライアントがサーバーに接続し、メッセージを送信すると、サーバーからの応答が表示されます。

- 5. サーバーとクライアントの終了
     サーバーまたはクライアントを終了させたい場合は、実行中のターミナルウィンドウで`Ctrl+C`を押します。
     サーバーを終了すると、KeyboardInterrupt, closing socket のようなメッセージが表示され、ソケットが閉じられます。

### 注意点

- UNIX ソケットは同じマシン上でのプロセス間通信にのみ使用できます。
- サーバースクリプトは、新しいクライアント接続を受け入れる前に前の接続を完全に処理する必要があります。
- 複数のクライアントを同時に処理するには、スレッディングまたは非同期 IO を使用する必要があります。
