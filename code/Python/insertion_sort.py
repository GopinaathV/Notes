def insertion_sort(lt):
   for i in range(1,len(lt)):
      key = lt[i]
      j = i-1
      print(lt)
      while(j>=0 and key<lt[j]):
         lt[j+1] = lt[j]
         j-=1
      lt[j+1] = key   
   return lt 


if __name__ == '__main__':
   lt =[23,1,10,5,2]
   print(insertion_sort(lt))
