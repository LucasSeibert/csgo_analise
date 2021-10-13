import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns




def get_df(map: str='') -> pd.DataFrame and pd.DataFrame:
    """
    Função que devolve os dois dataframes já separados do mapa (map) escolhido
    """
    
    if not isinstance(map, str):
        print('Map nao eh string')
        return None, None

    # lendo o csv
    path = r"csgo_round_snapshots.csv"
    df = pd.read_csv(path)

    if map not in df['map'].unique():
        print('Map nao esta na lista de mapas')
        return None, None
    
    # filtrando apenas o mapa requisitado
    df = df.loc[df['map'] == map]
 

    # retirando colunas que nao serao usadas
    cols_to_drop = ['time_left', 'ct_score', 't_score', 'map', 'bomb_planted', 'ct_health',
       't_health', 'ct_armor', 't_armor', 'ct_money', 't_money', 'ct_helmets',
       't_helmets', 'ct_defuse_kits', 'ct_players_alive', 't_players_alive']

    df.drop(cols_to_drop, axis=1, inplace=True) # retirando colunas
    df.reset_index(drop=True, inplace=True)     # ajustando indices

    
    cols_ct = []
    cols_tr = []

    for col in df.columns:  # separando colunas de TR e CT
        if col.startswith('ct_'):  # colunas CT iniciam com "ct_"
            cols_ct.append(col)
        elif col.startswith('t_'): # colunas TR iniciam com "t_"
            cols_tr.append(col)
        else:                      # a unica colunas que nao inicia com "ct_" ou "t_" eh o resultado do round ('round_winner')
            cols_ct.append(col)
            cols_tr.append(col)


    df_ct = df[cols_ct]
    df_tr = df[cols_tr]
    


    return df_ct, df_tr




def plota_matriz_correlacao(df: pd.DataFrame = pd.DataFrame()) -> plt.figure:

    if not isinstance(df, pd.DataFrame):
        print('df nao eh um dataframe')
        return None

    fig, ax = plt.subplots(figsize=(12,7), dpi=120)

    ax.tick_params(axis="x", labelsize=20)
    ax.tick_params(axis="y", labelsize=20)
    ax.spines['left'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)

    f, ax = plt.subplots(figsize=(12, 7), dpi=120)
    corr = df.corr()
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap='viridis',
                square=True, ax=ax)
    plt.title('Matriz de Correlação')

    plt.show()

    return



def test_matrix(df):
    

    f, ax = plt.subplots(figsize=(12, 7), dpi=120)
    corr = df.corr()
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap='viriadis ',
                square=True, ax=ax)
    plt.show()
    return  
if __name__ == '__main__':

    get_df()