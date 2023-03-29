import json

# Open the JSON file and load its contents as a Python dictionary
with open('meta_data.json', 'r') as f:
    data = json.load(f)

# Print the dictionary
print(data['chunk_0'])
