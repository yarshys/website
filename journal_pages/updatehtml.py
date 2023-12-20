import webbrowser
import os
def edithtml():

    x = input("What is the file name? DDMMYY \n")
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

edithtml()
