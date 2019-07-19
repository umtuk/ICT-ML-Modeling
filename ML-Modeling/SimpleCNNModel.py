import tensorflow as tf
from tensorflow import keras
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

encoder_input = keras.Input(shape=(WSIZE, HSIZE, 3), name='img')
x = layers.Conv2D(32, kernel_size=3, padding='same', activation='relu')(encoder_input)
x = layers.Conv2D(32, kernel_size=3, padding='same', activation='relu')(x)
x = layers.MaxPooling2D(2)(x)
x = layers.Flatten()(x)
encoder_output = layers.Dense(10, activation='softmax')(x)

encoder = keras.Model(encoder_input, encoder_output, name='encoder')
encoder.summary()

# 학습 후 저장하고 싶다면 다음 코드 추가
# model.save_weights('./saved/'+FILENAMEV+'.h5', save_format='h5')
