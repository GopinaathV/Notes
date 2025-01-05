
def dict_merger(d1,d2):
    merger = {}
    all_keys = set(d1.keys()).union(d2.keys())
    for key in all_keys:
        if key in d1 and key in d2 and isinstance(d1[key],dict) and isinstance(d2[key],dict):
            merger[key] = dict_merger(d1[key],d2[key])
        elif key in d2 and key not in d1:
            merger[key] = d2[key]
        elif key in d1 and key not in d2:
            merger[key] = d1[key] 
        else:
            merger[key] = d1[key] + d2[key]               
    return merger            

def dict_flatten(d1):
    flatten = {}
    for key in data:
        print(f'{d1,d1[key]}')
        if isinstance(d1[key],dict): 
            flatten[key] = dict_flatten(d1[key])
        else:
            flatten[key] = d1[key]    
    return flatten        

def flatten_list(lt):
    flt = []
    for ele in lt:
        if isinstance(ele,list):
            flt.extend(flatten_list(ele))
        else:
            flt.append(ele) 
    return flt        

def generator():
    yield 1
    yield 2
    yield 3    

if __name__ == '__main__':
    # Combining two dict 
    # d1 = {'a':{'x':1,'y':2,'z':3},'b':3,'c':2}
    # d2 = {'a':{'z':3,'w':5},'b':3,'d':2}
    # output = {'a':{'x':1,'y':2,'z':6,'w':5},'b':6,'c':2,'d':2}
    # print(dict_merger(d1,d2))
    
    # Flatting a dict
    # data = {'a':{'x':1,'y':{'z':5}},'b':5}
    # print(dict_flatten(data))
    
    # Flatting a list    
    # data = [1,2,3,[4,5,[6,7,[8,9,[10]]]]]
    # print(flatten_list(data))

    # n = 3
    # mat = []
    # for i in range(3):
    #    ele = list(map(int,input().split()))  
    #    mat.append(ele)
    # print(mat)   
    
    # lt = [10,10,10,20,30,10,10,40]
    # prev = lt[0]
    # op = []
    # for i in lt[1:]:
    #    if i != prev:
    #        op.append(prev)
    #        prev = i 
    
    # print(op)

    #Generator 
    # gen = generator()
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))

    set1 = set([1,2,3,4])
    set2 = set([5,6,7,4])
    set3 = set([3,4,5,6])
    common = set1 & set2 & set3 
    print(common)
