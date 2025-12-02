import argparse
from PIL import Image
import numpy as np
import tensorflow as tf

def preprocess(img_path):
    img = Image.open(img_path).convert("RGB").resize((128, 72))
    x = np.asarray(img) / 255.0
    return np.expand_dims(x, axis=0).astype(np.float32)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="artifacts/model/steering.h5")
    parser.add_argument("--image", required=True)
    args = parser.parse_args()

    model = tf.keras.models.load_model(args.model)
    x = preprocess(args.image)
    pred = model.predict(x)[0][0]
    print(f"Predicted steering angle: {pred:.3f}")

if __name__ == "__main__":
    main()