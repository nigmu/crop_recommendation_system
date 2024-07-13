import joblib

crop_names = {
    0: "apple", 1: "banana", 2: "blackgram", 3: "chickpea", 4: "coconut",
    5: "coffee", 6: "cotton", 7: "grapes", 8: "jute", 9: "kidneybeans",
    10: "lentil", 11: "maize", 12: "mango", 13: "mothbeans", 14: "mungbean",
    15: "muskmelon", 16: "orange", 17: "papaya", 18: "pigeonpeas",
    19: "pomegranate", 20: "rice", 21: "watermelon"
}

def load_model():
    return joblib.load("C:/NPersonal/Projects/CropRecommendationSystem/utils/gaussian_nb_model.joblib")

def crop_predictor(data):
    y_pred = load_model().predict([data])
    predicted_crop = crop_names.get(y_pred[0], "")
    print("Crop predictor called")
    return predicted_crop

# if __name__ == "__main__":
#     data = [97,	12,	47,	25.287846,	89.636679,	6.765095,	58.286977]

#     predicted_crop = crop_predictor(data)

#     print("Predicted crop:", predicted_crop)
