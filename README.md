# 本文基于tensorflow、keras/pytorch实现对自然场景的文字检测及端到端的OCR中文文字识别
## 环境部署
## cython nms
## python2.7
## tensorflow=1.3
## keras=2.0.8 or pytorch=0.2.0
## 安装运行 sh setup.sh

# 模型训练参考

## 训练keras版本的crnn   

cd train & sh train-keras.sh   
## 训练pytorch版本的crnn   
cd train & sh train-pytorch.sh   


# 文字检测
[文本检测参考](https://github.com/eragonruan/text-detection-ctpn)(https://github.com/eragonruan/text-detection-ctpn) [blog](http://slade-ruan.me/2017/10/22/text-detection-ctpn/
在原作者的代码基础上修改编译代码，新增支持CPU模式下的文字检测，详见:https://github.com/chineseocr/new-text-detection-ctpn.git   

# OCR 端到端识别:GRU+CTC
## ocr识别采用GRU+CTC端到到识别技术，实现不分隔识别不定长文字
提供keras 与pytorch版本的训练代码，在理解keras的基础上，可以切换到pytorch版本，此版本更稳定   


# 识别结果展示
## 文字检测及OCR识别结果
<div>
<img width="300" height="300" src="https://github.com/chineseocr/chinses-ocr/blob/master/img/tmp.jpg"/>
<img width="300" height="300" src="https://github.com/chineseocr/chinses-ocr/blob/master/img/tmp.png"/>
</div>

### 倾斜文字
<div>
<img width="300" height="300" src="https://github.com/chineseocr/chinses-ocr/blob/master/img/tmp1.jpg"/>
<img width="300" height="300" src="https://github.com/chineseocr/chinses-ocr/blob/master/img/tmp1.png"/>
</div>