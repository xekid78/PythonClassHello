# PythonClassHello
継承でハローワールド

## 処理
Greetingクラスを親クラスとしてHelloクラスを子クラスにして処理を行う。

## コード
```
class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = " world"

class Hello(Greeting):
    def say_hello(self):
        print(self.msg + self.target)

hello = Hello()
hello.say_hello()
```

## 出力結果  
```
hello world
```
  
## 開発環境
| 開発ツール |  |
|:-|:-|
| OS | Windows10 |
| 仮想化ソフト | Oracle VM VirtualBox 5.2 |
| 構築ソフト | Vagrant 2.0.2 |
| 仮想化上OS | CentOS 6.9 |
| SSHクライアント | PuTTY 0.6.8 |
| FTPクライアント | Cyberduck 6.3.5 |
| エディタ | Atom 1.24.0 |
| 開発言語 | Python 3.6.4 |
