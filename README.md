# Surrogate Set Imputer - A Library for Imputing Continous Feature Values 
### This library is based on the paper: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4640047 

# Installation 
### Installation via pip 
For use of the surrogate set imputer, install via 
``` pip install surrogate_set_imputer ```

# Example Usage
```
from sklearn.datasets import load_diabetes
from surrogate_set_imputer import surrogate_set_imputer
import numpy as np

data = load_diabetes()
X = data.data
y = data.target 
X[0][0] = np.nan
instance_interest = 0
num_neighbours = 3
features_to_impute = [0]

imputer = surrogate_set_imputer.SurrogateSetImputer(X, instance_interest, num_neighbours, features_to_impute)
result, shap_values = imputer.impute_missing_features()

print("Original instance:", X[instance_interest])
print("Imputed instance:", result)
```
