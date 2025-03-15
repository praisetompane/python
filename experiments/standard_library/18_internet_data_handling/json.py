# json
import json
address_book = {}

address_book["bob"] = {"name": "bob", "address": "1 red street, NY", "phone": 98989898}
address_book["tom"] = {
    "name": "tom",
    "address": "1 blue street, WS",
    "phone": 234234234,
}


json_address_book = json.dumps(address_book)
print(json_address_book)
print("\n")

# files
print("writing file")
with open("./experiments/address_book.json", "w") as file:
    file.write(json_address_book)

print("reading file")
with open("./experiments/address_book.json", "r") as file:
    addresses_loaded_raw_file = file.read()
    print(f"addresses_loaded_raw_file {type(addresses_loaded_raw_file)}\n")

print("reading file and loading it into dictionary")
with open("./experiments/address_book.json", "r") as file:
    print("read file manually and then convert to dictionary")
    addresses_loaded = json.loads(file.read())
    print(type(addresses_loaded))
    print(f"addresses_loaded type: {type(addresses_loaded)}")
    print(addresses_loaded)
    print("\n")

    print("Bob's record:", addresses_loaded["bob"])
    print("Bob's phone:", addresses_loaded["bob"]["phone"])


print("print everyone")
with open("./experiments/address_book.json", "r") as file:
    address_book = json.load(file)
    for p in address_book:
        print(f"{p} : {address_book[p]}")

with open("./experiments/address_book.json", "r") as file:
    print("file to dictionary bypassing reading it directly")
    addresses_loaded = json.load(file)
    print(type(addresses_loaded))
