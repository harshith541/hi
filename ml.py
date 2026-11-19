Program to perform Support Vector Regressor(SVR) on predicting diabetes 
progression using the Diabetes dataset. 
1. What are the Mean Sqaured Error and R-squared values for the evaluation. 
2. Additionally,visualize the predicted values versus the true values on a scatter 
plot. 
 
 
Source Code: 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
 
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVR 
from sklearn.metrics import mean_squared_error,r2_score 
from sklearn.preprocessing import StandardScaler 
 
df=pd.read_csv('diabetes.csv') 
df.head() 
df.info() 
 
df.shape 
df.isnull().sum() 
X=df.drop(['Outcome'],axis=1) 
y=df.loc[:,'Outcome'].values 
 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1) 
scaler=StandardScaler() 
X_train_scaled=scaler.fit_transform(X_train) 
X_test_scaled=scaler.transform(X_test) 
svr_regressor=SVR(kernel='linear',C=1.0) 
svr_regressor.fit(X_train_scaled,y_train) 
 
 
predictions=svr_regressor.predict(X_test_scaled) 
mse=mean_squared_error(y_test,predictions) 
r2=r2_score(y_test,predictions) 
print(f'Mean Squared error : {mse:.2f}') 
print(f'R-Squared error:{r2:.2f}') 
 
 
 
plt.scatter(y_test,predictions,color='blue') 
plt.plot([min(y_test),max(y_test)],[min(y_test),max(y_test)],linestyle=''
,color='red',linewidth=1) 
plt.xlabel('True values') 
plt.ylabel('Predictions') 
plt.title('True value vs. predictions-SVM Regressions') 
plt.show()
Program to perform Principal Component Analysis (PCA) using fetch_olivetti_faces 
dataset. 
 
 
Source Code: 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler 
from sklearn.datasets import fetch_olivetti_faces 
from sklearn.decomposition import PCA 
from sklearn.model_selection import train_test_split 
 
faces=fetch_olivetti_faces(shuffle=True,random_state=42) 
images=faces.images 
data=faces.data 
 
scaler=StandardScaler() 
data_std=scaler.fit_transform(data) 
 
X_train,X_test=train_test_split(data_std,test_size=0.3,random_state=42) 
 
pca=PCA(n_components=30,whiten=True) 
X_train_pca=pca.fit_transform(X_train) 
X_reconstructed=pca.inverse_transform(X_train_pca) 
plt.figure(figsize=(20,6)) 
for i in range(10): 
plt.subplot(2,10,i+1) 
plt.imshow(X_train[i].reshape(64,64),cmap='gra
y') plt.title("Original") 
plt.xticks([]);plt.yticks([]) 
 
plt.figure(figsize=(20,6)
) for i in range(10): 
plt.subplot(2,10,i+11) 
plt.imshow(X_reconstructed[i].reshape(64,64),cmap='gray') 
plt.title("PCA") 
plt.xticks([]);plt.yticks([
]) plt.show() 
 
 