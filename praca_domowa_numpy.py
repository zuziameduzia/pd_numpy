import numpy as np

data = np.load('ex3_data.npy')
row, col = data.shape
#print(row)
#print(col)
mask = np.isnan(data)
data_without_nan = data[~np.isnan(data).any(axis=1)]
#print(data_without_nan)
row_without_nan, col_without_nan = data_without_nan.shape

droped_rows = row - row_without_nan

nan_count_by_column = np.isnan(data).sum(axis=0)
#print(nan_count_by_column)
print(f'Podczas filtowania usunięto {droped_rows} wierszy.')
print(f'Przed filtowaniem w pierwszej kolumnie jest {nan_count_by_column[0]} wartości NaN, w drugiej kolumnie {nan_count_by_column[1]}, w trzeciej {nan_count_by_column[2]}, a w czwartej kolumnie jest {nan_count_by_column[3]} wartości NaN.')


