# 2024
2024秋软件测试代码作业，测试对象是faceNet人脸识别模型。模拟多个不同的测试场景进行人脸识别测试并进行测试评价。

#### 运行环境

window11，anaconda默认环境。

需要conda命令为默认环境安装库：

```
conda install keras_facenet
conda install cv2
conda install os 
```

进入工作目录下，运行命令：(命令无法执行则进入ide执行)

```
 python -u .\setup.py
```

解压后，可以进入python-notebook进行执行。（内核选择conda base）

### 文件结构

```
项目文件结构
2024
│── dataset (zip文件，解压后产生以下4个文件夹)
│── att_faces
│── ca-aligned
│── cp-aligned
│── CroppedYalePNG
│
├── pre-process-script
|   ├──	align_arc_pose.py
│   └── align_arc_age.py
│
├── 参考论文
│   └── 开展本项目参考的论文
├── setup.py （进行解压）
├── age.ipynb
├── expression.ipynb
├── illumination.ipynb
└── pose.ipynb

```

#### 4个测试数据集：

att_faces

ca-aligned

cp-aligned

CroppedYalePNG

#### 图片裁剪脚本：（无需运行，数据集中的图片已经经过裁剪）

pre-process-script

#### 参考论文：

开展本项目参考的论文

#### 自动化测试脚本，每一个都可直接运行：模拟不同场景下的测试脚本。

age.ipynb

expression.ipynb

illumination.ipynb

pose.ipynb