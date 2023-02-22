magic_squar=[[1,3,0],
             [1,1,9],
             [0,7,1]]
i=0
sum_row=0
sum_col=0
sum_diagnal=0
while i<len(magic_squar):
    sum_row=sum_row+magic_squar[i][0]
    sum_col=sum_col+magic_squar[i][1]
    sum_diagnal=sum_diagnal+magic_squar[i][2]
    i=i+1
print('total of row 1 =',sum_row)
print('total of row 2 =',sum_col)
print('total of row 3 =',sum_diagnal)
if sum_row==sum_col==sum_diagnal:
    print("it is magic squear")
else:
    print("it is not magic squear")






