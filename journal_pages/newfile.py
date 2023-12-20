from datetime import date
import os
today = date.today().strftime("%d%m%y")
filepath = os.path.join(r'C:\Users\kieren\Documents\website\journal_pages', today+".txt")
f = open(filepath, "a")
f.close()
