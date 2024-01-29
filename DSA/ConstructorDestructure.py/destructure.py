import time

class Test:
    def __init__(self) -> None:
        print("Object Initilization ...............")
    def __del__(self):
        print("Fulfiling the last wish and performing the clean up process.")


t1 = Test()
t1 = None
time.sleep(5)
print("End of Application.")

