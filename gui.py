import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from src import *
from tkinter.scrolledtext import ScrolledText


class LegitCheckApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Legit Check")
        self.geometry("700x300")
        self.selected_txt_file = ""
        self.selected_file = ""
        self.name_list = []
        self.phone_list = []

        # Ramka dla wszystkich elementów oprócz obszaru wyświetlania informacji
        main_frame = tk.Frame(self)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Lewa część interfejsu użytkownika
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.select_file_button = tk.Button(left_frame, text="Select TXT File", command=self.select_txt_file)
        self.select_file_button.pack(pady=10)

        self.info_label = tk.Label(left_frame, text="")
        self.info_label.pack(pady=5)

        self.search_options = ttk.Combobox(left_frame,
                                           values=["Phone Number", "Name and Surname", "JSON File", "VCF File"])
        self.search_options.pack(pady=5)
        self.search_options.bind("<<ComboboxSelected>>", self.on_search_option_selected)

        self.entry_label = tk.Label(left_frame, text="")
        self.entry_label.pack(pady=5)

        self.entry_box = tk.Entry(left_frame)
        self.entry_box.pack(pady=5)

        self.submit_button = tk.Button(left_frame, text="Submit", command=self.submit)
        self.submit_button.pack(pady=5)

        # Prawa część interfejsu użytkownika - obszar wyświetlania informacji
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.file_info_label = tk.Label(right_frame, text="File Information:")
        self.file_info_label.pack()

        self.file_info_text = ScrolledText(right_frame, width=30, height=10)
        self.file_info_text.pack()

    def select_txt_file(self):
        self.selected_txt_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        self.info_label.config(text=f"Selected TXT File: {self.selected_txt_file}")

    def on_search_option_selected(self, event):
        selection = self.search_options.get()
        if selection == "JSON File":
            self.selected_file = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
            self.entry_label.config(text="Enter cities (comma-separated) or leave empty:")
            self.display_json_info()
        elif selection == "VCF File":
            self.selected_file = filedialog.askopenfilename(filetypes=[("VCF files", "*.vcf")])
            self.entry_label.config(text="Leave empty")
            self.display_vcf_info()
        else:
            self.entry_label.config(
                text=f"Enter {'Phone Number' if selection == 'Phone Number' else 'Name and Surname'}:")
            self.file_info_text.delete(1.0, tk.END)

    def display_json_info(self):
        if self.selected_file:
            json_info = read_data_from_json_file(self.selected_file)
            self.file_info_text.delete(1.0, tk.END)
            self.file_info_text.insert(tk.END, json_info)
            self.adjust_results_width()

    def display_vcf_info(self):
        if self.selected_file:
            vcf_info = read_data_from_vcf_file(self.selected_file)
            self.file_info_text.delete(1.0, tk.END)
            self.file_info_text.insert(tk.END, vcf_info)
            self.adjust_results_width()

    def adjust_results_width(self):
        max_line_length = max(len(line) for line in self.file_info_text.get("1.0", "end").split("\n"))
        self.file_info_text.configure(width=max_line_length)

    def submit(self):
        search_option = self.search_options.get()
        cities_entry = self.entry_box.get().strip()
        if not self.selected_txt_file:
            messagebox.showerror("Error", "Please select a TXT file.")
            return
        if search_option == "Phone Number":
            result = find_user_by_phone_number(self.selected_txt_file, self.entry_box.get())
        elif search_option == "Name and Surname":
            result = find_user_by_name_and_surname(self.selected_txt_file, self.entry_box.get())
        elif search_option == "JSON File":
            self.name_list = read_data_from_json_file(self.selected_file)
            if not self.name_list:
                messagebox.showerror("Error", "No friends found in the JSON file.")
                return
            if cities_entry:
                cities = [city.strip() for city in cities_entry.split(",")]
                result = find_friends_json(self.selected_txt_file, self.name_list, cities)
            else:
                result = find_friends_json(self.selected_txt_file, self.name_list)
        elif search_option == "VCF File":
            self.phone_list = read_data_from_vcf_file(self.selected_file)
            if not self.phone_list:
                messagebox.showerror("Error", "No friends found in the VCF file.")
                return
            result = find_friends_vcf(self.selected_txt_file, self.phone_list)
        else:
            messagebox.showerror("Error", "Invalid search option.")
            return

        self.display_results(result)

    def display_results(self, result):
        if not result:
            messagebox.showinfo("Result", "No matching records found.")
            return

        result_window = tk.Toplevel(self)
        result_window.title("Search Result")

        result_text = ScrolledText(result_window, width=50, height=10)
        for line in result:
            result_text.insert(tk.END, line + "\n")
        result_text.pack(expand=True, fill=tk.BOTH)
        result_text.update_idletasks()

        max_line_length = max(len(line) for line in result_text.get("1.0", "end").split("\n"))
        result_text.configure(width=max_line_length)


if __name__ == "__main__":
    app = LegitCheckApp()
    app.mainloop()
