import time
from itertools import islice

def simple_hamilton(data):
    start = time.time()
    if data["colums"]%2:
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
    
    
    if len(data["body"])*2 > len(data["grid"]):
        #Only search for shortcuts if some space is left
        return path
    
    find_skip(path,solver.game)
    end=time.time()
    data["times"]["shortcuts"] += end-start
    return path





        

