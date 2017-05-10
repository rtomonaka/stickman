class MyClass:
    def __init__(self, init_val):
        self.val = init_val

    def get_val(self):
        return self.val

    def add(self, y):
        self.val = self.val + y

    def add3(self, x,y,z):
        self.val = self.val + add3(x,y,z)
        

def add3(x,y,z):
    return x + y + z

o = MyClass(10)

platform_config = {
    "platform1.gif" : [[0,480,100,10],
                       [150,440,100,10],
                       [300,400,100,10],
                       [300,160,100,10]],
    "platform2.gif" : [[175,350,66,10],
                       [50,300,60,10],
                       [170,120,60,10],
                       [45,60,60,10]],
    "platform3.gif" : [[170,250,30,10],
                       [230,200,30,10]] }
