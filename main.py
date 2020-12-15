import requests
import bs4
import os

url = "https://pogoda1.ru/katalog/sverdlovsk-oblast/temperatura-vody/10-dney/"

res = requests.get(url)

if res.status_code != requests.codes.ok:
    print("Something went wrong, please check your internet connection!")
else:
    text = res.text

    bs = bs4.BeautifulSoup(text, "html.parser")

    tagsDates = bs.select('table th')

    dates = []

    for var in tagsDates:
        dates.append(var.text)

    dates.remove(dates[0])

    tagsRivers = bs.select('table a')

    rivers = []

    for var in tagsRivers:
        rivers.append(var.text)

    tagsTemps = tagsDates = bs.select('table tr td')

    temps = []

    for i in range(0, len(tagsTemps)):
        if i != 0 and i % 11 != 0:
            temps.append(tagsTemps[i].text)

    for i in range(0, len(rivers)):
        print("\n ----- " + rivers[i] + " ")
        for j in range(0, len(dates)):
            print("Температура на " + dates[j] + " : " + temps[10 * i + j])

    workPath = "C:\\python"

    os.chdir(workPath)

    file = open(os.getcwd() + "\\temp.txt", "w")

    for i in range(0, len(rivers)):
        file.write("\n ----- " + rivers[i] + " \n ")
        temp = 0
        for j in range(0, len(dates)):
            temp += float(temps[10 * i + j])
            file.write("Температура на " + dates[j] + " : " + temps[10 * i + j] + "\n")

        mid = temp / len(rivers)
        file.write("Средняя температура - " + format(mid, ".3f") + "\n")
