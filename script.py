###--- IMPORTS ---###
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


###--- CODE ---###
df = pd.read_csv(r'Youtube03-LMFAO.csv', encoding="latin-1")

comments = ''
sw = set(STOPWORDS)

for i in df.CONTENT:
    i = str(i)

    tokens = i.split()

    for j in range(len(tokens)):
        tokens[j] = tokens[j].lower()

    comments += ' '.join(tokens) + ' '


wc = WordCloud(width=800, height=800, background_color='grey',
               stopwords=sw, min_font_size=10).generate(comments)

plt.figure(figsize=(10, 10), facecolor=None)
plt.imshow(wc)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
