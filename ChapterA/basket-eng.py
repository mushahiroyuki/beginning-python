class Basket: 

    # Always remember the *self* argument 
    def __init__(self, contents=None): 
        self.contents = contents or [] 

    def add(self, element): 
        self.contents.append(element) 
            
    def print_me(self): 
        result = "" 
        for element in self.contents: 
            result = result + " " + repr(element) 
        print("Contains:", result) 
