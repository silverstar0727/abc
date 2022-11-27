python yolov7/train.py \
--workers 8 \
--device 0 \
--batch-size 16 \
--data yolov7/data/coco.yaml \
--img 640 640 \
--cfg yolov7/cfg/training/yolov7.yaml \
--weights runs/train/yolov74/weights/last.pt \
--name yolov7 \
--hyp yolov7/data/hyp.scratch.p5.yaml