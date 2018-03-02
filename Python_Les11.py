import json
import chardet
import operator


def open_file(file_json):
    with open(file_json, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
    with open(file_json, encoding=result['encoding']) as f:
        result = json.load(f)
        result_list = []
        i = 0
        while i < len(result['rss']['channel']['items']):
            result_list.append(result['rss']['channel']['items'][i]['description'])
            i += 1
        return result_list


def list_to_dict(txt_list):
    i = 0
    dict_word = {}
    while i < len(txt_list):
        j = 0
        for len_word in txt_list:
            if txt_list[i] == len_word:
                j += 1
        dict_word[txt_list[i]] = j
        i += 1
    return dict_word


def max_word(new_dict):
    sorted_dict = sorted(new_dict.items(), key=operator.itemgetter(1))
    sorted_dict.reverse()
    i = 0
    while i < 10:
        print('Слово:', sorted_dict[i][0], 'количество повторов:', sorted_dict[i][1])
        i += 1


def search_word(file_name):
    result = open_file(file_name)
    list_file = result[0].split(' ')
    list_file.sort()
    new_list = []
    for word in list_file:
        if len(word) > 6:
            new_list.append(word)
    new_dict = list_to_dict(new_list)
    print(file_name)
    max_word(new_dict)


search_word('newsafr.json')
search_word('newscy.json')
search_word('newsfr.json')
search_word('newsit.json')
