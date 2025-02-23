# Yolo-NaiLong

[English](https://github.com/LanternCX/Yolo-NaiLong/blob/main/Readme.md) | [中文](https://github.com/LanternCX/Yolo-NaiLong/blob/main/Readme_zh.md)

A NaiLong recognition project using **[YOLOv5](https://github.com/ultralytics/yolov5)**.

## Setup

1. Clone the project.
2. Download the weight file: [Release](https://github.com/LanternCX/Yolo-NaiLong/releases).
3. Set up a virtual Python environment with PyCharm. 

3. Clone the **[YOLOv5](https://github.com/ultralytics/yolov5)** repository. 

```bash
git clone https://github.com/ultralytics/yolov5.git
```

The project directory should look like this:

```
.
├── .venv
│   ├── ...
│   ...
├── yolov5
│   ├── ...
│   ... 
├── Main.py
├── Train.sh
├── Readme.md
└── NaiLong-v5s-e500.pt
```


4. Install the required packages:

```bash
cd yolov5
pip install -r requirements.txt 
```

5. Run

```bash
python Main.py
```

## Dataset

[Hugging Face: LanternCX/NaiLong-YOLOv5-PyTouch](https://huggingface.co/datasets/LanternCX/NaiLong-YOLOv5-PyTouch)
