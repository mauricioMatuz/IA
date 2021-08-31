# Libreria para usar/movernos en directorios del SO
import sys
import os
# Preprocesar imagenes
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
# Libreria para hacer NN en orden (sequencial)
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
# Capas en las que se hará convoluciones
from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D
# Manejo de background en el ordenador
from tensorflow.python.keras import backend as K
# importación global de tensorflow
import tensorflow as tf
# libreria para hacer los graficos de la red
import matplotlib.pyplot as plot
# Libreria para arreglos
import numpy as np
# Libreria para metricas del modelo
from sklearn.metrics import classification_report, confusion_matrix

# Limpiamos los procesos que estan en background
K.clear_session()

# path de dataset
path_training = './data/training'
path_validate = './data/validate'

# Parametros para la NN
# iteraciones en todo el proceso de entrenamiento
epochs = 100
# Re dimensionando las imagenes del dataset a 100px
#height, width = 500, 374
height, width = 250, 292
# No de imagenes (lote) a enviar por cada paso 
batch_size = 1
# Filtros a usar en la convolucion
# Capa 1 = 32 profundidad
# Capa 2 = 64 profundidad
filter_conv1 = 32
filter_conv2 = 64
# Tamaño de filtros
# Capa 1 = 3 de altura, 3 de longitud
# Capa 2 = 2 de altura, 2 de longitud
size_filter1 = (3,3)
size_filter2 = (2,2)
# Tamaño de filtro para MaxPooling
size_pool = (2,2)
# No de clases en dataset
classes = 4
# Tasa de aprendizaje (lambda)
lr = 0.00005

# pre-procesamiento de imagenes
datagen_training = ImageDataGenerator(
    rescale = 1./255, # Re escala las imagenes (0-1 px)
    shear_range = 0.3, # Inclinar imagenes para mejor entrenamiento
    zoom_range = 0.3, # Aumentar/Alejar imagenes para mejor entrenamiento
    horizontal_flip = True # Invertir imagen para mejor entrenamiento
)

datagen_validate = ImageDataGenerator(rescale=1./255)

img_training = datagen_training.flow_from_directory(
    path_training, # path de imagenes para entrenamiento
    target_size = (height, width), # Lee y procesa las imagenes a $height, $width
    batch_size = batch_size, # Crea lotes de imagenes
    class_mode = 'categorical',
    shuffle = False
)

img_validate = datagen_validate.flow_from_directory(
    path_validate, # path de imagenes para validación
    target_size = (height, width), # Lee y procesa las imagenes a $height, $width
    batch_size = batch_size, # Crea lotes de imagenes
    class_mode = 'categorical',
    shuffle = False
)

# Crear red Convolucional
# Red secuencial por capas
cnn = Sequential()
# 1er capa: Convolution2D
# encargada de recibir las imagenes con $height, $width px y los canales por imagen (RGB)
# aplicando los filtros y tamaños de filtros indicados
cnn.add(Convolution2D(filter_conv1, size_filter1, padding='same', input_shape=(height, width, 3),
    activation='relu'))
# 2da capa: MaxPooling2D
# filtro para esta: (2,2) px
cnn.add(MaxPooling2D(pool_size=size_pool))
# 3ra capa: Convolution2D
cnn.add(Convolution2D(filter_conv2, size_filter2, padding='same', activation='relu'))
# 4ta capa: MaxPooling2D
cnn.add(MaxPooling2D(pool_size=size_pool))

# Convertimos profundidad a 1D
cnn.add(Flatten())
cnn.add(Dense(256, activation='relu'))
# Cada paso tendrá el 50% de neuronas en el entrenamiento
# para evitar sobreajuste
cnn.add(Dropout(0.5))
# añadiendo las clases como neuronas en la capa
# softmax: nos devuelve las probabilidades en base a las clases.
cnn.add(Dense(classes, activation='softmax'))

# imprimir un resumen de la red construida
cnn.summary()

# Durante el entrenamiento
# categorical_crossentropy: Calcula la pérdida de entropía cruzada entre 
# las etiquetas y las predicciones.
# optimizers.Adam: método de descenso de gradiente estocástico que se basa
# en la estimación adaptativa de momentos de primer y segundo orden. 
# Metrics.accuracy: Calcula la frecuencia con la que las predicciones son iguales a las etiquetas.
cnn.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(learning_rate=lr),
    metrics=['accuracy'])

# Entrenamiento:
# usando las imagenes de entrenamiento y validación
# Guardando los registros de funciones de perdida
# y precisión por epoca
history = cnn.fit(img_training, epochs=epochs, validation_data=img_validate)

# Guardar el modelo
# para no tener que entrenar cada que se requiera hacer una predicción
directory = './model/'

# Creamos el directorio si no existe
if not os.path.exists(directory):
    os.mkdir(directory)

# Guardamos el modelo y los pesos
cnn.save('./model/model.h5')
cnn.save_weights('./model/weights.h5')

# Graficando la función de perdida
# y la precisión del modelado
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)
plot.plot(epochs, acc, 'r', label='Training acc')
plot.plot(epochs, val_acc, 'b', label='Validation acc')
plot.title('Training and validation accuracy')
plot.legend()
plot.figure()
plot.plot(epochs, loss, 'r', label='Training loss')
plot.plot(epochs, val_loss, 'b', label='Validation loss')
plot.title('Training and validation loss')
plot.legend()
plot.show()

# Matriz de confusión
predictions = cnn.predict(img_training)
pred_y = np.argmax(predictions, axis=1)
print('Confusion Matrix')
cm = confusion_matrix(img_training.classes, pred_y)
print(cm)
fig, ax = plot.subplots()
# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
plot.title('Confusion Matrix')
ax.table(cellText=cm, loc='center', colLabels=["3ra edad", "Adolescentes", "Adulto", "Infancia"],
    rowLabels=["3ra edad", "Adolescentes", "Adulto", "Infancia"])
fig.tight_layout()
plot.show()
print('Classification Report')
cr = classification_report(img_training.classes, pred_y,
    target_names=['3ra edad', 'Adolescentes', 'Adultos', 'Infancia'])
print(cr)