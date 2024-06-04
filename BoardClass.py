# Board Class

class B_Node:
    def __init__(self, name, onLandAbility = None, onCollectAbility = None, moveOptions = []): #List of other B_Nodes
        self.name = name
        self.moveOptions = moveOptions
        self.onLandAbility = onLandAbility
        self.onCollectAbility = onCollectAbility
        

        
class Board:
    def __init__(self, NodeGrid = []):
        self.NodeGrid = NodeGrid #Collection of B_Nodes
        
