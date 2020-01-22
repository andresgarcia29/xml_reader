import os
import re
from os import listdir
from os.path import isfile, join

SPACE = '\n'
CONDITION = 4

def get_files_from_directory(path):
    return [join(path, file) for file in listdir(path) if isfile(join(path, file))]

def remove_tags(item):
    tags = ['<text>', '</text>']
    for tag in tags:
        item = item.replace(tag, '')
    return item

def check_condition(text):
    return len(text) >= CONDITION

def get_information_from_file(file, data):
    with open(file, 'r') as xml:
        text = xml.read()
        results = re.findall('<text>[\s\S]*?<\/text>', text)
        for result in results:
            clean_text = remove_tags(result)
            if check_condition(clean_text):
                data.append(clean_text)

def main():
    print('Starting Program')

    path = './files/'
    files = get_files_from_directory(path)

    data = list()
    for file in files:
        get_information_from_file(file, data)

    for item in data:
        with open('results.csv', 'a') as file:
            file.write(item + SPACE)

if __name__ == "__main__":
    main()