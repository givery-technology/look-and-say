# 線分を連結せよ

*これはcodecheckのチャレンジです。  
初めての方はまず[チュートリアル](https://app.code-check.io/orgs/codecheck/challenges/77)をご覧ください。*

数直線上にいくつかの線分があります。

重なっている線分は連結することができます。
連結された線分の中で最も長いものを見つけましょう。

## ザ・ミッション
与えられた線分を連結していき、最も長い線分の長さを返す関数を実装してください。

## 実装の詳細
#### CLI
入力値を引数に取り、結果を標準出力に出力するCLIアプリケーションとして解答を実装してください。
CLIの実装方法については[指定言語].mdを参照ください。

#### 仕様
- このCLIアプリケーションの第1引数には、線分の座標が書かれたファイル名が渡されます。
  - 存在しないファイル名が渡されることはありません。
- 線分座標ファイルは、次のようなフォーマットで書かれています。

```
N
s1 e1
s2 e2
...
sN eN
```
- `N`は線分の数で、`1 ≦ N ≦ 10000`です。
- `si`、`ei`はそれぞれ`i`番目の線分の始点と終点の座標で、次の不等式が成り立ちます。
  - `-10000 ≦ si ≦ 10000`
  - `-10000 ≦ ei ≦ 10000`
  - `si ≦ ei`
- 始点座標が`si`、終点座標が`ei`のとき、線分`i`の長さは`ei - si`です。
- `si = ej`のとき、線分`i`と線分`j`は連結できます。

#### 処理ルール
- CLIアプリケーションは線分座標ファイルを読み込み、標準出力に最大の長さを出力してください。
- 外部ライブラリの利用は不可とします。

#### CLIアプリケーションの実行例
以下に、入力ファイルとして`./input/sample1.txt`、`./input/sample2.txt`、`./input/sample3.txt`が与えられた場合の実行例を示します。

**sample1.txt**
```
2
1 2
3 4
```
```shell
$./line_segments ./input/sample1.txt
1
```

**sample2.txt**
```
2
1 2
2 4
```
```shell
$./line_segments ./input/sample2.txt
3
```

**sample3.txt**
```
1
-10000 10000
```
```shell
$./line_segments ./input/sample3.txt
20000
```

## Answer.md
[answer.md](./answer.md)を用意してあるので、その中に

- 実装したアルゴリズムの計算量を[オーダー記法](https://ja.wikipedia.org/wiki/%E3%83%A9%E3%83%B3%E3%83%80%E3%82%A6%E3%81%AE%E8%A8%98%E5%8F%B7#%E4%B8%80%E8%88%AC%E7%9A%84%E3%81%AA%E3%82%AA%E3%83%BC%E3%83%80%E3%83%BC)で(必須)
- 実装で工夫した点(任意)


等を書いてください。
