# Square
# for b in range(0,5):
#     for a in range(0,6):
#         print("0",end=" ") 
#     print("")

# Right-triangle
# for b in range(0,3):
#     for a in range(b+1):
#         print(a, end=" ")
#     print("")

# Upside-down right-triangle
# for b in range(0,4):
#     for a in range(4-b):
#         print(a, end=" ")
#     print("")

# Isoceles triangle
for b in range(0,4):
    for a in range(4-b):
        print("0", end=" ")
    for c in range(b+1):
        print("0",end="")
    print(" ")
