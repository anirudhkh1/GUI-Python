import colorama

# If using Windows, init() will cause anything sent to stdout or stderr
# will have ANSI color codes converted to the Windows versions. Hooray!
# If you are already using an ANSI compliant shell, it won't do anything


# Now regular ANSI codes should work, even in Windows
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset
print(CLEAR_SCREEN + RED + 'Welcome!' + RESET)