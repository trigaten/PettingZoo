"""
This script reads documentation from /docs and puts it into zoo python files
"""

__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

import sys
import os
sys.path.append("..")
sys.path.append("../..")

dirs = ["atari"]

# for env_type in dirs:
#     dir_path = "../" + env_type
#     for env_file in os.listdir(dir_path):
#         with open((os.path.join(dir_path, env_file)),'r') as file:
#             if file.name[-3:] == ".md":
#                 module_dir = os.path.join("../..", "pettingzoo", env_type, file)
#                 print(file.readlines())

def get_python_file(env_type, env_name):
    dir_path = os.path.join("../..", "pettingzoo")
    for env_file in os.listdir(os.path.join(dir_path, env_type)):
        if env_file[-3:] == ".py":
            with open((os.path.join(dir_path, env_type, env_file)),'r') as file:
                if env_name in file.name:
                    return file.name

def insert_docstring_into_python_file(file_path, doc):
    with open(file_path,'r+') as file:
        file_text = file.read()
        print(file_text)

if __name__ == "__main__":
    file = get_python_file("butterfly", "prison")

    # print(file)
    insert_docstring_into_python_file(file, "")