import numpy as np

import random as random
from math import *
from point import Point

class EESTOPlanner():

	def __init__(self):
		pass

	def get_path(self, costMap, startPoint, endPoint):

		num_paths = 20
		max_num_its = 100
		decay_factor = .99
		cur_decay = decay_factor
		N = 30