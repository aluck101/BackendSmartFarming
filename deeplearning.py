
from fastai.vision.all import *
from fastai import *

learn = load_learner('models/plant_detection_model.pkl')


# This class is used to convert Numpy object to JSON Object
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def predict_image(img_file):
    label, _, probs = learn.predict(img_file)
    classification = (label.split('/')[-1])
    probability = (max(probs))
    return {
        'category': classification,
        'probs': json.dumps(probability.numpy(), cls=NumpyEncoder)
    }
