# import my_module as mod       # Here mod is an alias for modules_in_python like a nickname

# mod.hello() # Hello from a module

# mod.bye() # Bye from a module

############ ANOTHER WAY TO IMPORT MODULES ############

from my_module import hello, bye # import only hello and bye functions from modules_in_python.py
hello() # Hello from a module
bye() # Bye from a module

# To find all accessible modules
help('modules')