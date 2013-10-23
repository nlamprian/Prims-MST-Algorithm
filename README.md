Prims-MST-Algorithm
-------------------

Implementations of the following algorithms:
* Prim's Minimum Spanning Tree (MST) algorithm
* a library for the heap data structure

<br>
* * *
The use of the heap data structure gives Prim's algorithm an `O(mlogn)` running time, where m is the number of edges and n is the number of vertices.

The MST algorithm expects an adjacency list. That list should be a dictionary where for every vertex v and every edge(v,w) with weight j and an assigned identifier eID, there is an entry such that v is the key is v and its value is a list of all tuples (w,j,eID). The algorithm returns a set containing the edge ids of all the dges in the MST.

* * *
<br>
The code was tested on `Python 3.3.2`.
