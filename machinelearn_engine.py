import tensorflow

import train_data_process
tf = train_data_process.tensorflow

func_name = ['Input', 'Model', 'Sequential', 'activations', 'applications', 'backend', 'callbacks', 'constraints',
             'datasets', 'estimator', 'experimental', 'initializers', 'layers', 'losses', 'metrics', 'mixed_precision',
             'models', 'optimizers', 'preprocessing', 'regularizers', 'utils', 'wrappers']


learn_rate = 0.001
input_layer = tf.keras.layers.Input(
                                    shape=(480, 640, 3),
                                    # batch_size=64,
                                    dtype=tensorflow.float32
                                )

xception_app = tf.keras.applications.Xception(
    include_top=False,
    weights=None,
    input_shape=(480, 640, 3)
)(input_layer)
"""
dense_all = tensorflow.keras.layers.AveragePooling2D(pool_size=[2, 2], strides=[1, 2], padding='SAME')(xception_app)
wrong single   ValueError: Shapes (None, 13) and (None, 15, 10, 13) are incompatible
"""
dense_all = tensorflow.keras.layers.AveragePooling2D(pool_size=[2, 2], strides=[1, 2], padding='SAME')(xception_app)
"""
dense_all = tensorflow.keras.layers.GlobalAveragePooling2D()(xception_app)
wrong single   ValueError: Shapes (None, 50) and (None, 9) are incompatible
"""
print(f"xception_app shape is {xception_app.shape}, \n GlobalAveragePooling2D out shape is {dense_all.shape}")

dense_all1 = tensorflow.keras.layers.Dense(2048, activation="relu")(dense_all)
dense_all2 = tensorflow.keras.layers.Dense(1024, activation="relu")(dense_all1)


dense_drill_angle = tensorflow.keras.layers.Dense(512, activation="relu")(dense_all2)
dense_drill_angle1 = tensorflow.keras.layers.Dense(256, activation="relu")(dense_drill_angle)
dense_drill_angle2 = tensorflow.keras.layers.Dense(256, activation="relu")(dense_drill_angle1)
dense_drill_anglea = tensorflow.keras.layers.GlobalAveragePooling2D()(dense_drill_angle2)

# dense_drill_angle3 = tensorflow.keras.layers.Dense(1, activation="softmax")(dense_drill_anglea)
dense_drill_angle3 = tensorflow.keras.layers.Dense(13, activation="softmax")(dense_drill_anglea)
print(dense_drill_angle3.shape)
print(dense_drill_angle3)
print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")


# dense_temperature = tensorflow.keras.layers.Dense(512, activation="relu")(dense_all2)
# dense_temperature1 = tensorflow.keras.layers.Dense(256, activation="relu")(dense_temperature)
# dense_temperature2 = tensorflow.keras.layers.Dense(64, activation="relu")(dense_temperature1)
# dense_temperaturea = tensorflow.keras.layers.GlobalAveragePooling2D()(dense_temperature2)
# dense_temperature3 = tensorflow.keras.layers.Dense(9, activation="softmax")(dense_temperaturea)
# dense_temperature3 = tensorflow.keras.layers.Dense(1, activation="softmax")(dense_temperaturea)

# ValueError: Dimensions must be equal, but are 13 and 20 for '{{node Equal}} = Equal[T=DT_FLOAT,
# incompatible_shape_error=true](Cast_7, Cast_8)' with input shapes: [?,13], [?,15,20].

# dense_up_down_angle = tensorflow.keras.layers.Dense(512, activation="relu")(dense_all2)
# dense_up_down_angle1 = tensorflow.keras.layers.Dense(256, activation="relu")(dense_up_down_angle)
# dense_up_down_angle2 = tensorflow.keras.layers.Dense(64, activation="relu")(dense_up_down_angle1)
# dense_up_down_anglea = tensorflow.keras.layers.GlobalAveragePooling2D()(dense_up_down_angle2)
# dense_up_down_angle3 = tensorflow.keras.layers.Dense(49, activation="softmax")(dense_up_down_anglea)


# out_put = [dense_drill_angle3, dense_temperature3, dense_up_down_angle3]
out_put = dense_drill_angle3
model = tf.keras.models.Model(
    inputs=input_layer,
    outputs=[dense_drill_angle3,]

)
model.summary()
# mm = model.get_layer(name="dense_13")

"""
loss="sparse_categorical_crossentropy"
Node: 'sparse_categorical_crossentropy_1/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits'
logits and labels must have the same first dimension, got logits shape [1,9] and labels shape [49]


"""
"""
Epoch 1/3
110/110 [==============================] - 8s 5ms/step - loss: 2.6861 - categorical_crossentropy: 2.6861
WARNING:tensorflow:Your input ran out of data; interrupting training. Make sure that your dataset or 
generator can generate at least `steps_per_epoch * epochs` batches (in this case, 330 batches). 
You may need to use the repeat() function when building your dataset.
"""
#  metrics=[tf.keras.metrics.'Accuracy'()] is ok
# "acc" cant ok    metrics=[tf.keras.metrics.CategoricalCrossentropy() is ok


model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=learn_rate),
    loss=tf.keras.losses.CategoricalCrossentropy(),
    metrics=[tf.keras.metrics.CategoricalCrossentropy(), tf.keras.metrics.Accuracy()]
)

history = model.fit(
    train_data_process.trainover,
    epochs=3,
    steps_per_epoch=110,

)
model.save("updown_backet.h5")
model.save_weights()
model.to_jason("updown_frame_.h5")
# model_ = tf.keras.Sequential()
# model_.add(Xception_app)
# model_.add(tf.keras.layers.GlobalAveragePooling2D())
# model_.add(tf.keras.layers.Dense(512, activation="relu"))
# model_.add(tf.keras.layers.Dense(13, activation="softmax"))
# model_.compile(
#    optimizer=tf.keras.optimizers.Adam(lr=learn_rate),
#    loss="mse",
#    metrics="mae"
# )
# history = model_.fit(
#             train_data_process.trainover,
#             epochs=1,
#             steps_per_epoch=109,
# )