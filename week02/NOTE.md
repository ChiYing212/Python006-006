学习笔记

 一. requests库
    模仿浏览器产生的操作
    
 二.增加程序健壮性
    1.上下文管理器：with open...
    2.异常处理
        语法：try..except...finally；
        异常是一种类，所有的异常类继承自BaseException；
        异常捕获过程： 
            打包错误信息到一个对象中
            该对象自动查找到调用栈
            直到运行系统找到明确声明如何处理这些类异常的位置
        常见的异常类型：LookupError,IOError,NameError,TypeError,ZeroDivisionError等

