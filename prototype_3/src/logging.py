# Centralized error logging, so callers can count/filter "// ERROR: ..." diagnostics
# instead of every module printing directly.

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
