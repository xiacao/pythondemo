#python py2exe 库的使用步骤
#第一步:确定python程序可执行, SchedulePrint.py 
#第二步:写一个发布脚本 setup.py
from distutils.core import setup
import py2exe

setup(console = ['SchedulePrint.py'])
#第三步:打开命令行,在cmd命令行运行
#第四步:运行结果:dist 包含了发布的exe程序
	__pycache__是过程文件,可以删除

#注意:目录dist需要整体拷贝到其他系统使用,
	其中包含了exe运行的依赖库，不能只拷贝exe文件
#目前不兼容python3.6