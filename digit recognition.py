from sklearn.datasets import load_digits
from matplotlib import pyplot as plt
from sklearn.svm import SVC
from scipy import misc
mydata=load_digits()
#print(mydata.keys())
x_feature=mydata.data
y_target=mydata.target
#print(y_target.shape)
#print(x_feature.shape)
#print(x_feature)
input_image=mydata.images[1]
#print(input_image.shape)
#print(input_image.dtype)
i=x_feature[0]
t=y_target[0]
#print(i)
#print(t)
#print(i.shape)
#print(i[8:16])
#print(input_image)
#plt.matshow(input_image)
myteacher=SVC(gamma=.0001)
mylearner=myteacher.fit(x_feature,y_target)
#for testing ...... image reading
mytest_image=misc.imread("8.jpg")
#print(mytest_image)
#print(mytest_image.shape)
test_image_resize=misc.imresize(mytest_image,(8,8))
#print(test_image_resize.shape)
#print(test_image_resize.dtype)
#print(mydata.images.dtype)
#dtype .......... conversions
mytest_image_float=test_image_resize.astype(mydata.images.dtype)
#print(mytest_image_float.dtype)
#print(mytest_image_float)
#down scaling
mytest_image_downscale=misc.bytescale(mytest_image_float,high=16,low=0)
#print(mytest_image_downscale.dtype)
mytest_image_downscale=test_image_resize.astype(mydata.images.dtype)
#print(mytest_image_downscale.dtype)
#print(mytest_image_downscale.shape)
xx_test_image=[]
for i in mytest_image_downscale:
    for j in i:
        xx_test_image.append(sum(j/3.0))
print(len(xx_test_image))
print(mylearner.predict(xx_test_image))
    
    
    
    
    
    
    
    