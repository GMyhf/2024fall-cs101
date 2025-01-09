# 抓取codeforce.com题目元数据并分析统计

Updated 1836 GMT+8 Jan 9 2025

2024 fall, Complied by Hongfei Yan



课程中练习到一些codeforce.com（简记为CF）题目，因此希望统计出CF的题目类型（标签）、难度（编号中的字母）分布。在2023年9月4日，我们通过spider直接抓取题目列表页面，NLP提取，然后进行分析统计（https://github.com/GMyhf/2019fall-cs101/blob/master/20230904_CFTagDifficultyDistribution.md）。由于CF很容易封禁程序抓取，因此改用CF提供的API获得题目数据，然后分析统计。



## 1.查看题目页面确定CF题目元数据

![image-20250109155116617](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20250109155116617.png)

题目列表中第一列是数字和字母组合，表示题目编号和字母序增大的难度（Usually, a letter or letter with digit(s) indicating the problem index in a contest），即`{problem['contestId']}{problem['index']}`；

第二列是标题（name），即`problem.get('name', '')`；

第三列是标签（tags），即`problem.get('tags', [])`；

倒数第二列是问题难度（rating (difficulty)），即`problem.get('rating', [])`；

倒数第一列是完成题目人数（Number of users, who solved the problem），即`stat.get('solvedCount', 0)`。



## 2.找到codeforces提供的API

https://codeforces.com/apiHelp/objects

**Problem**: Represents a problem.

| Field          | Description                                                  |
| :------------- | :----------------------------------------------------------- |
| contestId      | Integer. Can be absent. Id of the contest, containing the problem. |
| problemsetName | String. Can be absent. Short name of the problemset the problem belongs to. |
| index          | String. Usually, a letter or letter with digit(s) indicating the problem index in a contest. |
| name           | String. Localized.                                           |
| type           | Enum: PROGRAMMING, QUESTION.                                 |
| points         | Floating point number. Can be absent. Maximum amount of points for the problem. |
| rating         | Integer. Can be absent. Problem rating (difficulty).         |
| tags           | String list. Problem tags.                                   |

**ProblemStatistics**: Represents a statistic data about a problem.

| Field       | Description                                                  |
| :---------- | :----------------------------------------------------------- |
| contestId   | Integer. Can be absent. Id of the contest, containing the problem. |
| index       | String. Usually, a letter or letter with digit(s) indicating the problem index in a contest. |
| solvedCount | Integer. Number of users, who solved the problem.            |



## 3.抓取元数据并保存

代码 cf_guide-1.py

```python
import requests
import os
import csv


def fetch_problems():
    # 定义API URL
    url = "https://codeforces.com/api/problemset.problems"

    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查是否发生HTTP错误

        data = response.json()

        if data['status'] != 'OK':
            print(f"API call failed with comment: {data['comment']}")
            return None

        problems = data['result']['problems']
        problem_stats = data['result']['problemStatistics']

        # 将问题和统计信息组合起来
        combined_data = []
        for problem in problems:
            problem_id = f"{problem['contestId']}{problem['index']}"
            for stat in problem_stats:
                if stat['contestId'] == problem['contestId'] and stat['index'] == problem['index']:
                    combined_data.append({
                        'id': problem_id,
                        'name': problem.get('name', ''),
                        'tags': problem.get('tags', []),
                        'rating': problem.get('rating', 0),
                        'solvedCount': stat.get('solvedCount', 0),
                    })
                    break

        return combined_data

    except requests.exceptions.HTTPError as e:
        print("HTTP error occurred:", e)
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None


# 调用函数并保存结果
problems = fetch_problems()
if problems:
    # for problem in problems:
    # print(problem)
    # %% output the problem set to csv files
    root = os.getcwd()
    with open(os.path.join(root, "CodeForces-ProblemSet.csv"), "w", encoding="utf-8") as f_out:
        f_csv = csv.writer(f_out)
        f_csv.writerow(['ID', 'Name', 'Tags', 'Rating', 'SolvedCount'])
        for row in problems:
            print(row)
            f_csv.writerow([row['id'], row['name'], ','.join(row['tags']), row['rating'], row['solvedCount']])
        f_out.close()
else:
    print("Failed to fetch the problems.")

```



## 4.分析和保存

代码 cf_guide-2.py

```python
import csv
import os
import re

root = os.getcwd()
filepath = os.path.join(root, "CodeForces-ProblemSet.csv")

codeforces = {}

with open(filepath, "r", encoding="utf-8") as f_in:
    f_csv = csv.reader(f_in)
    header = next(f_csv)  # 读取文件头
    for row in f_csv:
        id = row[0]
        if id == "ID":
            continue

        name = row[1]
        tags = row[2].split(",")
        tags = [tag.strip() for tag in tags]
        rating = row[3]
        solvedCount = row[4]
        codeforces[id] = {'name': name, 'tags': tags, 'rating': rating, 'solvedCount': solvedCount}
    f_in.close()

# %% analyze the problem set
# initialize the difficult and tag list
difficult_level = {}
tags_level = {}
for id in codeforces:
    match = re.findall('([A-Z])', id)
    if match:
        difficult = match[0]
        tags = codeforces[id]['tags']
        difficult_level[difficult] = difficult_level.get(difficult, 0) + 1
        for tag in tags:
            tags_level[tag] = tags_level.get(tag, 0) + 1


tag_level = sorted(tags_level.items(), key=lambda x: x[1], reverse=True)
tag_list = [_[0] for _ in tag_level]
print(tag_list)

difficult_level = sorted(difficult_level.items())
difficult_list = [_[0] for _ in difficult_level]
print(difficult_list)

# initialize the 2D relationships matrix
# matrix_freq: the number of tag frequency for each difficult level
matrix_freq = [[0] * len(difficult_list) for _ in range(len(tag_list))]

# construct the 2D relationships matrix
for id in codeforces:
    match = re.findall('([A-Z])', id)
    if match:
        difficult = match[0]
        difficult_id = difficult_list.index(difficult)
        tags = codeforces[id]['tags']
        for tag in tags:
            tag_id = tag_list.index(tag)
            matrix_freq[tag_id][difficult_id] += 1

# %% visualization
root = os.getcwd()
def outputMatrix(name, data):
    with open(os.path.join(root, name), "w", encoding="utf-8") as f_out:
        f_csv = csv.writer(f_out)
        f_csv.writerow(['Tags/Difficult '] + difficult_list)
        for i in range(len(tag_list)):
            tag = tag_list[i]
            f_csv.writerow([tag] + data[i])
        f_out.close()
    return

outputMatrix('Matrix-Freq.csv', matrix_freq)
```



## 5.可视化

代码 heapmap_Matrix-Freq.py

```python
# ref: https://stackoverflow.com/questions/37790429/seaborn-heatmap-using-pandas-dataframe
# https://seaborn.pydata.org/generated/seaborn.heatmap.html
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Matrix_Freq = pd.read_csv("Matrix-Freq.csv", index_col=0)
#print(Matrix_Freq)

fig, ax = plt.subplots(figsize=(14, 9))

sns.heatmap(Matrix_Freq, annot=True, fmt="d", linewidths=.5, cmap='viridis')

plt.show()
```



结果程序。pychar中运行这个可视化，竟然很多单元格是空的，找了半天找不到bug。在anaconda/spyder中运行，可视化结果正常如下。

![image-20250109183346524](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20250109183346524.png)



