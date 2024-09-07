import webbrowser, psutil

# List of blocked programs
program_list = []


# Append to the list of blocked programs
with open("Exes.txt", "r") as file:
    for line in file:
        program_list.append(line.strip())


# Open the blocker image in a browser
def open_blocker_image():
    webbrowser.open_new(
        "https://i.pinimg.com/736x/5c/b7/37/5cb737b195f6cc3c3e3a0e53e5aaab99.jpg"
    )


# Kill process
def kill_process():
    for process in psutil.process_iter():
        if process.name() in program_list:
            process.kill()
            open_blocker_image()
            break


# Constant scanning
while True:
    kill_process()
