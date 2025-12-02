import argparse
from pathlib import Path
import tensorflow as tf
from src.data import load_dataset
from src.model import build_model

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--img-dir", default="data/sample")
    parser.add_argument("--labels", default="data/sample/labels.csv")
    parser.add_argument("--epochs", type=int, default=2)
    parser.add_argument("--out", default="artifacts/model")
    args = parser.parse_args()

    X, y = load_dataset(args.img_dir, args.labels)
    model = build_model(input_shape=X.shape[1:])
    model.fit(X, y, validation_split=0.2, epochs=args.epochs, batch_size=16)
    Path(args.out).mkdir(parents=True, exist_ok=True)
    model.save(Path(args.out) / "steering.h5")

if __name__ == "__main__":
    main()