def write_student_data():
  """Prompts user for student information and writes it to a file"""
  try:
    with open("student_data.txt", "w") as file:
      name = input("Name: ")
      stream = input("Stream: ")
      age = int(input("Age: "))
      phone = input("Phone: ")
      
      # Write data in a structured format
      file.write(f"Name: {name}\n")
      file.write(f"Stream: {stream}\n")
      file.write(f"Age: {age}\n")
      file.write(f"Phone: {phone}\n")
      print("Student data written successfully!")
  except FileNotFoundError:
    print("Error: The file could not be created.")

def read_student_data():
  """Reads the contents of the student_data.txt file and displays them"""
  try:
    with open("student_data.txt", "r") as file:
      data = file.read()
      if data:
        print("Student Data:")
        print(data)
      else:
        print("The file is empty.")
  except FileNotFoundError:
    print("Error: student_data.txt file not found.")

def append_student_data():
  """Appends email and roll number information to the student_data.txt file"""
  try:
    with open("student_data.txt", "a") as file:
      email = input("Email: ")
      roll_number = input("Roll Number: ")
      file.write(f"\nEmail: {email}\n")
      file.write(f"Roll Number: {roll_number}\n")
      print("Additional data appended successfully!")
  except FileNotFoundError:
    print("Error: student_data.txt file not found.")

def count_words():
  """Counts the number of words in the student_data.txt file"""
  try:
    with open("student_data.txt", "r") as file:
      data = file.read()
      if data:
        # Split data by spaces and count the words
        word_count = len(data.split())
        print(f"Number of words in the file: {word_count}")
      else:
        print("The file is empty.")
  except FileNotFoundError:
    print("Error: student_data.txt file not found.")

# User menu
while True:
  print("\nMenu:")
  print("1. Write Student Data")
  print("2. Read Student Data")
  print("3. Append Student Data")
  print("4. Count Words in File")
  print("5. Exit")

  choice = input("Enter your choice (1-5): ")

  if choice == '1':
    write_student_data()
  elif choice == '2':
    read_student_data()
  elif choice == '3':
    append_student_data()
  elif choice == '4':
    count_words()
  elif choice == '5':
    print("Exiting...")
    break
  else:
    print("Invalid choice. Please try again.")