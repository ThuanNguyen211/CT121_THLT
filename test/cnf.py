import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
import os 
import time
import gc # Garbage collection

def read_grammar(filename):
    """
    Đọc ngữ pháp từ file
    Trả về: (grammar_dict, start_symbol, terminal_symbol)
    """
    grammar = {}
    start = None
    terminal = set()

    with open(filename, 'r') as f:
        # Đọc số lượng quy tắc và ký tự bắt đầu
        n = int(f.readline().strip())
        start = f.readline().strip()
        
        # Đọc các quy tắc ngữ pháp
        for _ in range(n):
            rule = f.readline().strip()
            left, rights = rule.split("->")
            left = left.strip()
            productions = [right.strip().split() for right in rights.split("|")]
            grammar[left] = productions
    
        for left, productions in grammar.items():
            for prod in productions:
                for symbol in prod:
                    if symbol.islower():
                        terminal.add(symbol)
    # print(grammar) # {'S': [['A'], ['A', 'b', 'A']], 'A': [['a', 'A'], ['a'], ['B']], 'B': [['b', 'B'], ['b']]}    
    terminal = sorted(terminal)
    return grammar, start, terminal

def print_grammar_to_string(grammar):
    """
    Chuyển đổi ngữ pháp thành chuỗi để hiển thị
    """
    result = []
    for left, productions in grammar.items():
        result.append(f"{left} -> " + " | ".join(" ".join(prod) for prod in productions))
    return "\n".join(result)

def eliminate_useless(grammar, start):
    """
    Loại bỏ các ký tự vô ích (không thể sinh ra chuỗi terminal)
    """
    # Tìm các ký tự có thể sinh ra chuỗi terminal
    useful = set()
    flag = True

    while flag:
        flag = False
        # Left chứa ký hiệu không kết thúc
        for left in grammar:
            productions = grammar[left]
            for prod in productions:
                # Hữu ích nếu nó đã trong tập hữu ích hoặc nếu nó nằm trong tập ký hiệu kết thúc
                if all(symbol in useful or symbol.islower() for symbol in prod):
                    if left not in useful:
                        useful.add(left)
                        flag = True

    # Loại bỏ các quy tắc không hữu ích
    new_grammar = {}
    for left, productions in grammar.items():
        if left in useful:
            new_grammar[left] = [prod for prod in productions
                               if all(symbol in useful or symbol.islower() for symbol in prod)]

    return new_grammar

def eliminate_epsilon(grammar, start):
    """
    Loại bỏ các quy tắc epsilon (ε)
    """
    # Tạo ngữ pháp mới không có ε
    new_grammar = {}
    for left, productions in grammar.items():
        new_productions = []
        for prod in productions:
            # print(prod[0])
            if prod[0] == 'epsilon': # Bỏ qua quy tắc ε
                continue
            new_productions.append(prod)
        if(len(new_productions) > 0):
            new_grammar[left] = new_productions
    return new_grammar

def eliminate_unit(grammar):
    """
    Loại bỏ các quy tắc đơn vị (A -> B)
    """
    new_grammar = {}
    for left, productions in grammar.items():
        new_productions = []
        for prod in productions:
            if len(prod) == 1 and prod[0].isupper():
                # Nếu là quy tắc đơn vị, thêm các quy tắc của ký tự bên phải
                if prod[0] in grammar:
                    new_productions.extend(grammar[prod[0]])
            else:
                new_productions.append(prod)
        new_grammar[left] = new_productions
    return new_grammar

