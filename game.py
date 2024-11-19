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
        self.backpack = dict() #Storing seeds or crops
    
    def nextDay(self):
        self.day += 1
        
    def gainMoney(self, profit):
        self.money += profit
        
    def expense(self, loss):
        if self.money - loss < 0:
            return False
        else:
            self.money -= loss
            return True
        
    def addTools(self, tool):
        self.tools.append(tool)
        
    def addBackpack(self, item, qty):  # need to be changed
        if not self.backpack.get(item):
            self.backpack[item] = 0
        self.backpack[item] += qty
    
    def stats(self):
        print(f"Money: {self.money}")
        print(f"Tools: {self.tools}")
        print(f"Backpack: {self.backpack}")
        

class Market:
    def __init__(self):
        self.marketDisplay = []
    
    def displayItems(self):
        print(f"====== Available Items in Market ======")
        print()
        print("="*40)
        print("Tools")
        print("-"*40)
        for item in self.marketDisplay:
            if not item.soldOut and item.type == "Tools":
                print(f"{item.name} {item.price}")
        print("="*40)
        print("Seeds")
        print("-"*40)
        for item in self.marketDisplay:
            if item.type == "Seeds":
                print(f"{item.name} {item.price}")
        print("="*40)
    
    def addToMarketDisplay(self, item):
        exist = False
        
        for i in self.marketDisplay:  # Handle whether the object item is already added to display or not
            if i.name == item.name:
                exist = True
                
        if not exist:
            self.marketDisplay.append(item)
    
    def buyItem(self):
        name = str(input("What do you want to buy?")).lower()
        
        exist = False
        for item in self.marketDisplay:
            if item.name.lower() == name:
                exist = item
                break

        print()
        if exist:
            if item.type == "Tools":
                if user.expense(exist.price):
                    item.soldOut = True # Tool only can be bought once
                    user.addTools(exist.name)
                    print("Purchased")
                else:
                    print("Not enough money")
                
            elif item.type == "Seeds":
                qty = int(input("How many seeds do you want to buy?"))
                if user.expense(exist.price * qty):
                    user.addBackpack(exist.name, qty)
                    print("Purchased")
                else:
                    print("Not enough money")
        
        else:
            print(f"Item not found")

class MarketItems: # Succesful
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type
        self.soldOut = False

class UpcomingItems: # Succesful
    def __init__(self):
        # (name, price, type, unlockedAtDay)
        self.upcoming = [
            ("Watering Can", 100, "Tools", 0), 
            ("Hoe", 100, "Tools", 0), 
            ("Corn seeds", 20, "Seeds", 0),
            ("Sickle", 20, "Tools", 0),
            ("Tomato seeds", 30, "Seeds", 0),
            ("Wheat seeds", 10, "Seeds", 0)
        ]
    
    def validUpcomingObj(self):
        for item in self.upcoming:
            if item[3] == user.day:
                marketItem = MarketItems(item[0], item[1], item[2])
                market.addToMarketDisplay(marketItem)

class Farm: # Succesful but unfinished
    def __init__(self):
        self.land = []
    
    def displayFarm(self):
        for row in self.land:
            for col in row:
                if col.readyToHarvest:
                    if col.type == "Corn":
                        print(f"[ 🌽 ]", end=" ")
                    elif col.type == "Tomato":
                        print(f"[ 🍅  ]", end=" ")
                    elif col.type == "Wheat":
                        print(f"[ 🌾  ]", end=" ")
                elif col.growing:
                    print(f"[ 🌱 ]", end=" ")
                elif not col.planted:
                    print(f"[ 🟤 ]", end=" ")
            print()
    
    def plant(self):
        pass
    
    def harvest(self):
        pass
    
    def removePlant(self):
        pass
    
    def waterPlant(self):
        for row in self.land:
            for col in row:
                if planted:
                    col.dayWater += 1

class Square:
    def __init__ (self):
        self.readyToHarvest = False
        self.planted = False
        self.growing = False
        self.dayWater = 0
        self.plantType = None

class MainProgram: # Succesful but unfinished
    def __init__(self):
        pass
    
    def menu(self):
        print("Menu")
        print("=" * 40)
        print("1. Check backpack 🎒")
        print("2. Go to Market 🛒")
        print("3. Go to Farm 🏡")
        print("4. Sell crops 💰")
        print("5. Call the day 🛏️")
        print("=" * 40)
        print(f"Current Day: {user.day}")
    
    def menuOption(self):
        op = int(input("Menu Option ( 1 / 2 / 3 / 4 / 5 ): "))
        cls()
        if op == 1:
            user.stats()
        
        elif op == 2:
            market.displayItems()
            market.buyItem()
            
        elif op == 3:
            print("Farm")
            print("=" * 40)
            farm.displayFarm()
            print("="*40)
            print("1. Plant")
            print("2. Water")
            print("3. Harvest")
            print("4. Remove")
            print("5. Nothing")
            print("="*40)
            to_do = str(input("What do you want to do? "))
            
            if to_do == 1:
                farm.plant()
            
            elif to_do == 2:
                farm.water()
            
            elif to_do == 3:
                farm.harvest()
            
            elif to_do == 4:
                farm.removePlant()
            
            elif to_do == 5:
                pass
        
        elif op == 4:
            pass
        
        elif op == 5:
            print("Good job for today. Let's work harder tomorrow!")
            user.nextDay()
            upcomingItems.validUpcomingObj()
        
        print()


user = User()
main = MainProgram()
farm = Farm()
upcomingItems = UpcomingItems()
market = Market()

square = Square() # For making farm square
for i in range (5):
    row = []
    for j in range (5):
        row.append(square)
    farm.land.append(row)

upcomingItems.validUpcomingObj()

while True:
    cls()
    main.menu()
    main.menuOption()
    enter = str(input("[ ENTER ] to continue"))
