"""
This script reads documentation from /docs and puts it into zoo python files
"""

__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

import sys
import os
import re
sys.path.append("..")
sys.path.append("../..")

dirs = ["butterfly", "classic", "magent", "mpe", "sisl"]

def get_python_file_name(env_type, env_name):
    dir_path = os.path.join("../..", "pettingzoo")
    for env_file in os.listdir(os.path.join(dir_path, env_type)):
        if env_file == env_name:
            with open((os.path.join(dir_path, env_type, env_file, env_file + ".py")),'r') as file:
                if env_name in file.name:
                    print(file.name)
                    # return file.name
    exit()
    
def insert_docstring_into_python_file(file_path, doc):
    # doc = remove_front_matter(doc)
    doc = remove_html(doc)
    with open(file_path,'r+') as file:
        file_text = file.read()

        file_text = f'"""\n{doc}\n"""\n\n' + file_text
        file.seek(0)
        file.write(file_text)

def remove_front_matter(string):
    regex = re.compile(r"---[a\.\S\s]*---")
    match = regex.match(string)
    g = match.group(0)
    return string[len(g):]

def remove_html(string):
    splits = string.split("</div>")
    return splits[-2].strip()

for env_type in dirs:
    dir_path = "../" + env_type
    for env_name in os.listdir(dir_path):
        if str(env_name)[-3:] == ".md":
            with open((os.path.join(dir_path, env_name)),'r') as file:
                python_file_name = get_python_file_name(env_type, env_name[:-3])
                # print(remove_html(file.read()))
                # print(file.read())
                # print("-0-0-0-0-0-0-0")
                # exit()
                insert_docstring_into_python_file(python_file_name, file.read())

# if __name__ == "__main__":
#     file = get_python_file("butterfly", "prison")

#     # print(file)
#     insert_docstring_into_python_file(file, "")