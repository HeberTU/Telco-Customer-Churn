# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:05:22 2020

@author: HTRUJILLO
"""

def count_null_entries(df):
    '''
    count the null entries at each column of a Pandas DataFrame
    

    Parameters
    ----------
    df : pd.DataFrame
        The Pandas DataFrame to be analyzed  .

    Returns
    -------
    null_df : pd.DataFrame
        Pandas Dataframe containing the following columns:

        + Col_Name: column name
        + Num_Nulls: Number of null values found at each column.

    '''
    
    import pandas as pd
    import numpy as np
    
    null_df = pd.DataFrame(np.sum(df.isnull())).reset_index()
    null_df.columns = ['Col_Name','Num_Nulls']
    
    return null_df



def get_cat_summary(df):
    '''
    Returns for each categorical variable on a DataFrame object:
        + The most frequent category,
        + Total number of categories within the variable, e.g. (Yes/No = 2),
        + The frequency of the most frequent category.
        

    Parameters
    ----------
    df :  pd.DataFrame
        The Pandas DataFrame to be analyzed .

    Returns
    -------
    cat_summary_df : pd.DataFrame
        Pandas Dataframe containing the following columns:

        + BiggestCat: The most frequent category,
        + NumLevels: Total number of categories within the variable, e.g. (Yes/No = 2),
        + BiggestShare: The frequency of the most frequent category.

    '''
    import pandas as pd
    
    categories = []
    b_share = []
    num_levels = []
    for column in df.columns:
        df_gpr = df.groupby(column).size().reset_index()
        df_gpr['share'] = df_gpr[0]/df_gpr[0].sum()
        df_gpr.sort_values('share', ascending = False, inplace = True)
    
        categories.append(df_gpr.head(1)[column].values[0])
        b_share.append(round(df_gpr.head(1)['share'].values[0],4))
        num_levels.append(df_gpr.shape[0])
        
    cat_summary_df = pd.concat(
        [pd.DataFrame(df.columns),
             pd.DataFrame(categories),
             pd.DataFrame(num_levels),
             pd.DataFrame(b_share)], axis = 1) 
    
    cat_summary_df.columns = ['ColName', 'BiggestCat', 'NumLevels', 'BiggestShare']
    
    return cat_summary_df