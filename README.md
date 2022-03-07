## NYT Best Sellers Optimized Searcher BETA
Using the Best Sellers API from The New York Times,  my application (which is in BETA) looks through the main NYT's API for the best sellers of this month and gives a result based on the user's input of either a book's title, ISBN, or author. When the user gives a close enough query (5 characters or more),  the book, (if it is a best seller for the current month the user is in), is fetched along with the book's title, description, contribute, price, author, and finally ISBN numbers. 

**FOR TEST, ENTER THE .JSON FILE INTO YOUR URL AND CHECK FOR THE KEYS IN ORDER TO SEE THE TITLE, ISBN, AND AUTHOR.**

https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key= {YOUR_API_KEY}

---

## Packages

The following are packages I used for this BETA application:

- [Import Requests](https://docs.python.org/3/library/urllib.request.html?highlight=requests) 
	- I use this package to help me do a URL request for The New York Times API
- [Import json](https://docs.python.org/3/library/json.html?highlight=json)
	- I use this package to help me load the .json directly from The New York Times API
- [Difflib --> get_close_matches](https://docs.python.org/3/library/difflib.html?highlight=get_close_matches)
	- I use the Difflib package to help me import the algorithmic searcher get_close_matches. This will help with using an optimized searcher and it will also condense the amount of code I would have to write.
- Extra packages
	- From the GUI aspect of this project (which is incomplete but I still thought it would be nice to mention).....
		- [I used the tkinter package](https://docs.python.org/3/library/tkinter.html): to help create a crude application interface for my script. It made a search box with it along with a button you can click to initiate your search query. 
		- [I also imported multiprocessing threading.](https://docs.python.org/3/library/multiprocessing.html?highlight=multiprocessing#module-multiprocessing) When I was watching a tutorial on tkinter, it was mentioned that for opening images or anything graphically related, Importing multiprocessing can optimize the GUI for the device it is run on. This would help speed up the application by using different paths running in parallel on the computer.  

---

## Intro block
In the non-GUI version of my code, I start out by importing the following packages/libraries. These are: requests, json, and difflib's get_close_matches.
These packages are very essential to the working of the code as they respectively serve the following purposes: allowing for URL requests, allowing for utilization of the .json file, searching for close keywords via algorithmic matching.  
```python
import requests
# allowing for the utilization of the requests package and its functions
import json
# allowing for utilization of the .json
from difflib import get_close_matches
# searching for close keywords via algorithmic matching
```
I continue my code by creating empty lists for the information that I am hoping to return to the user via terminal with appended information snatched from The New York Times Best Seller API.  These are the lists I created:

```python
title = []
description = []
contributer = []
price = []
author = []
isbns = []
Script_Switch = True
```
Next, for PEP-8 optimization, I attempted to save line space by creating a variable named "key" which would store The New York Time's Developer API key that would allow me to gain access to the Best Sellers API directory. I also create a variable called "url" and set it to the requests function (using the request package) of the URI for The New York Time's Best Seller API.

```python
key = "XXXX"
url = requests.get(f'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key={key}')
```

## Iterative Block
In this block, I start off my code by loading the .json of the Best Sellers API and setting it the variable "NYTS_API_JSON_FILE". I'm doing this so I can can create a cleaner iteration. Also, it helps me keep track of what I am doing. 
```python
NYTS_API_JSON_FILE = json.loads(url.text)
```
Next, I start my iteration. I begin iterating over the .json via a for loop. I could have chosen to enumerate, however, I tend to save enumeration for iterative loops of objects that are too big for me to calculate. Also, I didn't have to use a counting variable for this "for loop" iteration, so I didn't feel prompted to investigate any further with enumerate. 
In the iteration block, I have the for loop create a temporary variable named index as it goes through the ["result"] key of the targeted .json variable (named "NYTS_API_JSON_FILE"). Next, as this loop is going on, I have the targeted information from the sub keys of the initial key append respectively to the blank lists that I created in the beginning of the script. 
Next, I made a variable called Script_Switch and set it to the bool True. This will come in handy later on in the script when I attempt to have the code run in a loop unless a condition is specified.

- I also do something else as well: I had the iterated index for the subkey ["title"] and ["author"] set to a string method that would make their internal information UPPERCASED via the .upper() string method
	- What does this mean? Essentially, the information stored in these two specific lists will be matched as uppercase characters. However, they won't print as uppercase character (this will be explained later).
```python
for index in NYTS_API_JSON_FILE["results"]:
    title.append(index["title"][1:].upper())
    description.append(index["description"])
    contributer.append(index["contributor"])
    author.append(index['author'].upper())
    price.append(index['price'])
    isbns.append(index["isbns"])
```
## Final Block: User interaction/data retrieval block
Finally, in this block, the goal was to start a process that would take the user's input[s]. I started out this block with a message directing the user what to do so they could successfully interact with the script:

```python
print(
    "Please pick an option for your search of the NYT's most recent Best Sellers List. \n The more characters you put in for your querey (< 5) the better the result!"
)
```
Next, I wanted to take some things into consideration. One of the main questions I had thought of was how did I want to end my code? Perhaps this seems early as I have not even thought of the user input retrieval process or the data retrieval as well, however, I wanted to think of how the ways I would terminate the code. 

For instance, if a user entered a wrong selection, would the code terminate or would there be a loop until the user entered the right input? Would I also present a termination function to the script? These were all things I considered. 

Eventually, I came to the conclusion of using a while loop along with some nested try/except-exception conditions. 

Looking at the first bit of the block I started with the while loop being on the condition of what variable Script_Switch was set to. Script_Switch was set to True in the beginning of the script so that it would run the contents underneath it starting beginning with the try statement, I printed to the screen some options that a user could do with the script which included Searching the Best Sellers API via Title, ISBN, or Author. The user can also choose to terminate this script.
```python
while Script_Switch:
    try:
        print("1. Search with Title ")
        print("2. Search with ISBN")
        print("3. Search with Author")
        print("4. Quit")
```

I made a variable called option and hard set it to an integer-input. This would mean that the user MUST put in an integer otherwise the user would be forced into the **except Exception** sub-block at the end of the script telling them some error happened. I then went on to make 4 conditional statements each set to the corresponding integer from the printed list and set that to the option variable. This, in turn, would create a selection that the user can choose to search with. For example, if the user wanted to search via author name, they would need to respond to the  `option = int(input(">>>"))` with an integer of 3 then proceeded to type the name of the title with (for more accurate measures) about 5 or more characters.  

-I mentioned earlier that for the title and author selection, I used a string method that would set the listed data to uppercase inputs. I did the same thing for the user input for option 1 and option 3 as it would help the script recognize anything that the user typed would be passed through and recognized as the same character. For example, if the user used a combination of uppercase and lowercase characters, it would still respond with all uppercase letters due to the string upper() method. 

-For each option I use the get_close_matches method from the difflib package and set it to a variable labeled as optimized_search. This will help take the users input and use the matching algorithm within the method to respond with a good enough search result.  

-For option 4, I made the variable Script_Switch = False. This, within the Python interpreter, would break the loop and quit the application as the loop can only run so far as the Script_Switch = True. 

```python
while Script_Switch:
    try:
        print("1. Search with Title ")
        print("2. Search with ISBN")
        print("3. Search with Author")
        print("4. Quit")
        option = int(input(">>>"))
        if option == 1:
            search = input("Enter title: ").upper()
            print("[INFO] Searching ...")
            optimized_search = get_close_matches(search, title)
            if optimized_search != []:
                location = title.index(optimized_search[1])
                print(
                    "===RESULT==="
                )
                print(f"""
                    Title: {title[location]}
                    Description: {description[location]}
                    Contributor: {contributer[location]}
                    price: {price[location]}
                    author: {author[location]}
                    isbns: {isbns[location]}
                """)
            else:
                print("OOPS! Entered Query is not matched \n")
        elif option == 2:
            search = input("Enter ISBN: ")
            print("[INFO] Searching ...")
            optimized_search = get_close_matches(search, isbns)
            if optimized_search != []:
                location = isbns.index(optimized_search[0])
                print(
                    "===RESULT==="
                )
                print(f"""
                    Title: {title[location]}
                    Description: {description[location]}
                    Contributor: {contributer[location]}
                    price: {price[location]}
                    author: {author[location]}
                    isbns: {isbns[location]}
                """)
            else:
                print("OOPS! Entered Query is not matched \n")
        elif option == 3:
            search = input("Enter author's name: ").upper()
            print("[INFO] Searching ...")
            optimized_search = get_close_matches(search, author)
            if optimized_search != []:
                location = author.index(optimized_search[0])
                print(
                    "===RESULT==="
                )
                print(f"""
                    Title: {title[location]}
                    Description: {description[location]}
                    Contributor: {contributer[location]}
                    price: {price[location]}
                    author: {author[location]}
                    isbns: {isbns[location]}
                """)
            else:
                print("OOPS! Entered Query is not matched \n")
        elif option == 4:
          print("End of application! ")
          Script_Switch = False
        else:
            print("Hmm! Not a valid option try agian :) \n")
    except Exception as e:
        print("[ERROR] OOPS! something went wrong, try again! \n")
```


## What I Would do Next
There is actually a version of this code that uses the Tkinter GUI. It is largely incomplete and can only search by title, however, if I had more time I would certainly work on it more.  When I started out this project, I wanted to do more with the code so that the GUI would display a mini application where you would be able to have a somewhat crude but good enough interface that would allow you to sift through the Best Sellers API. 

(This version of the code will be presented at the very bottom). 

Much of my project initially relied on the GUI being the "charm" however the the standard terminal perhaps suffices enough. I watched many tutorials on using Tkinter's package which also gave me insights on parallel threading and multiprocessing. 

Also, when you run either code varaints, for a user who doesn't know what's going on, it could seem that you will never get a result. For this code DEMO (I guess this is in BETA ?) it would help if you had the .json file as an example to test out if the inputs really work.

**FOR TEST, ENTER THE .JSON FILE INTO YOUR URL AND CHECK FOR THE KEYS IN ORDER TO SEE THE TITLE, ISBN, AND AUTHOR.**

https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key={YOUR API KEY}

## Main code for the project



```python
import requests
import json
from difflib import get_close_matches

title = []
description = []
contributer = []
price = []
author = []
isbns = []


key = "YOU KEY GOES HERE!!!!"
url = requests.get(
    f'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key={key}'
)

text = json.loads(url.text)
for index in text["results"]:
    title.append(index["title"][1:].upper())
    description.append(index["description"])
    contributer.append(index["contributor"])
    author.append(index['author'].upper())
    price.append(index['price'])
    isbns.append(index["isbns"])

print(
    "Please pick an option for your search of the NYT's most recent Best Sellers List. \n The more characters you put in for your querey (< 5) the better the result!"
)

while True:
    try:
        print("1. Search with Title ")
        print("2. Search with ISBN")
        print("3. Search with Author")
        print("4. Quit")
        opt = int(input(">>>"))
        if opt == 1:
            search = input("Enter title: ").upper()
            print("[INFO] Searching ...")
            optimized_search = get_close_matches(search, title)
            if optimized_search != []:
                location = title.index(optimized_search[1])
                print(
                    "===RESULT==="
                )
                print(f"""
                    Title: {title[location]}
                    Description: {description[location]}
                    Contributor: {contributer[location]}
                    price: {price[location]}
                    author: {author[location]}
                    isbns: {isbns[location]}
                """)
            else:
                print("OOPS! Entered Query is not matched \n")
        elif opt == 2:
            search = input("Enter ISBN: ")
            print("[INFO] Searching ...")
            optimized_search = get_close_matches(search, isbns)
            if optimized_search != []:
                location = isbns.index(optimized_search[0])
                print(
                    "===RESULT==="
                )
                print(f"""
                    Title: {title[location]}
                    Description: {description[location]}
                    Contributor: {contributer[location]}
                    price: {price[location]}
                    author: {author[location]}
                    isbns: {isbns[location]}
                """)
            else:
                print("OOPS! Entered Query is not matched \n")
        elif opt == 3:
            search = input("Enter author's name: ").upper()
            print("[INFO] Searching ...")
            optimized_search = get_close_matches(search, author)
            if optimized_search != []:
                location = author.index(optimized_search[0])
                print(
                    "===RESULT==="
                )
                print(f"""
                    Title: {title[location]}
                    Description: {description[location]}
                    Contributor: {contributer[location]}
                    price: {price[location]}
                    author: {author[location]}
                    isbns: {isbns[location]}
                """)
            else:
                print("OOPS! Entered Query is not matched \n")
        elif opt == 4:
            print("End of application! ")
            flag = False
        else:
            print("Hmm! Not a valid option try agian :) \n")
    except Exception as e:
        print("[ERROR] OOPS! something went wrong, try again! \n")

```
----
---
---
---
## GUI version of the code
```python
from tkinter import *
# this loads the tkinter package and allows
# the use of the Tk Interface GUI tool kit.
import requests
import json
from difflib import get_close_matches
# get close matches allows for seeking through
# the targeted data object for specifc keywords
# in the case it will find near similar keys
# and return the value pairs throughout the
#.json file

import multiprocessing

title = []
description = []
contributer = []
price = []
author = []
isbns = []


# Empty lists are created to be appended later on
# with the information targeted/found in the .json

key = "YOUR KEY"
url = requests.get(
    f'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key={key}'
)

# A variable "url" is set to the NYT's API best-seller
# of the month key. The key of the API is set
# to a variable and later passed through the
# url's requests.get()

NYT_JSON_FILE = json.loads(url.text)
for index in NYT_JSON_FILE["results"]:
  title.append(index["title"][1:].upper())
  description.append(index["description"])
  contributer.append(index["contributor"])
  author.append(index['author'])
  price.append(index['price'])
  isbns.append(index["isbns"])


# the lists created from the start 
# are appended and with the information
# found in the .json file via difflib's
# get_close_matches

print("[INFO] READY")

root = Tk()
search = Entry()
search.grid(row=0, column=0)
area = Text(root, height=50)
area.grid(columnspan=2)

def get_text():
    area.insert(END, "[INFO] Searching ... \n")

    optimized_search = get_close_matches(search.get().upper() , title)
    if optimized_search != []:
        location = title.index(optimized_search[0])
        area.insert(INSERT, "==================================RESULT================================== \n")
        area.insert(END, f" Title: {title[location]} \n Description: {description[location]}]\n Contributor: {contributer[location]} \n price: {price[location]} \n author: {author[location]} \n isbns: {isbns[location]}\n\n")
    else:
        area.insert(END, "OOPS! Entered Query is not matched \n\n")


btn_ipadx = Button(root, text="Search", command=lambda:get_text())
btn_ipadx.grid(row=0, column=1)
root.mainloop()
```

