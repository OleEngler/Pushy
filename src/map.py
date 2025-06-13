import json
from pathlib import Path

class Map():
    def __init__(self,map_file_name=None):
        self.name = None
        self.start_pos = None
        self.goal_pos = None
        self.layout = None
        self.project_file = Path(__file__).resolve().parent.parent
        self.map_file_name = map_file_name

    def get_name(self):
        return self.name
    
    def get_start_pos(self):
        return self.start_pos
    
    def get_goal_pos(self):
        return self.goal_pos
    
    def get_layout(self):
        return self.layout
    
    def set_name(self,name):
        self.name = name
    
    def set_start_pos(self,pos):
        self.start_pos = pos

    def set_goal_pos(self,pos):
        self.goal_pos = pos
    
    def set_layout(self,layout):
        self.layout = layout

    
    def load_map(self):
        if self.map_file_name == None:
            self.load_default_map()
        else:
            with open(f"{self.project_file}\\maps\\{self.map_file_name}", "r", encoding="utf-8") as f:
                daten = json.load(f)

            self.set_name(daten["Name"])
            self.set_start_pos(daten["Start_pos"])
            self.set_goal_pos(daten["Goal_pos"])
            self.set_layout(daten["Layout"])


    def load_default_map(self):
        self.set_start_pos([5,1])
        self.set_goal_pos([1,8])
        self.set_layout(layout=[[1,1,1,1,1,1,1,1,1,1],
                                [1,8,0,0,0,0,0,0,3,1],
                                [1,0,0,0,0,5,0,0,0,1],
                                [1,7,0,4,0,0,0,0,0,1],
                                [1,0,0,0,0,0,0,0,0,1],
                                [1,2,0,0,0,0,0,0,0,1],
                                [1,1,1,1,1,1,1,1,1,1]])
        




    

