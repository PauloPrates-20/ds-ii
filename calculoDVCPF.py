def calcular_digito_verificador(cpf_parcial):
    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf_parcial[i]) * (10 - i) for i in range(9))
    primeiro_digito = 11 - (soma % 11)
    primeiro_digito = 0 if primeiro_digito >= 10 else primeiro_digito

    # Calcula o segundo dígito verificador
    cpf_com_primeiro = cpf_parcial + str(primeiro_digito)
    soma = sum(int(cpf_com_primeiro[i]) * (11 - i) for i in range(10))
    segundo_digito = 11 - (soma % 11)
    segundo_digito = 0 if segundo_digito >= 10 else segundo_digito

    return str(primeiro_digito) + str(segundo_digito)

cpf = "123456789"
digitos_verificadores = calcular_digito_verificador(cpf)
print("Dígitos verificadores:", digitos_verificadores)
