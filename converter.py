import json

# Read the text data from the file
with open('moz_data.txt', 'r') as file:
    text_data = file.readlines()

# Convert the text data into a list of dictionaries
list_of_dicts = [json.loads(line.strip()) for line in text_data]

# Write the list of dictionaries to a JSON file
with open('output1.json', 'w') as json_file:
    json.dump(list_of_dicts, json_file, indent=4)

