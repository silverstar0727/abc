import os
import random
from tqdm import tqdm
import shutil

data_list = os.listdir("ir/images")
random.shuffle(data_list)

train_list = []
val_list = []
test_list = []
for idx, data_name in enumerate(data_list):
    if idx < 30000:
        train_list.append(data_name)
    elif 30000 < idx <= 34000:
        val_list.append(data_name)
    else:
        test_list.append(data_name)

os.makedirs("coco/train/images", exist_ok=True)
os.makedirs("coco/val/images", exist_ok=True)
os.makedirs("coco/test/images", exist_ok=True)
os.makedirs("coco/train/labels", exist_ok=True)
os.makedirs("coco/val/labels", exist_ok=True)
os.makedirs("coco/test/labels", exist_ok=True)

def f(target_data_list, mode):
    origin_dir = "ir/images/"
    origin_label_dir = "ir/labels"
    if mode == "train":
        move_dir = "coco/train/images"
        move_label_dir = "coco/train/labels"
    elif mode == "val":
        move_dir = "coco/val/images"
        move_label_dir = "coco/val/labels"
    else:
        move_dir = "coco/test/images"
        move_label_dir = "coco/test/labels"
    
    for data in tqdm(target_data_list):
        
        data_name = data.split(".")[0]

        # try:
        shutil.copyfile(f"{origin_dir}/{data_name}.jpg", f"{move_dir}/{data_name}.jpg")
        shutil.copyfile(f"{origin_label_dir}/{data_name}.json", f"{move_label_dir}/{data_name}.json")
        # except:
        #     print(data_name)
        

f(train_list, "train")
f(val_list, "val")
f(test_list, "test")