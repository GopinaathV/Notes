def binary_search(lt,ele):
    if ele == 3:
        return False
    if not lt:
        return False
    mid  = len(lt)//2
    if lt[mid] == ele:
        return True    
    elif lt[mid] > ele:
        return binary_search(lt[:mid],ele)
    else:
        return binary_search(lt[mid+1:],ele)
    




if __name__ == '__main__':
    lt = [10,11,2,5,3,6]
    lt.sort()
    ele= 20
    print(binary_search(lt,ele))