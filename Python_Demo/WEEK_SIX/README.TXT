#python pyinstaller
#第一步:确定python程序可执行, SchedulePrint.py 
#第二步:pyinstaller xxxx.py
	pyinstaller D:\demo\xxxx.py

#第三步:运行结果:dist 包含了发布的exe程序
	build是过程文件,可以删除

#注意:目录dist需要整体拷贝到其他系统使用,
	其中包含了exe运行的依赖库，不能只拷贝exe文件