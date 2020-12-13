num = 10


def demo():
    # 若不写global，则会创建局部变量num，无法对全局变量进行修改
    global num
    num = 99
    print("num=%d" % num)


demo()
