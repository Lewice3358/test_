

class Room:
    
    numberOfRooms = 0
    def __init__ (self, name, width, length, height = 0, chairs = 0):
        #print("in constructor")
        temp = 10
        self.__name = name
        self.__width = width
        self.__length = length
        self.__height = height
        self.__chairs = chairs
        Room.numberOfRooms += 1
        
    def setname (self, name):
        self.__name = name
        return True
    def getname (self):
        return self.__name
    
    def setwidth (self, width):
        if width > 0 and width < 100:
            return True
        else:
            return False
    def getwidth (self):
        return self.__width
    
    def setlength (self, length):
        if length >= 0:
            self.__length = length
            return True
        else:
            return False
    def getlength (self):
        return self.__length
    
    def setheight (self, height)
    
    
    #I have made some changes just for learning. 
    #let's see how it goes. Lol.
