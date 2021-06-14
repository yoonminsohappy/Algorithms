# 문제 1. 식당의 메뉴가 다음과 같을 때, 손님이 주문한 음식의 결제 총액을 구하시오.
def test():
   menu_dict = {
        "1": "steak",
        "2": "pizza",
        "3": "pasta",
        "4": "hambureger",
        "5": "sandwitch",
    }

guest = int(input("Number of guests?"))
ordered_list = []
count = 0
price = 0

while count < guest:
        menu = int(input("select menu?"))

        if menu == 1:
            count += 1
            price += 25000
            ordered_list.append(menu_dict["1"])
        elif menu == 2:
            count += 1
            price += 28000
            ordered_list.append(menu_dict["2"])
        elif menu == 3:
            count += 1
            price += 14000
            ordered_list.append(menu_dict["3"])
        elif menu == 4:
            count += 1
            price += 8500
            ordered_list.append(menu_dict["4"])
        elif menu == 5:
            count += 1
            price += 4500
            ordered_list.append(menu_dict["5"])
        else:
            menu = int(input("Reselect menu?"))

print("ordered list>>", ordered_list)
print("total payment>>", price, "won")

    return
test()

# Reselect 버그
