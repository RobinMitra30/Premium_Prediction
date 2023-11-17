import pickle
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
# with open('D:\only projects\Machine learning projects\Premium_insurance\Deployment\gbr.pkl', 'rb') as file:
#     loaded_model = pickle.load(file)

model = pickle.load(open('D:\only projects\Machine learning projects\Premium_insurance\Deployment\gbr.pkl' , "rb"))

# with open('D:\only projects\Machine learning projects\Premium_insurance\Deployment\labels.pkl', 'rb') as file:
#     encoder = pickle.load(file)

#yoo = pd.DataFrame([[42,1,22,2,1,0,0,1]])
#loaded_model.predict(yoo.loc[0].values)
#print(loaded_model)

y_pred = model.predict(np.array([[ 42,1,22,2,1,0,0,1 ]]))
print(y_pred[0])