def convert_to_cnf(grammar, terminal):
    """
    Chuyển đổi ngữ pháp sang dạng CNF (Chomsky Normal Form)
    """
    # Chuyển đổi các quy tắc có ký tự terminal
    ter = []
    for left, productions in grammar.items():
        for prod in productions:
            for i in range(len(prod)):
                if prod[i].islower():
                    position = terminal.index(prod[i])
                    prod[i] = f'S{position}'
    for i in range(len(terminal)):
        grammar[f'S{i}'] = [[terminal[i]]]
    
    new_grammar = {}
    new_symbols = 0

    def get_new_symbol(symbol):
        nonlocal new_symbols
        new_symbols += 1
        return f'{symbol}{new_symbols}'

    def get_sybol(symbol, index):
        return f'{symbol}{index}'

    new_prod = []
    # Chuyển đổi các quy tắc có độ dài lớn hơn 2
    for left, productions in grammar.items():
        new_productions = []
        for prod in productions:
            if len(prod) <= 2:
                new_productions.append(prod)
            else:
                # Chuyển đổi quy tắc dài hơn 2 thành các quy tắc có độ dài 2
                current = left
                for i in range(len(prod) - 2):
                    new_symbol = get_new_symbol('X')
                    new_prod.append([prod[i + 1], prod[i + 2]])
                    current = new_symbol
                new_productions.append([prod[-1], current])
        new_grammar[left] = new_productions
    for i in range(len(new_prod)):
        new_grammar[get_sybol('X', i+1)] = [new_prod[i]]

    return new_grammar

class GrammarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Xử Lý Ngữ Pháp")
        self.root.geometry("1000x1000")
        
        # Tạo frame chính
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Frame cho các nút
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=0, column=0, columnspan=2, pady=5)
        
        # Nút chọn file và thoát với màu sắc
        tk.Button(button_frame, text="Chọn File", command=self.load_file, bg='#4CAF50', fg='white', font=('Arial', 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Xử Lý", command=self.process_grammar,bg='#2196F3', fg='white', font=('Arial', 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Thoát", command=self.root.quit, bg='#f44336', fg='white', font=('Arial', 10)).pack(side=tk.LEFT, padx=5)
        
        # Text area cho input
        ttk.Label(main_frame, text="Input", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky=tk.W)
        self.input_text = scrolledtext.ScrolledText(main_frame, width=60, height=10)
        self.input_text.grid(row=2, column=0, columnspan=5, pady=5, sticky=(tk.W, tk.E))
        
        # Text area cho output
        ttk.Label(main_frame, text="Output", font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky=tk.W)
        for i in range(4):
            main_frame.columnconfigure(i, weight=1)
        titles = ["Loại bỏ ký tự vô ích", "Loại bỏ quy tắc epsilon", "Loại bỏ quy tắc đơn vị", "Chuyển đổi sang CNF"]
        for i, title in enumerate(titles):
            ttk.Label(main_frame, text=title, anchor="center").grid(row=4, column=i, pady=(5,0), sticky=(tk.W, tk.E)) 
        self.output_texts = []
        for i in range(4):
            output_text = scrolledtext.ScrolledText(main_frame, width=25, height=15)
            output_text.grid(row=5, column=i, pady=5, padx=5, sticky=(tk.W, tk.E, tk.N, tk.S))
            self.output_texts.append(output_text)
        
        # Frame cho bảng thời gian
        time_frame = ttk.LabelFrame(main_frame, text="Thời gian xử lý", padding="5")
        time_frame.grid(row=6, column=0, columnspan=5, pady=5, sticky=(tk.W, tk.E))
        
        # Tạo bảng thời gian
        self.time_tree = ttk.Treeview(time_frame, columns=('Step', 'Time'), show='headings', height=8)
        self.time_tree.heading('Step', text='Bước xử lý')
        self.time_tree.heading('Time', text='Thời gian (s)')
        self.time_tree.column('Step', width=300)
        self.time_tree.column('Time', width=100)
        self.time_tree.grid(row=0, column=0, sticky=(tk.W, tk.E))
            
        # Cấu hình grid
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        time_frame.columnconfigure(0, weight=1)
        
    def load_file(self):
        filename = filedialog.askopenfilename(
            title="Chọn file ngữ pháp",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            with open(filename, 'r') as f:
                self.input_text.delete(1.0, tk.END)
                self.input_text.insert(tk.END, f.read())
    
    def process_grammar(self):
        # Lấy nội dung từ text area
        content = self.input_text.get(1.0, tk.END)
        
        # Lưu vào file tạm thời
        with open('temp_grammar.txt', 'w') as f:
            f.write(content)
        
        # Xử lý ngữ pháp
        self.output_texts[0].delete(1.0, tk.END)
        self.time_tree.delete(*self.time_tree.get_children())
        total_time = 0
        
        try:
            gc.collect()
            time.sleep(0.1)  # Thêm khoảng chờ nhỏ để đảm bảo thời gian được đo chính xác
            start_time = time.perf_counter()  # Sử dụng perf_counter() thay vì time()
            grammar, start, terminal = read_grammar('temp_grammar.txt')
            read_time = time.perf_counter() - start_time
            self.time_tree.insert('', 'end', values=('Đọc ngữ pháp', f'{read_time:.4f}'))   
            
            # Loại bỏ ký tự vô ích
            gc.collect()
            time.sleep(0.1)
            start_time = time.perf_counter()
            grammar = eliminate_useless(grammar, start)
            useless_time = time.perf_counter() - start_time
            self.output_texts[0].delete(1.0, tk.END)
            self.output_texts[0].insert(tk.END, print_grammar_to_string(grammar) + "\n\n")
            self.output_texts[0].see(tk.END)
            self.time_tree.insert('', 'end', values=('Loại bỏ ký tự vô ích', f'{useless_time:.4f}'))
            total_time += useless_time
            
            # Loại bỏ quy tắc epsilon
            gc.collect()
            time.sleep(0.1)
            start_time = time.perf_counter()
            grammar = eliminate_epsilon(grammar, start)
            epsilon_time = time.perf_counter() - start_time
            self.output_texts[1].delete(1.0, tk.END)
            self.output_texts[1].insert(tk.END, print_grammar_to_string(grammar) + "\n\n")
            self.output_texts[1].see(tk.END)
            self.time_tree.insert('', 'end', values=('Loại bỏ quy tắc epsilon', f'{epsilon_time:.4f}'))
            total_time += epsilon_time
            
            # Loại bỏ quy tắc đơn vị
            gc.collect()
            time.sleep(0.1)
            start_time = time.perf_counter()
            grammar = eliminate_unit(grammar)
            unit_time = time.perf_counter() - start_time
            self.output_texts[2].delete(1.0, tk.END)
            self.output_texts[2].insert(tk.END, print_grammar_to_string(grammar) + "\n\n")
            self.output_texts[2].see(tk.END)
            self.time_tree.insert('', 'end', values=('Loại bỏ quy tắc đơn vị', f'{unit_time:.4f}'))
            total_time += unit_time
            
            # Chuyển đổi sang CNF
            gc.collect()
            time.sleep(0.1)
            start_time = time.perf_counter()
            grammar = convert_to_cnf(grammar, terminal)
            cnf_time = time.perf_counter() - start_time
            self.output_texts[3].delete(1.0, tk.END)
            self.output_texts[3].insert(tk.END, print_grammar_to_string(grammar))
            self.output_texts[3].see(tk.END)
            self.time_tree.insert('', 'end', values=('Chuyển đổi sang CNF', f'{cnf_time:.4f}'))
            total_time += cnf_time
            
            # Thêm tổng thời gian vào bảng
            self.time_tree.insert('', 'end', values=('Tổng thời gian', f'{total_time:.4f}'))
            
        except Exception as e:
            self.output_texts[0].insert(tk.END, f"Lỗi: {str(e)}")
        
        # Xóa file tạm
        if os.path.exists('temp_grammar.txt'):
            os.remove('temp_grammar.txt')

def main():
    root = tk.Tk()
    app = GrammarGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()