#################################################################
# Linear Regression - ABC Grocery Task
#################################################################


#################################################################
# Libraries
#################################################################

import pandas as pd
import pickle
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import r2_score
from feature_engine.encoding import OneHotEncoder
from sklearn.feature_selection import RFECV


#################################################################
# Import sample data
#################################################################

# Import

data_for_model = pickle.load(open("data/abc_regression_modelling.p", "rb"))

# Drop uneccessary columns

data_for_model.drop("customer_id", axis = 1, inplace = True)

# Shuffle data

data_for_model = shuffle(data_for_model, random_state = 42)


#################################################################
# Deal with missing values
#################################################################

data_for_model.isna().sum()
data_for_model.dropna(inplace = True)


#################################################################
# Deal with outliers
#################################################################

outlier_investigation = data_for_model.describe()

outlier_columns = ["distance_from_store","total_sales", "total_items"]

for column in outlier_columns:
    
    lower_quartile = data_for_model[column].quantile(0.25)
    upper_quartile = data_for_model[column].quantile(0.75)
    iqr = upper_quartile - lower_quartile
    iqr_extended = iqr * 2
    min_border = lower_quartile - iqr_extended
    max_border = upper_quartile + iqr_extended
    
    outliers = data_for_model[(data_for_model[column] < min_border) | (data_for_model[column] > max_border)].index
    print(f"{len(outliers)} outliers detected in column {column}")
    
    data_for_model.drop(outliers, inplace=True)

#################################################################
# Split Input Variables & Output Variable
#################################################################

X = data_for_model.drop(["customer_loyalty_score"], axis = 1)
y = data_for_model["customer_loyalty_score"]


#################################################################
# Split Training & Test sets
#################################################################

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)


#################################################################
# Deal with Categorical Variables
#################################################################

ohe_enc = OneHotEncoder(top_categories = None,
                        variables = ["gender"], 
                        drop_last = True)

X_train = ohe_enc.fit_transform(X_train)
X_test = ohe_enc.transform(X_test)


#################################################################
# Feature Selection
#################################################################

regressor = LinearRegression()
feature_selector = RFECV(regressor)

fit = feature_selector.fit(X_train, y_train)

optimal_feature_count = feature_selector.n_features_
print(f"Optimal number of features: {optimal_feature_count}")

X_train = X_train.loc[:, feature_selector.get_support()]
X_test = X_test.loc[:, feature_selector.get_support()]


plt.plot(range(1, len(fit.cv_results_['mean_test_score']) + 1), fit.cv_results_['mean_test_score'], marker = "o")
plt.ylabel("Model Score")
plt.xlabel("Number of Features")
plt.title(f"Feature Selection using RFE \n Optimal number of features is {optimal_feature_count} (at score of {round(max(fit.cv_results_['mean_test_score']),4)})")
plt.tight_layout()
plt.show()


#################################################################
# Model Training
#################################################################

regressor = LinearRegression()
regressor.fit(X_train, y_train)


#################################################################
# Model Assessment
#################################################################

# Predict on the Test Set

y_pred = regressor.predict(X_test)

# Calculate R-Squared

r_squared = r2_score(y_test, y_pred)
print(r_squared)

# Cross Validation

cv = KFold(n_splits = 4, shuffle = True, random_state = 42)
cv_scores = cross_val_score(regressor, X_train, y_train, cv = cv, scoring = "r2")
cv_scores.mean()

# Calculate Adjusted R-Squared

num_data_points, num_input_vars = X_test.shape
adjusted_r_squared = 1 - (1 - r_squared) * (num_data_points - 1) / (num_data_points - num_input_vars - 1)
print(adjusted_r_squared)

# Extract Model Coefficients

coefficients = pd.DataFrame(regressor.coef_)
input_variable_names = pd.DataFrame(X_train.columns)
summary_stats = pd.concat([input_variable_names, coefficients], axis = 1)
summary_stats.columns = ["input_variable", "coefficients"]

# Extract Model Intercept

regressor.intercept_
