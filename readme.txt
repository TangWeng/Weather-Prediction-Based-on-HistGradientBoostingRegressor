文件说明：
- 数据集Time_Series_448.dat ：训练集数据
- 数据集Time_Series_660.dat：预测集数据

运行说明：
- step01：将本项目中所有的文件，移入一个纯净的python项目中
- step02：执行001-add_noise.py文件，随机添加噪声
【执行完，在项目当前目录下，生成modified_数据集Time_Series448_detail.dat与modified_数据集Time_Series660_detail.dat】
- step03：执行002-main.py文件，训练模型并预测数据


环境说明：
- python==3.9
- scikit-learn==1.4.1.post1  
- pandas==2.1.2
- numpy==1.26.1
- scipy==1.12.0