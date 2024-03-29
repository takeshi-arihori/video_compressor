# RCP の実装

### システムの目標と実装詳細

この課題では、異なるプログラミング言語で書かれたクライアントとサーバが共通の方法で通信し、特定の関数を実行できるようにするシステムを作ることが求められています。具体的には、クライアントが Python で書かれたサーバに対して、JavaScript（Node.js を使用）から命令を出す場面を想定しています。


https://github.com/takeshi-arihori/video_compressor/assets/83809409/7c4e8f90-008a-4de6-91f7-d5005ff9d409


## リクエストとレスポンスの形式

次に、クライアントからサーバへの要求（リクエスト）と、サーバからクライアントへの返答（レスポンス）の形式を決めます。ここでは JSON 形式のメッセージが用いられ、リクエストには実行するメソッドの名前、その引数、引数の型、リクエストの ID が、レスポンスには結果、結果の型、同じリクエスト ID が含まれます。

### Request

```
{
   "method": "subtract",
   "params": [42, 23],
   "param_types": [int, int],
   "id": 1
}
```

### Response

```
{
   "results": "19",
   "result_type": "int",
   "id": 1
}
```

## 課題

### ステップ 1: ソケット通信の基礎を設定

サーバ側 (Python): socket モジュールを使用してソケットサーバを作成し、クライアントからの接続を待ち受けます。AF_INET または AF_UNIX ソケットファミリを選択し、TCP/IP (SOCK_STREAM) で通信します。
クライアント側 (Node.js): net モジュールを使用してサーバに接続します。サーバの IP アドレス（または UNIX ソケットパス）とポート番号が必要です。

### ステップ 2: JSON 形式でのリクエスト/レスポンスの定義

クライアントからサーバへのリクエスト は、指定された形式（メソッド名、パラメータ、パラメータの型、リクエスト ID を含む JSON オブジェクト）で送信します。
サーバからクライアントへのレスポンス は、実行結果、結果の型、リクエスト ID を含む JSON オブジェクトとして返します。

### ステップ 3: サーバ側での関数の実装と RPC メカニズム

サーバは、リクエストに含まれるメソッド名に基づいて、対応する関数を呼び出します。これには、メソッド名と関数をマッピングするハッシュマップ（または辞書）が必要です。
パラメータの検証は、リクエストに含まれる param_types を使用して行います。
エラー処理：無効なリクエストや実行時エラーが発生した場合、エラーメッセージを含むレスポンスをクライアントに送信します。

### ステップ 4: コードの構造と管理

サーバとクライアントの両方で、ソケット通信を管理するためのラッパークラスやモジュールを作成します。これにより、メインの処理ロジックから通信の詳細を抽象化し、コードの可読性と再利用性を向上させます。
