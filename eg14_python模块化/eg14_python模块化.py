import eg14_测试模块1 as DogModule
import eg14_测试模块2 as CatModule


def main():
    DogModule.say_hello()
    CatModule.say_hello()

    dog = DogModule.Dog()
    print(dog)
    cat = CatModule.Cat()
    print(cat)


# 只有当前执行的模块,__name__才是__main__
# 被导入的模块,__name__就是模块名
# print(__name__)
if __name__ == "__main__":
    main()
