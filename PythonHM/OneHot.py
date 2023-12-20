import random
import pandas as pd
import numpy as np

# Исходный код
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# Код преобразования в формат one-hot
for value in data['whoAmI'].unique():
    data[value] = np.where(data['whoAmI'] == value, 1, 0)

data.head()
