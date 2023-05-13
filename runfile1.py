def test_tic():
    print('Покупка билетов')
test_tic()


order = int(input('Количество билетов к бронированию: '))

age = int(input('Возраст: '))

if age <= 17:
    print("Вход бесплатно")

if age >= 18 <= 25:
    result = 990 * order
    if age > 25:
        result = 1390 * order
    else:
        order <= 3
    print("К оплате: ", result)
    if order >= 3:
        discount = result / 100 * 10

        print("Ваша скидка: ", discount)
        print("Оплата с учетом скидки:", result - discount)
























