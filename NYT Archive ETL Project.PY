import requests
import json
from datetime import datetime

abstract = []
source = []
section_name = []
author = []
word_count = []
headline = []
year_flag = True
month_flag = True

while year_flag:
    year = int(input("Please enter a year: "))
    if year <= datetime.now().year:
            year = year
            year_flag = False
            break
    else:
        print("This is not a valid year. Enter a valid year! ")
        continue
    
while month_flag:
    month = int(input("Enter Month: "))
    if month in range(1, 13):
        month = month
        year_flag = False
        break
    else:
        print("[ERROR] Enter a valid month.")
        print("[INFO] month should be in range of 1-12")
        continue

print("""
From below please select the option number:
1) US
2) Opinion
3) Sports
4) World

enter 5 to exit
""")

number = int(input("Enter Number: "))
author_name = input("Enter Author name: ").upper()
key = "XXXX"

print("[INFO] Searching ...")
url = requests.get(f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={key}")



text = json.loads(url.text)

# 
for i in text["response"]["docs"]:
    headline.append(i["headline"]["main"])
    abstract.append(i["abstract"])
    source.append(i["source"])
    section_name.append(i["section_name"])
    name = i["byline"]["original"][2:].strip().upper()
    author.append(name)
    word_count.append(i["word_count"])

print("==================================RESULT==================================")
try:
    real_author = get_close_matches(author_name, author)[0]
    
    print(real_author)
    if number == 1:
        for i in range(0, len(section_name)):
            if section_name[i] == "U.S." and author[i] == real_author:
                print(f"""

                Headline: {headline[i]}
                Abstract: {abstract[i]}
                Source: {source[i]}
                author: {author[i]}
                word count: {word_count[i]}

                ======================================================================================================================================== 

                """)
        
    if number == 2:
        for i in range(0, len(section_name)):
            if section_name[i] == "Opinion" and author[i] == real_author:
                print(f"""

                Headline: {headline[i]}
                Abstract: {abstract[i]}
                Source: {source[i]}
                author: {author[i]}
                word count: {word_count[i]}

                ======================================================================================================================================== 

                """)

    if number == 3:
        for i in range(0, len(section_name)):
            if section_name[i] == "Sports" and author[i] == real_author:
                print(f"""

                Headline: {headline[i]}
                Abstract: {abstract[i]}
                Source: {source[i]}
                author: {author[i]}
                word count: {word_count[i]}

                ======================================================================================================================================== 

                """)


    if number == 4:
        for i in range(0, len(section_name)):
            if section_name[i] == "World" and author[i] == real_author:
                print(f"""

                Headline: {headline[i]}
                Abstract: {abstract[i]}
                Source: {source[i]}
                author: {author[i]}
                word count: {word_count[i]}

                ======================================================================================================================================== 

                """)
except:
    print("No author found")