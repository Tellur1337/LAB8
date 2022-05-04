#Second task- Author - Repin Nikita
s = input("Введите список строк через tab: ").split('\t')
num = int(input("Введите позицию вашей новой строки: "))
nl = input("Введите новую строку: ")
def list(s):
    count = 1
    for x in s:
        print(count, x)
        count += 1

s.clear(2)
s.insert(num, nl)

print(list(s))



