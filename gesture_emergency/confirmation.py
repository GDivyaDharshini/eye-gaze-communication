confirmation = None

def confirm_yes():
    global confirmation
    confirmation = "YES"
    print("Selection Confirmed")

def confirm_no():
    global confirmation
    confirmation = "NO"
    print("Selection Cancelled")