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

		self.camera_position = np.array(camera_position)
		self.camera_look_at = np.array(camera_look_at)
		self.field_of_view = field_of_view

		self.camera_direction = self.camera_look_at - self.camera_position
		self.camera_direction = self.camera_direction / np.linalg.norm(self.camera_direction)

		# Temp: Should be rotated not projected 
		self.camera_up = np.cross(self.camera_position, np.cross(np.array([0,0,1]), self.camera_direction))
		self.camera_up = self.camera_up / np.linalg.norm(self.camera_up)
		self.camera_right = np.cross(self.camera_direction, self.camera_up)


	