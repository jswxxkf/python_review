class Cat:
    def __init__(self, name):
        self.name = name
        self.__secret = "小秘密"
        print("{} 来了".format(self.name))

    def __del__(self):
        print("%s 我去了" % self.name)

    # override
    def __str__(self):
        return "我是一只猫，名叫{}".format(self.name)

    def __show_secret(self):
        return "小秘密是：{}".format(self.__secret)


cat = Cat("Tom")
# 强行访问私有方法或属性
# print(cat._Cat__show_secret())
print(cat)
del cat
