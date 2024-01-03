import webbrowser
import os
from git import Repo
PATH_OF_GIT_REPO = r'C:\Users\kieren\Documents\website\.git'
x = input("What is the file name? DDMMYY \n")
def edithtml():


    html_string_to_add = f'\n<font size="+1"><a href="./journal_pages/{x}.txt">{x}</a></font> <br>'

    # Specify the path to your HTML file
    html_file_path = 'C:\\Users\\kieren\\Documents\\website\\journal.html'

    # Open the HTML file in append mode
    with open(html_file_path, 'a') as html_file:
        # Append the HTML string to the file
        html_file.write(html_string_to_add)

    print(f"The HTML string has been added to {html_file_path}")

    # Open the modified HTML file in a web browser
    webbrowser.open(html_file_path, new=2)
    pushgit()
    
def pushgit():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(".")
        repo.index.commit(x)
        origin = repo.remote(name='origin')
        origin.push()
        webbrowser.open("https://github.com/yarshys/website")
    except:
        print('Some error occured while pushing the code')    
edithtml()
