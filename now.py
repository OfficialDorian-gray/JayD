class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):

        # Initializes a bank account with account number, customer name, and balance.

        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):

        # Deposits the given amount into the account.

        self.balance += amount
        print(f"Deposit of {amount} successfully made. Current balance: {self.balance}")

    def withdraw(self, amount):

        # Withdraws the given amount from the account if sufficient balance is available.

        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. Current balance: {self.balance}")
        else:
            print("Insufficient funds")

    def check_balance(self):

        # Checks and prints the current balance of the account.

        print(f"Current balance: {self.balance}")

    def transfer_funds(self, recipient_account, amount):

        # Transfers funds from this account to another account.

        if amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transfer of {amount} to {recipient_account.customer_name} successful.")
            print(f"Your current balance: {self.balance}")
        else:
            print("Insufficient funds")

class Customer:
    def __init__(self, name):

        # Initializes a customer with a name and an empty list of accounts.

        self.name = name
        self.accounts = []

    def add_account(self, account):

        # Adds a bank account to the customer's list of accounts.

        self.accounts.append(account)
        print("Account added successfully.")

    def list_accounts(self):

        # Lists all accounts associated with the customer.

        print(f"Accounts for customer {self.name}:")
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Balance: {account.balance}")

class StudentProfile:
    def __init__(self, student_id, name, age, gender):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender

class CourseEnrollment:
    def __init__(self, student_id, course_name):
        self.student_id = student_id
        self.course_name = course_name

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student_profile):
        self.students.append(student_profile)

    def update_student(self, student_id, new_data):
        for student in self.students:
            if student.student_id == student_id:
                for key, value in new_data.items():
                    setattr(student, key, value)

    def search_student_by_name(self, name):
        return [student for student in self.students if student.name == name]

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def generate_report(self):
        for student in self.students:
            print(f"Student ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Gender: {student.gender}")

# Example usage:
if __name__ == "__main__":
    # Create accounts and customers
    account1 = BankAccount("ACC001", "Alice")
    account2 = BankAccount("ACC002", "Bob")
    customer1 = Customer("Issac")
    customer2 = Customer("Bob")

    # Add accounts to customers
    customer1.add_account(account1)
    customer2.add_account(account2)

    # Perform transactions
    account1.deposit(1000)
    account1.withdraw(200)
    account1.transfer_funds(account2, 500)

    # List accounts for customers
    customer1.list_accounts()
    customer2.list_accounts()

    # Create student profiles and database
    student_db = StudentDatabase()
    student1_profile = StudentProfile(1, "Alice", 20, "Female")
    student2_profile = StudentProfile(2, "Bob", 22, "Male")
    student3_profile = StudentProfile(3, "Charlie", 21, "Male")

    # Add students to the database
    student_db.add_student(student1_profile)
    student_db.add_student(student2_profile)
    student_db.add_student(student3_profile)

    # Update student details
    student_db.update_student(1, {"age": 21, "gender": "Male"})

    # Search for students
    print("Students named Bob:")
    print(student_db.search_student_by_name("Bob"))
    print("\nStudent with ID 3:")
    print(student_db.search_student_by_id(3))

    # Generate report
    print("\nStudent Database Report:")
    student_db.generate_report()
