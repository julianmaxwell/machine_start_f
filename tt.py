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


def get_every_file_last_img(file_path, n=-2):
    all_data = numpy.load(file_path)
    pic_N = n

    plt.imshow(all_data[pic_N])
    plt.xlabel(file_path)
    plt.show()
    lable_angle = []
    xx = numpy.zeros(all_data.shape[0])

# get_every_file_last_img(r"I:\导向仪图片\旋转角度为主\angle_1__updown_up_0__temperature_16__battery4.8_94x.npy")
def get_(path_):
    file_name = os.path.basename(path_)
    try:
        all_data = numpy.load(path_)
    except Exception:
        all_data = numpy.load(path_, allow_pickle=True)
    list_file = file_name.split("_")
    print(list_file)
    angle_ = float(list_file[1])
    updown = float(int(list_file[5]) if list_file[4] == "up" else float(int(list_file[5]) * (-1)))
    temperature = float(list_file[8])

    lable_angle = numpy.zeros(shape=(all_data.shape[0])) + angle_
    lable_updown = numpy.zeros(shape=(all_data.shape[0])) + updown
    lable_temperature = numpy.zeros(shape=(all_data.shape[0])) + temperature
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
        print(new_size)
        b = tensorflow.image.resize(a, new_size, method=tensorflow.image.ResizeMethod.NEAREST_NEIGHBOR)
        plt.subplot(2, 2, 2)
        plt.xlabel(new_size)

        plt.imshow(b)
        plt.show()
        break
# modify_img_size()

def modify_all_img_size(path_, name="train"):
    new_paths = os.listdir(path_)
    print(new_paths)
    path_ = str(path_, encoding="utf-8")
    print(path_)
    for pat in new_paths:
        if type(pat) is bytes:
            pat = str(pat, encoding="utf-8")
        print(type(path_), path_)
        pat = os.path.join(path_, pat)
        train_data, lable_data = get_(pat)
        print(pat)
        index = new_paths.index(bytes(os.path.basename(pat), "utf-8"))
        try:
            print("next path file is :")
            print(new_paths[index+1])
        except Exception:
            pass
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa111222")
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


data_train_lable = data_train_lable.unbatch()
trainover = tensorflow.data.Dataset.zip((datatrain, data_train_lable))
trainover = trainover.batch(64)
trainover.shuffle(buffer_size=1024)
n = 0
for x in trainover.as_numpy_iterator():
    print(x[0].shape, n)
    n = n + 1





