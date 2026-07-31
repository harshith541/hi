import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
from sklearn.datasets import make_blobs 
x, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, 
random_state=0) 
kmeans = KMeans(n_clusters=4, init='k-means++', n_init=10, 
random_state=42) 
kmeans.fit(x) 
y_kmeans = kmeans.predict(x) 
Page | 32  
 
centroids = kmeans.cluster_centers_ 
plt.scatter(x[:, 0], x[:, 1], c=y_kmeans, s=50, cmap='viridis') 
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.75, marker='x', 
label='Centroids') 
plt.title("K-Means Clustering") 
plt.xlabel("Feature 1") 
plt.ylabel("Feature 2") 
plt.legend() 
plt.show()