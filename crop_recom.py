import numpy as np
import joblib

crop_names = {
    0: "apple",
    1: "banana",
    2: "blackgram",
    3: "chickpea",
    4: "coconut",
    5: "coffee",
    6: "cotton",
    7: "grapes",
    8: "jute",
    9: "kidneybeans",
    10: "lentil",
    11: "maize",
    12: "mango",
    13: "mothbeans",
    14: "mungbean",
    15: "muskmelon",
    16: "orange",
    17: "papaya",
    18: "pigeonpeas",
    19: "pomegranate",
    20: "rice",
    21: "watermelon",
}


def load_model(model_path):
    with open(model_path, "rb") as model_file:
        loaded_model = joblib.load(model_file)

    return loaded_model


def crop_predictor(model, data):
    y_pred = model.predict(data.reshape(1, -1))

    predicted_crop = crop_names.get(y_pred[0], "Unknown")

    return predicted_crop


if __name__ == "__main__":
    data_to_predict = np.array([90, 42, 43, 20.879744, 82.002744, 6.502985, 202.935536])

    model_path = "gaussian_nb_model.joblib"
    loaded_gnb = load_model(model_path)

    predicted_crop = crop_predictor(loaded_gnb, data_to_predict)

    print("Predicted crop:", predicted_crop)
