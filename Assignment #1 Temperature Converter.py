import math
print("Press 1 if you want to Convert from Celsius")
print("Press 2 if you want to Convert from Farenheit")
print("Press 3 if you want to Convert from Kelvin")
choice_to_convert_from = int(input())


if choice_to_convert_from == 1:
    print("Enter The Temperature In Celsius")
    temperature = int(input())
    farenheit = round(temperature*9/5 + 32)
    kelvin = round( temperature + 273.15)
    print("Press 1 if you want to Convert to Farenheit")
    print("Press 2 if you want to Convert to Kelvin")
    print("Press 3 if you want to Convert to Both")
    choice_to_convert_to = int(input())
    
    if choice_to_convert_to == 1:
        print("The Temperature In Farenheit Is: " +str(farenheit))
        
    elif choice_to_convert_to == 2:
        print("The Temperature In Kelvin Is: " +str(kelvin))
    
    elif choice_to_convert_to == 3:
        print("The Temperature In Farenheit Is: " +str(farenheit))
        print("The Temperature In Kelvin Is: " +str(kelvin))
        
    else:
        print("You Entered An Invalid Input.")
        print("Please Run The Program Again And Enter A Valid Input")
        


elif choice_to_convert_from == 2:
    print("Enter The Temperature In Farenheit")
    temperature = int(input())
    celsius = round((temperature - 32)*5/9)
    kelvin = round(((temperature - 32)*5/9) + 273.15)
    print("Press 1 if you want to Convert to Celsius")
    print("Press 2 if you want to Convert to Kelvin")
    print("Press 3 if you want to Convert to Both")
    choice_to_convert_to = int(input())
    
    if choice_to_convert_to == 1:
        print("The Temperature In Celsius Is: " +str(celsius))
        
    elif choice_to_convert_to == 2:
        print("The Temperature In Kelvin Is: " +str(kelvin))
    
    elif choice_to_convert_to == 3:
        print("The Temperature In Celsius Is: " +str(celsius))
        print("The Temperature In Kelvin Is: " +str(kelvin))
        
    else:
        print("You Entered An Invalid Input.")
        print("Please Run The Program Again And Enter A Valid Input")



elif choice_to_convert_from == 3:
    print("Enter The Temperature In Kelvin")
    temperature = int(input())
    celsius = round(temperature - 273.15)
    farenheit = round(((temperature - 273.15) * 9/5) + 32)
    print("Press 1 if you want to Convert to Celsius")
    print("Press 2 if you want to Convert to Farenheit")
    print("Press 3 if you want to Convert to Both")
    choice_to_convert_to = int(input())
    
    if choice_to_convert_to == 1:
        print("The Temperature In Celsius Is: " +str(celsius))
        
    elif choice_to_convert_to == 2:
        print("The Temperature In Farenheit Is: " +str(farenheit))
    
    elif choice_to_convert_to == 3:
        print("The Temperature In Celsius Is: " +str(celsius))
        print("The Temperature In Farenheit Is: " +str(farenheit))
        
    else:
        print("You Entered An Invalid Input.")
        print("Please Run The Program Again And Enter A Valid Input")



else :
    print("You Entered An Invalid Input.")
    print("Please Run The Program Again And Enter A Valid Input")