from tabulate import tabulate

# DISPLAY
def userOptionMenu():
    print('''
    - Fashion Store - 
          
    1. Admin
    2. Customer
    3. Exit
''')

def adminMenu():
    print(
'''
    - Admin Menu -

    1. Display Item
    2. Add Item
    3. Delete Item
    4. Edit Item
    5. Change User
    6. Exit 
''')

def customerMenu():
    print(
'''
    - Customer Menu -

    1. Display Item
    2. Buy
    3. Change User
    4. Exit
''')
    
# DISPLAY DATA
def displayData(data): # Display tabulate with parameter 
    print('\nFashion Stock:')
    headers = ['Index', 'Type', 'Color', 'Size', 'Stock', 'Price']
    formattedData = [(i+1, values['Type'], values['Color'], values['Size'], values['Stock'], values['Price']) for i, values in enumerate(data)]
    print(tabulate(formattedData, headers=headers, tablefmt='grid', stralign='left', numalign='left'))

# DISPLAY CART
def displayCart(): # Display item after adding to cart
    if fashionCart:
        print('\nFashion Cart:')
        headers = ['Type', 'Color', 'Size', 'Qty', 'Price', 'Subtotal']
        formattedData = [(values['Type'], values['Color'], values['Size'], values['Qty'], values['Price'], values['Qty']*values['Price']) for values in fashionCart]
        print(tabulate(formattedData, headers=headers, tablefmt='grid', stralign='left', numalign='left'))
    else:
        print('\nCart Empty.')

# FASHION STOCK DATA
fashionStock = [
    {'Type': 'Shirt', 'Color': 'Red', 'Size': 'S', 'Stock': 10, 'Price': 30000 },
    {'Type': 'Shirt', 'Color': 'Blue', 'Size': 'M', 'Stock': 20, 'Price': 32000 },
    {'Type': 'Shirt', 'Color': 'Red', 'Size': 'L', 'Stock': 15, 'Price': 34000 },
    {'Type': 'Jacket', 'Color': 'White', 'Size': 'S', 'Stock': 10, 'Price': 103000 },
    {'Type': 'Jacket', 'Color': 'Green', 'Size': 'M', 'Stock': 5, 'Price': 110000 },
    {'Type': 'Jacket', 'Color': 'Black', 'Size': 'L', 'Stock': 12, 'Price': 115000 },
    {'Type': 'Pant', 'Color': 'Black', 'Size': 'S', 'Stock': 15, 'Price': 212000 },
    {'Type': 'Pant', 'Color': 'Khaky', 'Size': 'M', 'Stock': 20, 'Price': 220000 },
    {'Type': 'Pant', 'Color': 'Gray', 'Size': 'L', 'Stock': 10, 'Price': 230000 },
]

# CART TABLE
fashionCart = [] # Space for adding item to cart

# FILTER AND SORT MENU
def filterAndSortMenu(): # Filter and short menu 
    print('''
    Filtering and Short Menu :
    1. Filtering
    2. Sorting
    3. Back to Menu
    ''')
    while True:
        filterAndSort = input('Input your choice: ') # Input user for filtering or sorting data  
        if filterAndSort == '1':
            filterStock()
            break
        elif filterAndSort == '2':
            sortStock()
            break
        elif filterAndSort == '3':
            break
        else: print('Invalid choice!')

# FILTERING
def filterStock():
    filteredStock = fashionStock[:]  # Create a copy of the original stock
    
    # Define available filter types for each column
    availableFilters = {
        'Type': set(item['Type'] for item in fashionStock), # Explain this line code use fore ?! Check item in column/keys from fashionStock (Data Collection)
        'Color': set(item['Color'] for item in fashionStock),
        'Size': set(item['Size'] for item in fashionStock)
    }
    
    # Function to prompt user and validate input
    def promptUserFilter(column):
        return input(f"Filter by {column} ({', '.join(availableFilters[column])}) (leave blank to skip): ").capitalize() # User input with option available filters

    # Filter by Type
    filterType = promptUserFilter('Type') # Filtering values in keys Type
    while filterType and filterType not in availableFilters['Type']: # Check the input there exist or not in data, mention twice 'filterType' for make sure that when choose 'leave blank to skip' can run
        print("Invalid input! Please select from the available options.")
        filterType = promptUserFilter('Type')
    if filterType:
        filteredStock = [item for item in filteredStock if item['Type'] == filterType]
    
    # Filter by Color
    filterColor = promptUserFilter('Color')
    while filterColor and filterColor not in availableFilters['Color']:
        print("Invalid input! Please select from the available options.")
        filterColor = promptUserFilter('Color')
    if filterColor:
        filteredStock = [item for item in filteredStock if item['Color'] == filterColor]
    
    # Filter by Size
    filterSize = input("Filter by Size (S/M/L, leave blank to skip): ").upper()
    while filterSize and filterSize not in availableFilters['Size']:
        print("Invalid input! Please select from the available options.")
        filterSize = input("Filter by Size (S/M/L, leave blank to skip): ").upper()
    if filterSize:
        filteredStock = [item for item in filteredStock if item['Size'] == filterSize]
    displayData(filteredStock)

