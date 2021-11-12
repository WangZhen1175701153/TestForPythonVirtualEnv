try:
    import tensorflow as tf
except:
    print("当前运行环境下没有正确安装Tensorflow")
try:
    import torch
except:
    print("当前环境下没有正确安装Torch")
import sys
class Test():
    def __init__(self):
        pass
    def TorchTest(self):
        import time
        print("torch版本为{}".format(torch.__version__))
        print(torch.cuda.is_available())        # 当CUDA可用时返回True
        print(torch.version.cuda)
        a = torch.randn(10000, 1000)    # 返回10000行1000列的张量矩阵
        b = torch.randn(1000, 2000)     # 返回1000行2000列的张量矩阵

        t0 = time.time()        # 记录时间
        c = torch.matmul(a, b)      # 矩阵乘法运算
        t1 = time.time()        # 记录时间
        print(a.device, t1 - t0, c.norm(2))     # c.norm(2)表示矩阵c的二范数

        device = torch.device('cuda')       # 用GPU来运行
        a = a.to(device)
        b = b.to(device)

        # 初次调用GPU，需要数据传送，因此比较慢
        t0 = time.time()
        c = torch.matmul(a, b)
        t2 = time.time()
        print(a.device, t2 - t0, c.norm(2))

        # 这才是GPU处理数据的真实运行时间，当数据量越大，GPU的优势越明显
        t0 = time.time()
        c = torch.matmul(a, b)
        t2 = time.time()
        print(a.device, t2 - t0, c.norm(2))
        print('#'*40,"Successfully Torch Test!! End",'#'*40)
        
    def PythonTest(self):
        print("Begin Python Test....")
        print("Successfully!! python-Hello World!!")
        print("当前python版本为:{}".format(sys.version))
        print('#'*40,"Successfully Python Test!! End",'#'*40)

    def TensorflowTest(self):
        print("Begin Tensorflow Test....")
        print("tensorflow版本为:{}".format(tf.__version__))
      
        import os
        os.environ["CUDA_VISIBLE_DEVICES"]="0"
        a=tf.constant(2)
        b=tf.constant(3)
        with tf.Session() as sess:
            print("a:%i" % sess.run(a),"b:%i" % sess.run(b))
            print("Addition with constants: %i" % sess.run(a+b))
            print("Multiplication with constant:%i" % sess.run(a*b))

        a=tf.placeholder(tf.int16)
        b=tf.placeholder(tf.int16)
        add=tf.add(a,b)
        mul=tf.multiply(a,b)
        with tf.Session() as sess:
            print("Addition with variables: %i" % sess.run(add,feed_dict={a:2,b:3}))
            print("Multiplication with variables: %i" % sess.run(mul,feed_dict={a:2,b:3}))

        with tf.Session() as sess:
            matrix1=tf.constant([[3.,3.]])
            matrix2=tf.constant([[2.],[2.]])
            product=tf.matmul(matrix1,matrix2)
            result=sess.run(product)
            print(result)
        print('#'*40,"Successfully Tensorflow Test!End",'#'*40)

if __name__ == "__main__":
    mainTest = Test()
    mainTest.PythonTest()
    mainTest.TensorflowTest()
    mainTest.TorchTest()