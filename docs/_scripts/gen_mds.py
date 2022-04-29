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
# print(str(action_space))
print(agents)

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

    docstring = env.__doc__
    if "error" not in docstring:
      print(docstring)
  except Exception as e:
    print(e)

# ['Scenario', 'SimpleEnv', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'env', 'make_env', 'parallel_env', 'parallel_wrapper_fn', 'raw_env']

