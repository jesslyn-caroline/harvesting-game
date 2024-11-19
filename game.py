from os import system, name

def cls():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

class User:
    def __init__(self):
        self.day = 0
        self.money = 500
        self.tools = []
        self.backpack = []
    
    def nextDay(self):
        self.day += 1
        
    def gainMoney(self, profit):
        self.money += profit
        
    def expense(self, loss):
        if self.money - loss < 0:
            return False
        else:
            print(loss)
            self.money -= loss
            return True
        
    def addTools(self, tool):
        self.tools.append(tool)
        
    def addBackpack(self, item):  # need to be changed
        self.backpack.append(item)
    
    def stats(self):
        print(f"Money: {self.money}")
        print(f"Tools: {self.tools}")
        print(f"Backpack: {self.backpack}")
        

class Market:
    def __init__(self):
        self.marketDisplay = []
    
    def displayItems(self):
        for item in self.marketDisplay:
            if not item.soldOut:
                print(f"{item.name} | {item.price} | {item.type}")
    
    def addToMarketDisplay(self, item):
        exist = False
        
        for i in self.marketDisplay:  # Handle whether the object item is already added to display or not
            if i.name == item.name:
                exist = True
                
        if not exist:
            self.marketDisplay.append(item)
    
    def buyItem(self, name):
        exist = False
        for item in self.marketDisplay:
            if item.name.lower() == name:
                exist = item
                break
                
        if exist:
            user.expense(exist.price)
            if item.type == "Tools":
                if user.expense(exist.price):
                    item.soldOut = True # Tool only can be bought once
                    user.addTools(exist.name)
                else:
                    print("Not enough money")
                
            elif item.type == "Seeds":
                pass
                # qty = int(input("How many seeds do you want to buy?"))
                # if user.expense(exist.price * qty):
                #     user.addBackpack([exist.name, qty])
                # else:
                #     print("Not enough money")

class MarketItems: # successful
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type
        self.soldOut = False

class UpcomingItems: # successful
    def __init__(self):
        # (name, price, type, unlockedAtDay)
        self.upcoming = [
            ("Watering Can", 100, "Tools", 0), 
            ("Hoe", 100, "Tools", 0), 
            ("Corn seeds", 20, "Seeds", 0),
            ("Sickle", 20, "Tools", 0),
            ("Turnip seeds", 10, "Seeds", 0),
            ("Tomato seeds", 30, "Seeds", 3),
            ("Wheat seeds", 10, "Seeds", 3)
        ]
    
    def validUpcomingObj(self):
        for item in self.upcoming:
            if item[3] == user.day:
                marketItem = MarketItems(item[0], item[1], item[2])
                market.addToMarketDisplay(marketItem)

class Farm: # successful but unfinished
    def __init__(self):
        self.land = [[f"[ {'🌱'} ]" for i in range(5)] for j in range(5)]
    
    def displayFarm(self):
        print("Farm")
        print("=" * 40)
        for row in self.land:
            for col in row:
                print(col, end=" ")
            print()

class MainProgram: # successful but unfinished
    def __init__(self):
        pass
    
    def menu(self):
        print("Menu")
        print("=" * 40)
        print("1. Check backpack")
        print("2. Go to Market")
        print("3. Go to Farm")
        print("4. Call the day")
        print("=" * 40)
        print(f"Current Day: {user.day}")
    
    def menuOption(self):
        op = int(input("Menu Option ( 1 / 2 / 3 / 4 ): "))
        cls()
        if op == 1:
            user.stats()
        
        elif op == 2:
            print(f"1. Buy Item")
            print(f"2. Sell Item")
            to_do = int(input("What would you like to do? ( 1 / 2 )"))
            if to_do == 1:
                market.displayItems()
                itemToBuy = str(input("What do you want to buy?")).lower()
                market.buyItem(itemToBuy)
            elif to_do == 2:
                pass
            
        elif op == 3:
            farm.displayFarm()
            
        elif op == 4:
            print("Good job for today. Let's work harder tomorrow!")
            user.nextDay()
        
        print()

user = User()
main = MainProgram()
farm = Farm()
upcomingItems = UpcomingItems()
market = Market()

while True:
    cls()
    upcomingItems.validUpcomingObj()
    main.menu()
    main.menuOption()
    enter = str(input("[ ENTER ] to continue"))
