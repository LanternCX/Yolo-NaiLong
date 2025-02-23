#!/bin/bash

source ./.venv/bin/activate
cd ./yolov5 &&
python train.py \
--img 416 \
--batch 16 \
--epochs "$1" \
--data ../Dataset/data.yaml \
--weights yolov5s.pt \
--name yolov5s_results \
--cache
