import pandas as pd

df = pd.read_excel('studentListInCourse-20240907.xls')
df_schools = df['所属院系'].value_counts().reset_index()
df_schools.columns = ['所属院系', 'Count']
#print(df_schools)

import itertools
#print(*df_schools.loc[:, ['所属院系']].values)
#print(*df_schools.loc[:, ['Count']].values)
labels = list(itertools.chain(*df_schools.loc[:, ['所属院系']].values))
sizes = list(itertools.chain(*df_schools.loc[:, ['Count']].values))

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['Heiti TC']

fig, ax = plt.subplots(figsize=(15, 15))
ax.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.title(label="2024/9/7 选课院系分布",
          fontsize=20,
          loc="left",
          color="green")
plt.show()
