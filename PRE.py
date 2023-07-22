from roboflow import Roboflow
import os
import torch
from IPython.display import Image, clear_output

rf = Roboflow(notebook="ultralytics")

os.environ['DATASET_DIRECTORY'] = '/content/dataset'


rf2 = Roboflow(api_key="pBWT53OXypNO7EkbVu33")
project = rf2.workspace().project("titi-uvqwk")
dataset = project.version(2).download("yolov5")
