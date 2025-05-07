#4. Class Variables and Class Methods
#Assignment:
#Create a class Bank with a class variable bank_name.
# Add a class method change_bank_name(cls, name) that allows changing the bank name. 
# Show that it affects all instances.

class Bank:
    # Class variable
    bank_name = "Default Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    # Class method to change the class variable
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {Bank.bank_name}")

# Creating instances
acc1 = Bank("Nimra")
acc2 = Bank("Tahira")

# Displaying before changing bank name
print("Before changing bank name:")
acc1.display()
acc2.display()

# Changing bank name using class method
Bank.change_bank_name("KoreanBank")

# Displaying after changing bank name
print("\nAfter changing bank name:")
acc1.display()
acc2.display()
