import logic.algorithms.Solve as solve
from random import randint


def update_plan(game):
    
    # updates plan if needed
    if game.data["name"]=="simple_hamilton":
        #keeps old plan after first time
        if "plan" not in game.data:  
            solve.simple_hamilton(game.data)
    
    
        

def generate_apple(game):
    #randomly genarates apple
    #outside of body
    

    
    free_spaces = game.data["grid"][game.data["tail"]-1:] + game.data["grid"][:game.data["head"]-1]

    #print("free spaces:", free_spaces, "body:", game.data["body"])
    if len(free_spaces) == 0:
        raise ValueError('No free Spaces')
    game.data.update({"apple":free_spaces[randint(0,len(free_spaces)-1)]})
    update_plan(game)






   
    

        
    
   
    


    
    