#!/usr/bin/env python3.4
import os
import subprocess
import shutil

class Styler_Class:
	"""
	use neural style and imagemagick to create ten PNG images and a GIF and save these with the content and style images
	to an appropriately named subdirectory
	"""
	def __init__(self):
		return

	def spawnImages(self):
		if (not os.getcwd().endswith("/neural-style/")):
			os.chdir(os.getcwd() + "/neural-style/")
		else:
			os.chdir(os.getcwd() + "/")
		os.environ['LD_LIBRARY_PATH'] = "/usr/local/cuda-7.0/lib64:$LD_LIBRARY_PATH"
		style_fpath = os.getcwd() +  "/../static/uploads/style.jpg"
		content_fpath = os.getcwd() + "/../static/uploads/content.jpg"
		subprocess.check_call(["th", "neural_style.lua", "-style_image", style_fpath, "-content_image", content_fpath, "-backend", "cudnn"])
		
		image_files = [f for f in os.listdir('.') if (os.path.isfile(f) and f.endswith(".png"))]
		for file in image_files:
			shutil.copy(os.getcwd() + "/" + file, os.getcwd() + "/../static/output/")
		os.chdir("../static/output/")
		os.rename("out.png", "out_999.png") #Rename final image so imagemagick uses it as the last image of the GIF
		subprocess.check_call(["convert", "-delay", "17", "*.png", "animation.gif"])