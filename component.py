class point:
    def __init__(self,x = int,y = int):
        self.x = x
        self.y = y

class chess_piece:
    def __init__(self,current_location = point,color = str,icon = str):
        self.color = color
        self.current_location = current_location
        self.icon = icon

class pawn(chess_piece):
    def __init__(self,current_location,color,icon):
        super().__init__(current_location,color,icon)
        
class knight(chess_piece):
    def __init__(self,current_location,color,icon):
        super().__init__(current_location,color,icon)
    def getPossibleLocations(self)->list:
        lst = []
        x0 = self.current_location.x
        y0 = self.current_location.y
        for xi in [-2,-1,1,2]:
            for yi in [-2,-1,1,2]:
                if xi + yi % 2 != 0:
                    pi = point(x0 + xi,y0 + yi)
                    lst.append(pi)
        return lst
        
        