# -*- coding: utf-8 -*-
"""chessrank.ipynb

!pip install bootstrapped

!pip install scrapy-poet

import pandas as pd
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.chess.com/ratings")
print(r)
print(r.content)

r.text

r.content

chess = BeautifulSoup(r.text,'html.parser')
chess

print(chess.prettify)

chess.title

chess.title.name

chess.title.string

chess.title.parent.name

chess.a

player_names = []
classical_ratings = []
rapid_ratings = []
blitz_ratings = []

for row in chess.find_all('tr')[1:]:
    cols = row.find_all(['th', 'td'])
    player_name = cols[1].text.strip().replace('GM\n\n\n', '')
    player_names.append(player_name)
    classical_ratings.append(cols[3].text.strip())
    rapid_ratings.append(cols[4].text.strip())
    blitz_ratings.append(cols[5].text.strip())

data = {
    'Name': player_names,
    'Classical Rating': classical_ratings,
    'Rapid Rating': rapid_ratings,
    'Blitz Rating': blitz_ratings
}

df = pd.DataFrame(data)
df

player_names = []
classical_ratings = []
rapid_ratings = []
blitz_ratings = []

for page in range(1, 11):
    url = f"https://www.chess.com/ratings?page={page}"
    response = requests.get(url)
    chess = BeautifulSoup(response.text, 'html.parser')

    for row in chess.find_all('tr')[1:]:
        cols = row.find_all(['th', 'td'])
        player_name = cols[1].text.strip().replace('GM\n\n\n', '')
        player_names.append(player_name)
        classical_ratings.append(cols[3].text.strip())
        rapid_ratings.append(cols[4].text.strip())
        blitz_ratings.append(cols[5].text.strip())

data1 = {
    'Name': player_names,
    'Classical Rating': classical_ratings,
    'Rapid Rating': rapid_ratings,
    'Blitz Rating': blitz_ratings
}

df1 = pd.DataFrame(data1)
df1

import matplotlib.pyplot as plt
import seaborn as sns

df[['Classical Rating', 'Rapid Rating', 'Blitz Rating']].astype(float).hist(bins=20, figsize=(12, 8))
plt.suptitle('Rating Distributions', x=0.5, y=0.92, ha='center', fontsize='large')
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(95,45))
plt.scatter(df1['Classical Rating'], df1['Rapid Rating'], alpha=0.7)
plt.title('Scatter Plot: Classical vs Rapid Rating')
plt.xlabel('Classical Rating')
plt.ylabel('Rapid Rating')
plt.show()

plt.figure(figsize=(10,8))
plt.plot(df['Name'], df['Classical Rating'], label='Classical Rating', marker='o')
plt.plot(df['Name'], df['Rapid Rating'], label='Rapid Rating', marker='o')
plt.xticks(rotation=90, ha='right')
plt.xlabel('Player Name')
plt.ylabel('Rating')
plt.title('Classical vs Rapid Ratings')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 8))
plt.hexbin(df['Classical Rating'], df['Rapid Rating'], gridsize=25, cmap='viridis')
plt.xlabel('Classical Rating')
plt.ylabel('Rapid Rating')
plt.title('Hexagonal Bin Plot: Classical vs Rapid Ratings')
plt.colorbar(label='Count in Bin')
plt.show()

df[['Classical Rating', 'Rapid Rating', 'Blitz Rating']] = df[['Classical Rating', 'Rapid Rating', 'Blitz Rating']].apply(pd.to_numeric, errors='coerce')

plt.figure(figsize=(10, 8))
sns.heatmap(df[['Classical Rating', 'Rapid Rating', 'Blitz Rating']].corr(), annot=True, cmap='YlGnBu', fmt='.2f')
plt.title('Heatmap of Ratings Correlation')
plt.show()

import bootstrapped.bootstrap as bs
import bootstrapped.stats_functions as bs_stats

classical_lower, classical_upper = str(classical_ci.lower_bound), str(classical_ci.upper_bound)
rapid_lower, rapid_upper = str(rapid_ci.lower_bound), str(rapid_ci.upper_bound)

plt.figure(figsize=(10, 8))
plt.errorbar(x=[classical_lower, classical_upper], y=[rapid_lower, rapid_upper], fmt='o', markersize=8, capsize=5, linestyle='none')
plt.title('Bootstrap Plot: Classical vs Rapid Ratings')
plt.xlabel('Classical Rating')
plt.ylabel('Rapid Rating')
plt.show()

df.nunique()

plt.figure(figsize=(12, 8))
sns.boxplot(data=df[['Classical Rating', 'Rapid Rating', 'Blitz Rating']].astype(float))
plt.title('Boxplot of Rating Categories')
plt.show()
