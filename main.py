from bs4 import BeautifulSoup
import requests

fetching_data = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=node+js&txtLocation=').text

soup = BeautifulSoup(fetching_data,'lxml')

# print(fetching_data)

all_question = soup.find('li',class_='clearfix job-bx wht-shd-bx')

# print(all_question)

questions = all_question.find('h3',class_='joblist-comp-name').text

print(questions)