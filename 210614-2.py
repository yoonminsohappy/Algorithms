# 문제 2. 다음과 같은 품목을 쇼핑할 때, 결제 총액을 구하시오.
def test():
    item_list = [
        {"price": 23400, "brand": "ivory"},
        {"price": 38500, "brand": "tommy"},
        {"price": 21000, "brand": "arena"},
        {"price": 38500, "brand": "metro"},
        {"price": 45000, "brand": "coach"},
    ]
    payment = 0
    ordered_list = []

    while True:
        item = int(input("Select Item?"))
        if item == 0:
            break
        elif item == 1:
            payment += 23400
            ordered_list.append("ivory")
        elif item == 2:
            payment += 38500
            ordered_list.append("tommy")
        elif item == 3:
            payment += 21000
            ordered_list.append("arena")
        elif item == 4:
            payment += 38500
            ordered_list.append("metro")
        elif item == 5:
            payment += 45000
            ordered_list.append("coach")
        else:
            item = int(input("Reselect?"))
            payment += item_list[(item - 1)]["price"]
            ordered_list.append(item_list[(item - 1)]["brand"])

    print("Order List", ordered_list)
    print("TotalPayment", payment, "won")

    return


test()
