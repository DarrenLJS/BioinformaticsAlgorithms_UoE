import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("testfile_combined.txt", sep = "\t", header = None, names = ["kmer", "enrichment"])
df = df.iloc[:30]

plt.figure(figsize = (10, 6))
ax = sns.barplot(
    x = "kmer", y = "enrichment", 
    data = df
)
ax.set_title("Enrichment Plot = How much more often kmer appear in Oct4 peaks than expected by chance")
ax.set_ylim(0, 1)
ax.tick_params(axis = "x", labelrotation = 90)
plt.tight_layout()
plt.show()
