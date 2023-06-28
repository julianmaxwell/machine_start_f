import pandas
import cv2 as cv
import inspect
import numpy
import tensorflow
import tensorflow.python.keras as keras
import matplotlib.pyplot as plt
tensorflow.compat.v1.disable_eager_execution()
noises1 = numpy.random.randn(100)*0.13
noises2 = numpy.random.randn(100)*0.17
train_data_x = numpy.linspace(-1, 1, 100) + noises1
train_data_y = numpy.linspace(-1, 1, 100)*2 + noises2
data = tensorflow.keras.datasets.fashion_mnist.load_data()
print(len(data))


data2 = tensorflow.keras.datasets.imdb.load_data(num_words=10000)
(train_x, train_y), (test_x, test_y) = data2

data2_index = tensorflow.keras.datasets.imdb.get_word_index()
# print(data2[0][0][0])
(train_data2_x, train_data2_y), (test_data2_x, test_data2_y) = data2
train_data2_x_300 = tensorflow.keras.preprocessing.sequence.pad_sequences(train_data2_x, 300)


test_x_300 = tensorflow.keras.preprocessing.sequence.pad_sequences(test_data2_x, 300)
xm = keras.Sequential()

"""
keras:
['Input', 'Model', 'Sequential',  
 'activations', 'applications', 'backend', 'callbacks',
  'constraints', 'datasets', 'estimator', 'experimental',
   'initializers', 'layers', 'losses', 'metrics', 'mixed_precision', 
   'models', 'optimizers', 'preprocessing', 'regularizers', 'utils',
    'wrappers']
"""
"""
karas.application:
['DenseNet121', 'DenseNet169', 'DenseNet201', 'EfficientNetB0', 
'EfficientNetB1', 'EfficientNetB2', 'EfficientNetB3', 
'EfficientNetB4', 'EfficientNetB5', 'EfficientNetB6', 'EfficientNetB7', 
'EfficientNetV2B0', 'EfficientNetV2B1', 'EfficientNetV2B2', 'EfficientNetV2B3', 
'EfficientNetV2L', 'EfficientNetV2M', 'EfficientNetV2S', 'InceptionResNetV2', 
'InceptionV3', 'MobileNet', 'MobileNetV2', 'MobileNetV3Large', 'MobileNetV3Small', 
'NASNetLarge', 'NASNetMobile', 'ResNet101', 'ResNet101V2', 'ResNet152', 
'ResNet152V2', 'ResNet50', 'ResNet50V2', 'VGG16', 'VGG19', 'Xception', 
'densenet', 'efficientnet', 'efficientnet_v2', 'imagenet_utils', 
'inception_resnet_v2', 'inception_v3', 'mobilenet', 'mobilenet_v2', '
mobilenet_v3', 'nasnet', 'resnet', 'resnet50', 'resnet_v2', 'vgg16', 'vgg19', 
'xception']
"""

