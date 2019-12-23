import os

def get_dir_tree(dir_path,branch=None):
    if os.path.isdir(dir_path):
        list_of_dir = os.listdir(dir_path)
        # print the file name
        for file_count,file_name in enumerate(list_of_dir):
            get_dir_tree(dir_path+'/'+file_name,file_count)
    else:
        if os.path.isfile(dir_path):
            print(dir_path)
        else:
            print('Invalid path {0}'.format(dir_path))

get_dir_tree('.git')