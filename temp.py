import pandas as pd

from features.importance import use_most_important_features
from parameters.optimize import optimize_hyperparameters

# set pandas print width
from utils.load import load_data

# pd.option.display.width = 200

# load data
from utils.preprocess import preprocess_data

print("Loading Data...")
DIR = "./data/input"
train_df, test_df = load_data(DIR)

# preprocess, massage, scale, merge and clean data
print("Preprocessing Data...")
train_df, test_df = preprocess_data(train_df, test_df)

# use only most important features
print("Extracting Most Important Features...")
train_df, test_df = use_most_important_features(train_df, test_df)

print("Optimizing Hyperparameters...")
optimize_hyperparameters(train_df)
