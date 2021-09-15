import os

file_path = os.path.join(os.getcwd(), 'recipes.txt')

def create_dict (file_name: str) -> dict:
    result: dict = dict()
    with open (file_name) as file:
        for line in file:
            dishes_name = line.strip()
            records_quantity = int(file.readline())
            ingredients_list = []
            for ingredients in range (records_quantity):
                ingredient_name, quantity, measure = file.readline().split('|')
                ingredients_list.append (
                    {'ingredient_name': ingredient_name, 'quantity': int (quantity), 'measure': measure}
                )
                result[dishes_name] = ingredients_list
                file.readline()
        return result


result_dict = create_dict (file_path)
create_dict(result_dict)
   
