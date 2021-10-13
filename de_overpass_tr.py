import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import time


from main import get_df, plota_matriz_correlacao

overpass_ct, overpass_tr = get_df('de_overpass')      # pegando os dataframes da overpass2

threshold = 0.962                          # porcentagem de zeros na coluna da UMP-45


map_round_winner_tr = {"CT": 0, "T": 1}

overpass_tr['round_winner'] = overpass_ct['round_winner'].replace(map_round_winner_tr)


###### ANALISE DO LADO TR


map_round_winner_tr = {"CT": 0, "T": 1}

overpass_tr['round_winner'] = overpass_tr['round_winner'].replace(map_round_winner_tr)


cols_to_keep_tr = []
for col in overpass_tr.columns:

    x = overpass_tr[col]

    dict_col = {}
    for val in x:
        if val not in dict_col:
            dict_col[val] = 1
        else:
            dict_col[val] = dict_col[val] + 1

    if dict_col[0]/x.shape[0] > threshold:
        pass
    else:
        cols_to_keep_tr.append(col)



overpass_tr = overpass_tr[cols_to_keep_tr]



plota_matriz_correlacao(overpass_tr)
plt.matshow(overpass_tr.corr(method='pearson'))
plt.show()