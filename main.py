import tkinter as tk
import datetime
from openai import OpenAI
from dotenv import load_dotenv
import os

class GUIConfig:

    def __init__(self, chatName, botName, systemMessage) -> None:
        self.chatName = chatName
        self.botName = botName
        self.systemMessage = systemMessage



class GUI(tk.Tk):
    def __init__(self, config:GUIConfig, client, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        super().__init__(screenName, baseName, config.chatName, useTk, sync, use)
        self.msgs = []
        self.config = config
        self.client = client
        self.createWidgets()
        self.setWindowPosition()
        self.inputBox.focus()

    def createWidgets(self):
        self.createChatHistory()
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

    def createResetButton(self):
        buttonReset = tk.Button(self, text="Reset", command=self.reset)
        buttonReset.pack(side="right")
        self.buttonReset = buttonReset

    def createSendButton(self):
        buttonSend = tk.Button(self, text="Send", command=self.sendMessage)
        buttonSend.pack(side="right")
        self.buttonSend = buttonSend

    def setWindowPosition(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = int((screen_width/2) - (self.winfo_reqwidth()/2))
        y_coordinate = int(screen_height/3)
        self.geometry("+{}+{}".format(x_coordinate, y_coordinate))

    def sendMessage(self):
        user_input = self.inputBox.get()
        if user_input == "quit()":
            self.destroy()
            return
        elif user_input == "reset()":
            self.reset()
            self.inputBox.delete(0, tk.END)
            return
        self.msgs.append({"role": "user", "content": user_input})
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.msgs
        )
        reply = response.choices[0].message.content
        # response = user_input
        # reply = response
        self.msgs.append({"role": "assistant", "content": reply})
        self.chatHistory.insert(tk.END, "\nYou:\n", "bold")
        self.chatHistory.insert(tk.END, user_input + "\n", "inputfont")
        self.chatHistory.insert(tk.END, "\n" + self.config.botName + ":\n", "bold")
        self.chatHistory.insert(tk.END, reply + "\n", "responsefont")
        self.inputBox.delete(0, tk.END)
        self.chatHistory.yview(tk.END)
        self.chatHistory.tag_configure("inputfont", font=("Arial", 12), foreground="#FFFFFF")
        self.chatHistory.tag_configure("responsefont", font=("Arial", 12), foreground="#FFFFFF")
        self.chatHistory.tag_configure("bold", font=("Arial", 12, "bold"))


    def reset(self):
        self.msgs = []
        self.chatHistory.delete(1.0, tk.END)
        self.msgs.append({"role": "system", "content": self.config.systemMessage})






def main():
    now = datetime.datetime.now()
    day = now.strftime("%A")
    time = now.strftime("%I:%M %p")

    user = "STEDBOT"
    botName = "BOT"
    load_dotenv()
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    config = GUIConfig(
                chatName=user, 
                botName=botName, 
                systemMessage=
                f"You are a historian for St Edwards Hall at the University of Notre Dame. You know all the history about the dorm. \
                Our hall, St. Edward's Hall, holds a rich history dating back to 1882. Initially serving as a grammar school, it was transformed into a residence for men in 1928. \
                During World War II, it remained a civilian haven on campus. In 1980, a fire threatened its existence, but alumni support ensured its reconstruction. \
                Notable residents include Paul Hornung, and in 1924, Knute Rockne's baptism took place in our chapel.  \
                From its origins in the vision of Fr. Sorin to its modern-day vibrancy, St. Ed's remains a cherished part of Notre Dame's legacy. \
                \
                You are tasked to answer any questions the user may ask informing about the history and cultures of St. Edwards Hall"
    )

    gui = GUI(
        config=config,
        client=client
    )

    gui.mainloop()


if __name__ == "__main__":
    main()