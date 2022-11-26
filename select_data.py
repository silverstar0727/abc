import os
import random
import shutil

from tqdm import tqdm

image_path = "/workspace/images"
label_path = "/workspace/labels"

therm_image_path = "/workspace/yolov7-finetune/therm/images"
therm_label_path = "/workspace/yolov7-finetune/therm/labels"
ir_image_path = "/workspace/yolov7-finetune/ir/images"
ir_label_path = "/workspace/yolov7-finetune/ir/labels"
os.makedirs(therm_image_path, exist_ok=True)
os.makedirs(therm_label_path, exist_ok=True)
os.makedirs(ir_image_path, exist_ok=True)
os.makedirs(ir_label_path, exist_ok=True)

data_list = os.listdir(image_path)
random.shuffle(data_list)
therm_list = []
ir_list = []
for idx, data in enumerate(data_list):
    data_type = data.split("_")[2]
    
    if data_type == "THERM":
        if len(therm_list) < 38000:
            therm_list.append(data)
    elif data_type == "IR":
        if len(ir_list) < 38000:
            ir_list.append(data)

for data in tqdm(therm_list):
    data_name = data.split(".")[0]

    try:
        shutil.copyfile(f"{image_path}/{data_name}.jpg", f"{therm_image_path}/{data_name}.jpg")
        shutil.copyfile(f"{label_path}/{data_name}.json", f"{therm_label_path}/{data_name}.json")
    except:
        print(data_name)


for data in tqdm(ir_list):
    data_name = data.split(".")[0]

    try:
        shutil.copyfile(f"{image_path}/{data_name}.jpg", f"{ir_image_path}/{data_name}.jpg")
        shutil.copyfile(f"{label_path}/{data_name}.json", f"{ir_label_path}/{data_name}.json")
    except:
        print(data_name)
