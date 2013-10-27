#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*-

import sys
from sklearn.datasets import load_svmlight_file
from sklearn.cross_validation import train_test_split

#データの読み込み
X_train, y_train = load_svmlight_file(sys.argv[1])
#データを学習用テスト用に分割
data_train, data_test, label_train, label_test = train_test_split(X_train, y_train)

#データの確認
print data_train
print
print data_test
print
print label_train
print
print label_test
print

print 'please press enter key...'
raw_input()



#### GBDTによる分類 ####
from sklearn.ensemble import GradientBoostingClassifier
classif = GradientBoostingClassifier()
#### RFによる分類 ####
#from sklearn.ensemble import RandomForestClassifier
#classif = RandomForestClassifier()

#train
print 'train...'
classif.fit(data_train.toarray(), label_train)

#pred
print 'predict...'
pred = classif.predict(data_test.toarray())
print 'finish'

#output results
print pred
print label_test

zipped = zip(pred, label_test)
ok = 0
cnt = 0

for item in zipped:
    cnt += 1
    if(item[0] == item[1]):
        ok += 1
print 'Accuracy:',(float(ok)/cnt),'(',ok,'/',cnt,')'
