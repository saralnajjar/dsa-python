# dsa-python

Data structures and algorithms implemented from scratch in Python, with complexity analysis and explanations throughout.

Built alongside my CS degree at Leeds to sharpen interview prep and deepen understanding of the fundamentals.

---

## Structure

```
dsa-python/
├── data-structures/
│   ├── linked-list/
│   ├── stack/
│   ├── queue/
│   ├── binary-search-tree/
│   └── hash-map/
├── algorithms/
│   ├── sorting/
│   ├── searching/
│   └── graph/
└── leetcode/
```

---

## Data Structures

| Structure | File | Key operations |
|---|---|---|
| Linked List | [linked_list.py](data-structures/linked-list/linked_list.py) | prepend O(1), append O(n), delete O(n) |
| Stack | [stack.py](data-structures/stack/stack.py) | push/pop/peek O(1) |
| Queue | [queue.py](data-structures/queue/queue.py) | enqueue/dequeue O(1) |
| Binary Search Tree | [bst.py](data-structures/binary-search-tree/bst.py) | insert/search/delete O(log n) avg |
| Hash Map | [hash_map.py](data-structures/hash-map/hash_map.py) | get/set/delete O(1) avg |

---

## Algorithms

| Algorithm | File | Time | Space |
|---|---|---|---|
| Bubble Sort | [bubble_sort.py](algorithms/sorting/bubble_sort.py) | O(n²) | O(1) |
| Merge Sort | [merge_sort.py](algorithms/sorting/merge_sort.py) | O(n log n) | O(n) |
| Quick Sort | [quick_sort.py](algorithms/sorting/quick_sort.py) | O(n log n) avg | O(log n) |
| Linear Search | [linear_search.py](algorithms/searching/linear_search.py) | O(n) | O(1) |
| Binary Search | [binary_search.py](algorithms/searching/binary_search.py) | O(log n) | O(1) |
| BFS | [bfs.py](algorithms/graph/bfs.py) | O(V+E) | O(V) |
| DFS | [dfs.py](algorithms/graph/dfs.py) | O(V+E) | O(V) |


---

## Big O Cheat Sheet

| | Average | Worst |
|---|---|---|
| **Array access** | O(1) | O(1) |
| **Linked list search** | O(n) | O(n) |
| **BST search** | O(log n) | O(n) |
| **Hash map get** | O(1) | O(n) |
| **Binary search** | O(log n) | O(log n) |
| **Merge sort** | O(n log n) | O(n log n) |
| **Quick sort** | O(n log n) | O(n²) |
| **BFS / DFS** | O(V+E) | O(V+E) |

---

## Running any file

```bash
python3 data-structures/linked-list/linked_list.py
python3 algorithms/sorting/sorting.py
# etc.
```

No dependencies — standard library only.