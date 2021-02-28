board = [[0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]
basket = []

for col in moves:
    for row in range(len(board[0])):
        print(board[row][col-1])
        if board[row][col-1] != 0:
            basket.append(board[row][col-1])
            print(basket)
            board[row][col-1] = 0
            break

i = 0
count = 0
while(i<len(basket)-1):
    if basket[i] == basket[i+1]:
        del(basket[i])
        del(basket[i])
        count += 2
        i=0
        continue
    i += 1

print(count)