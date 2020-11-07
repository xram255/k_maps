
q = [[1, 1],
     [1, 0]]

def scan2xhor(inval):
     if (q[inval][0] == 1) & (q[inval][1] == 1):
          print("success")
     else:
          print("not found")

def scan2xver(inval):
     if (q[0][inval] == 1) & (q[1][inval] == 1):
          print("success")
     else:
          print("not found")

scan2xver(0)

