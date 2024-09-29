import pandas as pd
import numpy as np

# Read the CSV file
data = pd.read_csv("n-back_results_test.csv")

# Calculate metrics
metrics = pd.DataFrame({
    'Total': len(data),
    'TP': ((data['ShouldRespond'] == 1) & (data['Response'] == 1)).sum(),
    'TN': ((data['ShouldRespond'] == 0) & (data['Response'] == 0)).sum(),
    'FP': ((data['ShouldRespond'] == 0) & (data['Response'] == 1)).sum(),
    'FN': ((data['ShouldRespond'] == 1) & (data['Response'] == 0)).sum(),
    'P': data['ShouldRespond'].sum(),
    'N': (data['ShouldRespond'] == 0).sum()
}, index=[0])

# Calculate additional metrics
metrics['Accuracy'] = (metrics['TP'] + metrics['TN']) / metrics['Total']
metrics['Sensitivity'] = metrics['TP'] / metrics['P']
metrics['Specificity'] = metrics['TN'] / metrics['N']
metrics['ResponseDelay'] = data['Response Time (ms)'].mean()

# Print the results
print(metrics)