import map


class Model:
    def __init__(self,map):
        map.load_map()
        self.layout = map.get_layout()
        self.current_pos = map.get_start_pos()
        self.goal_pos = map.get_goal_pos()
        self.stand_on = 0


    def check_win(self):
        self.balls_gone()
        if self.current_pos == self.goal_pos and self.balls_gone():
            print("Gewonnen")
            return True
        else:
            return False 
        
    #Alle Bälle sind Weg
    def balls_gone(self):
        for x in self.layout:
            for y in x:
                if y == 7 or y == 9:
                    return False
        return True
                
        
        
    #Zahlensheet
    #0=Frei, 1=Mauer, 2=Pushy, 3=Haus, 4=Kiste, 5=Wasser, 6=KisteWasser, 7=Ball_rot, 8=Lager_Rot, 9=Ball_grün
    

    def move(self,pDirection):
        direction = pDirection.upper()
        #UP________________________________________________________________________________________
        if direction == "UP" or direction == "U":
            if self.layout[self.current_pos[0]-1][self.current_pos[1]] == 1:
                print("Mauer!!!")
            elif self.layout[self.current_pos[0]-1][self.current_pos[1]] == 4:
                self.push(self.current_pos,"UP",4)
            elif self.layout[self.current_pos[0]-1][self.current_pos[1]] == 7:
                self.push(self.current_pos,"UP",7)

            if self.layout[self.current_pos[0]-1][self.current_pos[1]] == 0:
                self.layout[self.current_pos[0]][self.current_pos[1]] = self.stand_on
                self.current_pos[0] -= 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
                self.stand_on = 0
            elif self.layout[self.current_pos[0]-1][self.current_pos[1]] == 6:
                self.layout[self.current_pos[0]][self.current_pos[1]] = self.stand_on
                self.current_pos[0] -= 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
                self.stand_on = 6
            elif self.layout[self.current_pos[0]-1][self.current_pos[1]] == 3:
                self.layout[self.current_pos[0]][self.current_pos[1]] = self.stand_on
                self.current_pos[0] -= 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
                self.stand_on = 3
        #DOWN______________________________________________________________________________________
        elif direction == "DOWN" or direction == "D":
            if self.layout[self.current_pos[0]+1][self.current_pos[1]] == 1:
                print("Mauer!!!")
            elif self.layout[self.current_pos[0]+1][self.current_pos[1]] == 4:
                self.push(self.current_pos,"DOWN",4)
            elif self.layout[self.current_pos[0]+1][self.current_pos[1]] == 7:
                self.push(self.current_pos,"DOWN",7)


            if self.layout[self.current_pos[0]+1][self.current_pos[1]] == 0:
                self.layout[self.current_pos[0]][self.current_pos[1]] = self.stand_on
                self.current_pos[0] += 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
                self.stand_on = 0
            elif self.layout[self.current_pos[0]+1][self.current_pos[1]] == 6:
                self.layout[self.current_pos[0]][self.current_pos[1]] = self.stand_on
                self.current_pos[0] += 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
                self.stand_on = 6
            elif self.layout[self.current_pos[0]+1][self.current_pos[1]] == 3:
                self.layout[self.current_pos[0]][self.current_pos[1]] = self.stand_on
                self.current_pos[0] += 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
                self.stand_on = 3
        #LEFT______________________________________________________________________________________
        elif direction == "LEFT" or direction == "L":
            if self.layout[self.current_pos[0]][self.current_pos[1]-1] == 1:
                print("Mauer!!!")
            elif self.layout[self.current_pos[0]][self.current_pos[1]-1] == 4:
                self.push(self.current_pos,"LEFT",4)
            elif self.layout[self.current_pos[0]][self.current_pos[1]-1] == 7:
                self.push(self.current_pos,"LEFT",7)

            if self.layout[self.current_pos[0]][self.current_pos[1]-1] == 0:
                self.layout[self.current_pos[0]][self.current_pos[1]] = self.stand_on
                self.current_pos[1] -= 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
                self.stand_on = 0
            elif self.layout[self.current_pos[0]][self.current_pos[1]-1] == 6:
                self.layout[self.current_pos[0]][self.current_pos[1]] = self.stand_on
                self.current_pos[1] -= 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
                self.stand_on = 6
            elif self.layout[self.current_pos[0]][self.current_pos[1]-1] == 3:
                self.layout[self.current_pos[0]][self.current_pos[1]] = self.stand_on
                self.current_pos[1] -= 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
                self.stand_on = 3
        #RIGHT_____________________________________________________________________________________
        elif direction == "RIGHT" or direction == "R":
            if self.layout[self.current_pos[0]][self.current_pos[1]+1] == 1:
                print("Mauer!!!")
            elif self.layout[self.current_pos[0]][self.current_pos[1]+1] == 4:
                self.push(self.current_pos,"RIGHT",4)
            elif self.layout[self.current_pos[0]][self.current_pos[1]+1] == 7:
                self.push(self.current_pos,"RIGHT",7)

            if self.layout[self.current_pos[0]][self.current_pos[1]+1] == 0:
                self.layout[self.current_pos[0]][self.current_pos[1]] = self.stand_on
                self.current_pos[1] += 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
                self.stand_on = 0
            elif self.layout[self.current_pos[0]][self.current_pos[1]+1] == 6:
                self.layout[self.current_pos[0]][self.current_pos[1]] = self.stand_on
                self.current_pos[1] += 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 2
                self.stand_on = 6
            elif self.layout[self.current_pos[0]][self.current_pos[1]+1] == 3:
                self.layout[self.current_pos[0]][self.current_pos[1]] = self.stand_on
                self.current_pos[1] += 1
                self.layout[self.current_pos[0]][self.current_pos[1]] = 3
                self.stand_on = 6


    def push(self, pos, dir, obj):
        richtung = {
        "UP":    (-1, 0),
        "DOWN":  (1,  0),
        "LEFT":  (0, -1),
        "RIGHT": (0,  1)
        }

        if dir not in richtung:
            return  # Ungültige Richtung, kein Push

        dx, dy = richtung[dir]

        # Start- & Zielkoordinaten berechnen
        x, y = self.current_pos
        ziel1 = (x + dx, y + dy)       # Feld direkt neben Spieler
        ziel2 = (x + 2*dx, y + 2*dy)   # Feld nach dem geschobenen Objekt

        zielwert = self.layout[ziel2[0]][ziel2[1]]

        if zielwert == 0:
            self.layout[ziel2[0]][ziel2[1]] = obj
            self.layout[ziel1[0]][ziel1[1]] = 0
        elif zielwert == 5 and obj == 4:  # Kiste in Wasser → Floß
            self.layout[ziel2[0]][ziel2[1]] = 6
            self.layout[ziel1[0]][ziel1[1]] = 0
        elif zielwert == 8 and obj == 7:  # Ball ins Lager
            self.layout[ziel2[0]][ziel2[1]] = 8
            self.layout[ziel1[0]][ziel1[1]] = 0





    def print_field(self):
        for x in self.layout:
            print(x)
            

m = map.Map("Map1.json")
g = Model(m)

while not g.check_win():
    dir = input("Direction")
    g.move(dir)
    g.print_field()
    
