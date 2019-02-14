import random

def randwhich():
    bread=random.randint(0,7)
    breads=["Italian","Flatbread","Italian Herbs and Cheese","9 Grain Wheat","Honey Oat","Tomato Basil Wrap","Spinach Wrap","Habanero Wrap"]
    print(breads[bread])
    meat=random.randint(0,9)
    doublemeats=[0,4,5,7,8,9]
    meats=["ham","chicken breast","roast beef","tuna","turkey salami","bacon","meatballs","pepperoni","Genoa salami","turkey bologna"]
    if(meat in doublemeats):
        meat2=random.choice(doublemeats)
        print(meats[meat2])
    print(meats[meat])
    cheese=random.randint(0,5)
    cheeses=["American cheese","cheddar cheese","provolone cheese","pepperjack cheese","Swiss cheese","Monterey cheddar cheese"]
    print(cheeses[cheese])
    veg=random.randint(0,10)
    veg2=random.randint(0,10)
    vegs=["Lettuce","tomatoes","red onions","green peppers","pickles","black olives","cucumbers","banana peppers","jalapeno peppers","green peppers","Spinach"]
    print(vegs[veg]+","+vegs[veg2])
    condiment=random.randint(0,17)
    condiments=["Caesar","Thousand Island","mayonnaise","light mayonnaise","mustard","honey mustard","Buffalo","Italian","ranch dressing","Barbeque","chipotle southwest","sweet onion sauce","salt","pepper","oregano","Parmesan cheese","Subway Vinaigrette","Creamy Sriracha"]
    print(condiments[condiment])
    
