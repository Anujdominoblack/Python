# ansi escapes sequences for colors and effects
BLACK='\u001b[30m'
RED='\u001b[31m'
GREEN='\u001b[32m'
YELLOW='\u001b[33m'
BLUE='\u001b[34m'
MAGNETA='\u001b[35m'
CYAN='\u001b[36m'
WHITE='\u001b[37m'
RESET='\u001b[0m'
BOLD='\u001b[1m'
UNDERLINE='\u001b[4m'
REVERSE='\u001b[7m'

print("this will be in red")
print(RESET)

def colour_print(text :str ,effect :str)->None:
    output="{0}{1}{2}".format(effect,text,RESET)
    print(output)


colour_print("this is my file",RED)