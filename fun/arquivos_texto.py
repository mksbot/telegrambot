def registro(registrar, nome='arq01', substituir="sim"):
    if substituir == "sim":
        s = 'w'
    else:
        s = 'a'
    with open(f'arquivos/registros/{nome}.txt', f'{s}') as arquivo:
        arquivo.write(f'{registrar}\n')
        arquivo.close()


def abrir_reg(nome="arq01"):
        with open(f'arquivos/registros/{nome}.txt') as arquivo:
            b = (arquivo.read())
            return b


