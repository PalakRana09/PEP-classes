import os

FILE_NAME = "data.txt"

def create_user():
    while True:
        try:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            designation = input("Enter your designation: ")
            salary = float(input("Enter your salary: "))

            with open(FILE_NAME, "a") as file:
                file.write(f"{name},{age},{designation},{salary}\n")

            choice = input("Do you want to continue adding users? (yes/no): ").lower()
            if choice != "yes":
                break
        except ValueError:
            print("Please enter valid data!")

def display_users():
    if not os.path.exists(FILE_NAME):
        print("No data found.")
        return

    print("\n--- User Information ---")
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, age, designation, salary = line.strip().split(",")
            hike = float(salary) * 0.30
            new_salary = float(salary) + hike
            print(f"Name: {name}, Age: {age}, Designation: {designation}, Salary: {salary}, Hike(30%): {hike}, After Hike: {new_salary}")

def raise_salary():
    name_to_update = input("Enter the name of the person whose salary is to be raised: ")

    if not os.path.exists(FILE_NAME):
        print("No data to update.")
        return

    lines = []
    updated = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            name, age, designation, salary = line.strip().split(",")
            if name.lower() == name_to_update.lower():
                try:
                    new_salary = float(input(f"Enter new salary for {name}: "))
                    lines.append(f"{name},{age},{designation},{new_salary}\n")
                    updated = True
                except ValueError:
                    print("Invalid salary amount. Try again.")
                    return
            else:
                lines.append(line)

    if updated:
        with open(FILE_NAME, "w") as file:
            file.writelines(lines)
        print("Salary updated successfully.")
    else:
        print("Person not found.")

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Create")
        print("2. Display")
        print("3. Raise Salary")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        try:
            if choice == "1":
                create_user()
            elif choice == "2":
                display_users()
            elif choice == "3":
                raise_salary()
            elif choice == "4":
                print("Thank you for using the application.")
                break
            else:
                print("Invalid option. Try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

main()
