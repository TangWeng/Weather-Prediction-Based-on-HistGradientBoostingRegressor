【本项目为西南民族大学机器学习期末作业】
提交人：孙浩、李佳熹
本项目使用'HistGradientBoostingRegressor'模型来实现每个目标变量的回归，并计算预测值与真实值之间的误差。因为存在多个目标变量，所以在本算法中，我们为每个目标变量创建一个'HistGradientBoostingRegressor'模型，并使用噪声数据训练每个目标变量的回归模型。最终，本算法比给出的待优化模型在训练速度和准确性上都更加具有优势。


数据集链接：链接：https://pan.baidu.com/s/1UpbpJMvqgs3v0aVkJH4RAg?pwd=w30x  提取码：w30x
result链接：链接：https://pan.baidu.com/s/1uHEUf4pw6gtoF8Hca7kHow?pwd=r3uw  提取码：r3uw


运行说明：
- step01：将本项目中所有的文件，移入一个纯净的python项目中
- step02：执行002-add_noise.py文件，随机添加噪声
【执行完，在项目当前目录下，生成modified_数据集Time_Series448_detail.dat与modified_数据集Time_Series660_detail.dat】
- step03：执行003-main.py文件，训练模型并预测数据
- step04：执行HistGradientBoostingRegressor.py文件，训练模型并预测数据
- step05：对比HistGradientBoostingRegressor.py文件和003-main.py文件生成的结果


环境说明：
- python==3.9
- scikit-learn==1.4.1.post1  
- pandas==2.1.2
- numpy==1.26.1
- scipy==1.12.0
