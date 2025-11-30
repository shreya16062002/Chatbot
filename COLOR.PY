import tkinter as tk
from tkinter import scrolledtext
from groq import Groq

# ----------------------
# PUT YOUR GROQ API KEY
# ----------------------
client = Groq(api_key="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")


def chat_with_gpt(user_input):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content


# ----------------------
# SEND MESSAGE FUNCTION
# ----------------------
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return

    # Show user's message as a bubble
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "\nYou:\n", "user_label")
    chat_window.insert(tk.END, user_input + "\n", "user_bubble")

    entry.delete(0, tk.END)
    chat_window.yview(tk.END)  # auto scroll

    # Bot response
    bot_response = chat_with_gpt(user_input)

    chat_window.insert(tk.END, "Bot:\n", "bot_label")
    chat_window.insert(tk.END, bot_response + "\n", "bot_bubble")

    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)


# ----------------------
# GUI SETUP
# ----------------------
root = tk.Tk()
root.title("AI Chatbot (Groq)")
root.geometry("500x600")
root.resizable(False, False)

# Chat window
chat_window = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 12), bg="#ECECEC"
)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Chat bubble styles
chat_window.tag_config(
    "user_bubble",
    background="#DCF8C6",
    foreground="black",
    spacing3=10,
    lmargin1=20,
    lmargin2=20,
    rmargin=80,
)

chat_window.tag_config(
    "bot_bubble",
    background="white",
    foreground="black",
    spacing3=15,
    lmargin1=80,
    lmargin2=80,
    rmargin=20,
)

chat_window.tag_config("user_label", foreground="green", font=("Arial", 9, "bold"))
chat_window.tag_config("bot_label", foreground="blue", font=("Arial", 9, "bold"))

# Entry frame
entry_frame = tk.Frame(root)
entry_frame.pack(fill=tk.X, padx=10, pady=10)

entry = tk.Entry(entry_frame, font=("Arial", 14))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

send_button = tk.Button(
    entry_frame, text="Send", font=("Arial", 12), width=8, command=send_message
)
send_button.pack(side=tk.RIGHT)

# Press Enter to send message
entry.bind("<Return>", lambda event: send_message())

root.mainloop()
