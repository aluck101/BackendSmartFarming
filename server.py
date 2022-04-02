import base64
from flask import Flask, request, jsonify
from PIL import Image
# from fastai.basic_train import load_learner
# from fastai.vision import open_image

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)


def stringToRGB(base64_string):
    imageData = base64.b64decode(str(base64_string))
    return imageData


# learner = load_learner(path='./models', file='')
# classes = learn.data.classes

# def predict_image(img_file):
#     prediction = learn.predict(open_image(img_file))
#     probs_list = prediction[2].numpy()
#     return {
#         'category': classes[prediction[1].item()],
#         'probs': {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(classes)}
#     }

@app.route('/prediction/', methods=['POST'])
def predict():
    return jsonify(predict_image(request.files['image']))


@app.route('/test', methods=['POST'])
def test():
    request_data = request.get_json()

    base64image = request_data['img']
    return jsonify(base64image)


if __name__ == '__main__':
    app.run(port=1105)
