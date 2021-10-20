import os
import sys
# This program gets the total size of files in a folder

dir_path = input('Input a folder path: ')

# If it isn't a file path alert the user
if os.path.isdir(dir_path):
	# convert input to a directory path that works for all systems
	dir_path = os.path.join(dir_path)
else:
    print(f'The input path: {dir_path} isn\'t a folder or directory')
    sys.exit()

# get all the filenames filtered from the directory
file_names = list(filter(lambda names: os.path.isfile(os.path.join(dir_path, names)), os.listdir(dir_path)))

# for each file_names in the directory path create a file_path for it
file_paths = [os.path.join(dir_path, name) for name in file_names]

# get the size of each file
file_sizes = [os.path.getsize(file) for file in file_paths]

# get the sum of the file sizes
total_size = sum(file_sizes)

print(f"Size of files in {dir_path}: {total_size} bytes")
