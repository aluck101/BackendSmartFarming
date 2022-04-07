
from flask import Flask, request, jsonify
import imagetransform as imgtrf
import deeplearning as learn


from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/prediction/', methods=['POST'])
def predict():
    return jsonify(learn.predict_image(request.files['image']))


@app.route('/test/', methods=['POST'])
def test():
    request_data = request.get_json()
    base64image = request_data['img']
    print(base64image)
    return jsonify(base64image)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
