# Board Class
import uuid

class B_Node:
    def __init__(self, name, onLandAbility = None, onCollectAbility = None, moveOptions = []): 
        self._name = name
        self._moveOptions = moveOptions #List of other B_Nodes
        self._onLandAbility = onLandAbility
        self._onCollectAbility = onCollectAbility
        self._id = uuid.uuid4().int
    
        
class Board:
    def __init__(self, NodeGrid = []):
        self.NodeGrid = NodeGrid #Collection of B_Nodes
        
