import pickle 
import LogicSnake
import matplotlib.pyplot as plt
import numpy as np

def save(data):
    with open("data/"+data["name"]+str(data["rows"])+"|"+str(data["rows"])+'.pkl', 'wb') as f:
        pickle.dump(data, f)

def open_file():
    #TODO how to open?        
    with open('saved_dictionary.pkl', 'rb') as f:
        return pickle.load(f)
    
def run_logik_snake():
    #for xx in range(10,71,20) for yy in range(10,51,10)
    
    size=[]
    moves=[]
    times=[]
    shortcuts =[]
    total = []
    moveTime=[]
    skipPercent = []
    for short in range(0,11):
        for ii in range(2,12):
        
            try: 
                game = LogicSnake.SnakeGame(4,ii,short*10)
            except:
                print("failed:",(4,ii))
                continue
            size.append(len(game.data["grid"]))
            moves.append(game.data["moves"])
            print(game.data["times"])
            times.append(game.data["times"]["planning_time"][0][1])
            total.append(game.data["times"]["total"])
            moveTime.append(game.data["times"]["total"]/game.data["moves"])
            shortcuts.append(game.data["times"]["shortcuts"])
            skipPercent.append(game.data["skipPercent"])
            #str(game.data["times"])+"Moves"+ +"Total time"+"\n"
    print("Sizes:", size)
    print("Moves:", moves)
    #print("Solving Time", times )
    #print("Total Time", total)
    #print(moveTime)
    print(skipPercent)
    TITLE= "Shortcuting random Hamilton"
    plt.figure(1)
    plt.ylabel("moves")
    col = iter(plt.cm.rainbow(np.linspace(0, 1, 10)))
    for s, col in zip(range(0,11), col):
        plt.plot(size[s*10:s*10+10],moves[s*10:s*10+10], color= col, label=str(s*10)+"%")
    plt.legend()
    plt.title(TITLE+" Steps")
    plt.xlabel("size")
    
    plt.savefig("logic/data/short_random_moves.png")

    plt.figure(2)
    plt.plot(size,times,"ro", color= "blue",label="Planning")
    plt.plot(size,shortcuts,"ro", color= "yellow",label="shortcuts")
    plt.legend()
    plt.title(TITLE)
    plt.xlabel("size")
    #plt.xlabel("Skipping in %")
    plt.ylabel("times")
    plt.savefig("logic/data/short_random_times.png")
    plt.plot(size,total,"ro", color= "red", label="Total")
    plt.legend()
    plt.savefig("logic/data/short_random_times_overhead.png")
    plt.yscale('log')
    plt.savefig("logic/data/short_random_log_times_overhead.png")

    plt.figure(3)
    plt.plot(size,moveTime,"ro", color= "blue",label="single move time")
    plt.xlabel("size")
    plt.ylabel("time/move")
    plt.savefig("logic/data/short_random_moveTimes.png")
    plt.yscale('log')
    plt.savefig("logic/data/short_random_log_moveTimes.png")



if __name__ == "__main__":           
    pass