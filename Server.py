import waitress
from Application import app
import tkinter as tk
from tkinter import messagebox
import threading

serverPort = 8080


class WebServerThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        waitress.serve(app, listen="*:%i" % serverPort)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Choose Server Port", font="Arial 12")
        label.pack(pady=10, padx=10)

        e1 = tk.Entry(self, text = "Port:")
        e1.insert(0, "8080")
        e1.pack(pady=10, padx=10)

        button = tk.Button(self, text = "Start Server", command=lambda: self.transition(e1.get(), controller))
        button.pack(pady=10, padx=10)

    def transition(self, port, controller):
        try:
            global serverPort
            serverPort = int(port)
            controller.show_frame(Master)
        except:
            pass

    def start(self):
        pass


class Master(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        title = tk.Label(self, text = "TBA Analyze Server", font = "Arial 18 bold")
        title.pack()

        quitButton = tk.Button(self, text = "Quit", command=lambda: self.prompt())
        quitButton.pack()

    def prompt(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            serverThread.stop()
            self.quit()


    def start(self):
        serverThread.start()


class ServerGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Master):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.start()

serverThread = WebServerThread(1, "serverThread")
localApp = ServerGUI()
localApp.mainloop()