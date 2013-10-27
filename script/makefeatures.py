#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*-

import MeCab
import sys
import string

def text2features(sentence):
    ret = {}
    try:
        tagger = MeCab.Tagger()
        m = tagger.parseToNode(sentence);
        while m:
            sp = m.feature.split(',')
            if sp[0] == 'BOS/EOS':
                m = m.next
                continue

            # feature
            feat = m.surface + "_" + sp[0] + "_" + sp[1]
            ret[feat] = ret.get(feat, 0) + 1

            m = m.next
    except RuntimeError, e:
        print "Mecab Runtime Error:", e

    return ret



if __name__ == '__main__':
    #すべての素性のリスト
    allfeatures = {}
    #行ごとの正解ラベル
    linelabels = []
    #行ごとの素性リスト
    linefeatures = []

    #行ごとの処理
    for line in iter(sys.stdin.readline,""):
        feats = {}
        sp = line.split('\t')

        #この行の正解ラベル
        linelabels.append(sp[1])

        #素性の作成
        res = text2features(sp[0])
        for k, v in res.items():
            feats[k] = v
            allfeatures[k] = 1

        #この行の素性リスト
        linefeatures.append(feats)


    ###### 以下、libsvm format出力 #######
    ## format ##
    ## 素性の種類数
    ## 素性リスト...
    ## 各行のラベルと素性リスト...

    #素性に番号をふる
    cnt = 1
    for k, v in allfeatures.items():
        allfeatures[k] = cnt
        cnt += 1
    
    #素性リストの出力
    print len(allfeatures)
    for k, v in allfeatures.items():
        print v, k

    #正解ラベル
    y = {'computer':1, 'domestic':2, 'economy':3,
         'entertainment':4, 'local':5, 'science':6,
         'sports':7, 'world':8}


    #行ごとに出力
    for i,label in enumerate(linelabels):
        features = {}
        for f,v in linefeatures[i].items():
            features[allfeatures[f]] = v

        sys.stdout.write(str(y[label]))
        sys.stdout.write(' ')
        for k,v in sorted(features.items()):
            sys.stdout.write(str(k))
            sys.stdout.write(':')
            sys.stdout.write(str(v))
            sys.stdout.write(' ')
        print
