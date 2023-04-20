
class Node:
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.adjacent = {}
        
        
    def get_name(self) -> str:
        """ Return the name of the node, i.e. "v1" """
        
        return self.name
    
    
    def add_adjacent(self, node, weight: int) -> None:
        """ Add a node that is adjacent to the current node. The weight of the
            path is given as a parameter, and this is added to self.adjacent dictionary
            as the value of the given adjacent node """
            
        self.adjacent[node] = weight
        
        
    def get_adjacent_node(self) -> list:
        """ Return a list of the adjacent nodes, retrieved from self.adjacent """
        
        return list(self.adjacent.keys())
    
    
    def get_adjacent_edge_weight(self) -> list:
        """ Get the edge weight for the adjacent node """
        
        return list(self.adjacent.values())
    

class Agent:
    
    def __init__(self, node: Node):
        self.position = node
        self.spanning_tree = {}
        self.add_to_spanning_tree(self.position, 0)
    
    
    def get_pos_name(self):
        """ Return the name of the node the agent is located in, i.e. "v1" """
        
        return self.position.get_name()
    
    
    def add_to_spanning_tree(self, node: Node, weight):
        """ Add the given node to the spanning tree dictionary, along with the weight of the edge """
        
        self.spanning_tree[node] = weight
        
    
    def detect_edge_weight(self):
        """ Sensor to detect the weight of the edge for adjacent node """
        
        return self.position.get_adjacent_edge_weight()
    
        
    def detect_neighboring_nodes(self):
        """ Sensor to detect neighboring nodes from where the agent is located """
        
        return self.position.get_adjacent_node()
    
    
    def get_spanningT_nodes(self) -> list:
        """ Return a list of all nodes in the spanning tree dictionary """
        
        return list(self.spanning_tree.keys())
    
    
    def get_spanning_tree_weights(self) -> list:
        """ Return a list of the edge weights for all nodes in spanning tree dictionary """
        
        return list(self.spanning_tree.values())
    
    
    def choose_best_path(self) -> list:
        """ Returns the best path (considering lowest weight) to an available node """
        
        nodes = self.detect_neighboring_nodes()
        weights = self.detect_edge_weight()
        shortest = []
        
        for i in range(len(nodes)):
            if nodes[i] not in self.get_spanningT_nodes():
                shortest = [nodes[i], weights[i]]
                break
            
        if shortest:
            for i in range(len(nodes)):
                if nodes[i] not in self.get_spanningT_nodes() and weights[i] < shortest[1]:
                    shortest = [nodes[i], weights[i]]
                
        return shortest
    
    
    def choose_best_path_from_spanningT(self):
        
        best_paths = []
        
        for i in self.get_spanningT_nodes():
            self.position = i
            temp = self.choose_best_path()
            
            if temp:
                best_paths.append(temp)
        
        if best_paths:
            shortest = [best_paths[0][0], best_paths[0][1]]
            
            for i in range(len(best_paths)):
                if best_paths[i][1] < shortest[1]:
                    shortest = [best_paths[i][0], best_paths[i][1]]
            
            self.add_to_spanning_tree(shortest[0], shortest[1])
            
            self.display()
            
            self.choose_best_path_from_spanningT()
            
    
    def display(self):
        
        nodes = self.get_spanningT_nodes()
        statement1 = ""
        
        for i in nodes:
            statement1 += str(i.get_name()) + ", "
        
        weights = self.get_spanning_tree_weights()
        
        statement2 = ""
        
        for i in weights:
            statement2 += str(i) + ", "
        
        print(f"Node objects = {statement1} edge weights = {statement2}")
        print()


def main():
        
    v1 = Node("v1")
    v2 = Node("v2")
    v3 = Node("v3")
    v4 = Node("v4")
    v5 = Node("v5")
    v6 = Node("v6")

    v1.add_adjacent(v2, 1)
    v1.add_adjacent(v4, 3)

    v2.add_adjacent(v1, 1)
    v2.add_adjacent(v3, 2)
    v2.add_adjacent(v5, 7)
    v2.add_adjacent(v6, 6)

    v3.add_adjacent(v2, 2)
    v3.add_adjacent(v6, 4)

    v4.add_adjacent(v1, 3)

    v5.add_adjacent(v2, 7)

    v6.add_adjacent(v2, 6)
    v6.add_adjacent(v3, 4)

    a = Agent(v1)

    a.choose_best_path_from_spanningT()
        

if __name__ == '__main__':
    main()
    