# SORTING
def promptSortOption(): # User input with option available sort (column)
    while True:
        sortOption = input('Sort by (Type/Color/Size/Price/Stock, leave blank to skip): ').capitalize()
        if sortOption in ['Type', 'Color', 'Size', 'Price', 'Stock', '']:  # Valid options
            return sortOption
        else:
            print("Invalid input! Please select from the available options.")

def promptSortOrder():
    while True:
        sortOrder = input('Sort order (Asc/Desc, leave blank for Ascending): ').capitalize() # User input with option available asc / desc
        if sortOrder in ['Asc', 'Desc', '']:  # Valid options
            return sortOrder
        else:
            print("Invalid input! Please select either 'Asc' or 'Desc'.")

def sortStock(): # sort function by column and desc/asc
    sortStock = fashionStock[:]  # Create a copy of the original stock
    sortOption = promptSortOption()
    if not sortOption:  # If user skips sorting
        displayData(sortStock)
        return
    sortOrder = promptSortOrder()
    if sortOption == 'Price' or sortOption == 'Stock':
        sortStock.sort(key=lambda x: x.get(sortOption), reverse=(sortOrder == 'Desc'))
    else:
        sortStock.sort(key=lambda x: x[sortOption], reverse=(sortOrder == 'Desc'))      
    displayData(sortStock)

# ADD ITEM AND UPDATE STOCK
def addStock():
    displayData(fashionStock)
    addType = input('Input item Type: ').capitalize()
    addColor = input('Input Color: ').capitalize()
    while True:
        addSize = input('Input Size (S/M/L): ').upper() # input size by parameter S/M/L
        if addSize in ['S', 'M', 'L']:
            break
        else: print('Size is not valid!')    
    for itemType in fashionStock: # to check if the input (item) already exist then just adding the stock
        if itemType['Type'] == addType and itemType['Color'] == addColor and itemType['Size'] == addSize:
            while True:
                try:
                    addStock = int(input('Input stock (must be greater than 0): '))
                    if addStock > 0:
                        break
                    else:
                        print('Stock must be greater than 0!')
                except ValueError:
                    print('Stock must be a number!')
            itemType['Stock'] += addStock
            print(f'Stock for {addType}, color {addColor}, and size {addSize} has been updated.')
            displayData(fashionStock)
            return
    while True:
        try:
            addStock = int(input('Input stock (must be greater than 0): ')) # input stock to the add new item
            if addStock > 0:
                break
            else:
                print('Stock must be greater than 0!') # handling input 
        except ValueError:
            print('Stock must be a number!')
    while True:
        try:
            addPrice = int(input('Input the price Rp. '))
            if addPrice > 0:
                break
            else:
                print('Price must be greater than 0!') # handling input 
        except ValueError:
            print('Price must be a number!')
    fashionStock.append({'Type': addType, 'Color': addColor, 'Size': addSize, 'Stock': addStock, 'Price': addPrice}) # adding new item to data collection
    print(f"Item {addType},{addColor},{addSize} added to stock.")
    displayData(fashionStock)

# EDIT ITEM STOCK
def editStock():
    while True:
        displayData(fashionStock)
        try:
            editItemIndex = int(input('Input index to edit (0 for back to Menu): '))
            if editItemIndex == 0: # back to menu
                return
            elif 0 < editItemIndex <= len(fashionStock): # option keys to edit 
                item = fashionStock[editItemIndex - 1]
                print("Editing item:")
                print("1. Type:", item['Type'])
                print("2. Color:", item['Color'])
                print("3. Size:", item['Size'])
                print("4. Stock:", item['Stock'])
                print("5. Price:", item['Price'])
                editChoice = input("Enter the number corresponding to the attribute you want to edit (leave blank cancel edit): ")
                if editChoice == '1':
                    newType = input('Input new type: ').capitalize() # edit type
                    item['Type'] = newType
                elif editChoice == '2':
                    newColor = input('Input new color: ').capitalize() # edit color
                    item['Color'] = newColor
                elif editChoice == '3':
                    newSize = input('Input new size (S/M/L): ').upper() # edit size
                    item['Size'] = newSize
                elif editChoice == '4':
                    newStock = int(input('Input new stock (must be greater than or equal to 0): ')) # edit stock
                    if newStock >= 0:
                        item['Stock'] = newStock
                    else:
                        print('Invalid stock value! Please input a non-negative number.') # invalid input
                elif editChoice == '5':
                    newPrice = int(input('Input new price: ')) # edit price
                    if newPrice > 0:
                        item['Price'] = newPrice
                    else:
                        print('Invalid price! Please input a positive number.')
                else:
                    print('Invalid choice!')
                print(f'Item updated: {item}') # notif updated item
            else:
                print('Index is not valid.')
        except ValueError:
            print('Input is not valid.')

