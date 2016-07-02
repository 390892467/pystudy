str = 'How are    you.'
print(str)
str_lst = str.split(" ")
print(str_lst)
str_lst_new =  [s for s in str_lst if s != ""]
print(str_lst_new)
new_str = " ".join(str_lst_new)
print(new_str)