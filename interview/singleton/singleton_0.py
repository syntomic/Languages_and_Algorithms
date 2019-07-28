# 模块第一次导入的时候， 生成.pyc文件， 第二次导入时，就会是直接加载.pyc文件.
class Singleton(object):
    def foo(self):
        pass


singleton = Singleton()

#from singleton_0 import singleton