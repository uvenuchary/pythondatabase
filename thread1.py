import threading
import time
def square(n):
    print("square root of n is")
    for i in n:
        time.sleep(0.5)
        print("square is",i*i)
def cube(n):
    print("cube is")
    for i in n:
        time.sleep(0.5)
        print("cube",i*i*i)
ar=[9,8,6,3]
t1=time.time()
th1=threading.Thread(target=square,args=(ar,))
th2=threading.Thread(target=cube,args=(ar,))
th1.start()
th2.start()
th1.join()
th2.join()
print("total time taken",time.time()-t1)
