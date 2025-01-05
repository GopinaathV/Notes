def bubble_sort(lt):
    for i in range(len(lt)):
        for j in range(i):
            if lt[i]<lt[j]:
                lt[i],lt[j] = lt[j],lt[i]
    return lt             

if __name__ == '__main__':
    lt = [23,10,4,20,10,20,30]
    print(bubble_sort(lt)) 