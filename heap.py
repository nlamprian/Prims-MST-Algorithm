''' Implementation of a binary min heap Class
    Assumption: Input elements are tuples (x,y) or lists [x,y]
                where their first element is a key (score)
                      their second element is an identifier (id)
                  and after those two, anything can follow '''

class Heap:

	def __init__(self, element = None, batch = None):
		# element - an element to be inserted into the heap
		# batch - a list of elements to be inserted into the heap
		self.h = [] # the heap
		self.hIdx = {} # a dictionary to keep the indices of the elements in the list (heap)
		if element: self.insert(element)
		if batch: self.heapify(batch)

	def length(self):
		return len(self.h) # return the number of elements in the heap

	def insert(self, element): # insert an element in the list (heap)
		self.h[self.length():] = [element] # place the element at the end of the list (heap)
		self.hIdx[element[1]] = self.length() - 1 # update the dictionary with the element's index in the list (heap)
		self.__siftUp() # enforce the heap property

	def __siftUp(self):
		childIdx = self.length() - 1
		parentIdx = int((childIdx-1)/2)
		while self.h[childIdx][0] < self.h[parentIdx][0]:
			# if the child's key is less than the parent's key
			# swap the elements and update the dictionary with the new indices
			parent, child = self.h[parentIdx], self.h[childIdx]
			self.h[parentIdx], self.hIdx[child[1]] = child, parentIdx
			self.h[childIdx], self.hIdx[parent[1]] = parent, childIdx
			parentIdx, childIdx = int((parentIdx-1)/2), parentIdx

	def heapify(self, batch):
		# heapify builds the heap in linear time
		# batch - list of elements (key,identifier) to be inserted into the heap
		self.h, self.hIdx = [], {}
		for idx,element in enumerate(batch): # populate the heap
			self.h.append(element)
			self.hIdx[element[1]] = idx
		for i in range(int(self.length()/2)-1,-1,-1): # enforce the heap property on every element
			self.__minHeapify(i)

	def __minHeapify(self, parentIdx):
		leftChildIdx, rightChildIdx = parentIdx*2+1, parentIdx*2+2
		lowest = leftChildIdx if leftChildIdx < self.length() and self.h[leftChildIdx] < self.h[parentIdx] else parentIdx
		if rightChildIdx < self.length() and self.h[rightChildIdx] < self.h[lowest]: lowest = rightChildIdx
		if lowest != parentIdx: # if the heap property is violated, fix it and recurse
			parent, child = self.h[parentIdx], self.h[lowest]
			self.h[parentIdx], self.hIdx[child[1]] = child, parentIdx
			self.h[lowest], self.hIdx[parent[1]] = parent, lowest
			self.__minHeapify(lowest)

	def extractMin(self):
		minE = self.h[0] # get the minimum element from the top of the heap
		del self.hIdx[minE[1]] # remove the corresponding entry of the element from the dictionary
		lastNode = self.h.pop() # extract the last element of the list (heap)
		if self.length():
			self.h[0] = lastNode # replace the gap on the top with the last element
			self.hIdx[lastNode[1]] = 0 # update its position on the dictionary
			self.__siftDown(0) # enforce the heap property, starting from the root
		return minE

	def __siftDown(self, parentIdx):
		if parentIdx*2+1 >= self.length(): return # if the "parent" doesn't have children, we are good to go!
		if parentIdx*2+2 >= self.length(): # if the parent has one child...
			# and its key is less than the parent's key, swap them
			if self.h[parentIdx][0] > self.h[parentIdx*2+1][0]:
				parent, child = self.h[parentIdx], self.h[parentIdx*2+1]
				self.h[parentIdx], self.hIdx[child[1]] = child, parentIdx
				self.h[parentIdx*2+1], self.hIdx[parent[1]] = parent, parentIdx*2+1
			return

		parent = self.h[parentIdx]
		leftChild, rightChild = self.h[parentIdx*2+1], self.h[parentIdx*2+2]
		minLeft = False
		if leftChild[0] <= rightChild[0]: minLeft = True
		if parent[0] > min(leftChild[0], rightChild[0]):
			self.h[parentIdx] = leftChild if minLeft else rightChild
			self.hIdx[leftChild[1] if minLeft else rightChild[1]] = parentIdx
			self.h[parentIdx*2+1 if minLeft else parentIdx*2+2] = parent
			self.hIdx[parent[1]] = parentIdx*2+1 if minLeft else parentIdx*2+2
			self.__siftDown(parentIdx*2+1+(not minLeft))

	def get(self, id):
		# return an element from the list (heap), else None
		return self.h[self.hIdx[id]] if id in self.hIdx else None

	def delete(self, id):
		if id not in self.hIdx: return None
		idx = self.hIdx[id] # get the element's position in the list (heap)
		del self.hIdx[id] # delete that element's entry from the dictionary
		node = self.h[idx] # backup the element of interest
		lastNode = self.h.pop() # extract the last element from the list (heap)...
		if idx != self.length():
			self.h[idx] = lastNode # ... place it in the "gap" from the element to be removed
			self.hIdx[lastNode[1]] = idx # ... and update its position 
			self.__siftDown(idx) # enforce the heap property, starting from the deleted element
		return node


if __name__ == "__main__":
	l = [[9,'a'],[7,'c'],[5,'d'],[4,'h'],[3,'f'],[2,'x'],[1,'r'],[6,'t'],[3,'u'],[7,'v'],[2,'w'],[6,'l'],[4,'o']]
	heap = Heap(batch=l)
	print(heap.h)
	heap.extractMin()
	print(heap.h)
