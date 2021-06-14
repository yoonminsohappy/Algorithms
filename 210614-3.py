# 문제 3. 유럽 여행 상품이 다음과 같을 때, 예산 경비에 맞춰 경유 도시 일정을 출력하시오.
def test():

    print("1 - Wroclaw 3day 250000")
    print("2 - Bilbao 4day 350000")
    print("3 - Colmar 3day 300000")
    print("4 - Hvar island 3day 270000")
    print("5 - Riga 4day 360000")
    print("6 - Milano 3day 450000")
    print("7 - Athens 2day 300000")
    print("8 - Budapest 3day 250000")
    print("9 - Lisbon 4day 380000")
    print("10 - Prague 5day 420000")

    product_list = [
        {"place": "Wroclaw", "plans": 3, "price": 250000},
        {"place": "Bilbao", "plans": 4, "price": 350000},
        {"place": "Colmar", "plans": 3, "price": 300000},
        {"place": "Hvar island", "plans": 3, "price": 270000},
        {"place": "Riga", "plans": 4, "price": 360000},
        {"place": "Milano", "plans": 3, "price": 450000},
        {"place": "Athens", "plans": 2, "price": 300000},
        {"place": "Budapest", "plans": 3, "price": 250000},
        {"place": "Lisbon", "plans": 4, "price": 380000},
        {"place": "Prague", "plans": 5, "price": 420000},
    ]

    payment = 0
    days = 0
    way_point = ""
    expenses = int(input("traveling expenses?"))

    while True:
        city = int(input("Select City?"))

        if city == 0:
            break

        elif 1 <= city <= 10:
            if (expenses - payment) < product_list[city - 1]["price"]:
                break
            else:
                payment += product_list[city - 1]["price"]
                days += product_list[city - 1]["plans"]
                way_point += product_list[city - 1]["place"] + " "
                print(payment)
                print(product_list[(city - 1)]["place"])

        else:
            city = int(input("Reselect City?"))
            payment += product_list[city - 1]["price"]
            days += product_list[city - 1]["plans"]
            way_point += product_list[city - 1]["place"] + " "
            print(payment)
            print(product_list[(city - 1)]["place"])

    print("===============================================")
    print("Waypoint", way_point)
    print(days, "- Days", "Total Payment :", payment, "won")

    return


test()
