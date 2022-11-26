import os
import random
import shutil

from tqdm import tqdm

image_path = "/workspace/images"
label_path = "/workspace/labels"

target_image_path = "/workspace/yolov7-finetune/images"
target_label_path = "/workspace/yolov7-finetune/labels"
os.makedirs(target_image_path, exist_ok=True)
os.makedirs(target_label_path, exist_ok=True)

data_list = os.listdir(image_path)
for data in tqdm(data_list):
    if random.uniform(0, 1) > 0.04:
        data_name = data.split(".")[0]

        try:
            shutil.copyfile(f"{image_path}/{data_name}.jpg", f"{target_image_path}/{data_name}.jpg")
            shutil.copyfile(f"{label_path}/{data_name}.json", f"{target_label_path}/{data_name}.json")
        except:
            print(data_name)