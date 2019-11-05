from tensorflow.keras.applications.mobilenet import MobileNet, decode_predictions

mobile = MobileNet()
# mobile.summary()

import cv2
import time


img = cv2.imread('./img/bird.jpg', -1)
img = cv2.resize(img, (224, 224))

start = time.time()
yhat = mobile.predict(img.reshape(-1, 224, 224, 3))
time = time.time() - start
# label_key = np.argmax(yhat)
label = decode_predictions(yhat)
label = label[0][0]

print("테스트 시 소요 시간 : {}".format(time))
print('%s (%.2f%%)' % (label[1], label[2]*100))
img = img[:,:,::-1]
plt.figure(figsize=(11,11))
plt.imshow(img)
plt.axis("off")
plt.show()