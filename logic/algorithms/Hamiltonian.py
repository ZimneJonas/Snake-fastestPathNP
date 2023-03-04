import time
from itertools import islice
import random

def simple_hamilton(data):
    
    start = time.time()
    if data["rows"]%2:
        raise ValueError('uneven colums not yet accepted')
    if data["rows"]<1 or data["colums"]<1:
        raise ValueError('too smal')
   
    plan = dict(())
    for yy in range(data["colums"]):
        for xx in range(data["rows"]):
            field = (xx,yy)
            if yy == 0 and xx!=0 :
                plan.update({field:"up"})
            elif not xx%2: #even
                if yy+1 == data["colums"]:
                    plan.update({field:"down"})
                else:
                    plan.update({field:"right"})
                #every second row goes left
            else: #uneven
                if yy == 1 and xx != data["rows"]-1:
                    plan.update({field:"down"})
                else:
                    plan.update({field:"left"}) 
    #   * - * - * - * - *
    #   |               |
    #   *   * - * - * - *
    #   |   |
    #   *   * - * - * - *
    #   |               |
    #   *   * - * - * - *
    #   |   |
    #   *   * - * - * - *
    #   |               |
    #   * - * - * - * - *    
    end = time.time()

    #TODO ILLIGAL ACCESS
    data["times"]["planning_time"].append(("simple_hamilton",end-start))

    return plan


class Stack:
        
    def __init__(self,data):
        self.data = data
        self.cycle = []
        self.visited = set()
        self.checked = []
        self.foundFlag = False
        self.hamCycle = []


    def safe_result(self):
        if not self.foundFlag:
            self.foundFlag = True
            self.hamCycle = self.cycle.copy()
    # 
    def build_stack(self, current_cell):
        if self.foundFlag:
            return False
        self.cycle.append(current_cell)    
        self.visited.add(current_cell)
        neighbors = get_neighbors(current_cell, self.data)
        if len(self.cycle) == len(self.data["grid"]):
            # Found a cycle!
            if not self.foundFlag and self.cycle[0] in neighbors:            
                self.safe_result()
                self.foundFlag = True
                return True
            else:
                return False
            

        unvisited_neighbors = [cell for cell in neighbors if cell not in self.visited]    
        # shuffle unvisited neighbor to explore a random path
        random.shuffle(unvisited_neighbors)

        for cell in unvisited_neighbors:
            if self.foundFlag:
                return False
            if not self.build_stack(cell):
                self.visited.remove(cell)
                self.cycle.pop()
        #print(self.cycle, self.hamCycle , len(self.cycle), "/", len(self.data["grid"]))
        return False
        

        
    def get_hamCycle(self):
        self.build_stack((1,0))
        
        return self.hamCycle


def random_hamilton(solver):
    start = time.time()
    myStack = Stack(solver.data)
    order = myStack.get_hamCycle()
    end = time.time()
    solver.data["times"]["planning_time"].append(("random_hamilton",end-start))
    return order
    


def get_neighbors(cell, data):
    """Get a list of neighboring cells in an n x n grid."""
    row, col = cell
    data["rows"]
    neighbors = []
    if row > 0:
        neighbors.append((row-1, col))
    if row < data["rows"]-1:
        neighbors.append((row+1, col))
    if col > 0:
        neighbors.append((row, col-1))
    if col < data["colums"]-1:
        neighbors.append((row, col+1))
    return neighbors



def find_skip(path,game):
    order=game.data["order"]
    dist_to_apple = len(path)-1
    step=0
    #print("before",path)
    #While Path to apple relativly long
    
    while dist_to_apple>step+2 :
        head_field = order[path[step]]
        x=head_field[0]
        y=head_field[1] 
        jump=0

        #check if adjacent tiles are in path
        for ii in range(step+1,len(path)):
            n = order[path[ii]]
            #TODO all directions
            if n==(x+1,y):
                jump=ii-step-1
                break
        
    
        #DO NOT jump if distance to tail is smaller then body
        dist=game.get_order_distance(path[step+jump],game.data["body"][0])
        if dist>len(game.data["body"]): # don't jump single steps
            #print(head_field,"to",(x+1,y),"jump:",jump,"becouse apple at",order[path[-1]])
            #print(head_field , "to", order[jump],jump)
            del path[step+1:step+jump+1]
            dist_to_apple -= jump

        step += 1

    #print("after ",path)
    
     



def short_cut(solver):

    start=time.time()
    data = solver.game.data
    head_index = data["body"][-1]
    apple_index = data["apple_at_index"]
    #fill path from 
    if apple_index > head_index:
        path = list(range(head_index+1,apple_index+1))
    else:   
    #if apple before head in order extend path to apple    
        path = list(range(head_index+1,len(data["order"])))
        path.extend(range(apple_index+1))
    
    
    if len(data["body"]) > len(data["grid"])*data["skipPercent"]/100:
        #Only search for shortcuts if some space is left
        return path
    
    find_skip(path,solver.game)
    end=time.time()
    data["times"]["shortcuts"] += end-start
    return path





        

