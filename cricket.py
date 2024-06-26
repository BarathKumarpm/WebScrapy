# -*- coding: utf-8 -*-

!pip install scrapy-poet

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/t20i")
print(r)

r.text

r.content

t20 = BeautifulSoup(r.text,"html.parser")
t20

print(t20.prettify())

t20.title

t20.title.string

t20.title.parent.name

o = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
o

o.text

o.content

odi = BeautifulSoup(o.text,"html.parser")
odi

print(odi.prettify())

t = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/test")
t

t.text

t.content

test = BeautifulSoup(t.text,"html.parser")
test

print(test.prettify())

ranking = []
for row in t20.find_all('tr')[1:]:
  columns = row.find_all('td')
  team = columns[1].text.strip().split()[-1].replace('\n', '')
  matches = int(columns[2].text.strip())
  points = int(columns[3].text.strip().replace(',', ''))
  rating = int(columns[4].text.strip())
  ranking.append([team, matches, points, rating])

columns = ['Team', 'Matches', 'Points', 'Rating']
df = pd.DataFrame(ranking, columns=columns)
df

ranking1 = []
for row in odi.find_all('tr')[1:]:
  columns = row.find_all('td')
  team = columns[1].text.strip().split()[-1].replace('\n', '')
  matches = int(columns[2].text.strip())
  points = int(columns[3].text.strip().replace(',', ''))
  rating = int(columns[4].text.strip())
  ranking1.append([team, matches, points, rating])

columns = ['Team', 'Matches', 'Points', 'Rating']
df1 = pd.DataFrame(ranking1, columns=columns)
df1

ranking2 = []
for row in test.find_all('tr')[1:]:
  columns = row.find_all('td')
  team = columns[1].text.strip().split()[-1].replace('\n', '')
  matches = int(columns[2].text.strip())
  points = int(columns[3].text.strip().replace(',', ''))
  rating = int(columns[4].text.strip())
  ranking2.append([team, matches, points, rating])

columns = ['Team', 'Matches', 'Points', 'Rating']
df2 = pd.DataFrame(ranking2, columns=columns)
df2

columns1 = ['Team', 'Matches', 'Points', 'Rating']
columns2 = ['Team', 'Matches', 'Points', 'Rating']
columns3 = ['Team', 'Matches', 'Points', 'Rating']

df = pd.DataFrame(ranking, columns=columns)
df1 = pd.DataFrame(ranking1, columns=columns)
df2 = pd.DataFrame(ranking2, columns=columns)

df3 = pd.concat([df,df1, df2], ignore_index=True)
df3

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
plt.plot(df3['Team'][:10], df3['Points'][:10], marker='o', label='Points')
plt.plot(df3['Team'][:10], df3['Matches'][:10], marker='o', label='Matches')
plt.title('Comparison of Points and Matches for Teams (First 10 values)')
plt.xlabel('Team')
plt.ylabel('Value')
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.show()

heatmap_data = df3.pivot(index='Team', columns='Rating', values='Points')
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, cmap='viridis')
plt.title('Heatmap of Points by Team and Rating')
plt.xlabel('Rating')
plt.ylabel('Team')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df3['Rating'][:10], bins=5, color='blue', edgecolor='black')
plt.title('Histogram of Ratings (First 10 values)')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
plt.hexbin(df3['Matches'][:10], df3['Points'][:10], gridsize=15, cmap='plasma')
plt.title('Hexagonal Bin Plot: Matches vs Points (First 10 values)')
plt.xlabel('Matches')
plt.ylabel('Points')
plt.colorbar()
plt.show()

print(df.to_string())

columns = ['Team', 'Matches', 'Points', 'Rating']
df = pd.DataFrame(ranking, columns=columns)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)

plt.hist(df['Rating'], bins=10, color='blue', edgecolor='black')
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')

plt.figure(figsize=(30, 16))
plt.subplot(2, 1, 2)

plt.plot(df['Team'], df['Points'], marker='o', color='green', label='Points')
plt.plot(df['Team'], df['Matches'], marker='o', color='red', label='Matches')
plt.title('Team Performance')
plt.xlabel('Team')
plt.ylabel('Points')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 20))
plt.subplot(3, 1, 3)

plt.hexbin(df['Matches'], df['Points'], gridsize=15, cmap='plasma')
plt.title('Hexagonal Bin Plot: Matches vs Points')
plt.xlabel('Matches')
plt.ylabel('Points')
plt.colorbar()
plt.tight_layout()
plt.show()
