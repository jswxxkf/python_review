def demo(num, num_list):
    print("函数内部的代码")
    num = 100
    # num_list.append("李丹")
    num_list += "李丹"  # 相当于调用列表的extend方法，即没有重新赋值
    print(num)
    print(num_list)
    print("函数执行完成")


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
