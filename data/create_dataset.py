import csv 
import json 


# Function to convert a CSV to JSON 
# Takes the file paths as arguments 
def make_json(csvFilePath, jsonFilePath):
    # create a dictionary 
    data = {}
    data['vocabs']='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    temp_list = []

    # Open a csv reader called DictReader 
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.reader(csvf)
        
        # Convert each row into a dictionary 
        # and add it to data 
        for rows in csvReader: 
            temp_dict = {}
            # Assuming a column named 'No' to 
            # be the primary key 
            temp_dict['text'] = rows[1]
            temp_dict['name'] = rows[0]
            temp_list.append(temp_dict)

    data['train'] = temp_list
    # Open a json writer, and use the json.dumps() 
    # function to dump data 
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonf.write(json.dumps(data, indent=4))

# Driver Code 

# Decide the two file paths according to your 
# computer system 
csvFilePath = r'dataset.csv'
jsonFilePath = r'license_dataset.json'

# Call the make_json function 
make_json(csvFilePath, jsonFilePath)
