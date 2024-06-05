import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# Modeli yükle
model = load_model('jr_murat.h5')

# Modeli compile et
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Görüntü yolu
image_path = '10.png'

# Görüntüyü yükle ve işleme tabi tut
img = image.load_img(image_path, target_size=(150, 150))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0

# Tahmin yap
predictions = model.predict(img_array)

# Sonucu değerlendir ve çıktı ver
if predictions[0][0] < 0.5:
    print("Görüntü anormal olarak sınıflandırılmıştır.")
else:
    print("Görüntü normal olarak sınıflandırılmıştır.")



