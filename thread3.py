import threading
def hello(n):
    print("I am waiting from _ minutes",n)
t1=threading.Thread(target=hello,args=(30,))
t1.start()
    