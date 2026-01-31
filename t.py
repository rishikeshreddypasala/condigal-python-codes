import tensorflow as ty
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = ty.keras.datasets.mnist.load_data()

#normalize the dataset
x_train, x_test = x_train / 255.0, x_test / 255.0

# build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"Test accuracy: {test_acc}")

# Make predictions
predicitions = model.predict(x_test)

# Display some predictions
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"Predicted label: {predicitions[0].argmax()}")
plt.show()