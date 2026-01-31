N = 8

def print_board(b):
    for i in range(N):
        for j in range(N):
            print("Q" if b[i][j]==1 else ".", end=" ")
        print()
    print()

def safe(b,r,c):
    for i in range(c):
        if b[r][i]==1:
            return False
    i,j=r,c
    while i>=0 and j>=0:
        if b[i][j]==1:
            return False
        i-=1; j-=1
    i,j=r,c
    while i<N and j>=0:
        if b[i][j]==1:
            return False
        i+=1; j-=1
    return True

def solve(b,c):
    if c==N:
        print_board(b)
        return True
    for r in range(N):
        if safe(b,r,c):
            b[r][c]=1
            solve(b,c+1)
            b[r][c]=0

board=[[0]*N for _ in range(N)]
solve(board,0)
