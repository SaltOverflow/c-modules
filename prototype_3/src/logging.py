# Centralized error logging so we can count the number of errors emitted

errorCount = 0
printEnabled = True

def reset():
    global errorCount
    errorCount = 0

def setPrintEnabled(enabled: bool):
    global printEnabled
    printEnabled = enabled

def error(message: str):
    global errorCount
    errorCount += 1
    if printEnabled:
        print(f"// ERROR: {message}")
