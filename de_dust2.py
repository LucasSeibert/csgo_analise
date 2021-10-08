import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from main import get_df

dust_ct, dust_tr = get_df("de_dust2") #pegando os dataframes da dust2



#análise do lado CT

for col in dust_ct.columns:
    x = dust_ct[col]
    for line in x:
        print(line)
    
    




if __name__ == "__main__":

    pass