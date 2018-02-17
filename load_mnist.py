import pickle
import gzip
import matplotlib.pyplot as plt

f = gzip.open("mnist.pkl.gz", 'rb')
training_data, validation_data, test_data = pickle.load(f, encoding="latin1")
f.close()

image = training_data[0][0].reshape((28, 28))
plt.imshow(image, cmap='gray')
plt.show()
