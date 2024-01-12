#example of data analysis in Google Colab 
#target = 762 (suicide)

#import the data
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

#setup regression method
from pycaret.regression import *

p_reg_762 = setup(data = data, target = '762', session_id=100)

#compare all the models at the same time
best_model_762_encoding = compare_models()

#train model
br_762 = create_model('br') #br stands for Bayesian Ridge model

#tune model
tuned_br_762 = tune_model(br_762, optimize = 'R2', n_iter = 100)

#evaluare model
evaluate_model(tuned_br_762)

#after the evaluation choose the 'Feature Importance' plot