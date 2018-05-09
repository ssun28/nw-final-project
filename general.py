'''
	Two general functions: 
	create_directory
	write_to_file
'''

import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_to_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()
