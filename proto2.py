import tkinter as tk
import datetime
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

from brAIn import brAIn

class GUIConfig:

    def __init__(self, chatName, botName, systemMessage) -> None:
        self.chatName = chatName
        self.botName = botName
        self.systemMessage = systemMessage



class GUI(tk.Tk):
    def __init__(self, model: brAIn.BHistorian, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        super().__init__(screenName, baseName, model.name, useTk, sync, use)
        self.model = model
        self.createWidgets()
        self.setWindowPosition()
        self.inputBox.focus()

    def createButtonRow(self):
        # Create a frame to contain the buttons
        button_frame = tk.Frame(self)
        button_frame.pack()

        # Create the buttons and place them in the frame
        button1 = tk.Button(button_frame, text="What is St. Edwards?", command=lambda: self.sendMessage("What is St. Edwards?"))
        button1.grid(row=0, column=0, padx=5, pady=5)

        button2 = tk.Button(button_frame, text="Who is Fr. Ralph Haag?", command=lambda: self.sendMessage("Who is Fr. Ralph Haag?"))
        button2.grid(row=0, column=1, padx=5, pady=5)

        button3 = tk.Button(button_frame, text="What has happened this week?", command=lambda: self.sendMessage("What's happened the week of March 18, 2024?"))
        button3.grid(row=0, column=2, padx=5, pady=5)

    def createWidgets(self):
        self.createChatHistory()
        self.createButtonRow()
        self.createInputBox()
        self.createResetButton()
        self.createSendButton()

    def createChatHistory(self):
        chatHistory = tk.Text(self)
        chatHistory.config(wrap="word", width=50, height=20)
        chatHistory.pack(fill="both", expand=True, padx=5, ipadx=5)
        self.chatHistory = chatHistory

    def createInputBox(self):
        inputBox = tk.Entry(self, width=50)
        inputBox.pack(side="left", fill="x", expand=True, padx=5, ipadx=5, ipady=5)
        self.inputBox = inputBox

        inputBox.bind("<Return>", lambda event: self.sendMessage(self.inputBox.get()))

    def createResetButton(self):
        buttonReset = tk.Button(self, text="Reset", command=self.reset)
        buttonReset.pack(side="right")
        self.buttonReset = buttonReset

    def createSendButton(self):
        buttonSend = tk.Button(self, text="Send", command=lambda: self.sendMessage(self.inputBox.get()))
        buttonSend.pack(side="right")
        self.buttonSend = buttonSend

    def setWindowPosition(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = int((screen_width/2) - (self.winfo_reqwidth()/2))
        y_coordinate = int(screen_height/3)
        self.geometry("+{}+{}".format(x_coordinate, y_coordinate))

    def sendMessage(self, user_input):
        if user_input == "quit()":
            self.destroy()
            return
        elif user_input == "reset()":
            self.reset()
            self.inputBox.delete(0, tk.END)
            return
        
        reply = self.model.ask(user_input)

        print(reply)

        self.chatHistory.insert(tk.END, "\nYou:\n", "bold")
        self.chatHistory.insert(tk.END, user_input + "\n", "inputfont")
        self.chatHistory.insert(tk.END, "\n" + self.model.name+ ":\n", "bold")
        self.chatHistory.insert(tk.END, reply + "\n", "responsefont")
        self.inputBox.delete(0, tk.END)
        self.chatHistory.yview(tk.END)
        self.chatHistory.tag_configure("inputfont", font=("Arial", 12), foreground="#000000")
        self.chatHistory.tag_configure("responsefont", font=("Arial", 12), foreground="#000000")
        self.chatHistory.tag_configure("bold", font=("Arial", 12, "bold"))


    def reset(self):
        self.model.reset()
        self.chatHistory.delete(1.0, tk.END)






def main():
    now = datetime.datetime.now()
    day = now.strftime("%A")
    time = now.strftime("%I:%M %p")



    historian = brAIn.demoBot()

    gui = GUI(
        model=historian
    )

    gui.mainloop()


if __name__ == "__main__":
    main()