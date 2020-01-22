import os
import re
from os import listdir
from os.path import isfile, join

SPACE = '\n'

def get_files_from_directory(path):
    return [join(path, file) for file in listdir(path) if isfile(join(path, file))]

def main():
    print('Starting Program')

    path = './files/'
    files = get_files_from_directory(path)

    data = list()
    for file in files:
        with open(file, 'r') as xml:
            text = xml.read()
            results = [] # Regex to find al the match
            for result in results:
                data.append(result)

    for item in data:
        with open('results.csv', 'a') as file:
            file.write(item + SPACE)

if __name__ == "__main__":
    main()