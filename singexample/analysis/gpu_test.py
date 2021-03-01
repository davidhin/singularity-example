import tensorflow as tf
import tensorflow.keras.metrics as met
import tensorflow_addons.metrics as tfa_met
from singexample.helpers import ml_utils as mlu
from singexample.helpers import tf_utils as tfu


def create_model() -> tf.keras.models.Sequential:
    """Create Keras model."""
    return tf.keras.models.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )


# Load data
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
num_classes = len(set(y_train))

# Encode labels
onehot = mlu.EncoderHelper()
onehot.fit(y_train)
y_train = onehot.transform(y_train)
y_test = onehot.transform(y_test)


# Create model
model = create_model()
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=[
        met.CategoricalAccuracy(name="categorical_accuracy"),
        met.Recall(name="recall"),
        met.Precision(name="precision"),
        met.AUC(name="auc"),
        tfa_met.F1Score(num_classes=num_classes, average="macro", name="f1_macro"),
        tfa_met.MatthewsCorrelationCoefficient(num_classes=num_classes, name="mcc"),
    ],
)

# Fit data
# tfu.kill_tensorboard_pids()
proc = tfu.start_tensorboard(tfu.get_tb_logdir("gpu_test", False))
model.fit(
    x=x_train,
    y=y_train,
    epochs=5,
    validation_data=(x_test, y_test),
    callbacks=[tfu.tb_callback(tfu.get_tb_logdir("gpu_test"))],
)
proc.terminate()
