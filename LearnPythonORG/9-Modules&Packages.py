#   Modules and Packages
''' Module is a piece of software that has a specific functionality. For example, when building a ping pong game, one module may be responsible for the game logic, and
another module draws the game on the screen. Each module consists of a different file, which may be edited separately.
- Modules are just Python files with a .py extension. ej:
    -mygame/
        -mygame/game.py  --->Logica del juego
        -mygame/draw.py  --->Dibuja el juego en pantalla
'''

    #Importar modulos
# game.py
# import the draw module
import draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()


# draw.py seria asi:
def draw_game():
    ...

def clear_screen(screen):
    ...

'''When the import draw directive runs, the Python interpreter looks for a file in the directory in which the script was executed with the module name and a .py suffix. In this case it will look for draw.py. If it is found, it will be imported. If it's not found, it will continue looking for built-in modules. 

-  when importing a module, a .pyc file is created. This is a compiled Python file. Python compiles files into Python bytecode so that it won't have to parse the files each time modules are loaded.

'''


#Incompleto..