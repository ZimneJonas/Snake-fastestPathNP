import time

def translate_dir(field, dir):
    if dir=="up":
        field =(field[0]-1,field[1]) 
    elif dir=="down":
        field =(field[0]+1,field[1]) 
    elif dir=="left":
        field =(field[0],field[1]-1)
    elif dir=="right":
        field =(field[0],field[1]+1)
    else:
        raise Exception('Wrong direction')
    return field
    

def grid_fix_order(game):
    #if plan gives dirs this translates to a grid order
    
    #take old body as start for new order
    new_grid = game.get_body()



    next = game.data["grid"][game.data["tail"]]
    #while the first field isn't reached
    while new_grid[0] != next:
    
        game.data["grid"][1]
        new_grid.append(new)

    print(new_grid)
    

        

def simple_hamilton(game):
    start = time.time()
    if game.data["colums"]%2:
        raise ValueError('uneven colums not yet accepted')
    if game.data["rows"]<1 or game.data["colums"]<1:
        raise ValueError('too smal')
   
    game.data.update({"plan" : dict(())})
    for xx in range(game.data["colums"]):
        for yy in range(game.data["rows"]):
            field = (xx,yy)
            if yy == 0 and xx!=0 :
                game.data["plan"].update({field:"up"})
            elif not xx%2: #even
                if yy+1 == game.data["colums"]:
                    game.data["plan"].update({field:"down"})
                else:
                    game.data["plan"].update({field:"right"})
                #every second row goes left
            else: #uneven
                if yy == 1 and xx != game.data["rows"]-1:
                    game.data["plan"].update({field:"down"})
                else:
                    game.data["plan"].update({field:"left"}) 
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
    grid_fix_order(game)
    game.data["planning_time"].append(("simple_hamilton",end-start))
    

    







if __name__ == "__main__":
    aPath=Path()
    print(aPath.info)