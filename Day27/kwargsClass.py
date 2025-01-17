class Car:
    def __init__(self,**kw):
        self.model=kw["model"]
        self.color=kw["color"]

my_car=Car(model="benz",color="black")
print(my_car.model)
    
#what if i dont pass any arg when calling it will print error so to fix that we use get keyword like this
class bike:
    def __init__(self,**kw):
        self.model=kw.get("model")
        self.color=kw.get("color")

my_bike=bike(model="RX100")
print(my_bike.color)
    