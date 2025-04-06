print("Online product purchase")
print("What would you like to perform?")
print("1.Order\n2.Cancel_Order\n3.Exit")
customer=[] 
a=["Apple","Samsung","Vivo","Xiaomi","Realme"]
Cust_rate=[] #customer rating

while True:
    try:
        n=int(input("Enter your choice: "))
        if n==3:
            print("Exit is success: ")
            break
        if 0<n<=2:
            if n==1:
                if a:
                    c=input("Do you want to place order? yes/no: ")
                    print("--------------------------------------------------------")
                    if c=="yes":
                        d=input("Enter product name: ")
                        print("----------------------------------------------------")
                        if d in a:
                            customer.append(d)
                            a.remove(d)
                            print("order placed successfully")
                            print("-----------------------------------------------")
                            print("This is Customer Order: ",customer)
                            print("---------------------------------------------------")
                            print(a)
                            print("---------------------------------------------------")
                            e=input("Would you like to give rating? yes/no: ")
                            if e=="yes":
                                f=int(input("Please give rating between 1-5: "))
                                print("-----------------------------------------------")
                                print("Thank for your rating")
                                Cust_rate.append(f)
                                print("----------------------------------------------")
                                print("This is what rating:",Cust_rate)
                            elif e=="no":
                                print("We understand the excitement to use new product,its ok")
                            else:
                                print("You should enter yes or no,no other responses are expected")
                        else:
                            print("we dont have such products in our store")
                    else:
                        print("You can continue to view products!")
                else:
                    print("products are out of stock,try again later")
            elif n==2:
                g=input("Are you sure you want to cancel the order? yes/no:")
                print("************************************************************")
                if g=="yes":
                    h=input("Enter the product name you want to cancel: ")
                    print("**********************************************************")
                    if h in customer:
                        customer.remove(h)
                        print("Order Canceled successfully")
                        print("###################################################")
                        print("This is customer order:",customer)
                        print("==================================================")
                        a.append(h)
                        print("Our stock:",a)
                    else:
                        print("No such product ordered yet")
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("This is your order: ",customer)
                else:
                    print("We assume you changed your mind,it happens")
            else:
                print("Your input should be between 1-3")
    except ValueError:
        print("Only int values are expected")
