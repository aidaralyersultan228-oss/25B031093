# 1)
x = 2
match x:
    case 1: print("one")
    case 2: print("two")
    case _: print("other")

# 2)
cmd = "stop"
match cmd:
    case "start": print("Starting")
    case "stop":  print("Stopping")
    case _:       print("Unknown")

# 3)
point = (0, 5)
match point:
    case (0, y): print("On Y axis:", y)
    case (x, 0): print("On X axis:", x)
    case _:      print("Somewhere else")

# 4)
status = 404
match status:
    case 200: print("OK")
    case 404: print("Not Found")
    case _:   print("Other")

# 5)
ch = "a"
match ch:
    case "a" | "e" | "i" | "o" | "u": print("vowel")
    case _: print("consonant")
