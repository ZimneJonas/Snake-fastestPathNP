from collections import deque
from random import randint
from algorithms.Solve import Solve as solve
from itertools import islice

class Info: 
    data = dict()
    def __init__(self, name = "simple_hamilton",rows = 72, colums = 48 ): #72/48
        self.data.update({"name" : name })
        self.data.update({"rows" : rows })
        self.data.update({"colums" : colums })
        self.data.update({"grid" : [(xx,yy) for xx in range(self.data["rows"]) for yy in range(self.data["colums"])]})
        
        self.data.update({"order": deque()})
        self.data.update({"order_status": False})
        #Head of Snake starts in middle of grid
        self.data.update({"head" : ((self.data["rows"]//2)-1, (self.data["colums"]//2)-1)})
        self.data.update({"body_length" : 1})
        self.data.update({"planning_time":[]})
        self.data.update({"moves" : 0})
        self.data.update({"times": dict()})


    def update_plan(self):
        # updates plan if needed
        if self.data["name"]=="simple_hamilton":
            #keeps old plan after first time
            if "plan" not in self.data:  
                self.data.update({"plan" : solve.simple_hamilton(self.data)})
                self.plan_to_order()


    def generate_apple(self):
        #randomly genarates apple
        #outside of body
        
        free = len(self.data["grid"]) - self.data["body_length"]
        
        if free:
            raise ValueError('No free Spaces')
        
        self.data.update({"apple":self.data["order"][randint(0,free)]})  
        self.update_plan()
   


    def plan_to_order(self):
        #Snake is 0-body_length-1 (right order)
        
        free = self.get_free_fields()
        #delete old path
        self.del_free_fields()
        #get new path
        for field in free:
            self.get_next_field(field)     
        
    
    def del_free_fields(self):
        self.data["order"]=islice(self.data["order"] ,0 , self.data["body_length"])

    def get_free_fields(self):
        return list(islice(self.data["order"] ,self.data["body_length"], len(self.data["grid"])))


    def get_next_field(self, field):
        driection = self.data["plan"][field]
        if driection=="up":
            field =(field[0]-1,field[1]) 
        elif driection=="down":
            field =(field[0]+1,field[1]) 
        elif driection=="left":
            field =(field[0],field[1]-1)
        elif driection=="right":
            field =(field[0],field[1]+1)
        else:
            raise Exception('Wrong direction')
        return field
