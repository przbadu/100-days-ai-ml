import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

# Load the California Housing dataset
housing = fetch_california_housing()
data = pd.DataFrame(housing.data, columns=housing.feature_names)
data['PRICE'] = housing.target

# Display basic information about the dataset
print("\nDataset Info:")
print(data.info())

print("\nFeature descriptions:")
for idx, feature in enumerate(housing.feature_names):
    print(f"{feature}")

print("\nFirst few rows:")
print(data.head())

print("\nBasic statistics:")
print(data.describe())

# Create a correlation matrix
correlation = data.corr()
