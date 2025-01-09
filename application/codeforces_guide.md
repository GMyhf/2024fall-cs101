# 抓取codeforce.com题目数据并分析统计

Updated 0801 GMT+8 Jan 9 2025

2024 fall, Complied by Hongfei Yan



课程中练习到一些codeforce.com（简记为CF）上面题目，因此希望统计出CF的题目类型、难度分布。在2023年9月4日，我们通过spider直接抓取题目列表页面，然后进行分析统计（https://github.com/GMyhf/2019fall-cs101/blob/master/20230904_CFTagDifficultyDistribution.md）。但是CF封禁程序抓取，改程序已经失效。因此直接利用CF提供的API获得题目数据，然后分析统计。



# codeforces提供的API

https://codeforces.com/apiHelp/objects

### Problem

Represents a problem.

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

### ProblemStatistics

Represents a statistic data about a problem.

| Field       | Description                                                  |
| :---------- | :----------------------------------------------------------- |
| contestId   | Integer. Can be absent. Id of the contest, containing the problem. |
| index       | String. Usually, a letter or letter with digit(s) indicating the problem index in a contest. |
| solvedCount | Integer. Number of users, who solved the problem.            |





```python
import requests

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

# 调用函数并打印结果
problems = fetch_problems()
if problems:
    for problem in problems:
        print(problem)
else:
    print("Failed to fetch the problems.")
```





# 附录

## 1.不通过api，直接抓取网页失败

![image-20250109075718170](https://raw.githubusercontent.com/GMyhf/img/main/img/202501090757043.png)



```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# 设置Chrome选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式，不打开浏览器窗口
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 指定WebDriver的位置
service = ChromeService(executable_path='/Users/hfyan/chromedriver-mac-arm64/chromedriver')

# 创建WebDriver对象
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    url = "https://codeforces.com/problemset/page/1"
    
    # 访问目标网址
    driver.get(url)
    
    # 等待页面加载完成
    wait = WebDriverWait(driver, 30)  # 增加超时时间
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.problem-code')))  # 等待所有问题的链接加载
    
    # 获取页面源代码
    page_source = driver.page_source
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # 找到所有问题链接
    problem_links = soup.find_all('a', class_='problem-code')
    
    for link in problem_links:
        problem_name = link.text.strip()
        problem_url = link['href']
        print(f"Problem: {problem_name}, URL: {problem_url}")

finally:
    # 关闭浏览器
    driver.quit()
```

