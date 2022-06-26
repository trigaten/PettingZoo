"""
Script to generate md files from environment class docstrings

The information in the md is the following

* the environment name
* an gif of the environment
* a table containing
  * import code
  * action space
  * observation space
  * parallel API
  * manual control
  * agents


docstring information
"""


__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

import sys
sys.path.append("..")
sys.path.append("../..")
sys.path.append("../../..")

import os
from os import mkdir, path

import re
import numpy as np
from tqdm import tqdm
from PettingZoo.test.all_modules import all_environments

# for env_spec in tqdm(
from pettingzoo.mpe import simple_v2
env = simple_v2.env()
module = list(all_environments.items())[30][1]
env = list(all_environments.items())[30][1].env()
print(module.__file__)
# exit()
env.reset()

py_path_split = os.path.abspath(simple_v2.__file__).split("/")

env_name = py_path_split[-1][:-3]
env_type = py_path_split[-2]

import_str = f"```python\nfrom pettingzoo.{env_type} import {env_name}```"

parallel_api = env.metadata["is_parallelizable"]

action_spaces = env.unwrapped.action_spaces
observation_spaces = env.unwrapped.observation_spaces

agents = env.agents


for name, module in list(all_environments.items()):
  try:
    env = module.env()
    env.reset()
    py_path_split = os.path.abspath(module.__file__).split("/")

    env_name = py_path_split[-1][:-3]
    env_type = py_path_split[-2]

    import_str = f"```python\nfrom pettingzoo.{env_type} import {env_name}```"

    parallel_api = env.metadata["is_parallelizable"]

    action_spaces = env.unwrapped.action_spaces
    observation_spaces = env.unwrapped.observation_spaces

    agents = env.agents

    manual_policy = "has_manual_policy" in env.metadata and env.metadata["has_manual_policy"]

    docstring = env.__doc__
    
    string = f"""
    ---
    title: {env_name}
    AUTOGENERATED: DO NOT EDIT FILE DIRECTLY
    ---
    
    ```\u007bfigure\u007d ../../_static/videos/{env_type}/{env_name}.gif 
    :width: 120px
    :name: air_raid
    ```

    This environment is part of the <a href='..'>{env_type} environments</a>. Please read that page first for general information.

    |   |   |\n|---|---|\n
    | Import | {import_str} |
    | Action Spaces | {action_spaces} |
    | Observation Spaces | {observation_spaces} |
    | Parallel API | {parallel_api} |
    | Agents | {agents} |
    | Manual Control | {manual_policy} |
    
    """
    if manual_policy:
      print(string)
    # exit()
  except Exception as e:
    print(e)

# ['Scenario', 'SimpleEnv', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'env', 'make_env', 'parallel_env', 'parallel_wrapper_fn', 'raw_env']
