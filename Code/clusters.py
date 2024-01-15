#example of determining clusters in Google Colab using sklearn 

import pandas as pd
import os

#set the search parameters
filename = 'homicide_contain_p_encoding.csv'
search_path = '/content/drive/My Drive'

#search for the file
for root, dirs, files in os.walk(search_path):
    if filename in files:
        file_path = os.path.join(root, filename)
        break

path = '/content/drive/MyDrive/Scriptie/analyse/homicide_contain_p_encoding.csv'
data = pd.read_csv(path)

#determine clusters row-based
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#transpose the DataFrame so that columns become rows
transposed_data = data.T

#choose the number of clusters (k)
k = 5

#apply k-means clustering on the transposed data
kmeans = KMeans(n_clusters=k)
transposed_data['Cluster'] = kmeans.fit_predict(transposed_data)

#create a heatmap to visualize the clustered columns
plt.figure(figsize=(12, 8))
sns.heatmap(transposed_data.drop('Cluster', axis=1), cmap='magma', cbar_kws={'label': 'Feature Values'})
plt.title('Clustered Columns Heatmap')
plt.xlabel('Features')
plt.ylabel('Clusters')
plt.show()

#determine clusters column-based

#transpose the data file so that columns become rows
transposed_data = data.T

#choose the number of clusters (k) (between 1 and 529)
k = 10

#apply k-means clustering on the transposed data
kmeans = KMeans(n_clusters = k)
transposed_data['Cluster'] = kmeans.fit_predict(transposed_data)

#create a heatmap to visualize the clustered columns
plt.figure(figsize = (12, 8))
sns.heatmap(transposed_data.drop('Cluster', axis = 1), cmap = 'viridis', cbar_kws = {'label': 'Feature Values'})
plt.title('Clustered Columns Heatmap')
plt.xlabel('Features')
plt.ylabel('Clusters')
plt.show()
