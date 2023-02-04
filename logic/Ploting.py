import pickle 

def save(data):
    with open("data/"+data["name"]+str(data["rows"])+"|"+str(data["rows"])+'.pkl', 'wb') as f:
        pickle.dump(data, f)

def open():
    #TODO how to open?        
    with open('saved_dictionary.pkl', 'rb') as f:
        return pickle.load(f)