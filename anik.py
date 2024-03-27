import json
import pandas as pd
import os
json_file=("output1.json")
    # Load the JSON data from the file
with open(json_file, 'r') as file:
    data = json.load(file)
    print(len(data))
 # Define the range
with open('output.txt', 'w') as file:
        start = 0
        end = 199
        for nik in data:
            for num in range(start, end + 1):
                print(num)
                domain = nik[num]['domain']
                print(domain)
                file.write(domain + '\n')
