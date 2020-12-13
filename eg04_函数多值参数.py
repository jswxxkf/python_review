def demo(arg, *args, **kwargs):
    print("arg={}".format(arg))
    print(args)
    print(kwargs)


demo(1, 2, 3)
