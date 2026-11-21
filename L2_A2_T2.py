try:
    with open("L2_A2_T2.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: The file 'L2_A2_T2.txt' was not found. Please ensure the file exists in the correct directory.")