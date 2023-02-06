from logic.Info import Info 
import logic.Ploting as plt
import time

#Show Game while solving
VISUALS=False
SOLVER="simple_hamilton"

if VISUALS:
    from logic.Display import Display
    FPS = 60


class SnakeGame(Info):

   
    def __init__(self): 
           
        if VISUALS:
            #Make smaler for faster results
            super().__init__(SOLVER,20,10)
            ui = Display(self)
        else:
            super().__init__(SOLVER, 72, 48)
                
        self.generate_apple()
        while self.move():
            if VISUALS:
                #TODO run Visuals after - Data efficent possible?
                ui.get_frame(FPS)
        
        if not VISUALS:
            #save data
            pass
            
                
if __name__ == "__main__":
    start = time.time()
    game = SnakeGame()
    end = time.time()
    #game.data.update({"total_time":end-start})
    print(game.data["planning_time"],"Moves", game.data["moves"],"Total time",end-start)
   
    
