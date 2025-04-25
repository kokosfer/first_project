
def calculator():
    while True:
        try:
            expression = input("Write the expression:")

            if "+" in expression:
                n1,n2 = expression.split("+")
                result = float(n1) + float(n2)
                

            elif "-" in expression:
                n1,n2 = expression.split("-")
                result = float(n1) - float(n2)
                
            elif "*" in expression:
                n1,n2 = expression.split("*")
                result = float(n1) * float(n2)
               

            elif "/" in expression:
                n1,n2 = expression.split("/")
                
                if float(n2) == 0:
                    print("Can't divide by zero")
                    continue
                    
                else:
                    result = float(n1) / float(n2)
                   

            integer,decimals = str(result).split(".")

            if decimals == "0":
                print(integer)
                        
            else:
                print(integer+"."+decimals)   


        except ValueError:
            print("Wrong spelling")

        except Exception as e:
            print("Unknown error:"+ e)

calculator()

