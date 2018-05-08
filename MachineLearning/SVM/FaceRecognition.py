# -*- coding: utf-8 -*-
"""
Created on Mon May  7 20:21:17 2018

@author: susmote
"""

from __future__ import print_function
from time import time
import logging
import matplotlib.pyplot as plt

from sklearn.cross_validation import train_test_split
from sklearn.datasets import fetch_lfw_people
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import RandomizedPCA
from sklearn.svm import SVC
from sklearn.cluster.tests.test_k_means import n_samples

print(__doc__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

n_samples,h,w = lfw_people.images.shape

x = lfw_people.data
n_features = x.shape[1]

print(str(lfw_people) + "\n" + str(x) + " " + str(n_features))
y = lfw_people.target

target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print("总共数据集大小 :")
print("n_sample: %d"%n_samples)
print("n_feature: %d"%n_features)
print("n_classed: %d"%n_classes)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

n_components = 150

print("extracting the top %d eigenfaces from the %d faces"%(n_components, x_train.shape[0]))

start_time = time()
pca = RandomizedPCA(n_components=n_components, whiten=True).fit(x_train)
print("运行 %0.3fs"%(time() - start_time))

eigenfaces = pca.components_.reshape((n_components, h, w))

print("将输入数据降维")
start_time = time()
x_train_pca = pca.transform(x_train)
x_test_pca = pca.transform(x_test)
print("运行 %0.3fs"%(time() - start_time))

print("分类数据集的拟合")
start_time = time()
param_grid ={'C':[1e3,5e3,1e4,5e4,1e5],'gamma':[0.0001,0.0005,0.001,0.005,0.01,0.1],}
clf = GridSearchCV(SVC(kernel='rbf', class_weight="balanced"), param_grid)
clf = clf.fit(x_train_pca, y_train)
print("运行 %0.3fs"%(time() - start_time))

print("grid search 最佳估计:")
print(clf.best_estimator_)


print("测试人名在测试集里面")
start_time = time()
y_pred = clf.predict(x_test_pca)
print("运行 %0.3fs"%(time() - start_time))

print(classification_report(y_test, y_pred, target_names=target_names))

def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    plt.figure(figsize=(1.8*n_col, 2.4*n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
    for i in range(n_row*n_col):
        plt.subplot(n_row, n_col, i+1)
        plt.imshow(images[i].reshape((h,w)), cmap=plt.cm.gray)
        plt.title(titles[i], size =12)
        plt.xticks()
        plt.yticks()

def title(y_pred, y_test, target_name, i):
    pred_name = target_names[y_pred[i]].rsplit(' ', 1)[-1]
    true_name = target_names[y_test[i]].rsplit(' ', 1)[-1]
    return 'predicted :%s \ntrue:  %s' %(pred_name,true_name)

prediction_titles=[title(y_pred,y_test,target_names,i)
                   for i in range(y_pred.shape[0])]

plot_gallery(x_test, prediction_titles, h, w)
eigenfaces_title = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenfaces_title, h, w)

plt.show()