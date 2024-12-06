def hanoi(n, start, end):
    if n == 1:
        move(start, end)
    else:
        other = 6 - (start + end)
        hanoi(n-1, start, other)
        move(start, end)
        hanoi(n-1, other, end)
 
def move(start, end):
    print(start, '->', end)

usr_input = int(input('Enter the number of disks: '))

hanoi(usr_input, 1, 3)