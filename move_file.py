import os
import shutil

def move_file(source_file_path, directory_path):

    print("The file: {0} has been moved to the destination: {1}".format(source_file_path, directory_path))

    shutil.move(source_file_path, directory_path) #moves target file to destination.

def main():
    source_file_path = 'dir/dir1/dir2/dir3/file.txt'
    directory_path = '/dir/dir1/dir2/target_dir'

    move_file(source_file_path, directory_path)

if __name__ == '__main__':
    main()    