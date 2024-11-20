class Bird:

    def fly(self):
        return "Flies in the sky"

class Airplane:
    
    def fly(self):
        return "Flies in the air"

def let_fly(thing):
    print(thing.fly())

let_fly(Bird())       # Output: Flies in the sky
let_fly(Airplane())   # Output: Flies in the air
