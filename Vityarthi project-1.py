# Data provided by the user
L = [["lamborghini", "urus s", 2024, 237848.0],
    ["lamborghini", "revuelto", 2024, 604363.0],
    ["lamborghini", "huracan", 2024, 285000.0],
    ["lamborghini", "countach", 2024, 2640000.0],
    ["lamborghini", "essenza", 2024, 3751988.0],
    ["mercedes benz", "senna", 2018, 7638461.0],
    ["mercedes benz", "maybach", 2023, 398809.0],
    ["mercedes benz", "cabriolet", 2022, 132530.0],
    ["mercedes benz", "limousine", 2023, 55421.0],
    ["mercedes benz", "cabriolet", 2021, 132530.0],
    ["bmw", "x3", 2019, 87349.0],
    ["bmw", "x5", 2021, 116867.0],
    ["bmw", "x7", 2023, 156626.0],
    ["bmw", "i7", 2022, 301204.0],
    ["bmw", "m4", 2018, 227710.0],
    ["honda", "amaze", 2018, 8674.0],
    ["honda", "city", 1981, 13132.0],
    ["honda", "accord hybrid", 2018, 59590.0],
    ["honda", "civic", 2020, 26927.0],
    ["honda", "elevate", 2023, 14084.0],
    ["tata", "tigor", 2024, 7228.0],
    ["tata", "curvv", 2019, 15662.0],
    ["tata", "nexon", 2024, 10843.0],
    ["tata", "punch", 2024, 9518.0],
    ["tata", "harrier", 2024, 22891.0],
    ["toyota", "innova", 2023, 24096.0],
    ["toyota", "fortuner", 2024, 39759.0],
    ["toyota", "vellfire", 2022, 146987.0],
    ["toyota", "camry", 2023, 29342.0],
    ["toyota", "land cruiser", 2024, 134000.0],
    ["rolls royce", "ghost", 2020, 113841.0],
    ["rolls royce", "phantom", 2024, 135455.0],
    ["rolls royce", "cullinan", 2021, 144578.0],
    ["rolls royce", "spectre", 2019, 420000.0],
    ["rolls royce", "boat tail", 2021, 2800000.0],
    ["maruti", "swift", 2024, 10843.0],
    ["maruti", "vitara breeza", 2024, 13843.0],
    ["maruti", "ertiga", 2024, 15662.0],
    ["maruti", "fronx", 2024, 14785.0],
    ["maruti", "scross", 2023, 15643.0]]
