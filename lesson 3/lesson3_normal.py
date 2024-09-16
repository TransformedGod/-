

names = ["Иван", "Федот", "Автотья", "Фекла", "Макарыч", "Патрикевна"]
salaries = [10000, 20000, 30000, 40000, 500000, 600000]

bugaltery_book = dict(zip(names, salaries))

def write_file(file_name, dict):
    file = open(file_name, "w", encoding = "utf-8")
    for key, value in dict.items():
        if value < 500001:
            file.write(f'{key} - {value}\n')
    file.close()

write_file("Bugaltery.txt", bugaltery_book)

file_open = open("Bugaltery.txt", encoding = "utf-8")
for line in file_open:
   name, slash, money = line.split()
   money = float(money) - float(money) * 0.13
   print(f"{name.upper()} - {money}")
