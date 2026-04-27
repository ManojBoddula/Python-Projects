class Atm():
    def __init__(self):
         self.pin=''
         self.balance = 0
    
    def main(self):
         
            user_input = input("""
            HI how can i help you?
            1.Press 1 to Create a pin
            2.Press 2 to Change Pin
            3.Press 3 to Check Balance
            4.Press 4 to WithDraw
            5.Anything Else to Exit
            """)
            if user_input == '1':
                self.Create_pin()
            elif user_input == '2':
                self.Change_pin()
            elif user_input == '3':
                self.Check_balance()
            elif user_input == '4':
                self.WithDraw()
            else:
                exit()
              
        
    #Create Pin
    def Create_pin(self):
         user_pin = int(input("Enter your pin: "))
         self.pin = user_pin
         user_balance = int(input("Enter your balance "))
         self.balance = user_balance
         print(f'Your Balance is: {self.balance}')
         print("Pin Created Successfully")

    #Change Pin
    def Change_pin(self):
        old_pin = int(input("Enter your pin: "))
        if old_pin == self.pin():
            new_pin=int(input("Enter your pin: "))
            self.pin = new_pin
            print("Pin Change successfully")
        else:
            print("Incorrect Pin")
        self.main()

    #Check Balance
    def Check_balance(self):
        user_pin= (int(input("Enter Your pin: ")))
        if user_pin == self.pin:
            print("Your Balance is",self.balance)
        else:
            print("InCorrect Pin")
    
    #WithDraw
    def WithDraw(self):
        user_pin = int(input("Enter your pin: "))
        if user_pin == self.pin:
            Amount= int(input("Enter your Balance: "))
            if self.balance > Amount:
                print("WithDraw Sucessfully")
            else:
                print("Insufficient Founds")
        else:
            print("InCorrect Pin")
            self.main()


atm = Atm()
atm.main()

