from logic.Info import Info 
import logic.Ploting as plt

import logic.Run as run
import time

#Show Game while solving
VISUALS=True
SOLVER="simple_hamilton"

if VISUALS:
    from logic.Display import Display
    FPS = 60


class SnakeGame(Info):

   
    def __init__(self): 
        start = time.time()   
        if VISUALS:
            #Make smaler for faster results
            super().__init__(SOLVER,20,10)
            ui = Display(self)
        else:
            super().__init__(SOLVER, 72, 48)
                
        run.generate_apple(self.data)
        while True:
            #snake moves
            self.move()
            # check if snake eats
            if self.data["head"]==self.data["apple"]: 
                #print("Progress:",len(self.data["body"]),"/",len(self.data["grid"]))
                try:
                    run.generate_apple(self)
                    
                except:
                    print("Game WON")
                    break
            
            if VISUALS:
                #TODO run Visuals after
                ui.get_frame(FPS)
        
        if not VISUALS:
            #save data
            end = time.time()
            
                

        





if __name__ == "__main__":
    
    game = SnakeGame()
    
    #game.data.update({"total_time":end-start})
    print(game.data["planning_time"],"Moves", game.data["moves"],"Total time",end-start)
   
    
