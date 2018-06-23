#LearnMatplotlib.py
"""
学习手册：http://www.labri.fr/perso/nrougier/teaching/matplotlib/

 
"""
"""
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4, 5, 6], 'ro') #表示123456各画一个点，形状是红色小圆圈
plt.ylabel('Description of y value') #Y轴的名称
plt.show()#显示画面
"""

"""#画sin()和cos()图像
import numpy as np  #导入库 使用前缀为np.不用as时使用前缀为numpy.
from matplotlib.pyplot import *#不需要使用前缀

X = np.linspace(-np.pi, np.pi, 256, endpoint = True)#起点终点 间隔个数，结束时打点
C, S = np.cos(X * X), np.sin(X) 
plot(X, C, "ro", label = "$sin(x)$")#x轴，y轴，样式， 标签名,#这个一个不定参数的列表
plot(X, S, label="$cos(x^2)$")
xlabel('xlabel')
ylabel('ylabel')
legend()    #两条曲线的标签
title('This is Title')
show()
"""

"""#画子图
from matplotlib.pyplot import *

subplot(2, 2, 1) #等分为几行，几列 编号为几等同于subplot(221)
subplot(2, 2, 2)
subplot(1, 2, 1)
subplot(2, 2, 4)
show()
"""

"""#双子图绘制
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.subplot(2, 1, 1)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(2, 1, 2)
plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
plt.show()
"""
"""#画直方图
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)#生成10000个为(0,1)的正态分布
plt.hist(x, 50, normed = 1, facecolor = 'g')#50个柱形，normed=1时表示概率，等于0时表示数值
plt.xlabel("Smarts")
plt.ylabel("Probability")
plt.title("Histogram of IQ")
plt.text(60, 0.025, r'$\mu=100,\ \sigma=15$')#指定位置添加文本标识
plt.axis([40, 160, 0, 0.03])#x轴，y轴
plt.show()
"""

#操作图像
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('python_logo.gif')
plt.imshow(img)
plt.show()
