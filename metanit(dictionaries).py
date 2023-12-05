users_list = [["+111123455", "Tom"], ["+384767557", "Bob"], ["+958758767", "Alice"]]
users_dict = dict(users_list)
print(users_dict)  # {"+111123455": "Tom", "+384767557": "Bob", "+958758767": "Alice"

users = {"+11111111": "Tom", "+33333333": "Bob", "+55555555": "Alice"}

# получаем элемент с ключом "+11111111"
print(users["+11111111"])  # Tom

# установка значения элемента с ключом "+33333333"
users["+33333333"] = "Bob Smith"
print(users["+33333333"])  # Bob Smith
users["+4444444"] = "Sam"
user = users["+4444444"]
key = "+4444444"
if key in users:
    user = users[key]
    print(user)
else:
    print("")

    users = {"+11111111": "Tom", "+33333333": "Bob", "+55555555": "Alice"}

user1 = users.get("+55555555")
print(user1)  # Alice
user2 = users.get("+33333333", "Unknown user")
print(user2)  # Bob
user3 = users.get("+44444444", "Unknown user")
print(user3)  # Unknown user
