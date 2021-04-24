def register_user():
    name = input("Enter your name: ")
    city = input("Enter your city: ")
    phone = input("Enter your 10 digit phone number: ")

    with open("D:\\Code\\Demo\\userdata.csv", 'a') as f:
        f.write(name + "," + city + "," + phone +"\n")

    print("Hello {}, Your registration is complete".format(name))

    with open("D:\\Code\\Demo\\userdata.csv", 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
        
register_user()