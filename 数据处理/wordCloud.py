# Start with one review:
from wordcloud import WordCloud
import pandas as pd
import matplotlib as plt
import preprocessor as p
from string import punctuation


def preprocess(fileName):
    nyc = pd.read_csv(fileName, encoding='ISO-8859-1')
    for i in range(0, len(nyc)):
        nyc.loc[:, 'tweet'][i] = p.clean(nyc.loc[:, 'tweet'][i])
        nyc.loc[:, 'tweet'][i] = ''.join(
            [c for c in nyc.loc[:, 'tweet'][i] if c not in punctuation])
        nyc.loc[:, 'tweet'][i] = nyc.loc[:, 'tweet'][i].lower()
    return nyc


df = preprocess('数据集/TimeSquareWeek12.csv')

text = df['tweet']

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
