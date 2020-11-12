#Ref:https://gist.github.com/jenningsb2/2d94bc286b5fafe878c9e493a0286298


import re
import os
from dateutil.parser import parse

path = '' #insert file path to your vault here
for root, dirs, files in os.walk(path):
    for f in files:
        fullpath = (os.path.join(root, f))
        with open(fullpath, 'r') as f: #opens each .md file 
            contents = f.read() #reads the contexts
            #substitutes dates with the format [[April 20th, 2020]] for [[2020-04-20]]
            new_contents = re.sub(r'(?<=\[)[\w]+\s\d{1,2}\w{1,2},\s\d{4}(?=\])',
                                  lambda x: str(parse(x.group(0), ignoretz=True)).split(" ")[0], contents, flags=re.M)
        with open(fullpath, 'w') as f:
            f.write(new_contents) #writes the files with the new substitutions
