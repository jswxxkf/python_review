def input_pw():
    # 1. 提示用户输入密码
    pw = input("请输入密码：")
    # 2. 判断密码长度>=8，返回用户输入的密码
    if len(pw) >= 8:
        return pw
    # 3. 如果<8，则主动抛出异常
    print("主动抛出异常")
    # 3.1 创建异常对象
    ex = Exception("密码长度不够！")
    # 3.2 主动抛出异常
    raise ex


try:
    # 提示用户输入密码
    print(input_pw())
except Exception as res:
    print("异常发生：{}".format(res))
