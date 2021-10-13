import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import time


from main import get_df, plota_matriz_correlacao

mirage_ct, mirage_tr = get_df('de_mirage')      # pegando os dataframes da mirage2

threshold = 0.962                          # porcentagem de zeros na coluna da UMP-45


map_round_winner_ct = {"CT": 1, "T": 0}

mirage_ct['round_winner'] = mirage_ct['round_winner'].replace(map_round_winner_ct)


cols_to_keep_ct = []
for col in mirage_ct.columns:

    x = mirage_ct[col]

    dict_col = {}
    for val in x:
        if val not in dict_col:
            dict_col[val] = 1
        else:
            dict_col[val] = dict_col[val] + 1

    if dict_col[0]/x.shape[0] > threshold:
        pass
    else:
        cols_to_keep_ct.append(col)



mirage_ct = mirage_ct[cols_to_keep_ct]



plota_matriz_correlacao(mirage_ct)
plt.matshow(mirage_ct.corr(method='pearson'))
plt.show()


# análise do lado CT



if __name__ == '__main__':
    pass
    