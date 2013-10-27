NLPwithScikitLearn
==================
ScikitLearnを使ってテキストを分類するまでに必要なことをまとめておく。

導入
------
### Scikit-Learn ###
MacPortsに入っているので、それを使う。Pythonや必要なパッケージも入れておく。

[installing scikit-learn](http://scikit-learn.org/stable/install.html "installing scikit-learn")

    $ sudo port install py27-scikit-learn

### mecab ###
以下のページから、mecab本体、各種辞書、pythonラッパーをダウンロードし、インストールする。

[mecab](https://code.google.com/p/mecab/)

このとき、pythonラッパーはmacportsのpythonに入れるようにする。

    $ /opt/local/bin/pyhton2.7 setup.py build
    $ sudo /opt/local/bin/pyhton2.7 setup.py install


ディレクトリ構成
------
|ディレクトリ名|説明|
| ---- | ---- |
| data/ | 記事データ(Y!Jのトピックスのダウンロードデータ) |
| script/  | 実行スクリプト(問題ごとに修正して利用) |


素性の作成と学習
------
script/makefeatures.pyをいじって作成する。

    $ ./script/makefeatures < data/201303.utf8.tsv > list
    $ tail +4693 list > list.feat

作成したデータを使って学習させる。

    $ ./script/learn.py ./list.feat
    ...
    Accuracy: 0.510158013544 ( 226 / 443 )

