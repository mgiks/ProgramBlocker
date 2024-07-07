import webbrowser, psutil

#List of blocked programs
prog_list = []

file = open("Exes.txt", "r")

for line in file:
    prog_list.append(line.strip())

exe = False

def open_browser():
    webbrowser.open_new("https://i.pinimg.com/736x/5c/b7/37/5cb737b195f6cc3c3e3a0e53e5aaab99.jpg")

def kill_process():
    global exe

    for process in (process for process in psutil.process_iter() if process.name() in prog_list):
        exe = True
        process.kill()

    if exe:
        open_browser()
    
    exe = False

while True:

    kill_process()

        








































