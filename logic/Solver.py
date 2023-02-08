import time
import logic.algorithms.Hamiltonian as hamil


class Solver:
    #TODO make solver do solving depending on stuff
    def __init__(self,game):
        self.data = game.data
        self.game = game
        self.initial_update()
        


            

    def apple_update(self):
        if "hamilton" in self.data["name"]:
            if "shortcuting" in self.data["name"]:
                self.data["tour"].extend(hamil.short_cut(self))
            elif len(self.data["tour"])<len(self.data["order"]):
                self.data["tour"].extend(range(len(self.data["order"])))
            

    def initial_update(self):
        if "simple_hamilton" in self.data["name"]:  
            self.data.update({"plan" : hamil.simple_hamilton(self.data)})
            self.initial_plan_to_order()
        if "shortcuting" in self.data["name"]:
            self.data["times"].update({"shortcuts":0})

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
        """Snake is 0-body_length-1 (right order) - nochange
        #get new path
        """
        for ii in range(len(self.data["grid"])):
            self.data["order"].rotate(-1) # one full round
            #in Body do nothing! (rotate through)
            if ii >= self.data["body_length"]-1:
                self.data["order"][0] = self.get_next_field(self.data["order"][-1])
                
        if len(self.data["order"]) != len(self.data["order"]):
            raise ValueError("CUSTOM ERROR: no complete order generated")

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




