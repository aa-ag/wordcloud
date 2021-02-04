###--- IMPORTS ---###
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


###--- CODE ---###
df = pd.read_csv(r'Youtube04-Eminem.csv', encoding="latin-1")

comment_words = ''
sw = set(STOPWORDS)

for i in df.CONTENT:
    i = str(i)

    tokens = i.split()

    for j in range(len(tokens)):
        tokens[j] = tokens[j].lower()

    comment_words += ' '.join(tokens) + ' '


wc = WordCloud(width=800, height=800, background_color='white',
               stopwords=sw, min_font_size=10).generate(comment_words)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wc)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
