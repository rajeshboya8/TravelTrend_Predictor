import sys
import os
import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.model_selection import train_test_split
import xgboost as xgb
import pickle


def logic_layer(x):
    workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in

    # Load the trained model using the new format
    model_path = os.path.join(workpath, 'xgboost_model.json')
    clf = xgb.XGBRegressor()
    clf.load_model(model_path)
    
    # Load scaling parameters
    scaling_params_path = os.path.join(workpath, 'scaling_params.pkl')
    with open(scaling_params_path, 'rb') as f:
        scaling_params = pickle.load(f)
    
    scale_list = scaling_params['scale_list']
    shift_list = scaling_params['shift_list']

    # Here we prepare our data in form of dataframe, same as in trained model
    a = pd.DataFrame(columns = ['quarter', 'mode','purpose','year','dur_stay','market', 'Spend (\xa3m)', '__target__'])
    a.loc[0]= x
    test = a

    # Apply rescaling using the new scaling parameters
    rescale_features = ['dur_stay', 'mode', 'Spend (\xa3m)', 'year', 'quarter', 'market', 'purpose']
    for cnt, feature_name in enumerate(rescale_features):
        test[feature_name] = (test[feature_name] - shift_list[cnt]).astype(np.float64) / scale_list[cnt]

    test_X = test.drop('__target__', axis=1)
    test_Y = np.array(test['__target__'])

    _predictions = clf.predict(test_X)
    predictions = pd.Series(data=_predictions, index=test_X.index, name='predicted_value')
    return int(round(predictions.iloc[0] * 1000))



# This is used for testing purpose in local environment as x, y, z three datasets are given as example	
if __name__ == "__main__":
    x = [-1.380899, -0.638146, 1.315741, -1.325480, -0.231486, 0.081364, -0.319305, 0.380]
    y = [3, 3, 2, 2016, 7, 5, 0.897155, 3.556813]
    z = [3, 1, 1, 2016, 15, 11, 8.235992, 6.062523]
    print(logic_layer(y))
    input()

