Prims-MST-Algorithm
-------------------

Implementations of the following algorithms:
* Prim's Minimum Spanning Tree (MST) algorithm
* a library for the heap data structure

<br>
* * *
The use of the heap data structure gives Prim's algorithm an `O(mlogn)` running time, where m is the number of edges and n is the number of vertices.

The MST algorithm expects an adjacency list. That list will be a dictionary where for a vertex v and every edge(v,w) with weight j and an assigned id eID, there is an entry in that dictionary where the key is v and the value is a list of all tuples (w,j,eID).

* * *
