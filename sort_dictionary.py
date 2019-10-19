dics = {"key":"value","ab":"hi there","we":"say what"}


def dic_sorter(dic):
    sorted_dic = {}
    for i in sorted(dic):
        sorted_dic[i] = dic[i]
    return sorted_dic

print(dic_sorter(dics))