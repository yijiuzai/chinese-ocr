# 本文基于tensorflow、keras/pytorch实现对自然场景的文字检测及端到端的OCR中文文字识别

# 实现功能

- [ ]  文字方向检测 0、90、180、270度检测 (运用vgg16分类模型实现，正在整理中)
- [x] 文字检测
- [x] 不定长OCR识别 

## 环境部署
``` Bash
sh setup.sh
```

# 模型训练

## 训练keras版本的crnn   

``` Bash
cd train & sh train-keras.sh   
```

## 训练pytorch版本的crnn   

``` Bash
cd train & sh train-pytorch.sh   
```

# 文字检测
[文本检测参考](https://github.com/eragonruan/text-detection-ctpn)(https://github.com/eragonruan/text-detection-ctpn)   

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
## 参考  

1.crnn https://github.com/meijieru/crnn.pytorch.git       

2.keras crnn 版本实现 https://www.zhihu.com/question/59645822       

3.ctpn https://github.com/eragonruan/text-detection-ctpn , https://github.com/tianzhi0549/CTPN   