"""
    shape=None,
    batch_size=None,
    name=None,
    dtype=None,
    sparse=None,
    tensor=None,
    ragged=None,
    type_spec=None,
    
print(dir(tensorflow.keras.layers))    
['AbstractRNNCell', 'Activation', 'ActivityRegularization', 'Add', 'AdditiveAttention', 'AlphaDropout', 'Attention', 
'Average', 'AveragePooling1D', 'AveragePooling2D', 'AveragePooling3D', 'AvgPool1D', 'AvgPool2D', 'AvgPool3D', 
'BatchNormalization', 'Bidirectional', 'CategoryEncoding', 'CenterCrop', 'Concatenate', 'Conv1D', 'Conv1DTranspose', 
'Conv2D', 'Conv2DTranspose', 'Conv3D', 'Conv3DTranspose', 'ConvLSTM1D', 'ConvLSTM2D', 'ConvLSTM3D', 'Convolution1D',
 'Convolution1DTranspose', 'Convolution2D', 'Convolution2DTranspose', 'Convolution3D', 'Convolution3DTranspose', 
'Cropping1D', 'Cropping2D', 'Cropping3D', 'Dense', 'DenseFeatures', 'DepthwiseConv1D', 'DepthwiseConv2D', 
'Discretization', 'Dot', 'Dropout', 'ELU', 'Embedding', 'Flatten', 'GRU', 'GRUCell', 'GaussianDropout', 'GaussianNoise
', 'GlobalAveragePooling1D', 'GlobalAveragePooling2D', 'GlobalAveragePooling3D', 'GlobalAvgPool1D', 'GlobalAvgPool2D',
'GlobalAvgPool3D', 'GlobalMaxPool1D', 'GlobalMaxPool2D', 'GlobalMaxPool3D', 'GlobalMaxPooling1D', 
'GlobalMaxPooling2D', 'GlobalMaxPooling3D', 'Hashing', 'Input', 'InputLayer', 'InputSpec', 'IntegerLookup', 'LSTM',
'LSTMCell', 'Lambda', 'Layer', 'LayerNormalization', 'LeakyReLU', 'LocallyConnected1D', 'LocallyConnected2D',
'Masking', 'MaxPool1D', 'MaxPool2D', 'MaxPool3D', 'MaxPooling1D', 'MaxPooling2D', 'MaxPooling3D', 'Maximum', 
'Minimum', 'MultiHeadAttention', 'Multiply', 'Normalization', 'PReLU', 'Permute', 'RNN', 'RandomContrast', 
'RandomCrop', 'RandomFlip', 'RandomHeight', 'RandomRotation', 'RandomTranslation', 'RandomWidth', 'RandomZoom', 
'ReLU', 'RepeatVector', 'Rescaling', 'Reshape', 'Resizing', 'SeparableConv1D', 'SeparableConv2D', 
'SeparableConvolution1D', 'SeparableConvolution2D', 'SimpleRNN', 'SimpleRNNCell', 'Softmax', 'SpatialDropout1D',
'SpatialDropout2D', 'SpatialDropout3D', 'StackedRNNCells', 'StringLookup', 'Subtract', 'TextVectorization', 
'ThresholdedReLU', 'TimeDistributed', 'UpSampling1D', 'UpSampling2D', 'UpSampling3D', 'Wrapper', 'ZeroPadding1D',
'ZeroPadding2D', 'ZeroPadding3D', 'add', 'average', 'concatenate', 'deserialize', 'dot', 'experimental', 
'maximum', 'minimum', 'multiply', 'serialize', 'subtract']
"""


input_ = tensorflow.keras.Input(shape=(299, 299, 3), batch_size=30,)
inser_net_m = tensorflow.keras.applications.xception.Xception(
                                                            include_top=False,
                                                            # weights="imagenet",
                                                            input_shape=(299, 299, 3),
                                                            pooling="avg",
                                                            )


inser_net = tensorflow.keras.applications.xception.Xception(
                                                            include_top=False,
                                                            # weights="imagenet",
                                                            input_shape=(299, 299, 3),
                                                            pooling="avg",
                                                            )(input_)
inser_net.trainable = False

gear_drill_box1 = tensorflow.keras.layers.Dense(1024, activation="relu")(inser_net)
print(gear_drill_box1.shape)
# gear_drill_box = tensorflow.keras.layers.Conv1D(1024, 3, activation="relu")(gear_drill_box1)
gear_drill_box = tensorflow.keras.layers.GlobalAvgPool2D(gear_drill_box1)
gear_drill_box = tensorflow.keras.layers.Dense(15, activation="softmax")(gear_drill_box)

tiger_run = tensorflow.keras.layers.Dense(1024, activation="relu")(inser_net)
tiger_run = tensorflow.keras.layers.Dense(10, activation="softmax")(tiger_run)

beam_run = tensorflow.keras.layers.Dense(1024, activation="relu")(inser_net)
beam_run = tensorflow.keras.layers.Dense(15, activation="softmax")(beam_run)

model_ = tensorflow.keras.Model(
    inputs=[input_],
    outputs=[gear_drill_box, tiger_run, beam_run]
)
# print(model_.summary())
model_.summary()
xx = model_.get_layer()
print(xx)


