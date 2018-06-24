import numpy as np
from sklearn.externals import joblib

from settings import (Y_TRAIN_PREDICTION_PATH, MODEL_PATH)


class AbalonePredictor:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        tp = np.load(Y_TRAIN_PREDICTION_PATH)
        self.y_train = tp[0]
        self.prediction = tp[1]

    def predict(self, input_sex, length, diameter, height, weight):
        if input_sex == 0:
            sex = [1, 0, 0]
        elif input_sex == 2:
            sex = [0, 0, 1]
        else:
            sex = [0, 1, 0]
        target = np.array(
            sex + [length / 200, diameter / 200, height / 200, weight / 200])
        return self.model.predict(target.reshape(1, -1))
