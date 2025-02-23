# Yolo-NaiLong

[中文](https://github.com/LanternCX/Yolo-NaiLong/blob/main/Readme_zh.md) | [English](https://github.com/LanternCX/Yolo-NaiLong/blob/main/Readme.md)

基于 **[YOLOv5](https://github.com/ultralytics/yolov5)** 奶龙识别

## 快速开始

1. `clone` 项目

```bash
git clone https://github.com/LanternCX/Yolo-NaiLong.git
```


2. 下载权重文件: [Release](https://github.com/LanternCX/Yolo-NaiLong/releases)
3. 在 PyCharm 设置 Python 虚拟环境。
3. `clone` **[YOLOv5](https://github.com/ultralytics/yolov5)** 仓库。
```bash
git clone https://github.com/ultralytics/yolov5.git
```

配置完成后项目目录结构应该像下面这样:

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

4. 安装依赖

```bash
cd yolov5
pip install -r requirements.txt 
```

5. 运行

```bash
python Main.py
```

## 数据集

[Hugging Face: LanternCX/NaiLong-YOLOv5-PyTouch](https://huggingface.co/datasets/LanternCX/NaiLong-YOLOv5-PyTouch)

