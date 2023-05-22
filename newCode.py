import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_table('kjjcs_keywords.csv', encoding="utf8")

print(df[:10])

df['keywords'] = df['keywords'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")

df[:20]

keywords_corpus = "".join(df['keywords'].tolist())
print(keywords_corpus)

from konlpy.tag import Okt
from collections import Counter

nouns_tagger = Okt()

nouns = nouns_tagger.nouns(keywords_corpus)

count = Counter(nouns)

count

remove_char_counter = Counter({x : count[x] for x in count if len(x) > 1})
print(remove_char_counter)

korean_stopwords_path = "Korean_Stopwords.txt"
with open(korean_stopwords_path, encoding='utf8') as f:
    stopwords = f.readlines()
stopwords = [x.strip() for x in stopwords]
print(stopwords[:20])

kjjcs_stopwords = ['대한', '관한', '통해', '따른', '중심', '관련', '통한', '년대', '로서', '이후', '정도', '사이', '파적']
for stopword in kjjcs_stopwords:
    stopwords.append(stopword)

remove_char_counter = Counter({x : remove_char_counter[x] for x in count if x not in stopwords})
print(remove_char_counter)
