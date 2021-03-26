## Part B Task 1

import re
import pandas as pd
import os

directory = 'cricket'
df = pd.DataFrame(columns = ['Filename', 'Document ID'])

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        
        continue
    else:
        continue

df.to_csv("test.csv", index = False)

#REGEX IS [A-Z]{4}\-\d{3}[A-Z]{0,1}