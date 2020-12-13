class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    single_instance = None
    # 记录是否执行过初始化操作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.single_instance is None:
            cls.single_instance = super().__new__(cls)
        return cls.single_instance

    def __init__(self):
        if not self.init_flag:
            print("对象在内存中的地址为：{}".format(id(self)))
            self.init_flag = True


player1 = MusicPlayer()
player2 = MusicPlayer()
