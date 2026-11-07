import string
password = input("введите пароль:")

len_pas = len(password)
low_pas = password.lower()
upp_pas = password.upper()
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'

eror = 0

if len_pas < 8:
    print("Длина пароля не равна 8")
    eror += 1

if low_pas == password:
    print("В пароле отсутствуют заглавные буквы")
    eror += 1

if upp_pas == password:
    print("В пароле отсутствуют строчные буквы")
    eror += 1

if any(symbol.isdigit() for symbol in password):
    pass
else:
    print("В пароле отсутствуют цифры")
    eror += 1

if "*" in password:
    pass
elif "#" in password:
    pass
elif "-" in password:
    pass
else:
    print("В пароле отсутствуют специальные символы")
    eror +=1

if not all(symbol in allowed for symbol in password):
    print("В пароле используются непредусмотренные символы")
    eror += 1
else:
    pass

if eror == 0:
    print("Надежный пароль")