
import numpy as np
from PIL import Image 
import math

epsilon = 1e-8

class ClassName:
	def __init__(self, camera_position, camera_look_at, field_of_view=10.0, gamma=0.05,focus=3.8, focal=7.5):

		self.objects = list()
		self.light_sources = list()
		self.ambient = RGB([100, 100, 100])
		self.gamma = gamma
		self.focus = focus
		self.focal = focal # High focal = better focus
		

