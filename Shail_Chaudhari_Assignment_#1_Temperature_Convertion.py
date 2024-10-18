#Shail Chaudhari
# Computer Science 20 P-5
# October 17, 2024

# Temperature Conversion Program
# Purpose: To convert a temperature from celsius to farenheit and kelvin and vice versa.

#Take from the user what to convert from
print("Press 1 if you want to Convert from Celsius")
print("Press 2 if you want to Convert from Farenheit")
print("Press 3 if you want to Convert from Kelvin")
try: 
    choice_to_convert_from = int(input())
except:
    print("You Entered An Invalid Input.")
    print("Please Run The Program Again And Enter A Valid Input")
else:


    if choice_to_convert_from == 1:
        print("Enter The Temperature In Celsius")
        try:
            temperature = int(input())
        except:
            print("You Entered An Invalid Input.")
            print("Please Run The Program Again And Enter A Valid Input")
        else:
#Instead Of first choosing what to convert to I did the calculation first so i could add The Choice to convert to both. This repeats in all three choices            
            farenheit = round(temperature*9/5 + 32)
            kelvin = round( temperature + 273.15)
            print("Press 1 if you want to Convert to Farenheit")
            print("Press 2 if you want to Convert to Kelvin")
            print("Press 3 if you want to Convert to Both")
            try: 
                choice_to_convert_to = int(input())
            except:
                print("You Entered An Invalid Input.")
                print("Please Run The Program Again And Enter A Valid Input")
            else:
# This is just choosinng what all stuff to print out                    
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
        try:
            temperature = int(input())
        except:
            print("You Entered An Invalid Input.")
            print("Please Run The Program Again And Enter A Valid Input")
        else:
            celsius = round((temperature - 32)*5/9)
            kelvin = round(((temperature - 32)*5/9) + 273.15)
            print("Press 1 if you want to Convert to Celsius")
            print("Press 2 if you want to Convert to Kelvin")
            print("Press 3 if you want to Convert to Both")
            try: 
                choice_to_convert_to = int(input())
            except:
                print("You Entered An Invalid Input.")
                print("Please Run The Program Again And Enter A Valid Input")
            else:
        
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
        try:
            temperature = int(input())
        except:
            print("You Entered An Invalid Input.")
            print("Please Run The Program Again And Enter A Valid Input")
        else:    
            celsius = round(temperature - 273.15)
            farenheit = round(((temperature - 273.15) * 9/5) + 32)
            print("Press 1 if you want to Convert to Celsius")
            print("Press 2 if you want to Convert to Farenheit")
            print("Press 3 if you want to Convert to Both")
            try: 
                choice_to_convert_to = int(input())
            except:
                print("You Entered An Invalid Input.")
                print("Please Run The Program Again And Enter A Valid Input")
            else:
            
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
        

