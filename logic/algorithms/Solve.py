import time


    


    

        

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
    data["planning_time"].append(("simple_hamilton",end-start))

    return plan
    

    







if __name__ == "__main__":
    aPath=Path()
    print(aPath.info)