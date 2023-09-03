# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

friends_items = {}

while True:
    friend_name = input("Введите имя друга (или 'q' для завершения): ")
    if friend_name == 'q':
        break
    
    friend_items = input(f"Введите вещи, которые взяли с собой {friend_name} через запятую: ").split(',')
    
    friend_items = {item.strip() for item in friend_items}
    friends_items[friend_name] = friend_items

common_items = set.intersection(*friends_items.values())
print("Вещи, которые взяли все друзья:", common_items)

all_items = set.union(*friends_items.values())

item_to_friends = {}
for friend, items in friends_items.items():
    for item in items:
        if item in item_to_friends:
            item_to_friends[item].append(friend)
        else:
            item_to_friends[item] = [friend]

unique_items = {item for item, friends in item_to_friends.items() if len(friends) == 1}
print("Уникальные вещи, есть только у одного друга:", unique_items)

for item, friends in item_to_friends.items():
    if len(friends) == len(friends_items) - 1:
        absent_friend = set(friends_items.keys()) - set(friends)
        print(f"Вещь '{item}' есть у всех друзей, кроме {absent_friend.pop()}")