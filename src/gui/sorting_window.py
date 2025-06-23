from tkinter import Toplevel, Canvas, Button, Frame, Label
import random
import time

class SortingWindow:
    def __init__(self, master, algorithm):
        self.master = master
        self.algorithm = algorithm
        self.window = Toplevel(master)
        self.window.title(f"{algorithm} Visualization")
        self.canvas = Canvas(self.window, width=800, height=600, bg='white')
        self.canvas.pack()

        self.array = self.generate_array(100)
        self.draw_array(self.array)

        self.start_button = Button(self.window, text="Start Sorting", command=self.start_sorting)
        self.start_button.pack()

        self.info_label = Label(self.window, text="")
        self.info_label.pack()

    def generate_array(self, size):
        return [random.randint(1, 100) for _ in range(size)]

    def draw_array(self, array):
        self.canvas.delete("all")
        bar_width = 800 / len(array)
        for i, value in enumerate(array):
            x0 = i * bar_width
            y0 = 600 - (value * 5)
            x1 = (i + 1) * bar_width
            y1 = 600
            self.canvas.create_rectangle(x0, y0, x1, y1, fill='blue')

    def start_sorting(self):
        if self.algorithm == "Bubble Sort":
            self.bubble_sort(self.array)
        elif self.algorithm == "Selection Sort":
            self.selection_sort(self.array)
        elif self.algorithm == "Insertion Sort":
            self.insertion_sort(self.array)
        elif self.algorithm == "Merge Sort":
            self.merge_sort(self.array)
        elif self.algorithm == "Quick Sort":
            self.quick_sort(self.array)

    def bubble_sort(self, array):
        n = len(array)
        for i in range(n):
            for j in range(0, n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    self.draw_array(array)
                    self.window.update()
                    time.sleep(0.01)

    def selection_sort(self, array):
        n = len(array)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if array[j] < array[min_idx]:
                    min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]
            self.draw_array(array)
            self.window.update()
            time.sleep(0.01)

    def insertion_sort(self, array):
        n = len(array)
        for i in range(1, n):
            key = array[i]
            j = i-1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
            self.draw_array(array)
            self.window.update()
            time.sleep(0.01)

    def merge_sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            L = array[:mid]
            R = array[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                k += 1
                self.draw_array(array)
                self.window.update()
                time.sleep(0.01)

            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1
                self.draw_array(array)
                self.window.update()
                time.sleep(0.01)

            while j < len(R):
                array[k] = R[j]
                j += 1
                k += 1
                self.draw_array(array)
                self.window.update()
                time.sleep(0.01)

    def quick_sort(self, array):
        self._quick_sort(array, 0, len(array) - 1)

    def _quick_sort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self._quick_sort(array, low, pi - 1)
            self._quick_sort(array, pi + 1, high)

    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                self.draw_array(array)
                self.window.update()
                time.sleep(0.01)
        array[i + 1], array[high] = array[high], array[i + 1]
        self.draw_array(array)
        self.window.update()
        time.sleep(0.01)
        return i + 1