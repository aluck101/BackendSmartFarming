from flask import Flask, request, jsonify
# from fastai.basic_train import load_learner
# from fastai.vision import open_image

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

# learner = load_learner(path='./models', file='')
# classes = learn.data.classes

# def predict_image(img_file):
#     prediction = learn.predict(open_image(img_file))
#     probs_list = prediction[2].numpy()
#     return {
#         'category': classes[prediction[1].item()],
#         'probs': {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(classes)}
#     }

# @app.route('/prediction/', methods=['POST'])
# def predict():
#     return jsonify(predict_image(request.files['image']))


@app.route('/test/', methods=['POST'])
def test():
    return jsonify(category='plant')


if __name__ == '__main__':
    app.run(port=1105)
