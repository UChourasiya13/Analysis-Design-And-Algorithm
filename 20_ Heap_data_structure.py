# Define the heap data structure class
class Heap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i //= 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval


# Define the function to sort a list of integers using the heap data structure
def heap_sort(lst):
    h = Heap()
    for i in lst:
        h.insert(i)
    sorted_lst = []
    while h.current_size > 0:
        sorted_lst.append(h.del_min())
    return sorted_lst


# Example usage
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Unsorted list:", lst)
sorted_lst = heap_sort(lst)
print("Sorted list:", sorted_lst)
