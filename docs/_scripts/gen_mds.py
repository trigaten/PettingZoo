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

import os
from os import mkdir, path

import re
import numpy as np
from tqdm import tqdm
# from pettingzoo.test.all_modules import all_environments

# for env_spec in tqdm(
from pettingzoo.butterfly import cooperative_pong_v4
env = cooperative_pong_v4()