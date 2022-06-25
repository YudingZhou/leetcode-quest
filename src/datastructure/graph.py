from typing import TypeVar, Generic



T = TypeVar("T")


class IUndirectedGraph:
    '''
    An undirected graph.
    '''
    def __init__(self):
        '''
        A new graph never has any nodes or edges.
        '''
        pass


    def add_node(self, name):
        '''
        Create a new node and add it to the graph. Name must be a hashable type.
        return value indicates if a node was actually added, True means a new
        node was created and added, False means that a node with that name already
        exists in this graph, and it was not overwritten.
        '''
        pass


    def add_edge(self, a_name, b_name, weight = 1):
        '''
        Create an edge between a and b with the provided weight.
        If either of the names is not already a member of the graph, create
        that node and add it to the graph first.
        '''
        pass


    def neighbors(self, from_name):
        '''
        Return an iterator that yields (name, weight) of all the neighboring nodes.
        '''
        pass


    def contains(self, name):
        '''
        Return true if the name already maps to a node, false otherwise
        '''
        pass


    def nodes(self):
        '''
        Return an iterator that yields the node names (in no particular order)
        '''
        pass


    def edges(self):
        '''
        Return all the edges as an iterator of Edges (named tuples) with values
        (from_name, to_name, weight). Edges are yielded in no particular order.
        '''
        pass


'''
https://medium.com/tebs-lab/implementations-of-graphs-92eb7f121793
'''

class UndirectedGraph(IUndirectedGraph):

	class Edge:

		def __init__(self, a_name, b_name, weight = 1):
			self.a_name = a_name
			self.b_name = b_name
			self.weight = weight

		def equals(self, other: Edge) -> bool:
			return (self.a_name == other.a_name || self.a_name == other.b_name) && self.weight == other.weight
	 '''
    An undirected graph.
    '''
    def __init__(self):
        self.vertices = []
        self.edges = []


    def add_node(self, name):  # O(n)
    	if self.vertices.__contains__(name):  # O (n)
    		return False
    	else:
			self.vertices.append(name) # O(1)
    		return True

    def add_edge(self, a_name, b_name, weight = 1):  #O(N)
    	new_edge = Edge(a_name, b_name, weight)
        self.add_node(a_name)  #O(N)
        self.add_node(b_name)  #O(N)
        for edge in self.edges():   #O(N)
        	if edge.equals(new_edge):  
        		return
       	self.edges.append(new_edge) #O(1)
        



    def neighbors(self, from_name): # N
        for edge in self.edges():  
        	if from_name == edge.a_name or from_name == edge.b_name:
        		yield edge

    def get_edges(self, a_name, b_name): #N
    	for edge in self.edges():
    		if (a_name == edge.a_name and b_name == edge.b_name) or (a_name == edge.b_name and b_name == edge.a_name):
    			yield edge


    def contains(self, name): #N
        return self.vertices.__contains__(name)


    def nodes(self): #1
        [yield vertex for vertex in self.vertices]


    def edges(self):#1
        [yield edge for edge in self.edges]


class UndirectedGraph:

	def __init__(self):
		self.adjacent_map = {} #{ name : { name : weight } }


    def add_node(self, name):  # O(1)
    	if !self.adjacent_map.__contains__(name):
    		self.adjacent_map[name] = {}

    def add_edge(self, a_name, b_name, weight = 1):  #O(1)
    	self.add_node(a_name)
    	self.add_node(b_name)
    	self.adjacent_map[a_name][b_name] = 1
    	self.adjacent_map[b_name][a_name] = 1
        

    def neighbors(self, from_name): #o(1)
    	for vertix in self.adjacent_map[from_name]
    		yield vertix 


    def contains(self, name): #N
        return self.adjacent_map.__contains__(name)


    def nodes(self): #1
    	for vertix in self.adjacent_map:
    		yield vertix


    def edges(self): # o(n) * o(n) *o(x) = o(n2)*o(x) = o(x* n2)
    	# easiest way is to convert this to an adjacent matrix for removing duplicated edges
    	edge_matrix = int[self.adjacent_map.__len__()][self.adjacent_map.__len__()]
    	vertix_index = {}
    	edges = []
    	for idx, vertix in enumerate(self.adjacent_map) : #o(n)
    		vertix_index{idx, vertix}

    	for row in vertix_index.__len__():  #o(n)
    		for col in range(row + 1, vertix_index.__len__()): #o(n) - o(1)
    			vertix = vertix_index(col)
    			for other_vertix in self.adjacent_map[vertix]  # o(x)
    				weight = self.adjacent_map[other_vertix]
    				edges.append((vertix, other_vertix, weight))






