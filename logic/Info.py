from collections import deque
from random import randint
import logic.algorithms.Solve as solve
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
        self.data.update({"body_length" : 1})
        self.data.update({"planning_time":[]})
        self.data.update({"moves" : 0})
        self.data.update({"times": dict()})
        self.update_plan()

    def move(self):
        self.data["moves"] += 1
        
        if self.get_head()==self.data["apple"]: 
            #print("Progress:",self.data["body_length"],"/",len(self.data["grid"]))
            self.eat()
            if not self.generate_apple():
                print("game WON")
                return False #STOPS MOVING
        else:
            self.data["order"].rotate(-1)

        return True
    

    def update_plan(self):
        # updates plan if needed
        if self.data["name"]=="simple_hamilton":
            #keeps old plan after first time
            if "plan" not in self.data:  
                self.data.update({"plan" : solve.simple_hamilton(self.data)})
                self.initial_plan_to_order()


    def get_head(self):
        return self.data["order"][self.data["body_length"]-1]


    def eat(self):
        self.data["body_length"] += 1

    def generate_apple(self):
        #randomly genarates apple
        #outside of body
        
        free = self.get_free_fields()
        if len(free) == 0:
            return False
        
        self.data.update({"apple":free[randint(0,len(free)-1)]})  
        self.update_plan()
        return True
   

    def initial_plan_to_order(self):
        #creates order from 0 out of plan
        self.data["order"].append(tuple(((self.data["rows"]//2)-1, (self.data["colums"]//2)-1)))
        start = self.data["order"][0] #start
        step = self.get_next_field(start)
        while start!=step:
            self.data["order"].append(step)
            step = self.get_next_field(step)
        
        if len(self.data["order"]) != len(self.data["order"]):
            raise ValueError("CUSTOM ERROR: no complete order generated")

            

    def update_plan_to_order(self):

        #Snake is 0-body_length-1 (right order) - nochange
        self.data["body_length"]
        #get new path
        
        for ii in range(len(self.data["grid"])):
            self.data["order"].rotate(-1) # one full round
            #in Body do nothing! (rotate through)
            if ii >= self.data["body_length"]-1:
                self.data["order"][0] = self.get_next_field(self.data["order"][-1])
                
        if len(self.data["order"]) != len(self.data["order"]):
            raise ValueError("CUSTOM ERROR: no complete order generated")            
    
    def get_body(self):
        return list(islice(self.data["order"] ,0, self.data["body_length"]))
    
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
