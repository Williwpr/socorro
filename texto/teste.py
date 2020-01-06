import re
import os

content = ""

pattern = "\d{1,2}[./-]\d{1,2}[./-]\d{4}" #and "\d{1,}.txt"

# Open the file that you want to search
for filename in os.listdir('/home/wpr/Desktop/teste/texto'):
    if filename.endswith('.txt'):


    	
    	with open(os.path.join('/home/wpr/Desktop/teste/texto', filename)) as f:
        	content += f.read()
        	dates = re.findall(pattern, content)


print(dates)
f.close()