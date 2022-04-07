
from fastai.vision import open_image
from fastai.basic_train import load_learner

from fastai import *


learn = load_learner(path='./models', file='')
classes = learn.data.classes


def predict_image(img_file):
    prediction = learn.predict(open_image(img_file))
    probs_list = prediction[2].numpy()
    return {
        'category': classes[prediction[1].item()],
        'probs': {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(classes)}
    }
