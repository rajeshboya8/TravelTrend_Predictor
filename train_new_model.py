import pandas as pd
import xgboost as xgb
import pickle
import os
import numpy as np

def train_and_save_model():
    print("Loading dataset...")
    # Load the dataset
    data_path = os.path.join('Data and ML model', 'data_2014_2017_prepared.csv')
    ml_dataset = pd.read_csv(data_path)
    
    print("Preparing data...")
    # Prepare the data
    ml_dataset = ml_dataset[['quarter', 'Visits (000s)', 'mode', 'purpose', 'year', 'dur_stay', 'market', 'Spend (\xa3m)']]
    ml_dataset['__target__'] = ml_dataset['Visits (000s)']
    del ml_dataset['Visits (000s)']
    ml_dataset = ml_dataset[~ml_dataset['__target__'].isnull()]
    
    print("Handling missing values...")
    # Handle missing values
    for feature in ['quarter', 'mode', 'purpose', 'year', 'dur_stay', 'market', 'Spend (\xa3m)']:
        v = ml_dataset[feature].mean()
        ml_dataset[feature] = ml_dataset[feature].fillna(v)
    
    print("Rescaling features...")
    # Rescale features and save scaling parameters
    scale_list = []
    shift_list = []
    for feature in ['dur_stay', 'mode', 'Spend (\xa3m)', 'year', 'quarter', 'market', 'purpose']:
        shift = ml_dataset[feature].mean()
        scale = ml_dataset[feature].std()
        if scale != 0:
            ml_dataset[feature] = (ml_dataset[feature] - shift) / scale
            scale_list.append(scale)
            shift_list.append(shift)
        else:
            scale_list.append(1.0)
            shift_list.append(0.0)
    
    print("Preparing training data...")
    # Prepare training data
    train_X = ml_dataset.drop('__target__', axis=1)
    train_Y = ml_dataset['__target__']
    
    print("Training XGBoost model...")
    # Train the model
    clf = xgb.XGBRegressor(
        max_depth=10,
        learning_rate=0.1,
        gamma=0.0,
        min_child_weight=0.0,
        max_delta_step=0.0,
        subsample=1.0,
        colsample_bytree=0.75,
        colsample_bylevel=1.0,
        reg_alpha=0.0,
        reg_lambda=1.0,
        n_estimators=300,
        nthread=4,
        seed=1337,
    )
    
    clf.fit(train_X, train_Y)
    
    print("Saving model...")
    # Save the model using the newer XGBoost format
    model_path = os.path.join('main', 'xgboost_model.json')
    clf.save_model(model_path)
    
    # Also save scaling parameters
    scaling_params = {
        'scale_list': scale_list,
        'shift_list': shift_list
    }
    
    with open(os.path.join('main', 'scaling_params.pkl'), 'wb') as f:
        pickle.dump(scaling_params, f)
    
    print(f"Model saved to {model_path}")
    print("Training completed successfully!")
    
    return clf, scale_list, shift_list

if __name__ == "__main__":
    train_and_save_model()
