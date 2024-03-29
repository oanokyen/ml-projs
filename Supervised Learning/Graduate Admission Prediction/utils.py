# -*- coding: utf-8 -*-

# creating functions for quick machine learning framework implementation.


# load dependencies

from sklearn.pipeline import make_pipeline

#using minmax to ensure scaling to the same unit size
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from sklearn.decomposition import IncrementalPCA

# add multiple models per need
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score,roc_curve


class create_logistic_model:
  def __init__(self, X_train, y_train,X_test,y_test, normalizer=StandardScaler(),alg=LogisticRegression()):
    self.pipe = make_pipeline(normalizer, alg)
    self.pipe.fit(X_train, y_train)
    '''Implement linear supervised machine learning framework. 
    X: Training features, y=training label, 
    norm= type of normalizer function as used scikit, 
    alg: type of supervised learning algorithm as used in scikit'''
    self.X_train, self.y_train, self.X_test, self.y_test, self.normalizer, self.alg = X_train, y_train,X_test, y_test, normalizer,alg


  @property
  def coeff_(self):
    '''Return model coefficients'''
    return self.pipe.named_steps.logisticregression.coef_


  @property
  def intercept_(self):
    '''Return model intercept'''
    return self.pipe.named_steps.logisticregression.intercept_

  # predicting on training dataset
  @property
  def y_train_predict(self):
    '''Predict from the training dataset'''
    return self.pipe.predict(self.X_train)

  @property
  def y_test_predict(self):
    '''Predict class from test dataset'''
    return self.pipe.predict(self.X_test)

  
  # evaluating the model on training dataset

  @property
  def accuracy_train(self):
    return accuracy_score(self.y_train, self.y_train_predict)
  
  @property
  def precision_train(self): 
    return precision_score(self.y_train, self.y_train_predict)

  @property
  def recall_train(self):
    return recall_score(self.y_train, self.y_train_predict)



  # evaluating the model on test dataset

  @property
  def accuracy_test(self):
    return accuracy_score(self.y_test, self.y_test_predict)
  
  @property
  def precision_test(self): 
    return precision_score(self.y_test, self.y_test_predict)

  @property
  def recall_test(self):
    return recall_score(self.y_test, self.y_test_predict)

  @property
  def roc_auc (self): #ROC AUC Score
    return roc_auc_score(self.y_test,self.pipe.predict_proba(self.X_test)[:,1])

  @property
  def roc_curve (self):
    return roc_curve(self.y_test, self.pipe.predict_proba(self.X_test)[:,1])


  @property
  def score(self):
    print("The normalizer is {}".format(self.normalizer))
    print("\n")

    print("The model performance for the training set")
    print("-------------------------------------------")
    print("Accuracy Score of training set is {}".format(self.accuracy_train))
    print("Precision of training set is {}".format(self.precision_train))
    print("Recall score of training set is {}".format(self.recall_train))
    
    print("The model performance for the test set")
    print("-------------------------------------------")
    print("Accuracy Score of test set is {}".format(self.accuracy_test))
    print("Precision of test set is {}".format(self.precision_test))
    print("Recall score of test set is {}".format(self.recall_test))
    print("ROC AUC score is {}".format(self.roc_auc))
    print("\n")




# Principal Component Analysis (PCA) added to pipeline
class create_pca_logistic_model:
  def __init__(self, X_train, y_train,X_test,y_test, normalizer=StandardScaler(),pca =IncrementalPCA(n_components = 2) ,alg=LogisticRegression()):
    self.pipe = make_pipeline(normalizer, pca, alg)
    self.pipe.fit(X_train, y_train)
    '''Implement linear supervised machine learning framework with PCA capability. 
    X: Training features, y=training label, 
    norm= type of normalizer function as used scikit, pca,
    alg: type of supervised learning algorithm as used in scikit'''
    self.X_train, self.y_train, self.X_test, self.y_test, self.normalizer,self.pca, self.alg = X_train, y_train,X_test, y_test, normalizer,pca ,alg

  @property
  def X_train_pca (self):
    '''Return the transformed training data set'''
    return self.pipe.named_steps.incrementalpca.fit_transform(X_train)


  @property
  def coeff_(self):
    '''Return model coefficients'''
    return self.pipe.named_steps.logisticregression.coef_


  @property
  def intercept_(self):
    '''Return model intercept'''
    return self.pipe.named_steps.logisticregression.intercept_

  # predicting on training dataset
  @property
  def y_train_predict(self):
    '''Predict from the training dataset'''
    return self.pipe.predict(self.X_train)

  @property
  def y_test_predict(self):
    '''Predict class from test dataset'''
    return self.pipe.predict(self.X_test)

  
  # evaluating the model on training dataset

  @property
  def accuracy_train(self):
    return accuracy_score(self.y_train, self.y_train_predict)
  
  @property
  def precision_train(self): 
    return precision_score(self.y_train, self.y_train_predict)

  @property
  def recall_train(self):
    return recall_score(self.y_train, self.y_train_predict)



  # evaluating the model on test dataset

  @property
  def accuracy_test(self):
    return accuracy_score(self.y_test, self.y_test_predict)
  
  @property
  def precision_test(self): 
    return precision_score(self.y_test, self.y_test_predict)

  @property
  def recall_test(self):
    return recall_score(self.y_test, self.y_test_predict)

  @property
  def roc_auc (self): #ROC AUC Score
    return roc_auc_score(self.y_test,self.pipe.predict_proba(self.X_test)[:,1])

  @property
  def roc_curve (self):
    return roc_curve(self.y_test, self.pipe.predict_proba(self.X_test)[:,1])


  @property
  def score(self):
    print("The normalizer is {}".format(self.normalizer))
    print("\n")

    print("The model performance for the training set")
    print("-------------------------------------------")
    print("Accuracy Score of training set is {}".format(self.accuracy_train))
    print("Precision of training set is {}".format(self.precision_train))
    print("Recall score of training set is {}".format(self.recall_train))
    
    print("The model performance for the test set")
    print("-------------------------------------------")
    print("Accuracy Score of test set is {}".format(self.accuracy_test))
    print("Precision of test set is {}".format(self.precision_test))
    print("Recall score of test set is {}".format(self.recall_test))
    print("ROC AUC score is {}".format(self.roc_auc))
    print("\n")

