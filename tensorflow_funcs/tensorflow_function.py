import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from keras.src.datasets import mnist
from tensorflow import keras
from tensorflow.keras import layers


def tensorflow_test():
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    model = keras.Sequential([
        layers.Dense(512, activation='relu'),
        layers.Dense(10, activation="softmax")
    ])
    model.compile(optimizer="rmsprop", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

    train_images = train_images.reshape(60000, 28 * 28)
    train_images = train_images.astype('float32') / 255
    test_images = test_images.reshape(10000, 28 * 28)
    test_images = test_images.astype('float32') / 255

    model.fit(train_images, train_labels, epochs=5, batch_size=128)

    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print(test_acc)