# DELETE ITEM STOCK
def deleteStock(): # delete item by index
    while True:
        displayData(fashionStock)
        try: 
            deleteItem = int(input('Input index to delete (0 for back to Menu): '))
            if deleteItem == 0:
                return
            elif 0 < deleteItem <= len(fashionStock):
                deletedType = fashionStock[deleteItem - 1]['Type']
                deletedColor = fashionStock[deleteItem - 1]['Color']
                deletedSize = fashionStock[deleteItem - 1]['Size']
                del fashionStock[deleteItem - 1]
                print(f'Item {deletedType}, color {deletedColor}, and size {deletedSize} removed from stock!')
            else: 
                print('Index is not valid.')
        except:
            print('Input is not valid.')

# BUY ITEM
def addCart():
    while True:
        try:
            displayData(fashionStock)
            addCartIndex = int(input('Input index Type for add into cart (0 for payment, 99 for back to menu): ')) # add item by index to cart
            if addCartIndex == 0: # payment after adding an item to cart
                confirmPayment = input('Payment cant be canceled, want to process payment? (Y/N): ').capitalize() # confirmation payment
                if confirmPayment == 'Y':
                    payment()
                    break
                elif confirmPayment == 'N':
                    break
            elif addCartIndex == 99: # back to customer menu
                break
            elif 0 < addCartIndex <= len(fashionStock): 
                if fashionStock[addCartIndex - 1]['Stock'] == 0: # if stock is zero cant add to cart
                    print("Out of stock.")
                    continue
                itemAmount = int(input('Input amount item: '))
                if 0 < itemAmount <= fashionStock[addCartIndex - 1]['Stock']: # add to cart when item in stock
                    fashionCart.append({
                        'Type': fashionStock[addCartIndex - 1]['Type'],
                        'Color': fashionStock[addCartIndex - 1]['Color'],
                        'Size': fashionStock[addCartIndex - 1]['Size'],
                        'Qty': itemAmount, 
                        'Price': fashionStock[addCartIndex - 1]['Price'],
                        'Subtotal': itemAmount * fashionStock[addCartIndex - 1]['Price']})
                    fashionStock[addCartIndex - 1]['Stock'] -= itemAmount
                    print('\nItem added to Cart.')
                    displayCart()
                else:
                    print("Out of stock.")
            else:
                print("Invalid Index.")
        except ValueError:
            print("Invalid Input.")

# PAYMENT
def calculateTotal():
    total = sum(values['Price'] * values['Qty'] for values in fashionCart)
    return total

def payment():
    if not fashionCart:
        print('Empty cart.')
        return
    displayCart()
    total = calculateTotal()
    print('Total payment Rp.',total)
    while True:
        try:
            money = int(input('Enter amount of money Rp.')) # input payment
            if money < total:
                print('Not enough money.')
            else:
                change = money - total # change payment
                print('Change: ', change)
                fashionCart.clear()
                exit(print('\nThank you! Cart empty.'))
        except ValueError:
            print('Invalid input! Please enter a valid amount.')

# MAIN MENU
def MENU():
    while True:
        userOptionMenu()
        menuM = input('Who are you: ')
        if menuM == '1': loginAdmin()
        elif menuM == '2': CUSTOMER()
        elif menuM == '3': exit('\nThank You! ')
        else: print('Undefined, input correct number !')

# LOGIN
def loginAdmin():
    usernameAdmin = '1'
    passwordAdmin = '1'
    maxAttempts = 3
    attempts = 0
    while attempts < maxAttempts:
        try:
            username = input('Username: ')
            password = input('Password: ')
            if username == usernameAdmin and password == passwordAdmin:
                print('Login Success!')
                ADMIN()
            else:
                print('Login Failed! Wrong password/username!')
                attempts += 1
                if attempts == maxAttempts:
                    print('You have exceeded the number of attempts!')
        except ValueError:
            print('Invalid input! Please enter a valid number.')

# ADMIN
def ADMIN():
    while True:
        adminMenu()
        menuA = input('Input number of menu: ')
        if menuA == '1': 
            displayData(fashionStock)
            filterAndSortMenu()
        elif menuA == '2': addStock()
        elif menuA == '3': deleteStock()
        elif menuA == '4': editStock()
        elif menuA == '5': MENU()
        elif menuA == '6': exit('Thank You!')
        else: print('\nInput correct menu !\n')

# CUSTOMER
def CUSTOMER():
    while True:
        customerMenu()
        menuC = input('Input number of menu: ')
        if menuC == '1': 
            displayData(fashionStock)
            filterAndSortMenu()
        elif menuC == '2': addCart()
        elif menuC == '3': MENU()
        elif menuC == '4': exit(print('Thank You! '))
        else: print('\nInput correct menu !\n')

# MAIN LOOP PROGRAM
MENU()
