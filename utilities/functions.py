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


def plot_churn_probs(df_z_test):
    '''
    plot the churn with their confidence intervals and the total number of observations

    Parameters
    ----------
    df_z_test : pd.DataFrame
        DataFrame containing:
            + categories
            + p_churn: churn probability for each category.
            + churn: churn observations  for each category.
            + count: total number of observation for each category.
            + ci_(low/upp): lower and upper boundaries for the churn probability according to their confidence interval.

    Returns
    -------
    None.

    '''
    
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    column = df_z_test.columns[0]
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(x=df_z_test[column], y=df_z_test['ci_upp'], name="Upper Boundary", marker=dict(color='#6E7B8B')),
        secondary_y=True)
    fig.add_trace(
        go.Scatter(x=df_z_test[column], y=df_z_test['p_churn'], name="Churn Prob", marker=dict(color='#009ACD')),
        secondary_y=True)
    fig.add_trace(
        go.Scatter(x=df_z_test[column], y=df_z_test['ci_low'], name="Lower Boundary", marker=dict(color='#6E7B8B')),
        secondary_y=True)

    fig.add_trace(
        go.Bar(x=df_z_test[column], y=df_z_test['count'], name="No. Obs", marker=dict(color='#FFC125')), secondary_y=False)
    fig.update_xaxes(title_text=column)
    
    fig.update_yaxes(title_text="No. obs", secondary_y=False)
    fig.update_yaxes(title_text="Probability", secondary_y=True)

    fig.show()
    

def compare_churn_prob(df, column, churn = 'Churn', plot = True):
    '''
    Calculates the churn probability and the confidence interval for each category.

    Parameters
    ----------
    df : pd.DataFrame
        The Pandas DataFrame to be analyzed .
    column : srt
        Column name containing the categories to be compared.
    churn : str, optional
        Churn column. The default is 'Churn'.

    plot : bool, optional
        if true, the plot_churn_probs will be executed.

    Returns
    -------
    df_z_test : pd.DataFrame
        DataFrame containing:
            + categories
            + p_churn: churn probability for each category.
            + churn: churn observations  for each category.
            + count: total number of observation for each category.
            + ci_(low/upp): lower and upper boundaries for the churn probability according to their confidence interval.

    '''
    from statsmodels.stats.proportion import proportion_confint
    df_z_test = df.groupby(column).agg(p_churn = (churn, 'mean'), churn = (churn, 'sum'), count = (churn, 'count')).reset_index()

    ci_low, ci_upp = proportion_confint(count = df_z_test['churn'], nobs = df_z_test['count'])

    df_z_test['ci_low'] = ci_low
    df_z_test['ci_upp'] = ci_upp
    
    if plot:
        plot_churn_probs(df_z_test)    
    
    return df_z_test


