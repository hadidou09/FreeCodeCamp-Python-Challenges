** start of main.py **

def array_diff(arr1, arr2): 
   diff = list()
   for i in arr1:
       if i not in arr2:
           diff.append(i)
       else:
           continue
   for k in arr2:
       if k not in arr1:
           diff.append(k)
       else:
           continue

   diff = sorted(diff)
   
   return diff
            





** end of main.py **

