def prgMsg(message):
    """
    Print a progress message without a trailing newline, so a matching
    call to Done() can print "Done" on the same line right after it.

    Parameters
    ----------
    message : str
        The message to print, e.g. 'Loading file'.

    Returns
    -------
    None
    """
    print(f'{message}: ',end='')
def Done(start_time):
    """
    Print a green "Done" message with the elapsed time since start_time,
    intended to follow a prgMsg() call on the same line.

    Parameters
    ----------
    start_time : float
        A timestamp (as returned by time.time()) marking when the
        operation began.

    Returns
    -------
    None
    """
    from spaceToolsLib.tools.colors import color
    from time import time
    print(f'{color.GREEN}Done{color.END} at {color.YELLOW}{round(time() - start_time,1)} seconds {color.END}' )