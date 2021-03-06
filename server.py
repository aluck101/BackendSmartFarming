
from flask import Flask, request, jsonify
import imagetransform as imgtrf
import deeplearning as learn


from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/prediction/', methods=['POST'])
def predict():
    request_data = request.get_json()
    base64image = request_data['img']
    imgRGB = imgtrf.imgStringToRGB(base64image)
    prediction = learn.predict_image(imgRGB)
    print(prediction)
    return jsonify(learn.predict_image(imgRGB))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
