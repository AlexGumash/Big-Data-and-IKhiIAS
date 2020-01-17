# coding=utf-8
from __future__ import division
from collections import defaultdict
import numpy as np


def train(samples):
    classes, freq = defaultdict(lambda: 0), defaultdict(lambda: 0)
    for feats, label in samples:
        classes[label] += 1
        for feat in feats:
            freq[label, feat] += 1

    #Нормализация классов и признаков
    for label, feat in freq:
        freq[label, feat] /= classes[label]
    for c in classes:
        classes[c] /= len(samples)
    return classes, freq


#Определение класса
def classify(classifier, feats):
    classes, prob = classifier
    arr = {'spam': [], 'notspam': []}
    for cl in classes:
        for feat in feats:
            if prob[cl, feat]:
                # print(prob[cl, feat], feat, cl)
                arr[cl].append(prob[cl, feat])
    for keys in arr:
        arr[keys] = np.prod(arr[keys])
    return min(classes.keys(), key=lambda cl: classes[cl] * arr[cl])


def get_features(sample):
    result = []
    for word in sample.split():
        result.append(word)
    return result

samples = [line.strip().split('-/', 1) for line in open('letters.txt')]
features = [(get_features(feat), label) for label, feat in samples] #Признаки в обучающих примерах
# print(features)
classifier = train(features)

count = 0
right = 0

for line in open('letters.txt', encoding='utf-8'):
    st = line.partition('-/')
    res = classify(classifier, get_features(st[2]))
    if st[0] == res:
        right = right + 1
    count = count + 1

print(right/count)






print('Результат: ', classify(classifier, get_features("sindu got job in birla soft ..")))