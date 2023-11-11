import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

model = tf.keras.models.load_model('C:\\Users\\misha\\Desktop\\Bachelor\\eye_color_model.h5')

def predict_eye_color(img_path):
    img = image.load_img(img_path, target_size=(64, 64))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    class_indices = ['Blue', 'Brown', 'Green', 'Grey', 'Yellow']
    predicted_class = class_indices[np.argmax(prediction)]

    return predicted_class

test_image = 'try.jpg'
print(predict_eye_color(test_image))
