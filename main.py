name_user = input("digite o nome de usuario:")
if name_user == "nexusadmin/123":
    print("acesso permitido continue o login")
else:
    exit()
password = input("digite a senha:")
if password == "hash256//123":
    print("acesso permitido")
else:
    exit()
