                                                #                                public class object:
class Object:                                   #create classs                      name : string
    def __init__(self, given_name):             #define constructor              public procedure new(given_name)      
        self.name = given_name                  #create attributes                  name = given_name 
                                                #                                       
    def show_name(self):                        #create methods
        print("name = " , self.name)



object1 = Object("O1")

object1.show_name()