class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Удаляем пробелы в начале и в конце строки
        if not s:
            return 0  # Возвращаем 0, если строка пустая

        sign = 1  # Знак числа, по умолчанию положительный
        if s[0] == '-':
            sign = -1  # Если строка начинается с "-", меняем знак на отрицательный
            s = s[1:]  # Удаляем знак из строки
        elif s[0] == '+':
            s = s[1:]  # Если строка начинается с "+", удаляем его из строки

        res = 0  # Инициализируем результат

        # Проходим по символам строки, пока они являются цифрами
        for char in s:
            if char.isdigit():
                res = res * 10 + int(char)  # Умножаем текущий результат на 10 и добавляем новую цифру
            else:
                break  # Если встречаем символ, не являющийся цифрой, завершаем проход

        # Учитываем знак числа и проверяем на переполнение
        res = sign * res
        if res < -(2**31):
            return -(2**31)
        elif res > 2**31 - 1:
            return 2**31 - 1
        else:
            return res
    
sol=Solution()
print(sol.myAtoi("+4193     kefjowefi"))