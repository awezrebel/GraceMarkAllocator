arr=[[0,0,0],[0,1,0],[0,1,1]]
ans=0


def grid(i,j):
    if(i==2):
        return 1
    elif(arr[i+1][j]==0):
        grid(i+1,j)
    elif(j!=0 and arr[i][j+1]==0):
        grid(i,j+1)
    elif(j!=2 and arr[i][j-1]==0):
        grid(i,j-1)
    else:
        return 0

ans=grid(0,1)


print(ans)
