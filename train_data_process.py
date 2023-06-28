import os
import glob
import numpy
import matplotlib.pyplot as plt
import tensorflow

x = "I:\导向仪图片"
xx = "angle_6__updown_up_1__temperature_16"
taile = "npy"
x2 = os.path.join(x, xx, taile)
dir_list_angle = os.listdir(x)
x3 = os.path.join(x, '上下角度为主')
path_updown_ = glob.glob(r"I:\导向仪图片\上下角度为主\*.npy")
x4 =  'I:\导向仪图片\旋转角度为主\*.npy'
drill_path_ = glob.glob(x4 )

def get_(path_):
    file_name = os.path.basename(path_)
    try:
        all_data = numpy.load(path_)
    except Exception:
        all_data = numpy.load(path_, allow_pickle=True)
    list_file = file_name.split("_")
    angle_ = int(list_file[1])
    updown = int(list_file[5]) if list_file[4] == "up" else int(list_file[5]) * (-1)
    temperature = int(list_file[8])
    lable_angle = numpy.zeros(shape=(all_data.shape[0])) + angle_
    lable_angle = lable_angle.astype(int)
    lable_updown = numpy.zeros(shape=(all_data.shape[0])) + updown
    lable_updown = lable_updown.astype(int)
    lable_temperature = numpy.zeros(shape=(all_data.shape[0])) + temperature
    lable_temperature = lable_temperature.astype(int)

    re_data = numpy.c_[lable_angle, lable_updown, lable_temperature]
    return all_data, re_data

def modify_img_size():
    all_data = numpy.load(r"I:\导向仪图片\旋转角度为主\angle_1__updown_up_0__temperature_16__battery4.8_94x.npy")
    n = 0
    for a in all_data:
        plt.subplot(2, 2, 1)
        plt.xlabel(a.shape)
        plt.imshow(a)
        scattel = 0.5
        new_size = (int(480*scattel), int(640*scattel))
        b = tensorflow.image.resize(a, new_size, method=tensorflow.image.ResizeMethod.NEAREST_NEIGHBOR)
        plt.subplot(2, 2, 2)
        plt.xlabel(new_size)
        plt.imshow(b)
        plt.show()
        break

def modify_all_img_size(path_, name="train"):
    new_paths = os.listdir(path_)
    path_ = str(path_, encoding="utf-8")
    for pat in new_paths:
        if type(pat) is bytes:
            pat = str(pat, encoding="utf-8")
        pat = os.path.join(path_, pat)
        train_data, lable_data = get_(pat)
        train_data = tensorflow.image.convert_image_dtype(train_data, tensorflow.float32)
        if name == "train":
            yield train_data
        else:
            yield lable_data

data = modify_all_img_size("I:\导向仪图片\上下角度为主")
datatrain = tensorflow.data.Dataset.from_generator(modify_all_img_size,
                                               output_types=tensorflow.float32,
                                               output_shapes=tensorflow.TensorShape((None, 480, 640, 3)),
                                               args=(r"I:\导向仪图片\上下角度为主",))
datatrain = datatrain.unbatch()

data_train_lable = tensorflow.data.Dataset.from_generator(modify_all_img_size,
                                               output_types=tensorflow.float32,
                                               output_shapes=tensorflow.TensorShape((None, 3)),
                                               args=(r"I:\导向仪图片\上下角度为主", "lable"))

for d in datatrain:
    d = tensorflow.image.resize_with_crop_or_pad(d, 480, 640)
    d = d.numpy()
    try:
        new_datatrain.concatenate(numpy.array([d]))
    except Exception:
        new_datatrain = numpy.array([d])
datatrain = tensorflow.data.Dataset.from_tensor_slices(new_datatrain)
data_train_lable = data_train_lable.unbatch()

for x in data_train_lable.as_numpy_iterator():
    try:
        x.astype(int)
        lable_data = numpy.concatenate([lable_data, numpy.array([x])], axis=0)
    except Exception:
        lable_data = numpy.array([x])
hot_angle = lable_data[:, 0].astype(int)
angle_hot = numpy.eye(13, 13, k=-1)[hot_angle]
updown_angle = lable_data[:, 1].astype(int)
updown_angle_hot = numpy.eye(49, 49)[updown_angle]
temperature_ = lable_data[:, 2].astype(int)
temperature_ = (temperature_/4).astype(int)
temperature_lable_hot = numpy.eye(6, 9, k=3)[temperature_]
lable_data_set = tensorflow.data.Dataset.from_tensor_slices((angle_hot, updown_angle_hot, temperature_lable_hot))

trainover = tensorflow.data.Dataset.zip((datatrain, lable_data_set))
trainover = trainover.shuffle(buffer_size=1024).repeat().batch(16)



