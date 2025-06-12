import map


class Model:
    def __init__(self,map):
        map.load_map()
        self.layout = map.get_layout()
        self.current_pos = map.get_start_pos()
        self.goal_pos = map.get_goal_pos()


    def check_win(self):
        if self.current_pos == self.goal_pos:
            print("Gewonnen")
            return True
        else:
            return False 

    def move(self,pDirection):
        direction = pDirection.upper()
        if direction == "UP" or direction == "U":
            if self.layout[self.current_pos[0]-1][self.current_pos[1]] == 1:
                print("Mauer!!!")
            elif self.layout[self.current_pos[0]-1][self.current_pos[1]] == 4:
                self.push(self.current_pos,"UP",4)
            else:
                self.layout[self.current_pos[0]][self.current_pos[1]] = 0
                self.current_pos[0] -= 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
        elif direction == "DOWN" or direction == "D":
            if self.layout[self.current_pos[0]+1][self.current_pos[1]] == 1:
                print("Mauer!!!")
            elif self.layout[self.current_pos[0]+1][self.current_pos[1]] == 4:
                self.push(self.current_pos,"DOWN",4)
            else:
                self.layout[self.current_pos[0]][self.current_pos[1]] = 0
                self.current_pos[0] += 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
        elif direction == "LEFT" or direction == "L":
            if self.layout[self.current_pos[0]][self.current_pos[1]-1] == 1:
                print("Mauer!!!")
            elif self.layout[self.current_pos[0]][self.current_pos[1]-1] == 4:
                self.push(self.current_pos,"LEFT",4)
            else:
                self.layout[self.current_pos[0]][self.current_pos[1]] = 0
                self.current_pos[1] -= 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
        elif direction == "RIGHT" or direction == "R":
            if self.layout[self.current_pos[0]][self.current_pos[1]+1] == 1:
                print("Mauer!!!")
            elif self.layout[self.current_pos[0]][self.current_pos[1]+1] == 4:
                self.push(self.current_pos,"RIGHT",4)
            else:
                self.layout[self.current_pos[0]][self.current_pos[1]] = 0
                self.current_pos[1] += 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2

    def push(self,pos,dir,obj):
        if dir == "UP":
            if self.layout[self.current_pos[0]-2][self.current_pos[1]] == 0: #Feld zum Pushen ist frei
                self.layout[self.current_pos[0]-2][self.current_pos[1]] = obj
                self.layout[self.current_pos[0]][self.current_pos[1]] = 0
                self.current_pos[0] -= 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
        elif dir == "DOWN":
            if self.layout[self.current_pos[0]+2][self.current_pos[1]] == 0: #Feld zum Pushen ist frei
                self.layout[self.current_pos[0]+2][self.current_pos[1]] = obj
                self.layout[self.current_pos[0]][self.current_pos[1]] = 0
                self.current_pos[0] += 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
        elif dir == "LEFT":
            if self.layout[self.current_pos[0]][self.current_pos[1]-2] == 0: #Feld zum Pushen ist frei
                self.layout[self.current_pos[0]][self.current_pos[1]-2] = obj
                self.layout[self.current_pos[0]][self.current_pos[1]] = 0
                self.current_pos[1] -= 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
        elif dir == "RIGHT":
            if self.layout[self.current_pos[0]][self.current_pos[1]+2] == 0: #Feld zum Pushen ist frei
                self.layout[self.current_pos[0]][self.current_pos[1]+2] = obj
                self.layout[self.current_pos[0]][self.current_pos[1]] = 0
                self.current_pos[1] += 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2



    


    def print_field(self):
        for x in self.layout:
            print(x)
            

m = map.Map()
g = Model(m)

while not g.check_win():
    dir = input("Direction")
    g.move(dir)
    g.print_field()
    


