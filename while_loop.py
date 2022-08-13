# i =0
# while  i< 50:
#     if(i == 30):
#         print(i)
#         break
#     i+=1

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for i in picture:
    for j in i:
        if j:
            print('*',end='')
        else:
            print(' ',end='')
    print('')