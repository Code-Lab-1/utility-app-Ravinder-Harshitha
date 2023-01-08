#Vending Machine using Python
#This python program uses "pandas"

import pandas as pd
txt = "\033[31m WELCOME TO ALL-IN-ONE VENDING MACHINE\033[0m"
x = txt.center(75)
print(x)

#Desirable amount of money is entered in the input prompt given below
print('\033[33m-------------------------------------------------------------------------\033[0m')
g= int(input("Please enter the amount of money you'd like to insert: "))
print('\033[33m-------------------------------------------------------------------------\033[0m')
sum=0

#Another prompt appears that should be answered with yes(y) or no(n)
while True:
    j=input("\nDo u wish to continue with your selection? (y/n): ")
    if j=='y':
        print('\033[33m-------------------------------------------------------------------------\033[0m')
        txt = "\033[31mLIST\033[0m"
        x = txt.center(75)
        print(x)
        
        #The first list displays the categories of products available in the vending machine.
        print('\033[33m-------------------------------------------------------------------------\033[0m')
        print('\n\033[36m 1. Refreshments \n 2. Beverages \n 3. Snacks \n 4. Fast Food \n\033[0m  ')
        n=int(input('\nEnter your choice from the following categories given in the list:  '))
        print('\033[33m-------------------------------------------------------------------------\033[0m')
        
        #After choosing from the list above, a particular list of products appear with their serial number, names, price and availability in stock 
        if n==1:
            print('\n\033[36mThe products available in Refreshments are:\033[0m')
            print(' ')
            df=pd.DataFrame({'Name of the Item':["Water","Orange Juice","Chocolate Milkshake","Iced Tea","Iced Coffee"],'Price(per item)':[1,1,2,4,5],"In Stock(per pc)":[5,4,5,6,7]},index=[1,2,3,4,5])
            print(df)
            #To choose an particular item, its adjacent serial number should be entered
            z=int(input('\nEnter the serial number of the product of your choice: '))
            print(' ')
            x=pd.Series(df.loc[z])
            #Then the number of items purchased should be entered
            v_quan = int(input("Enter the number of items required: "))
            print(' ')
            #After the selection, the total amount is calculated
            m=(x['Price(per item)']*v_quan)
            sum=sum+m
            print(x)
            #Later, the code shows what item and how many items has been ordered and it also gives suggestions to check out other items in the vending machine
            print("\nYou've ordered",v_quan, x['Name of the Item'])
            print(v_quan, x['Name of the Item'], "has been dispensed.")
            print('\n\033[34mRefreshments energize us when combined with a delicious snack.\033[0m')
            print('\033[34mCheck out our collection of snacks by selecting "3" from the list!\033[0m')
        elif n==2:
            print('\n\033[36mThe products available in Beverages are:\033[0m')
            print(' ')
            df=pd.DataFrame({'Name of the Item':['Coca Cola','Redbull Energydrink','Pepsi','Sprite','Mountain Dew'],'Price(per item)':[3,5,4,4,2],'In Stock(per pc)':[7,8,9,5,2]},index=[1,2,3,4,5])
            print(df)
            #To choose an particular item, its adjacent serial number should be entered
            z=int(input('\nEnter the serial number of the product of your choice: '))
            print(' ')
            x=pd.Series(df.loc[z])
            #Then the number of items purchased should be entered
            v_quan = int(input("Enter the number of items required: "))
            print(' ')
            #After the selection, the total amount is calculated
            m=(x['Price(per item)']*v_quan) 
            sum=sum+m
            print(x)
            #Later, the code shows what item and how many items has been ordered and it also gives suggestions to check out other items in the vending machine
            print("\nYou've ordered",v_quan, x['Name of the Item'])
            print(v_quan, x['Name of the Item'], "has been dispensed.")
            print('\n\033[34mPair your beverage with a quick and tasty fast\033[0m')
            print('\033[34mfood item by selecting "4" from the list!\033[0m')
        elif n==3:
            print('\n\033[36mThe products available in Snacks are:\033[0m')
            print(' ')
            df=pd.DataFrame({'Name of the Item':['Lays Chips','Chocochip Cookies','Chocolate Muffin','Trident Gum','Doritos'],'Price(per item)':[2,3,2,1,5],'In Stock(per pc)':[8,7,4,5,6]},index=[1,2,3,4,5])
            print(df)
            #To choose an particular item, its adjacent serial number should be entered
            z=int(input('\nEnter the serial number of the product of your choice: '))
            print(' ')
            x=pd.Series(df.loc[z])
            #Then the number of items purchased should be entered
            v_quan = int(input("\nEnter the number of items required: "))
            print(' ')
            #After the selection, the total amount is calculated
            m=(x['Price(per item)']*v_quan)
            sum=sum+m
            print(x)
            #Later, the code shows what item and how many items has been ordered and it also gives suggestions to check out other items in the vending machine
            print("\nYou've ordered",v_quan, x['Name of the Item'])
            print(v_quan, x['Name of the Item'], "has been dispensed.")
            print('\n\033[34mSnack in and grab a refreshment along by\033[0m')
            print('\033[34mselecting "1" in the list!\033[0m')
        elif n==4:
            print('\n\033[36mThe products available in Fast Food are:\033[0m')
            print(' ')
            df=pd.DataFrame({'Name of the Item':['Chicken Sandwich','Cheese Burger','Hot Dog','Pizza Slice','Lunch Box'],'Price(per item)':[4,5,2,1,5],'In Stock(per pc)':[4,5,8,3,9]},index=[1,2,3,4,5])
            print(df)
            #To choose an particular item, its adjacent serial number should be entered
            z=int(input('\nEnter the serial number of the product of your choice: '))
            print(' ')
            x=pd.Series(df.loc[z])
            #Then the number of items purchased should be entered
            v_quan = int(input("\nEnter the number of items required: "))
            print(' ')
            #After the selection, the total amount is calculated
            m=(x['Price(per item)']*v_quan)
            sum=sum+m
            print(x)
            #Later, the code shows what item and how many items has been ordered and it also gives suggestions to check out other items in the vending machine
            print("\nYou've ordered",v_quan, x['Name of the Item'])
            print(v_quan, x['Name of the Item'], "has been dispensed.")
            print('\n\033[34mCombine your fast food with cool beverages by\033[0m')
            print('\033[34mselecting "2" from the list to keep you going!\033[0m')
        else:
            print('Enter input from the above choices only')
    else:
        #Finally, the total cost of the items purchased is displayed under 'FINAL CONFIRMATION'
        print("\n\033[32m*************** FINAL CONFIRMATION ***************\033[0m")
        print('\nYour total cost for all the items will be:',sum)
        print("Your balance is:", g-sum)
        print('\nCollect your items from the slot below.')
        print('Thank you, have a nice day!')
        print('And do not forget to take the remaining change!')
        print(' ')
        print('\033[33m-------------------------------------------------------------------------\033[0m')
        print('\033[33m-------------------------------------------------------------------------\033[0m')
        break