try:
    import tensorflow as tf
except:
    print("当前运行环境下没有正确安装Tensorflow")
try:
    import torch
except:
    print("当前环境下没有正确安装Torch")


def mainTest():
    print("tensorflow版本为:{}".format(tf.__version__))
    print("torch版本为{}".format(torch.__version__))


if __name__ == "__main__":
    mainTest()