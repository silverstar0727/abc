import os
import shutil
import random
import json
from tqdm import tqdm

root_dir = "/workspace/yolov7-finetune/coco/test"
image_dir = os.path.join(root_dir, "images")
label_dir = os.path.join(root_dir, "labels")

coco_dict = {
    "images": [],
    "categories": [
        {
            "supercategory": "person",
            "id": 1,
            "name": "사람"
        },
        {
            "supercategory": "person",
            "id": 2,
            "name": "오토바이탄사람"
        },
        {
            "supercategory": "person",
            "id": 3,
            "name": "킥보드탄사람"
        },
        {
            "supercategory": "person",
            "id": 4,
            "name": "자전거탄사람"
        },
        {
            "supercategory": "person",
            "id": 5,
            "name": "오토바이"
        },
        {
            "supercategory": "person",
            "id": 6,
            "name": "자전거"
        },
        {
            "supercategory": "person",
            "id": 7,
            "name": "킥보드"
        },
    ],
    "annotations": []
}
img_idx = 0
anno_idx = 0
data_list = os.listdir(image_dir)

names_to_idx_dict = {
    "사람": 0,
    "오토바이탄사람": 1,
    "킥보드탄사람": 2,
    "자전거탄사람": 3,
    "오토바이": 4,
    "자전거": 5,
    "킥보드": 6
}


for data_name in data_list:
    img_name = data_name
    data_name = data_name.split('.')[0]
    data_path = os.path.join(label_dir, f"{data_name}.json")
    with open(data_path, "r") as f:

        data = json.load(f)

    image_info = {
        "file_name": img_name,
        "height": data["image"]["size"]["height"],
        "width": data["image"]["size"]["width"],
        "id": img_idx
    }

    for ann in data["annotation"]:
        cls_name = ann["property"]["name"]
        cls_id = names_to_idx_dict[cls_name]
        
        xmin = ann["bndbox"]["xmin"]
        ymin = ann["bndbox"]["ymin"]
        xmax = ann["bndbox"]["xmax"]
        ymax = ann["bndbox"]["ymax"]
        w = xmax - xmin
        h = ymax - ymin

        anno_info = {
            "id": anno_idx,
            "image_id": img_idx,
            "bbox": [xmin, ymin, w, h],
            "area": w * h,
            "category_id": cls_id + 1
        }

        coco_dict["annotations"].append(anno_info)
        anno_idx += 1

    coco_dict["images"].append(image_info)

    img_idx += 1

with open("coco.json", "w", encoding="utf-8") as f:
    json.dump(coco_dict, f, indent="\t", ensure_ascii=False)