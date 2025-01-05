
def merge_sort(lt):
    if len(lt)<=1:
        return lt
    mid = len(lt)//2
    left = merge_sort(lt[:mid])
    right = merge_sort(lt[mid:]) 
    res = []
    i = j = 0

    while(i < len(left) and j < len(right)):
        if  left[i] < right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res    


if __name__ == '__main__':
    lt = [10,4,5,3,11,2,6]  
    print(merge_sort(lt))



