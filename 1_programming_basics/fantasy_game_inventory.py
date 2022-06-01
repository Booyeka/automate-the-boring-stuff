


dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12 }


def displayInventory(inventory):
    #takes in inventory outputs formatted inventory
    print('')
    print('Inventory:'.center(15))
    print(''.center(15, '~'))   
    total_items = 0  
    count = 1 
    for k, v in inventory.items(): 
         
        total_items += v
        #print(''.rjust(5), end = '')  
        
        if count == len(inventory):
            print(f'{k}'.ljust(10, '_'), end ='')
            print(f'{v}'.rjust(5, '_'))
            print(''.center(15, '~'))
        else:
            print(f'{k}'.ljust(10, '_'), end ='')
            print(f'{v}'.rjust(5, '_'))
            count += 1
    
    print(f'sum items'.ljust(10, '_'), end = '')
    print(str(total_items).rjust(5, '_'))

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory.update({item: inventory[item]+1})
    return inventory



while True:
    print(
        '1 - Add to inventory\n' 
        '2 - Display inventory\n'
        '3 - Exit'
    )

    action = input()

    if action == '1':
        while True:
            item_list = []
            print('what item do you wish to add? - type "done" when finsihed')
            val = input()
            if val == 'done':
                break
            print('How many?')
            switch = True
            while switch:
                num = input()
                try:
                    int(num)
                    switch = False
                        
                except ValueError:
                    print('Please enter a number')
            
            for i in range(int(num)):
                item_list.append(val)
            add_to_inventory(inventory, item_list)
    elif action == '2':
        displayInventory(inventory)
    else:
        break

