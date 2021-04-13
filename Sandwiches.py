def items_list(*sandwiches):
    print('\nHier sind die bestellten Sandwiches:')
    for sandwich in sandwiches:
        print('-', sandwich)



items_list('Beef Sandwiches', 'Cheese Sandwiches')
items_list('Grilled Cheese Sandwiches', 'Chicken Sandwiches', 'Ham Sandwiches')
items_list('Grilled Cheese Sandwiches', 'Chicken Sandwiches', 'Ham Sandwiches', 'Pork Sandwiches', 'Tuna Sandwiches', 'Turkey Sandwiches')