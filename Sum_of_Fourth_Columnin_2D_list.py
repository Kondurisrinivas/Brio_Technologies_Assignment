#Using Two Dimensional List Concept
data = [
    [10, 20, 4, 66, 56, 6, 12],
    [1, 60, 64, 6, 5, 556, 612],
    [176, 623, 6545, 126, 521, 55, 62]
]
# Considering 0-based index for Index of the 4th column 
index = 3  
sum = 0
for lis in data:
    sum += lis[index]
print("Sum of the 4th column:",sum)



import numpy as np
data = [
    [10, 20, 4, 66, 56, 6, 12],
    [1, 60, 64, 6, 5, 556, 612],
    [176, 623, 6545, 126, 521, 55, 62]
]
array = np.array(data)
column_index = 3  # Index of the 4th column (0-based index)
column_sum = np.sum(array[:, column_index])
print("Sum of the 4th column:", column_sum)


#Using Pandas 
import pandas as pd
data = [
    [10, 20, 4, 66, 56, 6, 12],
    [1, 60, 64, 6, 5, 556, 612],
    [176, 623, 6545, 126, 521, 55, 62]
]

df = pd.DataFrame(data)
column_index = 3  # Index of the 4th column (0-based index)
column_sum = df[column_index].sum()
print("Sum of the 4th column:", column_sum)
