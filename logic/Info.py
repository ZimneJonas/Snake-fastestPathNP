from collections import deque
from random import randint
from logic.Solver import Solver
from itertools import islice

class Info: 
    data = dict()
    def __init__(self, name = "simple_hamilton",rows = 72, colums = 48 ): #72/48
        self.data.update({"name" : name })
        self.data.update({"rows" : rows })
        self.data.update({"colums" : colums })
        self.data.update({"grid" : [(xx,yy) for xx in range(self.data["rows"]) for yy in range(self.data["colums"])]})
        self.data.update({"order": []})
        self.data.update({"tour": deque()}) #tour to apple
        self.data.update({"apple_at_step": [0]})
        #self.data.update({"order_status": False})
        #self.data.update({"body_length" : 1})
        self.data.update({"body":deque([0])})
        
        self.data.update({"moves" : 0})
        self.data.update({"times": dict()})
        self.data["times"].update({"planning_time":[]})
        self.solver = Solver(self)

    def move(self):
        self.data["moves"] += 1
        self.data["body"].append(self.data["tour"].popleft())
        #print(self.data["apple_at_step"][-1],self.data["moves"],self.get_apple_distance())
        
        if self.data["body"][-1]==self.data["apple_at_index"] : 
            print("Progress:",len(self.data["body"]),"/",len(self.data["grid"]))
            if not self.generate_apple():
                print("game WON")
                return False #STOPS MOVING
        else:
            self.data["body"].popleft()
            
        return True



    def get_next_in_order(self,index):
        if index+1<len(self.data["order"]):
            return index+1
        else:
            return 0



    def generate_apple(self):
        #randomly genarates apple
        #outside of body
        
        free_fields = self.get_free_fields()
        if len(free_fields)== 1:
            return False
        
        new_apple_index = free_fields[randint(0,len(free_fields)-1)]
        
        self.data.update({"apple":self.data["order"][new_apple_index]})   
        self.data.update({"apple_at_index":new_apple_index}) 
        self.solver.apple_update()
        return True
    
    def get_order_distance(self, index1,index2):
        #get distance from 1 to 2 in order
        if index2<=index1:
            return index1-index2
        else:
            return len(self.data["order"])-1-index2+index1

    def num_empty_fields(self):
        return len(self.data["order"])-len(self.data["body"])
    
    #def get_apple_distance_from_head(self):
    #    ''' gets distance from head to apple
    #    '''
    #    return self.data["apple_at_step"][-1]-self.data["moves"]
      
    
    def get_body(self):
        return {self.data["order"][ii] for ii in self.data["body"]}
    
    
    def get_free_fields(self):
        body_set = set(self.data["body"])
        free_fields=[index for index in range(0,len(self.data["grid"])) if index not in body_set]
        return free_fields


    def get_vertices(self):
        """ generates vertices 
            needed?
            ignores body for now #TODO maybe add
        """
        vertices = []
        for field in self.data["grid"]:
            if field[0]>0:
                vertices.append((field,(field[0]-1,field[1])))
            if field[1]>0:
                vertices.append((field,(field[0],field[1]-1)))
        return vertices

