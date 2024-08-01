import sys
sys.path.append('/mymodule/')
import mymodule
from mymodule.mathy import *
print(responces[0])
print(responces[1])
while True:
   print()
   text=input("Enter some text: ")
   for word in text.split(" "):
      if word.upper() in operations.keys():
         try:
            l=extract_numbers_from_text(text)
            r=operations[word.upper()] (l[0],l[1])
            print(r)
         except:
            print("Something is wrong please retry")
         finally:
            break
      elif word.upper() in commands.keys():
         commands[word.upper()]()
         break
   else:
      sorry()