import os
import json
from tqdm import tqdm

def get_info(anno_path):
    with open(anno_path, "r") as f:
        data = json.load(f)

    file_name = anno_path.split("/")[-1]
    height = data["image"]["size"]["height"]
    width = data["image"]["size"]["width"]
    annos = data["annotation"]
    classes = []
    bboxes = []
    for ann in annos:
        classes.append(ann["property"]["name"])

        xmin = ann["bndbox"]["xmin"]
        ymin = ann["bndbox"]["ymin"]
        xmax = ann["bndbox"]["xmax"]
        ymax = ann["bndbox"]["ymax"]
        bboxes.append([xmin, ymin, xmax, ymax])

    image_info = {
        "file_name": file_name,
        "height": height,
        "width": width,
        "classes": classes,
        "bboxes": bboxes
    }

    # print(image_info)
    return image_info

def make_yolo_format(image_info):
    img_width = image_info["width"]
    img_height = image_info["height"]

    results_lines = []
    for i in range(len(image_info["classes"])):
        class_str = image_info["classes"][i]

        x1 = float(image_info["bboxes"][i][0])
        y1 = float(image_info["bboxes"][i][1])
        x2 = float(image_info["bboxes"][i][2])
        y2 = float(image_info["bboxes"][i][3])
        
        intx1 = int(x1)
        inty1 = int(y1)
        intx2 = int(x2)
        inty2 = int(y2)

        bbox_center_x = float( (x1 + (x2 - x1) / 2.0) / img_width)
        bbox_center_y = float( (y1 + (y2 - y1) / 2.0) / img_height)
        bbox_width = float((x2 - x1) / img_width)
        bbox_height = float((y2 - y1) / img_height)

        line_to_write = str(names_to_idx_dict[class_str]) + ' ' + str(bbox_center_x)+ ' ' + str(bbox_center_y)+ ' ' + str(bbox_width)+ ' ' + str(bbox_height) +'\n'
    
        results_lines.append(line_to_write)
    return results_lines


if __name__ == "__main__":
    annotations_path = "/workspace/yolov7-finetune/ir/labels"
    yolo_annotations_path = "/workspace/yolov7-finetune/yolo/labels"
    names_to_idx_dict = {
        "사람": 0,
        "오토바이탄사람": 1,
        "킥보드탄사람": 2,
        "자전거탄사람": 3,
        "오토바이": 4,
        "자전거": 5,
        "킥보드": 6
    }

    annos = os.listdir(annotations_path)
    os.makedirs(yolo_annotations_path, exist_ok=True)

    for anno_name in tqdm(annos):
        anno_path = os.path.join(annotations_path, anno_name)
        img_info = get_info(anno_path)
        yolo_lines = make_yolo_format(img_info)

        with open(f"{yolo_annotations_path}/{img_info['file_name'].split('.')[0]}.txt", "w") as file:
            file.writelines(yolo_lines)