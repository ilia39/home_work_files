import pprint as pp


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
        end = False
        while end is not True:
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


pp.pprint(parse_cb_for())