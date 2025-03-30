import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title=[]
job_name=[]
location_name=[]
job_skill=[]
links=[]
page_num=0


while True:
    result= requests.get(f"https://wuzzuf.net/search/jobs/?a=navbg&q=General%20Accountant&start={page_num}")

    src=result.content

    soup=BeautifulSoup(src,"lxml")

    job_titles= soup.find_all("h2",{"class":"css-m604qf"})

    job_names= soup.find_all("a",{"class":"css-17s97q8"})

    locations_name=soup.find_all("span",{"class":"css-5wys0k"})

    job_skills =soup.find_all("div",{"class":"css-y4udm8"})

    for i in range(len(job_titles)):
        job_title.append(job_titles[i].text)

        links.append(job_titles[i].find("a").attrs['href'])

        job_name.append(job_names[i].text)

        location_name.append(locations_name[i].text)

        job_skill.append(job_skills[i].text)
    page_num+=1
    print("ps")
    if (page_num==100):
        print("break")
        break


file_list=[job_title,job_name,location_name,job_skill,links]

exported=zip_longest(*file_list)

with open("D:/ws/test.csv","w", newline='') as my_file:

    wr =csv.writer(my_file)

    wr.writerow(['job_titel','company name','location','skills','link'])

    wr.writerows(exported)
