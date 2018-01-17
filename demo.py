#coding:utf-8
import model
from glob import glob
import numpy as np
from PIL import Image
import time
paths = glob('./test/*.*')

if __name__ =='__main__':
    im = Image.open(paths[1])
    img = np.array(im.convert('RGB'))
    t = time.time()
    result,img,angle = model.model(img,model='keras')
    print "It takes time:{}s".format(time.time()-t)
    print "---------------------------------------"
    for key in result:
        print result[key][1]
