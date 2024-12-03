import random
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def pomysl():
    pomysly = ["Pudełko z patyczków po lodach","Stworek z plastikowej butelki i nakrętek","Pokrowiec na telefon z tkaniny"]
    return random.choice(pomysly)

def detect_bird(image, model=load_model("keras_model.h5", compile=False), class_names=open("labels.txt", "r", encoding="utf-8").readlines()):
    np.set_printoptions(suppress=True)
    model = load_model("keras_model.h5", compile=False)
    class_names = open("labels.txt", "r").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image).convert("RGB")

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    print("Class:", class_name[2:], end="")
    print("Confidence Score:", round(confidence_score*100, 2), "%")
    if confidence_score < 0.5:
        return "Przepraszam, nie wiem co jest na obrazku"
    else:
        if class_name == "1 Golab\n":
            return "Ptak na zdjęciu to najprawdopodobniej gołąb.\nOto co możesz podać gołębiom: ciecierzyca, pszenica, jęczmień, nasiona, kasza gryczana, proso, groch, soczewica i inne zboża w suchej postaci."
        elif class_name == "2 Wrobel\n":
            return "Ptak na zdjęciu to najprawdopodobniej wróbel.\nOto, co możesz dać wróblom: popękana kukurydza, ziarna zbóż, owies, pszenica, ryż i suszone owady."
        elif class_name == "0 Kruk\n":
            return "Ptak na zdjęciu to najprawdopodobniej kruk.\nOto, co możesz dać krukom: małe kawałki mięsa, jajka, kawałki owoców, orzechy, niesolone kawałki słoniny, sucha karma dla psów lub kotów."
        elif class_name == "3 Sikorka\n":
            return "Ptak na zdjęciu to najprawdopodobniej sikorka.\nOto, co możesz dać sikorkom: nasiona słonecznkika łuskanego, prosa, pszenicy, owsa, świerku, sosny."