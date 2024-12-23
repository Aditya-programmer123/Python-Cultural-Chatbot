import tkinter as tk
from tkinter import scrolledtext
from logic import generate_response  # Import the chatbot functions
from PIL import Image, ImageTk  # Import PIL for image handling


class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cultural Festival Chatbot")
        self.root.geometry("550x750")
        self.root.resizable(False, False)

        # Welcome Screen
        self.welcome_frame = tk.Frame(self.root, bg="#FF9933")
        self.welcome_frame.pack(fill=tk.BOTH, expand=True)

        # Set background image for welcome screen
        self.set_background_image(
            self.welcome_frame, r"C:\Users\Aditya\Downloads\sar.png-removebg-preview.png"
        )  # Specify your image path here

        # Welcome message
        welcome_message = "🙏 SWAGAT HAI AAPKA 🙏"
        welcome_label = tk.Label(
            self.welcome_frame,
            text=welcome_message,
            font=("Helvetica", 16, "bold"),
            bg="#FF9933",
            fg="white",
            justify="center",
        )
        welcome_label.pack(anchor="n", pady=(10, 5))

        # Continue button
        continue_button = tk.Button(
            self.welcome_frame,
            text="👉 Continue 👈",
            font=("Helvetica", 14, "bold"),
            bg="#138808",
            fg="white",
            activebackground="#1aaf11",
            activeforeground="white",
            relief="groove",
            bd=4,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.open_chatbot,
        )
        continue_button.pack(side="bottom", pady=20)

        # Chat Interface
        self.chat_frame = tk.Frame(self.root, bg="#F5F5F5")
        self.chat_frame.pack_forget()

        # Add a colorful header to the chat interface
        self.header_frame = tk.Frame(self.chat_frame, bg="#138808", height=50)
        self.header_frame.pack(fill=tk.X)
        header_label = tk.Label(
            self.header_frame,
            text="🌟 Indian Cultural Festival Chatbot 🌟",
            font=("Helvetica", 16, "bold"),
            bg="#138808",
            fg="white",
        )
        header_label.pack(pady=10)

        # Scrollable chat box
        self.chat_box = scrolledtext.ScrolledText(
            self.chat_frame,
            wrap=tk.WORD,
            state=tk.DISABLED,
            font=("Helvetica", 12),
            height=15,
            bg="#FFFFFF",
            fg="#000000",
            bd=0,
            padx=10,
            pady=10,
        )
        self.chat_box.pack(padx=10, pady=(5, 15), fill=tk.BOTH, expand=True)

        # Input area with a frame
        self.input_frame = tk.Frame(self.chat_frame, bg="#FFFFFF")
        self.input_frame.pack(padx=10, pady=10, fill=tk.X)

        # Input box
        self.input_field = tk.Entry(
            self.input_frame,
            font=("Helvetica", 12),
            bg="#F0F0F0",
            fg="#000000",
            relief="flat",
            bd=5,
        )
        self.input_field.pack(side=tk.LEFT, padx=(10, 5), pady=5, fill=tk.X, expand=True)

        # Send button
        self.send_button = tk.Button(
            self.input_frame,
            text="Send",
            font=("Helvetica", 12, "bold"),
            bg="#FF9933",
            fg="white",
            activebackground="#E67E22",
            activeforeground="white",
            relief="groove",
            bd=3,
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.send_message,
        )
        self.send_button.pack(side=tk.RIGHT, padx=(5, 10), pady=5)

    def set_background_image(self, frame, image_path):
        img = Image.open(image_path)
        img.thumbnail((550, 750), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        background_label = tk.Label(frame, image=photo)
        background_label.image = photo
        background_label.place(relwidth=1, relheight=1)

    def open_chatbot(self):
        self.welcome_frame.pack_forget()
        self.chat_frame.pack(fill=tk.BOTH, expand=True)
        self.start_conversation()

    def start_conversation(self):
        # Display styled greeting
        self.display_message(
            "Hello! I am your Cultural Festival Chatbot.\nWhat would you like to learn about?",
            "Mohini",
            style="bold",
        )
        # Display options without boxes and in black font
        self.display_message(
            "1. Festivals\n2. Dance\n3. Attire\n4. Food\n5. Languages",
            "Mohini",
            style="normal",
        )

    def send_message(self):
        user_message = self.input_field.get().strip()
        if user_message:
            self.display_message(user_message, "You")
            response = generate_response(user_message)
            self.display_message(response, "Mohini")
        self.input_field.delete(0, tk.END)

    def display_message(self, message, sender, style="normal"):
        self.chat_box.config(state=tk.NORMAL)
        # Apply styles
        if style == "bold":
            tag = "bold"
            self.chat_box.tag_config(
                tag, font=("Helvetica", 12, "bold"), foreground="#138808"
            )
        else:
            tag = "normal"
            self.chat_box.tag_config(
                tag, font=("Helvetica", 12), foreground="#000000"
            )
        # Insert sender's message
        self.chat_box.insert(tk.END, f"{sender}: ", ("Arial",))
        self.chat_box.insert(tk.END, f"{message}\n\n", tag)
        self.chat_box.config(state=tk.DISABLED)
        self.chat_box.yview(tk.END)


# Create the main window
root = tk.Tk()
chatbot_app = ChatbotGUI(root)
root.mainloop()
