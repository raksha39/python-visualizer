from tkinter import Tk, StringVar, OptionMenu, Button, Label, Entry, Frame
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.linear_search import linear_search
from algorithms.binary_search import binary_search
from visualizer.renderer import Renderer
from utils.array_generator import generate_random_array
import random


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Sorting & Searching Algorithm Visualizer")
        self.master.geometry("700x500")

        # Algorithm type selection
        self.algorithm_type_var = StringVar(master)
        self.algorithm_type_var.set("Select Type")
        self.algorithm_type_var.trace('w', self.update_algorithm_menu)

        self.algorithm_types = ["Sorting", "Searching"]
        
        Label(master, text="Algorithm Type:", font=("Arial", 12)).pack(pady=10)
        self.type_menu = OptionMenu(master, self.algorithm_type_var, *self.algorithm_types)
        self.type_menu.pack(pady=5)

        # Algorithm selection
        self.algorithm_var = StringVar(master)
        self.algorithm_var.set("Select Algorithm")

        Label(master, text="Algorithm:", font=("Arial", 12)).pack(pady=10)
        self.algorithm_menu = OptionMenu(master, self.algorithm_var, "")
        self.algorithm_menu.pack(pady=5)

        # Search value entry (only for searching algorithms)
        self.search_frame = Frame(master)
        self.search_frame.pack(pady=10)
        
        Label(self.search_frame, text="Search Value:", font=("Arial", 10)).pack(side="left")
        self.search_entry = Entry(self.search_frame, width=10)
        self.search_entry.pack(side="left", padx=5)
        self.search_frame.pack_forget()  # Hide initially

        self.start_button = Button(master, text="Start Visualization", command=self.start_visualization)
        self.start_button.pack(pady=20)

        self.info_label = Label(master, text="", wraplength=600)
        self.info_label.pack(pady=20)

        self.sorting_algorithms = [
            "Bubble Sort",
            "Selection Sort",
            "Insertion Sort",
            "Merge Sort",
            "Quick Sort"
        ]

        self.searching_algorithms = [
            "Linear Search",
            "Binary Search"
        ]

    def update_algorithm_menu(self, *args):
        algorithm_type = self.algorithm_type_var.get()
        
        # Clear current menu
        menu = self.algorithm_menu['menu']
        menu.delete(0, 'end')
        
        if algorithm_type == "Sorting":
            algorithms = self.sorting_algorithms
            self.search_frame.pack_forget()  # Hide search entry
        elif algorithm_type == "Searching":
            algorithms = self.searching_algorithms
            self.search_frame.pack(pady=10)  # Show search entry
        else:
            algorithms = []
        
        # Add new options
        for algorithm in algorithms:
            menu.add_command(label=algorithm, command=lambda value=algorithm: self.algorithm_var.set(value))
        
        self.algorithm_var.set("Select Algorithm")

    def start_visualization(self):
        algorithm_type = self.algorithm_type_var.get()
        algorithm = self.algorithm_var.get()
        
        if algorithm_type == "Select Type":
            self.info_label.config(text="Please select an algorithm type.")
            return
            
        if algorithm == "Select Algorithm":
            self.info_label.config(text="Please select an algorithm.")
            return

        array = generate_random_array(50)  # Generate an array of 50 random integers
        
        if algorithm_type == "Sorting":
            self.run_sorting_algorithm(algorithm, array)
        elif algorithm_type == "Searching":
            self.run_searching_algorithm(algorithm, array)

    def run_sorting_algorithm(self, algorithm, array):
        if algorithm == "Bubble Sort":
            steps = bubble_sort(array.copy())
        elif algorithm == "Selection Sort":
            steps = selection_sort(array.copy())
        elif algorithm == "Insertion Sort":
            steps = insertion_sort(array.copy())
        elif algorithm == "Merge Sort":
            steps = merge_sort(array.copy())
        elif algorithm == "Quick Sort":
            steps = quick_sort(array.copy())

        # Create renderer for sorting
        renderer = Renderer(array, width=800, height=600, mode="sorting")
        renderer.visualize(steps)

    def run_searching_algorithm(self, algorithm, array):
        # Get search target
        try:
            target = int(self.search_entry.get())
        except ValueError:
            # If no target specified, use a random value from the array
            target = random.choice(array)
            self.search_entry.delete(0, 'end')
            self.search_entry.insert(0, str(target))

        if algorithm == "Linear Search":
            steps = linear_search(array.copy(), target)
        elif algorithm == "Binary Search":
            steps = binary_search(array.copy(), target)

        # Create renderer for searching
        renderer = Renderer(array, width=800, height=600, mode="searching")
        renderer.visualize_search(steps)

def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()