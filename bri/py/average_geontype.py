import numpy as np
import pandas as pd
from scipy.stats.stats import pearsonr
import itertools

# Y-chromosome genotypes and their frequencies in the three populations (Icelandic, Nordic, and Irish)
y = np.array([[1, 1, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 1, 1]])
freq_y = np.array([[0.41, 0.26, 0.82],
                   [0.34, 0.51, 0.15],
                   [0.23,0.18,0],
                   [0.01,0.03,0.42]])

# Mitochondrial genotypes and their frequencies in the three populations (Icelandic, Nordic, and Irish)
m = np.array([[1,1,1,0,1,0,0,0],
              [0,0,1,1,0,1,0,0],
              [0,0,1,1,1,1,1,0],
              [0,0,0,0,1,0,0,1],
              [1,0,0,0,0,1,0,0]])
freq_m = np.array([[0.6, 0.29, 0.7],
                   [0.14, 0.52, 0.21],
                   [0.40,0.04,0.35],
                   [0.04,0.65,0.03],
                   [0.08,0.16,0.07]])


avg_y = np.matmul(y.T, freq_y)
avg_m = np.matmul(m.T, freq_m)

def stats_calc(df):
    '''
    calculate pearson's r coefficient and rmse between all columns of df
    '''
    columns = df.columns
    correlations = {}
    rmses = {}
    for col_a, col_b in itertools.combinations(columns, 2):
        correlations[col_a + '__' + col_b] = pearsonr(df.loc[:, col_a], df.loc[:, col_b])
        rmses[col_a + '__' + col_b] = ((df[col_a] - df[col_b]) ** 2).mean() ** .5
    corr_result = pd.DataFrame.from_dict(correlations, orient='index')
    corr_result.columns = ['PCC', 'p-value']

    rmse_result = pd.DataFrame.from_dict(rmses, orient='index')
    rmse_result.columns = ['RMSE']

    return corr_result, rmse_result

cols = ['Icelandic','Norse','Irish']
df = pd.DataFrame(avg_y, columns = cols)
_, rmse_df = stats_calc(df)
print('Y-chromosome RMSE')
print(rmse_df.sort_index())
print()

df = pd.DataFrame(avg_m, columns = cols)
_, rmse_df = stats_calc(df)
print('Mitochondrial RMSE')
print(rmse_df.sort_index())


