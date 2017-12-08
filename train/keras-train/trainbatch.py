# -*- coding: utf-8 -*-
from train import *
model,basemodel = get_model(height=imgH, nclass=nclass)
import os
modelPath = '../pretrain-models/keras.hdf5'
if os.path.exists(modelPath):
       model.load_weights(modelPath)
        
batchSize = 128
train_loader = torch.utils.data.DataLoader(
    train_dataset, batch_size=batchSize,
    shuffle=True, sampler=sampler,
    num_workers=int(workers),
    collate_fn=dataset.alignCollate(imgH=imgH, imgW=imgW, keep_ratio=keep_ratio))

testSize = 64
test_loader = torch.utils.data.DataLoader(
    train_dataset, batch_size=testSize,
    shuffle=True, sampler=sampler,
    num_workers=int(workers),
    collate_fn=dataset.alignCollate(imgH=imgH, imgW=imgW, keep_ratio=keep_ratio))

j = 0
crrentLoss = 1000
loss = 1000
interval  = 50
for i in range(3):
    for X,Y in train_loader:
                X = X.numpy()
                X = X.reshape((-1,imgH,imgW,1))
                Y = np.array(Y)
                X,Y = [X, Y, np.ones(batchSize)*int(63), np.ones(batchSize)*n_len], np.ones(batchSize)    
                model.train_on_batch( X,Y)  
                if j%interval==0:
                   X,Y  =  next(iter(test_loader))
                   X = X.numpy()
                   X = X.reshape((-1,imgH,imgW,1))
                   Y = np.array(Y)
                   X,Y = [X, Y, np.ones(testSize)*int(63), np.ones(testSize)*n_len], np.ones(testSize) 
                   crrentLoss = model.evaluate(X,Y)
                   print "step:{},loss:{},crrentLoss:{}".format(j,loss,crrentLoss)
                   if crrentLoss<loss:
                        loss = crrentLoss
                        path = 'save_model/model{}.h5'.format(loss)
                        print "save model:".format(path)
                        model.save(path)

                j+=1
                
