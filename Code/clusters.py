#example of determining clusters in Google Colab using sklearn 

import pandas as pd
import os

# Set the search parameters
filename = 'homicide_contain_p_encoding.csv'
search_path = '/content/drive/My Drive'

# Search for the file
for root, dirs, files in os.walk(search_path):
    if filename in files:
        file_path = os.path.join(root, filename)
        break

path = '/content/drive/MyDrive/Scriptie/analyse/homicide_contain_p_encoding.csv'
data = pd.read_csv(path)

import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Transpose the DataFrame so that columns become rows
transposed_data = data.T

# Choose the number of clusters (k)
k = 10

# Apply k-means clustering on the transposed data
kmeans = KMeans(n_clusters=k)
transposed_data['Cluster'] = kmeans.fit_predict(transposed_data)

# Create a heatmap to visualize the clustered columns
plt.figure(figsize=(12, 8))
sns.heatmap(transposed_data.drop('Cluster', axis=1), cmap='viridis', cbar_kws={'label': 'Feature Values'})
plt.title('Clustered Columns Heatmap')
plt.xlabel('Features')
plt.ylabel('Clusters')
plt.show()