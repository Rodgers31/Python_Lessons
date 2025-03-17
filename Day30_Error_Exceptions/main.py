#FileNotFound

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does nor exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#         file.close()
#         print("File was closed.")
#         raise TypeError("This is an error that i made up")

# You can raise exceptions using raise, and it will throw and error
height = float(input("Height: "))
weight = int(input("Height: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")
bmi = weight / height ** 2
print(bmi)
