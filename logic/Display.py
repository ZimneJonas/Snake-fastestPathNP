import pygame, sys, time
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
fps_controller = pygame.time.Clock()
scale = 20

# FPS (frames per second) controller

class Display:
    

    def __init__(self,game):
        self.game = game
        self.check_errors = pygame.init()
        # pygame.init() example output -> (6, 0)
        # second number in tuple gives number of errors
        if self.check_errors[1] > 0:
            print(f'[!] Had {self.check_errors[1]} errors when initialising game, exiting...')
            sys.exit(-1)
        else:
            print('[+] Game successfully initialised')

        self.game_window = pygame.display.set_mode((game.data["rows"]*scale, game.data["colums"]*scale))
        pygame.display.set_caption('Snake CRUSHER')

    def get_frame(self, fps=240):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #directions          
        # GFX
        self.game_window.fill(black)
        for pos in self.game.get_body():
            # Snake body
            # .draw.rect(play_surface, color, xy-coordinate)
            # xy-coordinate -> .Rect(x, y, size_x, size_y)
            pygame.draw.rect(self.game_window, green, pygame.Rect(pos[0]*scale, pos[1]*scale, scale-1, scale-1))
        #draw order
        if self.game.data["order"]:
            order = self.game.data["order"]
            for ii in range(len(order)-1):
                pygame.draw.line(self.game_window, blue,  (order[ii][0]*scale+scale/2,order[ii][1]*scale+scale/2) , (order[ii+1][0]*scale+scale/2,order[ii+1][1]*scale+scale/2))
            pygame.draw.line(self.game_window, blue,  (order[-1][0]*scale+scale/2,order[ii][-1]*scale+scale/2) , (order[0][0]*scale+scale/2,order[0][1]*scale+scale/2))
        # Snake food
        pygame.draw.rect(self.game_window, red, pygame.Rect(self.game.data["apple"][0]*scale, self.game.data["apple"][1]*scale, scale, scale))

        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        fps_controller.tick(fps)


 