def search():
    b=input('enter the brand:')
    m=input('enter the model:')
    fl=0
    brand=b.lower()
    model=m.lower()
    for i in L:
        if i[0]==brand and i[1]==model:
            print(i)
            fl=1
            x=input('if you want to know more type yes to get the link or no:')
            k=x.lower()
            if k=='yes':
                if brand=='maruti' and model=='swift':
                    print('https://www.carwale.com/maruti-suzuki-cars/swift/')
                elif brand=='maruti' and model=='vitarabreeza':
                    print('https://www.carwale.com/maruti-suzuki-cars/brezza/')
                elif brand=='maruti' and model=='ertiga':
                    print('https://www.carwale.com/maruti-suzuki-cars/ertiga/')
                elif brand=='maruti' and model=='fronx':
                    print('https://www.carwale.com/maruti-suzuki-cars/fronx/')
                elif brand=='maruti' and model=='scross':
                    print('https://www.carwale.com/maruti-suzuki-cars/s-cross/')
                elif brand=='bmw' and model=='x3':
                    print('https://www.carwale.com/bmw-cars/x3/')
                elif brand=='bmw' and model=='x5':
                    print('https://www.carwale.com/bmw-cars/x5/')
                elif brand=='bmw' and model=='x7':
                    print('https://www.carwale.com/bmw-cars/x7/')
                elif brand=='bmw' and model=='i7':
                    print('https://www.carwale.com/bmw-cars/i7/')
                elif brand=='bmw' and model=='m4':
                    print('https://www.carwale.com/bmw-cars/m4/')
                elif brand=='toyoto' and model=='innova':
                    print('https://www.carwale.com/toyota-cars/innova-crysta/')
                elif brand=='toyoto' and model=='fortuner':
                    print('https://www.carwale.com/toyota-cars/fortuner-legender/')
                elif brand=='toyoto' and model=='vellfire':
                    print('https://www.carwale.com/toyota-cars/vellfire/')
                elif brand=='toyoto' and model=='camry':
                    print('https://www.carwale.com/toyota-cars/camry/')
                elif brand=='toyoto' and model=='landcruiser':
                    print('https://www.carwale.com/toyota-cars/land-cruiser/')
                elif brand=='rollsroyce' and model=='ghost':
                    print('https://www.cardekho.com/carmodels/Rolls-Royce/Rolls-Royce_Ghost')
                elif brand=='rollsroyce' and model=='phantom':
                    print('https://www.cardekho.com/carmodels/Rolls-Royce/Rolls-Royce_Phantom')
                elif brand=='rollsroyce' and model=='cullinan':
                    print('https://www.cardekho.com/rolls-royce/cullinan')
                elif brand=='rollsroyce' and model=='spectre':
                    print('https://www.cardekho.com/rolls-royce/spectre')
                elif brand=='rollsroyce' and model=='dawn':
                    print('https://www.cardekho.com/rolls-royce/dawn')
                elif brand=='tata' and model=='tigor':
                    print('https://cars.tatamotors.com/tigor/ice.html')
                elif brand=='tata' and model=='curvv':
                    print('https://www.carwale.com/tata-cars/curvv/')
                elif brand=='tata' and model=='nexon':
                    print('https://www.carwale.com/tata-cars/nexon/')
                elif brand=='tata' and model=='punch':
                    print('https://www.cardekho.com/tata/punch')
                elif brand=='tata' and model=='harrier':
                    print('https://www.carwale.com/tata-cars/harrier/')
                elif brand=='lamborghini' and model=='urus':
                    print('https://www.carwale.com/lamborghini-cars/urus-s/')
                elif brand=='lamborghini' and model=='revuelto':
                    print('https://www.cardekho.com/lamborghini/revuelto')
                elif brand=='lamborghini' and model=='huracan':
                    print('https://www.carwale.com/lamborghini-cars/huracan-evo/')
                elif brand=='lamborghini' and model=='countach':
                    print('https://www.lamborghini.com/en-en/models/limited-series/countach-lpi-800-4')
                elif brand=='lamborghini' and model=='essenza':
                    print('https://www.carwale.com/news/lamborghini-essenza-scv12-limited-edition-trackonly-car-breaks-cover/')
                elif brand=='mercedes' and model=='senna':
                    print('https://silodrome.com/mercedes-benz-190e-2-3-16/')
                elif brand=='mercedes' and model=='maybach':
                    print('https://www.carwale.com/mercedes-benz-cars/maybach-s-class/')
                elif brand=='mercedes' and model=='cabriolet':
                    print('https://www.carwale.com/mercedes-benz-cars/cle-cabriolet/')
                elif brand=='mercedes' and model=='limousine':
                    print('https://www.carwale.com/mercedes-benz-cars/a-class-limousine/')
                elif brand=='mercedes' and model=='cabriolet':
                    print('https://www.carwale.com/mercedes-benz-cars/cle-cabriolet/')
                elif brand=='honda' and model=='amaze':
                    print('https://www.hondacarindia.com/honda-amaze')
                elif brand=='honda' and model=='city':
                    print('https://www.hondacarindia.com/honda-city-5th-generation')
                elif brand=='honda' and model=='accordhybrid':
                    print('https://www.carwale.com/honda-cars/accord/')
                elif brand=='honda' and model=='civic':
                    print('https://www.carwale.com/honda-cars/civic/')
                elif brand=='honda' and model=='elevate':
                    print('https://www.hondacarindia.com/honda-elevate')
                else:
                    print('link not available')
    if fl==0:
        print('The car which you are searching is unavailable')
def search_price():
    price=float(input('Enter the price lower limit in dollars:'))
    upprice=float(input('enter the price upper limit in dollars;'))
    fl=0
    for i in L:
        if float(i[3])>=price and float(i[3])<=upprice:
            print(i)
            fl=1 
    if fl==0:
        print('no cars available in this year range')
def search_brand(): 
    b=input('Enter the brand of the car:')
    brand=b.lower()
    fl=0
    for i in L:
        if i[0]==brand:
            print(i)
            fl=1
    if fl==0:
        print('No cars available in this brand')
def search_year():
    year=int(input('Enter the year:'))
    fl=0
    for i in L:
        if int(i[2])==year:
            print(i)
            fl=1
    if fl==0:
        print('no cars available in this year')
def search_year2():
    year1 = int(input('Enter the lower limit of the year:'))
    year2 = int(input('Enter the upper limit of the year:'))
    fl=0
    for i in L:
        if int(i[2])>=year1 and int(i[2])<=year2:
            print(i)
            fl=1
    if fl==0:
        print('no cars available in this year range')
def display():
    for i in L:
        print(i)
#main
while True:
    print('Choose any option from the menu to continue')
    print('menu')
    print('press 1 to search for a specific car')
    print('press 2 to search based on price')
    print('press 3 to search based on brand')
    print('press 4 to search for a car of a specific year')
    print('press 5 to search based on year range')
    print('press 6 to display all the cars available')
    print('press 7 to exit')
    ch=int(input('enter the choice you wish to:'))
    if ch==1:
        print('You can now search for a specific car')
        search()
        print('Hope you like it')
    elif ch==2:
        print('You can now search based on price')
        search_price()
        print('Hope you like it')
    elif ch==3:
        print('You can now search based on brand')
        search_brand()
        print('Hope you like it')
    elif ch==4:
        print('You can now search for a car of a specific year')
        search_year()
        print('Hope you like it')
    elif ch==5:
        print('You can now search based on a year range:')
        search_year2()
        print('Hope you like it')
    elif ch==6:
        print('You can now see all the cars available')
        display()
        print('Hope you like it')
    elif ch==7:
        print('Thanks for using')
        break
    else:
        print('Its a wrong choice go through the menu properly')
