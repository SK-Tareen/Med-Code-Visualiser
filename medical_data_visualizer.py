import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#1
df = pd.read_csv('medical_examination.csv')

#2
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

#3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


#4
def draw_cat_plot():
#5
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

#6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns={0: 'total'})

#7   
    graph = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")
    fig = graph.fig

#8    
    fig.savefig('catplot.png')
    return fig


#9
def draw_heat_map():
    # 10
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))
                 ]

    # 11
    corr = df_heat.corr()

    # 12
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 13
    fig, ax = plt.subplots(figsize=(16, 9))

    #14
    sns.heatmap(corr, mask=mask, square=True, linewidths=0.5, annot=True, fmt="0.1f")

    # 15 16
    fig.savefig('heatmap.png')
    return fig