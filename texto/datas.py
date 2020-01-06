import re
import os

content = ""
nome_arquivo = ""

# Open the file that you want to search
for filename in os.listdir('/home/wpr/Desktop/teste/texto'):
    if filename.endswith('.txt'):
    	with open(os.path.join('/home/wpr/Desktop/teste/texto', filename)) as f:
        	content += f.read()
        
# 	f = open("117930.txt", "r")

# Will contain the entire content of the file as a string
#content = f.read()

# The regex pattern that we created
pattern = "\d{1,2}[./-]\d{1,2}[./-]\d{4}"

# Will return all the strings that are matched
dates = re.findall(pattern, content)
print(dates)
f.close()
##########################################################################################################
# https://stackoverflow.com/questions/50532578/convert-multiple-txt-files-into-single-csv-file-python
# https://docs.python.org/3/library/csv.html
import re
import os

content = ""

pattern = "\d{1,2}[./-]\d{1,2}[./-]\d{4}" 
#and "\d{1,}.txt"

# Open the file that you want to search
for filename in os.listdir('/home/wpr/Desktop/teste/texto'):
    if filename.endswith('.txt'):
    	with open(os.path.join('/home/wpr/Desktop/teste/texto', filename)) as f:
        	content += f.read()
        	dates = re.findall(pattern, content)


#dates = re.findall(pattern, content)
print(dates)
f.close()