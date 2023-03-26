import requests 

def get_name_list():
    result = requests.get('https://gist.githubusercontent.com/akarca/fd99fea898db82dc39c41d03d68c93b8/raw/db67136bf7431be047a2faaef95eff5bd5df2f03/isimler')
    name_list = result.text.split()
    return name_list

def quicksort(name_list):
    if len(name_list) <= 1:
        return name_list

    pivot = name_list[0]
    less = []
    equal = []
    greater = []

    for name in name_list:
        if name < pivot:
            less.append(name)
        elif name == pivot:
            equal.append(name)
        else:
            greater.append(name)

    final_list = []
    for name in quicksort(less) + equal + quicksort(greater):
        if name not in final_list:
            final_list.append(name)
    
    return final_list

def chr_index():
    ascii_uppercase = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    d = {}
    for x in range(len(ascii_uppercase)):
        d[ascii_uppercase[x]] = x+1
        
    return d 


def total_score(final_list):
    alph_index = chr_index()
    total_score_out = 0 
    
    for name in final_list:
        name_index = final_list.index(name)+1
        total_length = 0
        for chr in name :
            total_length += alph_index[chr]
        total_score_out += (total_length*name_index)
        
    print(f"Skor Toplamları  :{total_score_out}")


name_list = get_name_list()
sorted_list = quicksort(name_list)

#print(sorted_list)
total_score(sorted_list)


