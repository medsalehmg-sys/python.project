# Decorator Concept :
# Code 4_C version 2 :
# creation of a Decorator command_handler():
def command_handler(func): # definition command_handler function 
    if not hasattr(command_handler,"commands"):
       command_handler.commands=[]
    def wrapper():
        command_handler.commands.append(func)
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
for cmd in command_handler.commands:
    print(cmd.__name__)