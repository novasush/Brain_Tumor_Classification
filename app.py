import os
# import cv2
import sys

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from gevent.pywsgi import WSGIServer

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Some utilites
import numpy as np
from util import base64_to_pil


# Declare a flask app
app = Flask(__name__)


# Model saved with Keras model.save()
MODEL_PATH = 'models/brain_model_finetune_v8.h5'

# Load your own trained model
model = tf.keras.models.load_model(MODEL_PATH)


def model_predict(img, model):
    # test_image = image.load_img(img)
    test_image = img.resize((224,224))

    # Preprocessing the image
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    test_image /= 255.
    preds = model.predict_classes(test_image)
    
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json)

        # Make prediction
        preds = model_predict(img, model)
        labels = {'glioma': 0, 'meningioma': 1, "no_tumor":2,'pituitary': 3}
        prediction = list(labels.keys())[list(labels.values()).index(list(preds)[0])]
        result = str(prediction)               # Convert to string
        result = result.replace('_', ' ').capitalize()
        return jsonify(result=result,preds = str(list(preds)))



if __name__ == '__main__':
    # app.run(port=5002, threaded=False)

    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
