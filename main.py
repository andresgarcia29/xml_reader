import os
import re
from os import listdir
from os.path import isfile, join

SPACE = '\n'

def get_files_from_directory(path):
    return [join(path, file) for file in listdir(path) if isfile(join(path, file))]

def remove_tags(item):
    tags = ['<text>', '</text>']
    for tag in tags:
        item = item.replace(tag, '')
    return item

def get_information_from_file(file, data):
    with open(file, 'r') as xml:
        text = xml.read()
        results = re.findall('<text>[\s\S]*?<\/text>', text)
        for result in results:
            data.append(remove_tags(result))

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