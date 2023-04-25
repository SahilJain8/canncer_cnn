from keras.models import model_from_json, load_model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2
import joblib
import pandas as pd
from PIL import Image, ImageOps
import numpy as np


class Models:
    def __init__(self):
        self.predection = None
        self.img = None
        self.breast_cancer_model = load_model("breastcancer.h5", compile=False)
        self.lung_cancer_model = joblib.load("svm_m.pkl")
        self.leukemia_model = load_model("lk.h5", compile=False)

    def breast_cancer_classification(self, img_path):
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        image = Image.open(img_path).convert("RGB")

        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        image_array = np.asarray(image)

        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        data[0] = normalized_image_array

        prediction = self.breast_cancer_model.predict(data)

        return prediction

    def leukemia_classification(self, img_path):
        np.set_printoptions(suppress=True)
        class_names = open("lk.txt", "r").readlines()
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        image = Image.open(img_path).convert("RGB")

        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        image_array = np.asarray(image)

        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        data[0] = normalized_image_array

        prediction = self.leukemia_model.predict(data)
        index = np.argmax(prediction)
        confidence_score = prediction[0][index]
        return index, confidence_score

    def lung_cancer_predection(self, inputs):
        data = pd.DataFrame(inputs).T
        data.columns = ['GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY',
                        'PEER_PRESSURE', 'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING',
                        'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH',
                        'SWALLOWING DIFFICULTY', 'CHEST PAIN']
        prediction = self.lung_cancer_model.predict(data)
        return prediction[0]
