import os
import pprint as pp


def concatenate_files():
    tree = os.walk('.')
    file_list = []
    for element in tree:
        if element[0] == '.':
            for file in element[2]:
                if file[-4:] == '.txt':
                    file_list += [file]
        else:
            break
    file_list.remove('cook_book.txt')
    file_list.remove('res_file.txt')
    res_file = os.path.join(os.getcwd(), 'res_file.txt')
    with open(res_file, 'w') as clearer:
        clearer.write('')
    list_by_lines_count = []
    for file in file_list:
        path = os.path.join(os.getcwd(), file)
        with open(path) as line_getter:
            line_count = 0
            for line in line_getter:
                line_count += 1
        list_by_lines_count.append([line_count, file])
    list_by_lines_count.sort()
    for file_info in list_by_lines_count:
        with open(res_file, 'a') as to_file:
            to_file.writelines([(file_info[1] + '\n'), (str(file_info[0]) + '\n')])
            with open(os.path.join(os.getcwd(), file_info[1])) as from_file:
                to_file.write(from_file.read())
                to_file.write('\n')


def parse_cb_for():
    with open('cook_book.txt', 'r') as cook_book:
        res_dict = {}
        go_do = 0
        is_iter = False
        for recipe in cook_book:
            if go_do > 0:
                recipe_list = recipe.strip().split(sep=' | ')
                res_dict[cur_key] += [{'ingredient_name': recipe_list[0],
                                       'quantity': recipe_list[1], 'measure': recipe_list[2]}]
                go_do -= 1
            elif go_do == 0 and recipe != '\n' and is_iter is False:
                cur_key = recipe.strip()
                res_dict.update({cur_key: []})
                is_iter = True
            elif recipe == '\n':
                continue
            elif is_iter is True:
                go_do = int(recipe.strip())
                is_iter = False
    return res_dict


def parse_cb_while():
    with open('cook_book.txt', 'r') as cook_book:
        res_dict = {}
        while True:
            name = cook_book.readline().strip()
            res_dict.update({name: []})
            cook_book.readline()
            line = cook_book.readline()
            while line != '\n' and line != '':
                recipe_list = line.strip().split(sep=' | ')
                res_dict[name] += [{'ingredient_name': recipe_list[0],
                                    'quantity': recipe_list[1], 'measure': recipe_list[2]}]
                line = cook_book.readline()
            if line == '':
                break
    return res_dict


def get_shop_list_by_dishes(dishes, person_count):
    if person_count == 0:
        return 'ничего покупать не надо'
    shop_list = {}
    cook_book = parse_cb_for()
    for dish in dishes:
        if cook_book.get(dish) is None:
            print(f'Блюдо "{dish}" отсутствует в книге рецептов')
        else:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] = \
                        shop_list[ingredient['ingredient_name']]['quantity'] \
                        + int(ingredient['quantity']) * person_count
                else:
                    shop_list.update({ingredient['ingredient_name']:
                                          {'measure': ingredient['measure'],
                                           'quantity': int(ingredient['quantity']) * person_count}})
    return shop_list


parsed_cook_book = parse_cb_for()
# parsed_cook_book = parse_cb_while()
pp.pprint(parsed_cook_book)
shop_list = get_shop_list_by_dishes(['Запеченный картофель',
                                     'Утка по-пекински', 'санкционная фуагра'], 0)
pp.pprint(shop_list)
concatenate_files()