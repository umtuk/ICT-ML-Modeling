import tensorflow as tf
from tensorflow.keras import layers

tf.keras.backend.clear_session()

# 사용자 설정 구간
FILENAME = 'SimpleCNNModel'
V = '1.0'
#


FILENAMEV = FILENAME + V

HSIZE = 48 # input 이미지 height 크기
WSIZE = 32 # input 이미지 width 크기


# 기존 모델을 불러오고 싶다면 다음 코드 추가
# model = tf.keras.models.load_model('./saved/'+FileNameV+'.h5')

inputs = tf.keras.Input(shape=(WSIZE, HSIZE, 3), name='img')

x = layers.Conv2D(32, 3, activation='relu')(inputs)
x = layers.Conv2D(32, 3, activation='relu')(x)
block_1_output = layers.MaxPooling2D(2)(x)

x = layers.Flatten()(x)
block_2_output = layers.add([x, block_1_output])

outputs = layers.Dense(10, activation='softmax')(x)

model = tf.keras.Model(inputs, outputs, name=FILENAME)
model.summary()

# 학습 후 저장하고 싶다면 다음 코드 추가
# model.save_weights('./saved/'+FILENAMEV+'.h5', save_format='h5')
