
def calculator():
    while True:
        try:
            expression = input("İşlemi girin:")

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
                    print("0 ile bölünmez")
                    continue
                    
                else:
                    result = float(n1) / float(n2)
                   

            integer,decimals = str(result).split(".")

            if decimals == "0":
                print(integer)
                        
            else:
                print(integer+"."+decimals)   


        except ValueError:
            print("Hatalı yazım")

        except Exception as e:
            print("Bilinmeyen hata:",e)

calculator()

