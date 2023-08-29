class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []
        self.populate_data()

    def populate_data(self):
        data = [
            ("161E90", "Raman", 41, 56000),
            ("161F91", "Himadri", 38, 67500),
            ("161F99", "Jaya", 51, 82100),
            ("171E20", "Tejas", 30, 55000),
            ("171G30", "Ajay", 45, 44000)
        ]
        for emp_id, name, age, salary in data:
            employee = Employee(emp_id, name, age, salary)
            self.employees.append(employee)

    def search_by_age(self, operator, age):
        results = []
        for employee in self.employees:
            if operator == '<' and employee.age < age:
                results.append(employee)
            elif operator == '>' and employee.age > age:
                results.append(employee)
            elif operator == '<=' and employee.age <= age:
                results.append(employee)
            elif operator == '>=' and employee.age >= age:
                results.append(employee)
        return results

    def search_by_name(self, name):
        results = []
        for employee in self.employees:
            if name.lower() in employee.name.lower():
                results.append(employee)
        return results

    def search_by_salary(self, operator, salary):
        results = []
        for employee in self.employees:
            if operator == '<' and employee.salary < salary:
                results.append(employee)
            elif operator == '>' and employee.salary > salary:
                results.append(employee)
            elif operator == '<=' and employee.salary <= salary:
                results.append(employee)
            elif operator == '>=' and employee.salary >= salary:
                results.append(employee)
        return results

def main():
    db = EmployeeDatabase()

    print("Search Parameters:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        operator = input("Enter operator (<, >, <=, >=): ")
        age = int(input("Enter age: "))
        results = db.search_by_age(operator, age)
    elif choice == 2:
        name = input("Enter name: ")
        results = db.search_by_name(name)
    elif choice == 3:
        operator = input("Enter operator (<, >, <=, >=): ")
        salary = int(input("Enter salary: "))
        results = db.search_by_salary(operator, salary)
    else:
        print("Invalid choice!")
        return

    if not results:
        print("No results found.")
    else:
        print("Search Results:")
        for employee in results:
            print(f"ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

if __name__ == "__main__":
    main()
