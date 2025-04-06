# # class ShoppingCart:
# #     def __init__(self):
# #         self.items = {}

# #     def add_item(self, item, price):
# #         if item in self.items:
# #             self.items[item] += 1
# #         else:
# #             self.items[item] = 1
# #         print(f"{item} added to cart.")

# #     def remove_item(self, item):
# #         if item in self.items:
# #             if self.items[item] > 1:
# #                 self.items[item] -= 1
# #                 print(f"{item} removed from cart.")
# #             else:
# #                 del self.items[item]
# #                 print(f"{item} removed from cart.")
# #         else:
# #             print(f"{item} not found in cart.")

# #     def calculate_total(self):
# #         total = 0
# #         for item, quantity in self.items.items():
# #             total += quantity * self.items[item]
# #         return total

# # # Example usage:
# # cart = ShoppingCart()
# # cart.add_item("apple", 2)
# # cart.add_item("banana", 3)
# # cart.add_item("apple", 1)
# # cart.remove_item("banana")
# # print("Total price:", cart.calculate_total())


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def work(self):
#         print(f"{self.name} is working.")

#     def get_salary(self):
#         print(f"{self.name}'s salary is {self.salary}")

# class HRManager(Employee):
#     def work(self):
#         print(f"{self.name} is managing the HR department.")

#     def add_employee(self, employee):
#         print(f"{self.name} added {employee.name} to the team.")

# # Example usage:
# employee1 = Employee("Raktim", 50000)
# employee1.work()
# employee1.get_salary()

# hr_manager = HRManager("SAMI", 70000)
# hr_manager.work()
# hr_manager.get_salary()
# hr_manager.add_employee(employee1)

import math

# class Shape:
#     def get_perimeter(self):
#         pass

#     def get_area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def get_perimeter(self):
#         return 2 * math.pi * self.radius

#     def get_area(self):
#         return math.pi * self.radius**2

# # Example usage:
# circle = Circle(5)
# print("Circle perimeter:", circle.get_perimeter())
# print("Circle area:", circle.get_area())
# def divide(a, b):
#     try:
#         result = a / b
#         print("Division result:", result)
#     except ZeroDivisionError:
#         print("Error: Division by zero")

# # Example usage:
# divide(10, 2)
# divide(10, 0)

# def get_integer_input():
#     while True:
#         try:
#             num = int(input("Enter an integer: "))
#             return num
#         except ValueError:
#             print("Invalid input. Please enter an integer.")

# # Example usage:
# num = get_integer_input()
# print("You entered:", num)

def divide_numbers(a, b):
    try:
        result = a / b
        print("Division result:", result)
    except ArithmeticError:
        print("Error: Arithmetic error occurred.")

# Example usage:
divide_numbers(10, 2)
divide_numbers(10, 0)