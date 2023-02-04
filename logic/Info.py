from collections import deque
class Info: 
    data = dict()

    def __init__(self, name = "simple_hamilton",rows = 72, colums = 48 ): #72/48
        self.data.update({"name" : name })
        self.data.update({"rows" : rows })
        self.data.update({"colums" : colums })
        self.data.update({"fields" : rows*colums })

 
        #grid[2] is spot in order
        self.data.update({"grid" : [(xx,yy) for xx in range(self.data["rows"]) for yy in range(self.data["colums"])]})
        self.data.update({"order": []})
        #Head of Snake starts in middle of grid
        self.data.update({"head" : self.data["grid"].index(((self.data["rows"]//2)-1, (self.data["colums"]//2)-1))})
        self.data.update({"tail" : self.data["head"]})
        self.data.update({"planning_time":[]})
        self.data.update({"moves" : 0})
        self.data.update({"times": dict()})

    def next(self, index):
        if index == len(self.data["grid"])-1:
            return 0
        else:
            return index+1
        
    def move(self):
        self.data["moves"] += 1 
        self.data["head"] = self.next(self.data["head"])
        if self.data["head"]!=self.data["apple"]:
            self.data["tail"] = self.next(self.data["tail"])
    
    def generate_body(self):
        if self.data["head"]>=self.data["tail"]:
            if self.data["head"]==len(self.data["grid"])-1:   # [smal:]
                body = self.data["grid"][self.data["tail"]:]
            else:
                body = self.data["grid"][self.data["tail"]:self.data["head"]+1]
        else: #data["head"]<data["tail"]
            body = self.data["grid"][self.data["tail"]:] +self.data["grid"][:self.data["head"]+1]
        self.data.update({"body": body})
        return body
    

            
        





if __name__ == "__main__":
    Info=Info()
    print(Info.data)
