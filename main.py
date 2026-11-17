import tkinter as tk
from tkinter import messagebox

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.x = 0
        self.y = 0

class BSTApp:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("Fase4StefaniaRedondo — BST Explorer")
        self.root.geometry("1100x750")
        self.root.config(bg="#0b132b")
        
        # Datos del estudiante
        self.app_name = "Fase4StefaniaRedondo"
        self.student_name = "Stefania Redondo Jimenez"
        self.course_info = "Data Structures - 301305"
        self.date_info = "November, 2026"
        
        self.bst_root = None
        self.node_count = 0
        self.max_height = 0
        
        self.create_login_window()

    def create_login_window(self):
        self.login_frame = tk.Frame(self.root, bg="#0b132b")
        self.login_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(self.login_frame, text="🌳 BST Explorer", font=("Arial", 26, "bold"), fg="#48cae4", bg="#0b132b").pack(pady=20)
        tk.Label(self.login_frame, text="Binary Search Tree — Phase 4", font=("Arial", 14), fg="#ade8f4", bg="#0b132b").pack(pady=5)
        
        info_frame = tk.Frame(self.login_frame, bg="#1c2541", bd=2, relief=tk.GROOVE)
        info_frame.pack(pady=20, padx=50, ipadx=20, ipady=10)
        
        tk.Label(info_frame, text=f"Application: {self.app_name}", font=("Arial", 11), fg="white", bg="#1c2541", anchor="w").pack(fill=tk.X, pady=2)
        tk.Label(info_frame, text=f"Student:     {self.student_name}", font=("Arial", 11), fg="white", bg="#1c2541", anchor="w").pack(fill=tk.X, pady=2)
        tk.Label(info_frame, text=f"Course:      {self.course_info}", font=("Arial", 11), fg="white", bg="#1c2541", anchor="w").pack(fill=tk.X, pady=2)
        tk.Label(info_frame, text=f"Date:        {self.date_info}", font=("Arial", 11), fg="white", bg="#1c2541", anchor="w").pack(fill=tk.X, pady=2)
        

        tk.Label(self.login_frame, text="Enter Password", font=("Arial", 12, "bold"), fg="#48cae4", bg="#0b132b").pack(pady=10)
        self.password_entry = tk.Entry(self.login_frame, font=("Arial", 14), show="—", justify="center", width=20)
        self.password_entry.pack(pady=5)
        tk.Label(self.login_frame, text="Password is masked (---)", font=("Arial", 9), fg="#8d99ae", bg="#0b132b").pack()
        
        login_btn = tk.Button(self.login_frame, text="Access BST Explorer →", font=("Arial", 12, "bold"), bg="#00b4d8", fg="white", command=self.verify_password, relief=tk.FLAT, padx=15, pady=8)
        login_btn.pack(pady=25)
        
        tk.Label(self.login_frame, text="UNAD - ECBTI - Systems Engineering", font=("Arial", 9), fg="#6c757d", bg="#0b132b").pack(side=tk.BOTTOM, pady=10)

    def verify_password(self):
        pwd = self.password_entry.get()
        if pwd == "UNAD":
            self.login_frame.destroy()
            self.create_main_interface()
        else:
            messagebox.showerror("Access Denied", "Incorrect password. The generic password is 'UNAD'.")

    def create_main_interface(self):
        # Barra superior de estado institucional
        top_bar = tk.Frame(self.root, bg="#1c2541", height=30)
        top_bar.pack(side=tk.TOP, fill=tk.X)
        tk.Label(top_bar, text="  🌳 BST Explorer — Binary Search Tree", font=("Arial", 10, "bold"), fg="#48cae4", bg="#1c2541").pack(side=tk.LEFT, pady=5)
        tk.Label(top_bar, text=f"{self.student_name}  |  {self.course_info}  ", font=("Arial", 9), fg="#ade8f4", bg="#1c2541").pack(side=tk.RIGHT, pady=5)

        # Panel izquierdo: Controles
        control_frame = tk.Frame(self.root, bg="#111827", width=260)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        tk.Label(control_frame, text="⚙️ Controls", font=("Arial", 12, "bold"), fg="#48cae4", bg="#111827").pack(anchor="w", padx=10, pady=10)
        tk.Label(control_frame, text="Node Value (Integer)", font=("Arial", 10), fg="white", bg="#111827").pack(anchor="w", padx=10)
        
        self.node_input = tk.Entry(control_frame, font=("Arial", 14), justify="center")
        self.node_input.pack(padx=10, pady=5, fill=tk.X)
        
        tk.Button(control_frame, text="+ Add Node", bg="#00b4d8", fg="white", font=("Arial", 10, "bold"), command=self.add_node_action).pack(padx=10, pady=5, fill=tk.X)
        tk.Button(control_frame, text="🔍 Search Node", bg="#2a9d8f", fg="white", font=("Arial", 10, "bold"), command=self.search_node_action).pack(padx=10, pady=5, fill=tk.X)
        tk.Button(control_frame, text="🗑️ Clear Tree", bg="#f4a261", fg="white", font=("Arial", 10, "bold"), command=self.clear_tree_action).pack(padx=10, pady=5, fill=tk.X)
        tk.Button(control_frame, text="🚪 Exit", bg="#e63946", fg="white", font=("Arial", 10, "bold"), command=self.root.quit).pack(padx=10, pady=5, fill=tk.X)
        
        # Estadísticas
        tk.Label(control_frame, text="Tree Statistics", font=("Arial", 11, "bold"), fg="#48cae4", bg="#111827").pack(anchor="w", padx=10, pady=(20, 5))
        self.stat_nodes = tk.Label(control_frame, text="nodes: 0", font=("Arial", 10), fg="white", bg="#111827")
        self.stat_nodes.pack(anchor="w", padx=15)
        self.stat_height = tk.Label(control_frame, text="height: 0", font=("Arial", 10), fg="white", bg="#111827")
        self.stat_height.pack(anchor="w", padx=15)
        self.stat_root = tk.Label(control_frame, text="root: -", font=("Arial", 10), fg="white", bg="#111827")
        self.stat_root.pack(anchor="w", padx=15)

        right_frame = tk.Frame(self.root, bg="#0b132b")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.tree_canvas = tk.Canvas(right_frame, bg="#0f172a", highlightthickness=1, highlightbackground="#1e293b")
        self.tree_canvas.pack(fill=tk.BOTH, expand=True, pady=(0, 5))
        
        traversal_frame = tk.Frame(right_frame, bg="#0b132b", height=150)
        traversal_frame.pack(fill=tk.X, expand=False)
        
        self.pre_canvas = self.create_traversal_box(traversal_frame, "📌 Pre-order")
        self.in_canvas = self.create_traversal_box(traversal_frame, "📌 In-order")
        self.post_canvas = self.create_traversal_box(traversal_frame, "📌 Post-order")

    def create_traversal_box(self, parent, title):
        frame = tk.LabelFrame(parent, text=title, font=("Arial", 9, "bold"), fg="#48cae4", bg="#0f172a", bd=1, relief=tk.SOLID)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2)
        canvas = tk.Canvas(frame, bg="#0f172a", height=80, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)
        return canvas

    def get_height(self, node):
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def add_node_action(self):
        val_str = self.node_input.get()
        # Validación de entero
        try:
            val = int(val_str)
        except ValueError:
            messagebox.showerror("Invalid Input", f"'{val_str}' is not a valid integer.\nOnly whole numbers are accepted (e.g. 10, 5, 42).")
            return


        temp_root = self.insert_bst(self.bst_root, val, check_only=True)
        if temp_root == -1:
            messagebox.showerror("Maximum Depth Reached", f"Cannot insert node {val}.\nThis tree is limited to 4 levels.\nAdding this node would create a level 5.\nClear the tree or choose a different value.")
            return

        self.bst_root = self.insert_bst(self.bst_root, val)
        self.node_count += 1
        self.max_height = self.get_height(self.bst_root)
        
        self.stat_nodes.config(text=f"nodes: {self.node_count}")
        self.stat_height.config(text=f"height: {self.max_height}")
        self.stat_root.config(text=f"root: {self.bst_root.key}")
        
        self.node_input.delete(0, tk.END)
        self.redraw_tree()
        self.update_traversals()

    def insert_bst(self, root, key, check_only=False):
        if not root:
            if check_only:
                return 1
            return BSTNode(key)
        
        if key < root.key:
            res = self.insert_bst(root.left, key, check_only)
            if check_only and res == -1:
                return -1
            if not check_only and res and not root.left:
                root.left = res
        elif key > root.key:
            res = self.insert_bst(root.right, key, check_only)
            if check_only and res == -1:
                return -1
            if not check_only and res and not root.right:
                root.right = res
        
        current_height = self.get_height(root)
        if current_height > 4:
            return -1
            
        return root if not check_only else 1

    def search_node_action(self):
        val_str = self.node_input.get()
        try:
            val = int(val_str)
        except ValueError:
            messagebox.showerror("Invalid Input", f"'{val_str}' is not a valid integer.")
            return
            
        found, path = self.search_bst(self.bst_root, val)
        path_str = " -> ".join(map(str, path))
        if found:
            messagebox.showinfo("Node Found", f"Node {val} was found in the tree.\nSearch path: {path_str}")
        else:
            messagebox.showwarning("Node Not Found", f"Node {val} does not exist in the tree.\nSearch path tried: {path_str}")

    def search_bst(self, root, key, path=None):
        if path is None:
            path = []
        if not root:
            return False, path
        path.append(root.key)
        if root.key == key:
            return True, path
        elif key < root.key:
            return self.search_bst(root.left, key, path)
        else:
            return self.search_bst(root.right, key, path)

    def clear_tree_action(self):
        self.bst_root = None
        self.node_count = 0
        self.max_height = 0
        self.stat_nodes.config(text="nodes: 0")
        self.stat_height.config(text="height: 0")
        self.stat_root.config(text="root: -")
        self.tree_canvas.delete("all")
        self.pre_canvas.delete("all")
        self.in_canvas.delete("all")
        self.post_canvas.delete("all")
        messagebox.showinfo("Tree Cleared", "The tree and traversals have been successfully cleared.")

    def redraw_tree(self):
        self.tree_canvas.delete("all")
        width = self.tree_canvas.winfo_width()
        if width < 100:
            width = 750
        self.draw_node_rec(self.bst_root, width // 2, 40, width // 4, 1)

    def draw_node_rec(self, node, x, y, offset, level):
        if not node:
            return
        node.x = x
        node.y = y
        
        if node.left:
            lx, ly = x - offset, y + 60
            self.tree_canvas.create_line(x, y, lx, ly, fill="#48cae4", width=2)
            self.draw_node_rec(node.left, lx, ly, offset // 2, level + 1)
        if node.right:
            rx, ry = x + offset, y + 60
            self.tree_canvas.create_line(x, y, rx, ry, fill="#48cae4", width=2)
            self.draw_node_rec(node.right, rx, ry, offset // 2, level + 1)
            
        r = 20
        self.tree_canvas.create_oval(x - r, y - r, x + r, y + r, fill="#00b4d8", outline="white", width=2)
        self.tree_canvas.create_text(x, y, text=str(node.key), fill="white", font=("Arial", 10, "bold"))

    def update_traversals(self):
        pre_res = []
        in_res = []
        post_res = []
        
        def preorder(n):
            if n:
                pre_res.append(n.key)
                preorder(n.left)
                preorder(n.right)
        def inorder(n):
            if n:
                inorder(n.left)
                in_res.append(n.key)
                inorder(n.right)
        def postorder(n):
            if n:
                postorder(n.left)
                postorder(n.right)
                post_res.append(n.key)
                
        preorder(self.bst_root)
        inorder(self.bst_root)
        postorder(self.bst_root)
        
        self.draw_traversal_nodes(self.pre_canvas, pre_res)
        self.draw_traversal_nodes(self.in_canvas, in_res)
        self.draw_traversal_nodes(self.post_canvas, post_res)

    def draw_traversal_nodes(self, canvas, elements):
        canvas.delete("all")
        start_x = 30
        y = 40
        for i, el in enumerate(elements):
            x = start_x + (i * 35)
            canvas.create_oval(x - 12, y - 12, x + 12, y + 12, fill="#f4a261", outline="white")
            canvas.create_text(x, y, text=str(el), fill="#0b132b", font=("Arial", 9, "bold"))

if __name__ == "__main__":
    root = tk.Euler if hasattr(tk, 'Euler') else tk.Tk()
    app = BSTApp(root)
    root.mainloop()