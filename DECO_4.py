# Decorator Concept :
# Code 4:
# creation of List :
commands=[]
# creation of a Decorator command_handler():
def command_handler(func):
    def wrapper():
        commands.append(func)
    return wrapper
# creation of start() function :
@command_handler
def start():  # we use command_handler()
    print(" start  the application")
# creation of stop() function :
@command_handler
def stop():
    print("stop the application")
    # creation if restart funcion :
@command_handler
def restart():
    print("restart the application")

start()
stop()
restart()
for cmd in commands:
    print(cmd.__name__)