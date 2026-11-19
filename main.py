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
    MAX_LEVELS = 4

    def __init__(self, root_window):
        self.root = root_window
        self.root.title("Fase4StefaniaRedondo — BST Explorer")
        self.root.geometry("1150x780")
        self.root.config(bg="#0b132b")

        self.app_name = "Fase4StefaniaRedondo"
        self.student_name = "Stefania Redondo Jimenez"
        self.course_info = "Data Structures - 301305"
        self.date_info = "November 19, 2026"

        self.bst_root = None
        self.node_count = 0
        self.max_height = 0
        self.highlighted_path = []
        self.found_node_key = None

        self.create_login_window()

    def create_login_window(self):
        self.login_frame = tk.Frame(self.root, bg="#0b132b")
        self.login_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            self.login_frame,
            text="🌳 BST Explorer",
            font=("Arial", 26, "bold"),
            fg="#48cae4",
            bg="#0b132b",
        ).pack(pady=20)
        tk.Label(
            self.login_frame,
            text="Binary Search Tree — Phase 4",
            font=("Arial", 14),
            fg="#ade8f4",
            bg="#0b132b",
        ).pack(pady=5)

        info_frame = tk.Frame(self.login_frame, bg="#1c2541", bd=2, relief=tk.GROOVE)
        info_frame.pack(pady=20, padx=50, ipadx=20, ipady=10)

        for label_text in [
            f"Application: {self.app_name}",
            f"Student:     {self.student_name}",
            f"Course:      {self.course_info}",
            f"Date:        {self.date_info}",
        ]:
            tk.Label(
                info_frame,
                text=label_text,
                font=("Arial", 11),
                fg="white",
                bg="#1c2541",
                anchor="w",
            ).pack(fill=tk.X, pady=2)

        tk.Label(
            self.login_frame,
            text="Enter Password",
            font=("Arial", 12, "bold"),
            fg="#48cae4",
            bg="#0b132b",
        ).pack(pady=10)
        self.password_entry = tk.Entry(
            self.login_frame,
            font=("Arial", 14),
            show="—",
            justify="center",
            width=20,
        )
        self.password_entry.pack(pady=5)
        self.password_entry.bind("<Return>", lambda _event: self.verify_password())
        tk.Label(
            self.login_frame,
            text="Password is masked (— — —)",
            font=("Arial", 9),
            fg="#8d99ae",
            bg="#0b132b",
        ).pack()

        tk.Button(
            self.login_frame,
            text="Access BST Explorer →",
            font=("Arial", 12, "bold"),
            bg="#00b4d8",
            fg="white",
            command=self.verify_password,
            relief=tk.FLAT,
            padx=15,
            pady=8,
        ).pack(pady=25)

        tk.Label(
            self.login_frame,
            text="UNAD - ECBTI - Systems Engineering",
            font=("Arial", 9),
            fg="#6c757d",
            bg="#0b132b",
        ).pack(side=tk.BOTTOM, pady=10)

    def verify_password(self):
        pwd = self.password_entry.get().strip()
        if pwd == "UNAD":
            self.login_frame.destroy()
            self.create_main_interface()
        else:
            messagebox.showerror(
                "Access Denied", "Incorrect password. The generic password is 'UNAD'."
            )

    def create_main_interface(self):
        top_bar = tk.Frame(self.root, bg="#1c2541", height=32)
        top_bar.pack(side=tk.TOP, fill=tk.X)
        tk.Label(
            top_bar,
            text="  🌳 BST Explorer — Binary Search Tree",
            font=("Arial", 10, "bold"),
            fg="#48cae4",
            bg="#1c2541",
        ).pack(side=tk.LEFT, pady=5)
        tk.Label(
            top_bar,
            text=f"{self.student_name}  |  {self.course_info}  ",
            font=("Arial", 9),
            fg="#ade8f4",
            bg="#1c2541",
        ).pack(side=tk.RIGHT, pady=5)

        control_frame = tk.Frame(self.root, bg="#111827", width=265)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        tk.Label(
            control_frame,
            text="⚙️ Controls",
            font=("Arial", 12, "bold"),
            fg="#48cae4",
            bg="#111827",
        ).pack(anchor="w", padx=10, pady=10)
        tk.Label(
            control_frame,
            text="Node Value (Integer)",
            font=("Arial", 10),
            fg="white",
            bg="#111827",
        ).pack(anchor="w", padx=10)

        self.node_input = tk.Entry(control_frame, font=("Arial", 14), justify="center")
        self.node_input.pack(padx=10, pady=5, fill=tk.X)
        self.node_input.bind("<Return>", lambda _event: self.add_node_action())

        tk.Button(
            control_frame,
            text="+ Add Node",
            bg="#00b4d8",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.add_node_action,
        ).pack(padx=10, pady=5, fill=tk.X)
        tk.Button(
            control_frame,
            text="🔍 Search Node",
            bg="#2a9d8f",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.search_node_action,
        ).pack(padx=10, pady=5, fill=tk.X)
        tk.Button(
            control_frame,
            text="🗑️ Clear Tree",
            bg="#f4a261",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.clear_tree_action,
        ).pack(padx=10, pady=5, fill=tk.X)
        tk.Button(
            control_frame,
            text="🚪 Exit",
            bg="#e63946",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.root.quit,
        ).pack(padx=10, pady=5, fill=tk.X)

        tk.Label(
            control_frame,
            text="Tree Statistics",
            font=("Arial", 11, "bold"),
            fg="#48cae4",
            bg="#111827",
        ).pack(anchor="w", padx=10, pady=(20, 5))
        self.stat_nodes = tk.Label(
            control_frame, text="nodes: 0", font=("Arial", 10), fg="white", bg="#111827"
        )
        self.stat_nodes.pack(anchor="w", padx=15)
        self.stat_height = tk.Label(
            control_frame, text="height: 0", font=("Arial", 10), fg="white", bg="#111827"
        )
        self.stat_height.pack(anchor="w", padx=15)
        self.stat_root = tk.Label(
            control_frame, text="root: -", font=("Arial", 10), fg="white", bg="#111827"
        )
        self.stat_root.pack(anchor="w", padx=15)

        # Leyenda visual
        legend_frame = tk.LabelFrame(
            control_frame,
            text="Legend",
            font=("Arial", 10, "bold"),
            fg="#48cae4",
            bg="#111827",
            bd=1,
            relief=tk.SOLID,
        )
        legend_frame.pack(fill=tk.X, padx=10, pady=(20, 5), ipady=5)
        for color, text in [
            ("#00b4d8", "Regular node"),
            ("#f4a261", "Search path"),
            ("#2ec4b6", "Found node"),
        ]:
            row = tk.Frame(legend_frame, bg="#111827")
            row.pack(anchor="w", padx=8, pady=2)
            dot = tk.Canvas(row, width=14, height=14, bg="#111827", highlightthickness=0)
            dot.pack(side=tk.LEFT, padx=(0, 6))
            dot.create_oval(2, 2, 12, 12, fill=color, outline="white")
            tk.Label(row, text=text, font=("Arial", 9), fg="white", bg="#111827").pack(
                side=tk.LEFT
            )

        right_frame = tk.Frame(self.root, bg="#0b132b")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.tree_canvas = tk.Canvas(
            right_frame,
            bg="#0f172a",
            highlightthickness=1,
            highlightbackground="#1e293b",
        )
        self.tree_canvas.pack(fill=tk.BOTH, expand=True, pady=(0, 5))
        self.tree_canvas.bind("<Configure>", lambda _event: self.redraw_tree())

        traversal_frame = tk.Frame(right_frame, bg="#0b132b", height=145)
        traversal_frame.pack(fill=tk.X, expand=False)

        self.pre_canvas = self.create_traversal_box(traversal_frame, "📌 Pre-order")
        self.in_canvas = self.create_traversal_box(traversal_frame, "📌 In-order")
        self.post_canvas = self.create_traversal_box(traversal_frame, "📌 Post-order")
        for c in (self.pre_canvas, self.in_canvas, self.post_canvas):
            c.bind("<Configure>", lambda _event: self.update_traversals())

    def create_traversal_box(self, parent, title):
        frame = tk.LabelFrame(
            parent,
            text=title,
            font=("Arial", 9, "bold"),
            fg="#48cae4",
            bg="#0f172a",
            bd=1,
            relief=tk.SOLID,
        )
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2)
        canvas = tk.Canvas(frame, bg="#0f172a", height=85, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)
        return canvas

    def get_height(self, node):
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def key_exists(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self.key_exists(node.left, key)
        return self.key_exists(node.right, key)

    def insert_node_bst(self, root, key):
        if not root:
            return BSTNode(key)
        if key < root.key:
            root.left = self.insert_node_bst(root.left, key)
        elif key > root.key:
            root.right = self.insert_node_bst(root.right, key)
        return root

    def clone_tree(self, node):
        if not node:
            return None
        new_node = BSTNode(node.key)
        new_node.left = self.clone_tree(node.left)
        new_node.right = self.clone_tree(node.right)
        return new_node

    def add_node_action(self):
        val_str = self.node_input.get().strip()
        try:
            val = int(val_str)
        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                f"'{val_str}' is not a valid integer.\nOnly whole numbers are accepted (e.g. 10, 5, 42).",
            )
            return

        # Evitar duplicados sin alterar el contador
        if self.key_exists(self.bst_root, val):
            messagebox.showwarning(
                "Duplicate Value",
                f"Node {val} already exists in the tree.\nDuplicate values are not allowed.",
            )
            self.node_input.delete(0, tk.END)
            return

        # Validar límite estricto de 4 niveles
        candidate_root = self.insert_node_bst(self.clone_tree(self.bst_root), val)
        if self.get_height(candidate_root) > self.MAX_LEVELS:
            messagebox.showerror(
                "Maximum Depth Reached",
                f"Cannot insert node {val}.\n"
                f"This tree is limited to {self.MAX_LEVELS} levels.\n"
                f"Adding this node would create level {self.MAX_LEVELS + 1}.",
            )
            return

        self.bst_root = self.insert_node_bst(self.bst_root, val)
        self.node_count += 1
        self.max_height = self.get_height(self.bst_root)
        self.highlighted_path = []
        self.found_node_key = None

        self.stat_nodes.config(text=f"nodes: {self.node_count}")
        self.stat_height.config(text=f"height: {self.max_height}")
        self.stat_root.config(text=f"root: {self.bst_root.key}")

        self.node_input.delete(0, tk.END)
        self.redraw_tree()
        self.update_traversals()

    def search_node_action(self):
        val_str = self.node_input.get().strip()
        try:
            val = int(val_str)
        except ValueError:
            messagebox.showerror("Invalid Input", f"'{val_str}' is not a valid integer.")
            return

        found, path = self.search_bst(self.bst_root, val)
        self.highlighted_path = path
        self.found_node_key = val if found else None
        self.redraw_tree()

        path_str = " -> ".join(map(str, path)) if path else "None"
        if found:
            messagebox.showinfo(
                "Node Found",
                f"Node {val} was found in the tree.\nSearch path: {path_str}",
            )
        else:
            messagebox.showwarning(
                "Node Not Found",
                f"Node {val} does not exist in the tree.\nSearch path tried: {path_str}",
            )

    def search_bst(self, root, key, path=None):
        if path is None:
            path = []
        if not root:
            return False, path
        path.append(root.key)
        if root.key == key:
            return True, path
        if key < root.key:
            return self.search_bst(root.left, key, path)
        return self.search_bst(root.right, key, path)

    def clear_tree_action(self):
        self.bst_root = None
        self.node_count = 0
        self.max_height = 0
        self.highlighted_path = []
        self.found_node_key = None
        self.stat_nodes.config(text="nodes: 0")
        self.stat_height.config(text="height: 0")
        self.stat_root.config(text="root: -")
        self.tree_canvas.delete("all")
        self.pre_canvas.delete("all")
        self.in_canvas.delete("all")
        self.post_canvas.delete("all")
        messagebox.showinfo(
            "Tree Cleared", "The tree and traversals have been successfully cleared."
        )

    def redraw_tree(self):
        self.tree_canvas.delete("all")
        if not self.bst_root:
            return
        width = self.tree_canvas.winfo_width()
        if width < 100:
            width = 800
        self.draw_node_rec(self.bst_root, width // 2, 48, max(width // 4, 45), 1)

    def draw_node_rec(self, node, x, y, offset, level):
        if not node:
            return
        node.x = x
        node.y = y

        path_set = set(self.highlighted_path)
        on_path = node.key in path_set

        if node.left:
            lx, ly = x - offset, y + 72
            left_highlighted = on_path and (
                node.left.key in path_set or self.found_node_key == node.left.key
            )
            edge_color = "#f4a261" if left_highlighted else "#48cae4"
            edge_width = 3 if left_highlighted else 2
            self.tree_canvas.create_line(x, y, lx, ly, fill=edge_color, width=edge_width)
            self.draw_node_rec(node.left, lx, ly, max(offset // 2, 24), level + 1)

        if node.right:
            rx, ry = x + offset, y + 72
            right_highlighted = on_path and (
                node.right.key in path_set or self.found_node_key == node.right.key
            )
            edge_color = "#f4a261" if right_highlighted else "#48cae4"
            edge_width = 3 if right_highlighted else 2
            self.tree_canvas.create_line(x, y, rx, ry, fill=edge_color, width=edge_width)
            self.draw_node_rec(node.right, rx, ry, max(offset // 2, 24), level + 1)

        if node.key == self.found_node_key:
            fill_color = "#2ec4b6"
            outline_color = "#ffffff"
        elif on_path:
            fill_color = "#f4a261"
            outline_color = "#ffffff"
        else:
            fill_color = "#00b4d8"
            outline_color = "white"

        r = 20
        self.tree_canvas.create_oval(
            x - r, y - r, x + r, y + r, fill=fill_color, outline=outline_color, width=2
        )
        self.tree_canvas.create_text(
            x, y, text=str(node.key), fill="white", font=("Arial", 10, "bold")
        )

    def update_traversals(self):
        if not self.bst_root:
            return
        pre_res, in_res, post_res = [], [], []

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
        if not elements:
            return
        canvas_w = max(canvas.winfo_width(), 240)
        canvas_h = max(canvas.winfo_height(), 70)
        y = canvas_h // 2

        count = len(elements)
        margin = 18
        usable_w = max(canvas_w - 2 * margin, 40)
        step = min(34, usable_w / max(count, 1))
        radius = min(12, max(8, int(step * 0.42)))
        font_size = 9 if radius >= 11 else 8

        total_span = (count - 1) * step
        start_x = max(margin + radius, (canvas_w - total_span) / 2)

        for i, el in enumerate(elements):
            x = start_x + i * step
            canvas.create_oval(
                x - radius,
                y - radius,
                x + radius,
                y + radius,
                fill="#f4a261",
                outline="white",
            )
            canvas.create_text(
                x, y, text=str(el), fill="#0b132b", font=("Arial", font_size, "bold")
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = BSTApp(root)
    root.mainloop()