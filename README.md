# TestForPythonVirtualEnv
简单测试工具，检测是否正确安装英伟达驱动及深度学习框架
## 文件说明 ##
### testGPU.bat ###
windows环境下双击直接运行，检查当前windows环境下是否正确安装英伟达驱动及CUDA计算工具。
如果正确安装，输出如下所示：![GPU-test](https://user-images.githubusercontent.com/33210252/140044219-072a4e6d-1018-491a-957d-be2638f44795.JPG)
![cuda-test](https://user-images.githubusercontent.com/33210252/140044232-3a139379-3a35-48d4-be98-b2908fe82136.JPG)

由于显卡型号不同，所以显示内容可能有差异。
### PyTest_GPU.py ###
正确Torch、Tensorflow后输出如下所示：

![pyTest](https://user-images.githubusercontent.com/33210252/140045430-85c25ec0-1dd8-4682-b8db-e734868d714d.JPG)
