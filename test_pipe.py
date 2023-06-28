import tensorflow as tf
from tensorflow.keras import Model
l=tf.keras.layers


def _conv(inputs, filters, kernel_size, strides, padding, bias=False, normalize=True, activation='relu', last=False):
    output = inputs
    padding_str = 'same'
    if padding>0:
        output = l.ZeroPadding2D(padding=padding, data_format='channels_first')(output)
        padding_str = 'valid'
    output = l.Conv2D(filters, kernel_size, strides, padding_str,
                  'channels_first', use_bias=bias,
                  kernel_initializer='he_normal',
                  kernel_regularizer=tf.keras.regularizers.l2(l=5e-4))(output)
    if normalize:
        if not last:
            output = l.BatchNormalization(axis=1)(output)
        else:
            output = l.BatchNormalization(axis=1, gamma_initializer='zeros')(output)
    if activation=='relu':
        output = l.ReLU()(output)
    if activation=='relu6':
        output = l.ReLU(max_value=6)(output)
    if activation=='leaky_relu':
        output = l.LeakyReLU(alpha=0.1)(output)
    return output

def _residual(inputs, out_channels, activation='relu', name=None):
    output1 = _conv(inputs, out_channels//2, 1, 1, 0, False, True, 'leaky_relu', False)
    output2 = _conv(output1, out_channels, 3, 1, 1, False, True, 'leaky_relu', True)
    output = l.Add(name=name)([inputs, output2])
    return output

def darknet53_base():
    image = tf.keras.Input(shape=(3,None,None))
    net = _conv(image, 32, 3, 1, 1, False, True, 'leaky_relu')     #32*H*W
    net = _conv(net, 64, 3, 2, 1, False, True, 'leaky_relu')       #64*H/2*W/2
    net = _residual(net, 64, 'leaky_relu')                         #64*H/2*W/2
    net = _conv(net, 128, 3, 2, 1, False, True, 'leaky_relu')      #128*H/4*W/4
    net = _residual(net, 128, 'leaky_relu')                        #128*H/4*W/4
    net = _residual(net, 128, 'leaky_relu')                        #128*H/4*W/4
    net = _conv(net, 256, 3, 2, 1, False, True, 'leaky_relu')      #256*H/8*W/8
    net = _residual(net, 256, 'leaky_relu')                        #256*H/8*W/8
    net = _residual(net, 256, 'leaky_relu')                        #256*H/8*W/8
    net = _residual(net, 256, 'leaky_relu')                        #256*H/8*W/8
    net = _residual(net, 256, 'leaky_relu')                        #256*H/8*W/8
    net = _residual(net, 256, 'leaky_relu')                        #256*H/8*W/8
    net = _residual(net, 256, 'leaky_relu')                        #256*H/8*W/8
    net = _residual(net, 256, 'leaky_relu')                        #256*H/8*W/8
    net = _residual(net, 256, 'leaky_relu')                        #256*H/8*W/8
    route1 = l.Activation('linear', dtype='float32', name='route1')(net)
    net = _conv(net, 512, 3, 2, 1, False, True, 'leaky_relu')   #512*H/16*W/16
    net = _residual(net, 512, 'leaky_relu')                        #512*H/16*W/16
    net = _residual(net, 512, 'leaky_relu')                        #512*H/16*W/16
    net = _residual(net, 512, 'leaky_relu')                        #512*H/16*W/16
    net = _residual(net, 512, 'leaky_relu')                        #512*H/16*W/16
    net = _residual(net, 512, 'leaky_relu')                        #512*H/16*W/16
    net = _residual(net, 512, 'leaky_relu')                        #512*H/16*W/16
    net = _residual(net, 512, 'leaky_relu')                        #512*H/16*W/16
    net = _residual(net, 512, 'leaky_relu')                        #512*H/16*W/16
    route2 = l.Activation('linear', dtype='float32', name='route2')(net)
    net = _conv(net, 1024, 3, 2, 1, False, True, 'leaky_relu')     #1024*H/32*W/32
    net = _residual(net, 1024, 'leaky_relu')                       #1024*H/32*W/32
    net = _residual(net, 1024, 'leaky_relu')                       #1024*H/32*W/32
    net = _residual(net, 1024, 'leaky_relu')                       #1024*H/32*W/32
    net = _residual(net, 1024, 'leaky_relu')                       #1024*H/32*W/32
    route3 = l.Activation('linear', dtype='float32', name='route3')(net)
    net = tf.reduce_mean(net, axis=[2,3], keepdims=True)
    net = _conv(net, 1000, 1, 1, 0, True, False, 'linear')         #1000
    net = l.Flatten(data_format='channels_first', name='logits')(net)
    net = l.Activation('linear', dtype='float32', name='output')(net)
    model = tf.keras.Model(inputs=image, outputs=[net, route1, route2, route3])
    return model
# <p>我们需要先基于这个骨干网络架构来进行Imagenet的预训练&#xff0c;以提取有效的图片内容的特征数据。我用这个网络训练了30个EPOCH&#xff0c;最终到达Top-1 71%&#xff0c;Top-5 91%的准确率。具体的训练过程可以见我的博客<a href="https://blog.csdn.net/gzroy/article/details/104170537">https://blog.csdn.net/gzroy/article/details/104170537</a></p>
# <p>训练好了骨干网络之后&#xff0c;我们就可以在这个网络的基础上再增加相应的卷积层&#xff0c;实现图像特征金字塔(FPN)的架构&#xff0c;这里我们会用到骨干网络输出的route1, route2, route3这几个不同图像分辨率的特征值&#xff0c;最终构建一个可以对图片进行下采样8倍&#xff0c;16倍和32倍的基于网格的检测系统&#xff0c;例如训练图片的分辨率为416*416&#xff0c;那么将输出52*52, 26*26, 13*13这三个不同维度的检测结果。具体的原理可以参见网上的一些文章&#xff0c;例如&#xff1a;我这里参照Darknet的源代码来搭建了一个YOLO V3的网络&#xff0c;代码如下&#xff1a;</p>
category_num = 80
vector_size = 3 * (1 + 4 + category_num)
def darknet53_yolov3(imageHeight, imageWidth):
    route1 = tf.keras.Input(shape=(256, None,None), name='input1')        #256*H/8*W/8
    route2 = tf.keras.Input(shape=(512, None,None), name='input2')        #256*H/16*W/16
    route3 = tf.keras.Input(shape=(1024, None,None), name='input3')       #256*H/32*W/32
    net = _conv(route3, 512, 1, 1, 0, False, True, 'leaky_relu')         #512*H/32*W/32
    net = _conv(net, 1024, 3, 1, 1, False, True, 'leaky_relu')           #1024*H/32*W/32
    net = _conv(net, 512, 1, 1, 0, False, True, 'leaky_relu')            #512*H/32*W/32
    net = _conv(net, 1024, 3, 1, 1, False, True, 'leaky_relu')           #1024*H/32*W/32
    net = _conv(net, 512, 1, 1, 0, False, True, 'leaky_relu')            #512*H/32*W/32
    route4 = tf.identity(net, 'route4')
    net = _conv(net, 1024, 3, 1, 1, False, True, 'leaky_relu')           #1024*H/32*W/32
    predict1 = _conv(net, vector_size, 1, 1, 0, True, False, 'linear')   #vector_size*H/32*W/32
    predict1 = l.Activation('linear', dtype='float32')(predict1)
    predict1 = l.Reshape((vector_size, imageHeight//32*imageWidth//32))(predict1)
    net = _conv(route4, 256, 1, 1, 0, False, True, 'leaky_relu')         #256*H/32*W/32
    net = l.UpSampling2D((2, 2), "channels_first", 'nearest')(net)    #256*H/16*W/16
    net = l.Concatenate(axis=1)([route2, net])                     #768*H/16*W/16
    net = _conv(net, 256, 1, 1, 0, False, True, 'leaky_relu')            #256*H/16*W/16
    net = _conv(net, 512, 3, 1, 1, False, True, 'leaky_relu')            #512*H/16*W/16
    net = _conv(net, 256, 1, 1, 0, False, True, 'leaky_relu')            #256*H/16*W/16
    net = _conv(net, 512, 3, 1, 1, False, True, 'leaky_relu')            #512*H/16*W/16
    net = _conv(net, 256, 1, 1, 0, False, True, 'leaky_relu')            #256*H/16*W/16
    route5 = tf.identity(net, 'route5')
    net = _conv(net, 512, 3, 1, 1, False, True, 'leaky_relu')            #512*H/16*W/16
    predict2 = _conv(net, vector_size, 1, 1, 0, True, False, 'linear')   #vector_size*H/16*W/16
    predict2 = l.Activation('linear', dtype='float32')(predict2)
    predict2 = l.Reshape((vector_size, imageHeight//16*imageWidth//16))(predict2)
    net = _conv(route5, 128, 1, 1, 0, False, True, 'leaky_relu')         #128*H/16*W/16
    net = l.UpSampling2D((2, 2), "channels_first", 'nearest')(net)    #128*H/8*W/8
    net = l.Concatenate(axis=1)([route1, net])                     #384*H/8*W/8
    net = _conv(net, 128, 1, 1, 0, False, True, 'leaky_relu')            #128*H/8*W/8
    net = _conv(net, 256, 3, 1, 1, False, True, 'leaky_relu')            #256*H/8*W/8
    net = _conv(net, 128, 1, 1, 0, False, True, 'leaky_relu')            #128*H/8*W/8
    net = _conv(net, 256, 3, 1, 1, False, True, 'leaky_relu')            #256*H/8*W/8
    net = _conv(net, 128, 1, 1, 0, False, True, 'leaky_relu')            #128*H/8*W/8
    net = _conv(net, 256, 3, 1, 1, False, True, 'leaky_relu')            #256*H/8*W/8
    predict3 = _conv(net, vector_size, 1, 1, 0, True, False, 'linear')   #vector_size*H/8*W/8
    predict3 = l.Activation('linear', dtype='float32')(predict3)
    predict3 = l.Reshape((vector_size, imageHeight//8*imageWidth//8))(predict3)
    predict = l.Concatenate()([predict3, predict2, predict1])
    predict = tf.transpose(predict, perm=[0, 2, 1], name='predict')
    model = tf.keras.Model(inputs=[route1, route2, route3], outputs=predict, name='darknet53_yolo')
    return model
# <p>可以看到&#xff0c;这个网络模型是以骨干网络的三个输出route1, route2, route3作为输入的&#xff0c;最终输出的Predict是三个不同维度的预测结果。</p>
# <h3>YOLO V3训练过程</h3>
# <p>有了训练数据和搭建好网络模型之后&#xff0c;我们就可以开始训练了。整个训练过程分为如下几步&#xff1a;</p>
# <p><strong>1. 对骨干网络进行更高分辨率的训练</strong></p>
# <p>因为我们的骨干网络是基于224*224这个分辨率来进行训练和提取图片特征的&#xff0c;但是在物体检测中&#xff0c;这个分辨率太低&#xff0c;不利于检测小物体&#xff0c;因此我们需要基于更加高的分辨率&#xff0c;例如416*416来进行训练。我们可以把骨干网络基于这个高的分辨率再多训练一些次数&#xff0c;让网络适应高分辨率&#xff0c;这样可以最终提升物体检测的性能。为此我们可以重新加载之前训练好的骨干网络来进行训练。</p>
# <p><strong>2. 骨干网络和检测网络组合</strong></p>
# <p>把预训练完成后的骨干网络和检测网络组合起来&#xff0c;构成一个YOLO V3的网络模型。训练图片先通过骨干网络进行特征提取&#xff0c;输出route1,route2,route3这三个不同维度的图像特征数据&#xff0c;然后作为输入进到检测网络中进行训练&#xff0c;最终得到三个维度的预测结果。这个组合网络中&#xff0c;需要设置骨干网络的参数为不可训练&#xff0c;只训练检测网络的参数。代码如下&#xff1a;</p>
# <pre><code class="language-python">#Load the pretrained backbone model
model_base = tf.keras.models.load_model('darknet53/epoch_60.h5')
model_base.trainable = False
imageHeight = 416
imageWidth = 416
image = tf.keras.Input(shape=(3, imageHeight, imageWidth))
_, route1, route2, route3 = model_base(image, training=False)

#The detect model will accept the backmodel output as input
predict = darknet53_yolov3(image.shape[1], image.shape[2])([route1, route2, route3])

#Construct the combined yolo model