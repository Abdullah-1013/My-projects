import tkinter as tk

class AnimatedLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tom & Jerry Animated Login")

        # Canvas for animations
        self.canvas = tk.Canvas(root, width=300, height=200, bg="white")
        self.canvas.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

        # Draw Tom (Static)
        self.draw_tom()

        # Draw Jerry (Animated)
        self.jerry_body = self.canvas.create_oval(150, 100, 200, 150, fill="brown")  # Jerry's body
        self.jerry_head = self.canvas.create_oval(160, 60, 190, 90, fill="brown")   # Jerry's head
        self.jerry_left_hand = self.canvas.create_line(160, 100, 140, 80, width=5)  # Left hand
        self.jerry_right_hand = self.canvas.create_line(190, 100, 210, 80, width=5)  # Right hand

        # Labels and Entry Fields
        tk.Label(root, text="Email:", font=("Arial", 14)).grid(row=0, column=1, sticky="w")
        self.email_entry = tk.Entry(root, font=("Arial", 14), width=25)
        self.email_entry.grid(row=0, column=2, padx=10, pady=5)

        tk.Label(root, text="Password:", font=("Arial", 14)).grid(row=2, column=1, sticky="w")
        self.password_entry = tk.Entry(root, font=("Arial", 14), width=25, show="*")
        self.password_entry.grid(row=2, column=2, padx=10, pady=5)

        # Buttons for password visibility
        self.show_password = tk.StringVar(value="Show Password")
        self.toggle_button = tk.Button(root, textvariable=self.show_password, font=("Arial", 12),
                                        command=self.toggle_password_visibility)
        self.toggle_button.grid(row=3, column=2, pady=10)

    def draw_tom(self):
        # Tom's head
        self.canvas.create_oval(50, 50, 100, 100, fill="gray", outline="black")
        # Tom's ears
        self.canvas.create_polygon(50, 50, 40, 30, 60, 40, fill="gray", outline="black")
        self.canvas.create_polygon(100, 50, 110, 30, 90, 40, fill="gray", outline="black")
        # Tom's face
        self.canvas.create_oval(60, 70, 90, 90, fill="white")
        self.canvas.create_oval(65, 75, 75, 85, fill="black")  # Eye
        self.canvas.create_line(75, 85, 85, 80, width=2)  # Mouth

    def toggle_password_visibility(self):
        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show="")
            self.show_password.set("Hide Password")
            self.animate_jerry_peek()
        else:
            self.password_entry.config(show="*")
            self.show_password.set("Show Password")
            self.animate_jerry_hide()

    def animate_jerry_peek(self):
        # Animate Jerry moving hands away from eyes
        for i in range(20):
            self.canvas.move(self.jerry_left_hand, -1, 1)
            self.canvas.move(self.jerry_right_hand, 1, 1)
            self.root.update()
            self.root.after(20)

    def animate_jerry_hide(self):
        # Animate Jerry moving hands back to eyes
        for i in range(20):
            self.canvas.move(self.jerry_left_hand, 1, -1)
            self.canvas.move(self.jerry_right_hand, -1, -1)
            self.root.update()
            self.root.after(20)

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedLoginApp(root)
    root.mainloop()
