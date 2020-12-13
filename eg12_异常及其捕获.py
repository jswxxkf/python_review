try:
    num = int(input("请输入一个整数："))
    res = 8 / num
except ValueError:
    print("请输入一个正确的整数！")
except ZeroDivisionError:
    print("除零错误")
except Exception as result:
    print("未知异常：{}".format(result))
else:
    print("没有出现任何异常")
finally:
    print("最终必定执行的代码")
