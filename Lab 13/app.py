from typing import List

def bubble(list: List[str]) -> List[str]:
    for x in range(len(list)):
        for y in range(len(list)-1):
            if(len(list[y])>len(list[y+1])):
                tmp = list[y]
                list[y] = list[y+1]
                list[y+1] = tmp
            
    return list