# Start with one review:
from wordcloud import WordCloud
import pandas as pd
import matplotlib as plt
df = pd.read_csv('TimeSquareWeek12.csv')

text = df['tweet']

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
