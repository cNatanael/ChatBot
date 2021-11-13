from tkinter import *
from chatbot import *


# from chatbot import get_response

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()


    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=370, height=750, bg='#fff')


        # head label
        head_label = Label(self.window, bg='#27b9e8', text='- - - ¡Supérate! Grupo Q - - -', pady='10', fg="white", font=("Arial", 14, "normal") )
        head_label.place(relwidth=1)

        # text widget
        self.text_widget = Text(self.window, width=10, height=2, bg='#fff', fg='#272727', padx=30, pady=20,
                                borderwidth=0)
        self.text_widget.place(relheight=0.840, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor='arrow', state=DISABLED, font=("Arial", 11, "normal"))

        # scroll bar
        # scrollbar = Scrollbar(self.text_widget)
        # scrollbar.place(relheight=1, relx=0.974)
        # scrollbar.configure(command=self.text_widget.yview)

        # botton
        bottom_label = Label(self.window, bg='#fff', height=80)
        bottom_label.place(relwidth=1, rely=0.92)

        # message
        self.msg_entry = Entry(bottom_label, bg='#f1f1f1', borderwidth=0)
        self.msg_entry.place(relwidth=0.74, relheight=0.03, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send btottom

        btn = PhotoImage(file="assets/send.png")

        send_button = Button(bottom_label, borderwidth=0, text='>', width=20, fg="#b4b4b4", command=lambda: self._on_enter_pressed(self), font=("ComicSans", 31, "bold"))

        send_button.place(relx=0.77, rely=0.008, relheight=0.03, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, 'You')

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{'you'}: {msg}\n "
        self.text_widget.configure(state=NORMAL)
        null = ' '
        self.text_widget.insert(END, null)
        self.text_widget.configure(state=DISABLED)

        intents = json.loads(open('preguntas.json').read())

        ints = predict_class(msg)

        res = get_response(ints, intents)
        lol = 'gato'

        msg1 = f"{'You'}: {msg}\n\n "
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{'Bot'}: {get_response(ints, intents)}\n\n "
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
