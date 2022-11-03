position = input("Enter the knight's starting position: ").split()

matrix = [['8|', '_', '_', '_', '_', '_', '_', '_', '_', '|'],
          ['7|', '_', '_', '_', '_', '_', '_', '_', '_', '|'],
          ['6|', '_', '_', '_', '_', '_', '_', '_', '_', '|'],
          ['5|', '_', '_', '_', '_', '_', '_', '_', '_', '|'],
          ['4|', '_', '_', '_', '_', '_', '_', '_', '_', '|'],
          ['3|', '_', '_', '_', '_', '_', '_', '_', '_', '|'],
          ['2|', '_', '_', '_', '_', '_', '_', '_', '_', '|'],
          ['1|', '_', '_', '_', '_', '_', '_', '_', '_', '|']]
try:
    if len(position) > 2 or not(int(position[1]) in range(1, 9)) or not(int(position[0]) in range(1, 9)):
        print("Invalid dimensions!")
    else:
        matrix[8 - int(position[1])][int(position[0])] = 'X'
        print(" -------------------")
        for i in matrix:
            for j in i:
                print(j, end=" ")
            print()

        print(" -------------------")
        print("   1 2 3 4 5 6 7 8")
except ValueError:
    print("Invalid dimensions!")
except IndexError:
    print("Invalid dimensions!")
