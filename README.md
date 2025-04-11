
# Drone Detection using YOLO v11

This project focuses on detecting drones in images using the YOLO v11 object detection algorithm. The model was trained on a custom dataset and evaluated over 124 epochs, with the best performance achieved at epoch 97.

---

##  Model Performance

| Metric              | Value   |
|---------------------|---------|
| **Best Epoch**      | 97      |
| **Precision**       | 0.9575  |
| **Recall**          | 0.9118  |
| **mAP@0.5**         | 0.9572  |
| **mAP@0.5:0.95**    | 0.6278  |
| **Total Epochs**    | 124     |

---

## Results & Visualizations

### 1. Confusion Matrix (Normalized)
![Confusion Matrix](images/confusion_matrix_normalized.png)

### 2. Precision-Recall Curve
![PR Curve](images/PR_curve.png)

### 3. F1-Score Curve
![F1 Curve](images/F1_curve.png)

### 4. Training Results Summary
![Training Results](images/results.png)

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/drone-detection-yolo-v11.git
   cd drone-detection-yolo-v11
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run inference:
   ```bash
   python detect.py --weights best.pt --img 640 --conf 0.25 --source data/images/
   ```

---

## Model Architecture

- **Backbone**: CSPDarkNet (YOLO v11)
- **Neck**: PANet
- **Head**: YOLO Head for bounding box regression and classification

---


## Training Details

- **Framework**: PyTorch
- **Input Size**: 640x640
- **Batch Size**: 16
- **Optimizer**: AdamW
- **Learning Rate**: 0.01 (with cosine decay)

