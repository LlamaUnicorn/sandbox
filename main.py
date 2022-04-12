censored = ['news', 'stupid']

news_title = 'Breaking news! Some stupid president does unthinkable!'

split_title_special_chars = news_title.split()
print('split_title_special_chars:', split_title_special_chars)
split_title_comprehension = [j.strip('.,!?:;').lower() for j in split_title_special_chars]
print('no special chars split:', split_title_comprehension)
# split_title_comprehension2 = [[j.strip('.,').lower() for j in i] for i in news_title]
# print('list comprehension: ', news_title)
# print(type(split_title_comprehension2))
# print(split_title_comprehension[0])

# print('this is split_title: ', split_title)
for word in split_title_comprehension:
    if word in censored:
        list_word = list(word)
        print(list_word)
        censored_list_word = '*' * len(list_word)
        # word = '*' * len(list_word)
        word = censored_list_word
        print(word)

# censored_title = [list(word) for word in split_title_comprehension]
print('this is censored:', split_title_comprehension)

# How to change the original list after censoring with *?


# name = 'Ben'
# word = list(name)
# print(word)
# word = '*' * len(name)
# print(word)


# l = [ ['Hello.', 'My', 'World,'] ]
# res = [[j.strip('.,').lower() for j in i] for i in l]
# print(res)