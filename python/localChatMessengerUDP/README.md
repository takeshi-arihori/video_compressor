# UDP によるチャットメッセンジャー

## 概要

UDP を用いて通信を行います。また、ソケットタイプとして SOCK_DGRAM を使用しています。これは、データを個別のパケット（データグラム）として送受信することを表します。

UDP は、インターネットプロトコルスイートの一部で、メッセージ（データグラム）をコンピュータネットワークを通じて送信するために使用されます。このプロトコルは信頼性が低い（データが必ず到着する保証がない）とされていますが、その一方で、TCP よりもオーバーヘッドが少なく、通信が速いという利点があります。

## 使い方