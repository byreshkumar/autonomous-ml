import csv
from pathlib import Path
from typing import List, Tuple

import numpy as np
from PIL import Image

def load_dataset(img_dir: str, labels_csv: str) -> Tuple[np.ndarray, np.ndarray]:
    X, y = [], []
    img_dir = Path(img_dir)
    with open(labels_csv, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            img_path = img_dir / row["filename"]
            angle = float(row["steering_angle"])
            img = Image.open(img_path).convert("RGB").resize((128, 72))
            X.append(np.asarray(img) / 255.0)
            y.append(angle)
    return np.stack(X).astype(np.float32), np.array(y, dtype=np.float32)