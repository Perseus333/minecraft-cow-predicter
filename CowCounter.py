import matplotlib.pyplot as plt


def cowCounter(days, adults=2, babies=0, do_sleep=True):

    record_b = []
    list_b = []
    list_a = []
    list_days = []
    if not do_sleep:
        days *= 2

    for day in range(days):
        day += 1
        babies_today = adults // 2
        babies += babies_today
        record_b.append(babies)

        if day > 3:
            b_grown_tdy = record_b[day-4]
            adults += b_grown_tdy
            babies -= b_grown_tdy

        list_days.append(int(day))
        list_a.append(adults)
        list_b.append(babies)

    return list_days, list_a, list_b


simple = True

if bool(input('Simple or advanced? [nothing to simple, False to advanced]')):
    days = int(input('Select the days: '))
    adults = int(input('Starting adults: '))
    babies = int(input('Starting babies: '))
    do_sleep = bool(input('Will you sleep? [True, False]'))
    list_days, list_a, list_b = cowCounter(days, adults, babies, do_sleep)
else:
    days = int(input('Select the days you will be feeding the cows: '))
    list_days, list_a, list_b = cowCounter(days)

plt.plot(list_days, list_a, label="Adults")
plt.plot(list_days, list_b, label="Babies")
plt.title('Cow Counter')
plt.xlabel('Days')
plt.ylabel('Num of Cows')
plt.legend()


if __name__ == '__main__':
    plt.show()
