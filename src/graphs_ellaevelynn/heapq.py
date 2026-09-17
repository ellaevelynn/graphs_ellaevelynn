import heapq as _heapq

class MinHeap:
    def __init__(self):
        self._heap = []

    def push(self, item):
        _heapq.heappush(self._heap, item)

    def pop(self):
        return _heapq.heappop(self._heap)

    def is_empty(self):
        return len(self._heap) == 0