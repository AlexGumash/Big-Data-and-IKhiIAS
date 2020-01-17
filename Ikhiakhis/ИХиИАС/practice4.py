
# coding=utf-8
import matplotlib.pyplot as plt, numpy as np
from sklearn.svm import SVC
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, 2:4]
y = iris.target

clf = SVC(kernel='linear')
clf.fit(X, y)

plt.scatter(X[:50,0], X[:50,1])
plt.scatter(X[50:100,0], X[50:100,1])
plt.scatter(X[100:,0], X[100:,1])

#
coef1 = clf.coef_[0]
coef2 = clf.coef_[1]
a = -coef1[0] / coef1[1]
aa = -coef2[0] / coef2[1]
xx = np.linspace(min(X[:,0]), max(X[:,0]),100)
yy = a * xx - (clf.intercept_[0]) / coef1[1]
yyy = aa * xx - (clf.intercept_[0]) / coef2[1]

print(clf.predict([[4, 0]]))
#
plt.plot(xx, yy)
plt.plot(xx,yyy)
plt.show()

