def prgMsg(message):
    print(f'{message}: ',end='')
def Done(start_time):
    from spaceToolsLib.tools.colors import color
    from time import time
    print(f'{color.GREEN}Done{color.END} at {color.YELLOW}{round(time() - start_time,1)} seconds {color.END}' )