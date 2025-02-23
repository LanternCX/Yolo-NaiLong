import cv2
import torch

import warnings
# filter FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning)

model = torch.hub.load("./yolov5", "custom", path="./NaiLong-v5s-e500.pt", source="local")

# open cam 2
cap = cv2.VideoCapture(2)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab frame.")
        break

    # run RGB frame
    res = model(frame[..., ::-1])

    # get Pandas frame
    res_df = res.pandas().xyxy[0]

    for _, row in res_df.iterrows():
        if row['confidence'] < 0.5 or res.names[row['class']] != 'NaiLong':
            continue
        x1, y1, x2, y2, conf, cls = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax']), row['confidence'], int(row['class'])

        # box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # tag
        label = f"{res.names[cls]} {conf:.2f}"
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # show
    cv2.imshow("cv2", frame)

    # wait for quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release
cap.release()
cv2.destroyAllWindows()
