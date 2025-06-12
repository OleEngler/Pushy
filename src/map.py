

class Map():
    def __init__(self):
        self.start_pos = None
        self.goal_pos = None
        self.layout = None

    def get_start_pos(self):
        return self.start_pos
    
    def get_goal_pos(self):
        return self.goal_pos
    
    def get_layout(self):
        return self.layout
    
    def set_start_pos(self,pos):
        self.start_pos = pos

    def set_goal_pos(self,pos):
        self.goal_pos = pos
    
    def set_layout(self,layout):
        self.layout = layout

    
    def load_map(self,path=None):
        if path == None:
            self.load_default_map()
        else:
            pass #TODO: Mapsladen evtl: JSON 


    def load_default_map(self):
        self.set_start_pos([5,1])
        self.set_goal_pos([1,8])
        self.set_layout(layout=[[1,1,1,1,1,1,1,1,1,1],
                                [1,0,0,0,0,0,0,0,3,1],
                                [1,0,0,0,0,0,0,0,0,1],
                                [1,0,0,4,0,0,0,0,0,1],
                                [1,0,0,0,0,0,0,0,0,1],
                                [1,2,0,0,0,0,0,0,0,1],
                                [1,1,1,1,1,1,1,1,1,1]])
        



    

