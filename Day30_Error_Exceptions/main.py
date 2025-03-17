#FileNotFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does nor exist")
else:
    content = file.read()
    print(content)
finally:
        file.close()
        print("File was closed.")
#Key Error
# a_dictionary = {"key": "value}
# value = a_dictionary["non_existent_key"]

# indexError
# fruit_list = ["Apple", "Soda", "Omena"]
