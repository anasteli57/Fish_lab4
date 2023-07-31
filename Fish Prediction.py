#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib


# In[2]:


# Load the dataset
file_path = "./Fish.csv"
data = pd.read_csv(file_path)


# In[3]:


# Separate features and target variable
X = data.drop(columns=["Weight"])
y = data["Weight"]


# In[4]:


# Perform one-hot encoding on categorical features in X
X_encoded = pd.get_dummies(X)


# In[5]:


# Split the data into training and testing sets (80% - 20%)
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=68)


# In[6]:


# Initialize the linear regression model
model = LinearRegression()


# In[7]:


# Train the model using the training data
model.fit(X_train, y_train)


# In[8]:


# Make predictions on the test set
y_pred = model.predict(X_test)


# In[10]:


# Save the trained model to a file
joblib.dump(model, "fish.pkl")

