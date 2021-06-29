# 문제 1. 식당의 메뉴가 다음과 같을 때, 손님이 주문한 음식의 결제 총액을 구하시오.
def test():

    menu_list = [
        {"pay": 25000, "dish": "steak"},
        {"pay": 28500, "dish": "pizza"},
        {"pay": 14000, "dish": "pasta"},
        {"pay": 8500, "dish": "hamburger"},
        {"pay": 4500, "dish": "sandwitch"},
    ]

    guest = int(input("Number of guests?"))
    ordered_list = []
    count = 0
    price = 0

    while count < guest:
        menu = int(input("select menu?"))

        if 1 <= menu <= 5:
            count += 1
            price += menu_list[(menu - 1)]["pay"]
            ordered_list.append(menu_list[(menu - 1)]["dish"])

        else:
            menu = int(input("Reselect menu?"))
            count += 1
            price += menu_list[(menu - 1)]["pay"]
            ordered_list.append(menu_list[(menu - 1)]["dish"])

    print("Ordered List :")
    print("\n".join(ordered_list))
    print("Total Payment :", price, "won")

    return


test()
