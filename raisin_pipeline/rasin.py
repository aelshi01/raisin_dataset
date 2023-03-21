#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 08:42:29 2023

@author: adamelshimi
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report, f1_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

import seaborn as sns
from aequitas.group import Group
from aequitas.bias import Bias
from aequitas.fairness import Fairness
from aequitas.plotting import Plot



data = pd.read_excel("./Raisin_Dataset/Raisin_Dataset.xlsx")
y = data.pop("Class")

# Split the data into train and validation, stratifying on the target feature.
X_train, X_val, y_train, y_val = train_test_split(data, y, stratify=y, random_state=23)

# Initiating logistic regression for training on the prepared dataset
lr = LogisticRegression(max_iter=1000, random_state=23)
# label binariser allows us to binarise our multiclass datasets to a binary one and compare via one vs all method
lb = LabelBinarizer()

y_train = lb.fit_transform(y_train)
y_val = lb.transform(y_val)


lr.fit(X_train, y_train.ravel())

scores = lr.predict_proba(X_val)
pre = lr.predict(X_val)


f1 = f1_score(y_val, pre)

cm = confusion_matrix(y_val, pre)

ConfusionMatrixDisplay(cm,display_labels=['kecimen','besni']).plot()

print(classification_report(y_val, lr.predict(X_val)))

#########################################

feature_set = ['Area','ConvexArea','MajorAxisLength']


for feat in feature_set:

   feat_mean = X_val[feat].mean()
   feat_slice_gt = X_val[feat] >= feat_mean
   feat_slice_lt = X_val[feat] < feat_mean
   
   print(f"F1 score on {feat} slices:")
   print("Greater than the mean = ",f1_score(y_val[feat_slice_gt],lr.predict(X_val[feat_slice_gt])))
   print("Less than the mean = ",f1_score(y_val[feat_slice_lt],lr.predict(X_val[feat_slice_lt])))
   print("\n")























