# Yolo-NaiLong

A NaiLong recognition project using **[YOLOv5](https://github.com/ultralytics/yolov5)**.

## Setup

1. Clone the project.
2. Download the weight file.
3. Set up a virtual Python environment with PyCharm. The project directory should look like this:

```
.
├── Main.py
├── .venv
│   ├── ...
│   ...
├── NaiLong-v5s-e500.pt
├── Readme.md
├── Train.sh
└── yolov5
    ├── ...
    ...
```

3. Clone the **[YOLOv5](https://github.com/ultralytics/yolov5)** repository:

```bash
git clone https://github.com/ultralytics/yolov5.git
```

```bash
git clone https://github.com/ultralytics/yolov5.git
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
