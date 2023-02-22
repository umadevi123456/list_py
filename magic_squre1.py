k=[[2,7,6],
[9,5,1],
[4,3,8]]
i=0
while i<len(k):
    j=0
    row=0
    column=0
    diagnoal=0
    while j<len(k[i]):
          row=row+k[i][j]
          column+=k[j][i]
          diagnoal+=k[j][j]
          j=j+1
    n=2
    dia=0
    while n>=0:
        dia+=k[i][n]
        n=n-1
    i=i+1
print(row)
print(column)
print(diagnoal)
print(dia)
if row==column==diagnoal==dia:
    print("magic square")
else:
    print("not a magic square")
    
    

