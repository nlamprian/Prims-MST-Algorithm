''' Prim's MST Algorithm (Finding minimum spanning tree on an undirected graph)
    Input:  adjList - a dictionary with vertices as keys,
                      and edges as values in the form of list of neighboring vertices,
                      with the corresponding edge weights and edge ids
    Output: mst - a set of all the edges that constitute the minimum spanning tree '''

import sys
from heap import Heap


def primsMSTAlgorithm(adjList):
	def updateHeap(v):
		for vertex,weight,edgeID in adjList[v]: # for every neighboring vertex 'vertex' to the vertex v
			if vertex not in explored: # if 'vertex' is unexplored
				element = unexplored.delete(vertex) # remove the entry from the heap corresponding to vertex 'vertex'
				if element and element[0] < weight: unexplored.insert(element) # if the new edge weight is worse than the one recorded earlier (if that happened)...
				else: unexplored.insert((weight,vertex,edgeID)) # reinsert the entry to the heap as is, else update the entry first and then reinsert

	# unexplored is a heap data structure that holds vertices that haven't already been explored, and
	# its element have the following format (minWeight, destinationVertex, edgeID)
	# explored contains all the vertices that have been explored
	# mst contains the edges that eventually will form the minimum spanning tree
	unexplored, explored, mst = Heap(), set([1]), set()
	updateHeap(1) # Use vertex 1 as source

	while unexplored.length(): # as long as there are unexplored vertices, explore them
		weight,vertex,edgeID = unexplored.extractMin() # get the next edge with the minimum weight
		explored.add(vertex) # add the destination vertex to the list of already explored vertices
		mst.add(edgeID) # add the edge to the set of edges that will constitute the mst
		updateHeap(vertex) # udpate the entries on the heap of all vertices that are neighboring to the one I just explored
	
	return mst


def graph(filename):
	# the file is assumed to specify the edges of the graph in the following format: v w e
	# where v is one vertex of the associated edge, w is the other vertex, and e is the edge's weight
	# the first line of the file specifies the number on the vertices and the number of the edges
	
	# Use of 2 graph representations
	# First: adjList[vertex1] = [(vertex21,weight1,edgeId1), (vertex22,weight2,edgeId2), ...]
	# Second: edgeList[edgeId] = (vertex1,vertex2,weight)
	adjList, edgeList = {}, {}

	with open(filename, 'r') as f:
		nums = f.readline().split()
		numVertices, numEdges = int(nums[0]), int(nums[1])
		edgeID = 1
		for line in f:
			edge = line.split()
			v1, v2, weight = int(edge[0]), int(edge[1]), int(edge[2])
			if v1 in adjList: adjList[v1].append((v2,weight,edgeID))
			else: adjList[v1] = [(v2,weight,edgeID)]
			if v2 in adjList: adjList[v2].append((v1,weight,edgeID))
			else: adjList[v2] = [(v1,weight,edgeID)]
			edgeList[edgeID] = (v1,v2,weight)
			edgeID += 1

	return adjList, edgeList


if __name__ == "__main__":
	if len(sys.argv) < 2: sys.exit("Error: No input filename.")
	filename = sys.argv[1]
	adjList, edgeList = graph(filename) # build an adjancency list and an incidence list

	# the algorithm returns edgeIDs that we can make use on the incidence list
	mst = primsMSTAlgorithm(adjList) # execute prim's algorithm

	cost = 0
	for edgeID in mst: # compute the sum of the weights of all edges in the MST
		cost += edgeList[edgeID][2]

	print(cost)
