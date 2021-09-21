def cal():
    try:
        a=100
        b=20
        c=a/b
        print(c)
    except :
        print("not divisible")
        raise Exception("New")
    else:
        print("else is executed")
    finally:
        print("code executed")
cal()
