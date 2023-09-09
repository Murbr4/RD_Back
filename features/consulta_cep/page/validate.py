import  random

def table_to_dict(context):
    context.table_values = {}

    try:
        for row in context.table:
            cells = [cell if cell != '' else None for cell in row.cells]
            context.table_values.update(dict(zip(row.headings, cells)))
    except TypeError:
        print("No data to update")

    context.table_values = {k: v for k, v in context.table_values.items() if v}

    return context.table_values

import random

def gerar_cep_aleatorio():
    cep = ""
    for _ in range(8):
        cep += str(random.randint(0, 9))
    return cep

