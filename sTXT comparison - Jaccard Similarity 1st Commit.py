sentences = [
"If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you will never have enough.",
"Are you ok with that situation?",
"If you set your goals ridiculously high and it's a failure, you will fail above evreyone else's success",
"Life is what happens when you're busy making other plans",
"I don like to wake up early",
"Did you do your homework?",
"This sentences is made up to be an outsider",
"I don't like the way he drives"
]

from nltk.metrics.distance import jaccard_distance

def jaccard_similarity(x,y):
    return 1 - jaccard_distance(x,y)

import pandas as pd 

rows = []

for text_1 in sentences:
    row = []
    for text_2 in sentences:
        sequence_1 = set(text_1) # sequence of characters 
        sequence_2 = set(text_2) # sequence of characters  

        row.append(jaccard_similarity(sequence_1, sequence_2))
    rows.append(row)

df = pd.DataFrame(data=rows, columns=["sentence_{}".format(i + 1) for i in range(0,8)])


import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt 

corr_matrix = np.corrcoef(df.T)

plt.figure(figsize=(5,5))
sns.heatmap(
    corr_matrix,
    cbar=False,
    annot=True,
    square=True,
    linewidths=.5,
    cmap="YlGnBu",
    xticklabels=df.columns,
    yticklabels=df.columns)

plt.show()
