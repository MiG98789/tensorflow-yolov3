import tensorflow as tf
from tensorflow.contrib import slim

from tests.darknet53_test import Darknet53Test
from tests.tf_utils_test import TFUtilsTest
from tests.yolov3_test import YOLOv3Test
from utils import tf_utils
from config.config import config

normalizer_params = {'decay': config['BATCH_NORM_DECAY'],
                     'epsilon': config['BATCH_NORM_EPSILON'],
                     'scale': True,
                     'is_training': True,
                     'fused': None}
LEAKY_RELU = config['LEAKY_RELU']
REUSE = config['REUSE']

with slim.arg_scope([slim.conv2d],
                    normalizer_fn=slim.batch_norm,
                    normalizer_params=normalizer_params,
                    biases_initializer=None,
                    activation_fn=lambda x: tf.nn.leaky_relu(x, alpha=LEAKY_RELU)):
    with slim.arg_scope([slim.batch_norm, slim.conv2d, tf_utils.fixed_padding], reuse=REUSE):
        Darknet53Test()
        TFUtilsTest()
        YOLOv3Test()

if __name__ == '__main__':
    tf.test.main()
