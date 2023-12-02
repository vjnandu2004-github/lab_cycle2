class Box:
    def __init__(self,length,breadth=None,height=None):
        #rectangular prism
        self.Length=length
        self.Breadth=breadth
        self.Height=height

        #cube
        if breadth is None and height is None:
            self.Breadth=length
            self.Height=length
        elif height is None:
            self.Height=length
    
    def Area(self):
        area=2*(self.Length*self.Breadth+self.Breadth*self.Height+self.Length*self.Height)
        return area
    
    def volume(self):
        vol=self.Length*self.Breadth*self.Height
        return vol
    
cube=Box(5)
sq_prism=Box(5,4)
rect_prisem=Box(5,4,3)
print("AREA OF CUBE:", cube.Area())
print("VOLUME OF CUBE:",cube.volume())

print("AREA OF SQUARE PRISM:", sq_prism.Area())
print("VOLUME OF SQUARE PRISM:",sq_prism.volume())

print("AREA OF RECTANGULAR PRISM:",rect_prisem.Area())
print("VOLUME OF RECTANGULAR PRISM:",rect_prisem.volume())

