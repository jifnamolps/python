list=[1,2,3,4,5,6,7,8,9,10,9]
n=9

def search(list,n):
 i=0
 while(i<len(list)):
    if list[i]==n:
      return True
    i=i+1

    return False
if search(list,n):
  print("found")
else:
  print('not found')
 

