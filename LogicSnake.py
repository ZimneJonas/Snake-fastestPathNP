from logic.Info import Info 
import time

#Show Game while solving
VISUALS = True

#SOLVER = "simple_hamilton"
#SOLVER = "shortcuting_simple_hamilton"
#SOLVER = "random_hamilton"
SOLVER = "shortcuting_random_hamilton"

if VISUALS:
    from logic.Display import Display
    FPS = 30


class SnakeGame(Info):

   
    def __init__(self, rows=6, colums=8, skipPercent = 100): 
        start = time.time()
        super().__init__(SOLVER, rows, colums,skipPercent)  
        if VISUALS:
            ui = Display(self)
                
        self.generate_apple()
        while self.move():
            if VISUALS:
                #TODO run Visuals after - Data efficent possible?
                ui.get_frame(FPS)
        
        if not VISUALS:
            #save data
            pass
        end = time.time()
        self.data["times"].update({"total":end-start})
                
if __name__ == "__main__":
    start = time.time()
    game = SnakeGame()
    end = time.time()
    #game.data.update({"total_time":end-start})
    print(game.data["times"],"Moves", game.data["moves"],"Total time",end-start)
   
    
