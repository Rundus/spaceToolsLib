

class color:
   """
   ANSI terminal escape codes for colored/styled console output.

   Used by spaceToolsLib.tools.diagnostics to print colored progress
   messages (e.g. green "Done" text). Concatenate a color constant before
   text and `color.END` after it to reset formatting, e.g.
   f'{color.GREEN}Done{color.END}'.
   """
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'