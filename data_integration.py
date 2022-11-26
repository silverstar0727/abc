import os
import shutil
from tqdm import tqdm

origin_root = "/workspace/datas"
img_root = os.path.join(origin_root, "TS_사건사고데이터이미지/사건사고데이터이미지")
view_list = os.listdir(img_root)
new_image_dir = "/workspace/images"
os.makedirs(new_image_dir, exist_ok=True)
for view_name in tqdm(view_list):
    view_path = os.path.join(img_root, view_name)
    for time_idx in os.listdir(view_path):
        time_path = os.path.join(view_path, time_idx)
        for img_name in os.listdir(time_path):
            img_path = os.path.join(time_path, img_name)
            target_path = os.path.join(new_image_dir, img_name)
            shutil.copy(img_path, target_path)

origin_root = "/workspace/datas"
img_root = os.path.join(origin_root, "사건사고데이터이미지")
view_list = os.listdir(img_root)
new_label_dir = "/workspace/labels"
os.makedirs(new_label_dir, exist_ok=True)
for view_name in tqdm(view_list):
    view_path = os.path.join(img_root, view_name)
    for time_idx in os.listdir(view_path):
        time_path = os.path.join(view_path, time_idx)
        for img_name in os.listdir(time_path):
            img_path = os.path.join(time_path, img_name)
            target_path = os.path.join(new_label_dir, img_name)
            shutil.copy(img_path, target_path)
