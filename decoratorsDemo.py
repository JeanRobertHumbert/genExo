import time

def getTimeExec(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()-t1
        print(f"{func.__name__} ran in {t2} seconds.")
    return wrapper

@getTimeExec
def do_this():
    time.sleep(1.2)

@getTimeExec
def do_that():
    time.sleep(.4)
    
do_this()
do_that()
print("Done")