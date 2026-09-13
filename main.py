#this is the main app(body) of tbe system
# this is the light weight version of enterprise IDE
# this will use CLI, sql and flask for web dashboard
# this will also be the project im going to make

with open("auth.log") as f:         #opening a file. Then close after the blocks end.
    for line in f:
        line = line.strip()
        if "Failed" in line:
            print(line)
