carne = input("Digite o nome da carne:")
qts = float(input("Digite o quantidade em kg:"))
metodoPagamento = input("A compra e no cartão (Sim/Não):")

if carne.lower().replace(" ", "") == "fileduplo":
    if qts <= 5:
        fileDuplo = round(qts * 4.90, 2)
        fileDuploDesconto = round(fileDuplo, 2)

        if metodoPagamento.lower() == "sim":
            fileDuploDesconto = round(fileDuplo - (fileDuplo * 0.05), 2)

        print("\n*__________CUPOM FISCAL_________*")
        print("TIPO DE CARNE: File Duplo")
        print("QUANTIDADE DE CARNE:", qts, "KG")
        print("PREÇO TOTAL:", fileDuplo, "R$")
        print("TIPO DE PAGAMENTO NO CARTÃO:", metodoPagamento.upper())
        print("VALOR COM DESCONTO (5%):", fileDuploDesconto, "R$")
        print("VALOR A PAGAR", fileDuploDesconto, "R$")

    elif qts > 5:
        fileDuplo = round(qts * 5.80, 2)
        fileDuploDesconto = round(fileDuplo, 2)

        if metodoPagamento.lower() == "sim":
            fileDuploDesconto = round(fileDuplo - (fileDuplo * 0.05), 2)

        print("\n*__________CUPOM FISCAL_________*")
        print("TIPO DE CARNE: File Duplo")
        print("QUANTIDADE DE CARNE:", qts, "KG")
        print("PREÇO TOTAL:", fileDuplo, "R$")
        print("TIPO DE PAGAMENTO NO CARTÃO:", metodoPagamento.upper())
        print("VALOR COM DESCONTO (5%):", fileDuploDesconto, "R$")
        print("VALOR A PAGAR", fileDuploDesconto, "R$")

if carne.lower().replace(" ", "") == "alcantra":
    if qts <= 5:
        alcantra = round(qts * 5.90, 2)
        alcantraDesconto = round(alcantra, 2)

        if metodoPagamento.lower() == "sim":
            alcantraDesconto = round(alcantra - (alcantra * 0.05), 2)

        print("\n*__________CUPOM FISCAL_________*")
        print("TIPO DE CARNE: ALCANTRA")
        print("QUANTIDADE DE CARNE:", qts, "KG")
        print("PREÇO TOTAL:", alcantra, "R$")
        print("TIPO DE PAGAMENTO NO CARTÃO:", metodoPagamento.upper())
        print("VALOR COM DESCONTO (5%):", alcantraDesconto, "R$")
        print("VALOR A PAGAR", alcantraDesconto, "R$")

    elif qts > 5:
        alcantra = round(qts * 6.80, 2)
        alcantraDesconto = round(alcantra, 2)

        if metodoPagamento.lower() == "sim":
            alcantraDesconto = round(alcantra - (alcantra * 0.05), 2)

        print("\n*__________CUPOM FISCAL_________*")
        print("TIPO DE CARNE: ALCANTRA")
        print("QUANTIDADE DE CARNE:", qts, "KG")
        print("PREÇO TOTAL:", alcantra, "R$")
        print("TIPO DE PAGAMENTO NO CARTÃO:", metodoPagamento.upper())
        print("VALOR COM DESCONTO (5%):", alcantraDesconto, "R$")
        print("VALOR A PAGAR", alcantraDesconto, "R$")

if carne.lower().replace(" ", "") == "picanha":
    if qts <= 5:
        picanha = round(qts * 6.90, 2)
        picanhaDesconto = round(picanha, 2)

        if metodoPagamento.lower() == "sim":
            fileDuploDesconto = round(picanha - (picanha * 0.05), 2)

        print("\n*__________CUPOM FISCAL_________*")
        print("TIPO DE CARNE: PICANHA")
        print("QUANTIDADE DE CARNE:", qts, "KG")
        print("PREÇO TOTAL:", picanha, "R$")
        print("TIPO DE PAGAMENTO NO CARTÃO:", metodoPagamento.upper())
        print("VALOR COM DESCONTO (5%):", picanhaDesconto, "R$")
        print("VALOR A PAGAR", picanhaDesconto, "R$")

    elif qts > 5:
        picanha = round(qts * 7.80, 2)
        picanhaDesconto = round(picanha, 2)

        if metodoPagamento.lower() == "sim":
            picanhaDesconto = round(picanha - (picanha * 0.05), 2)

        print("\n*__________CUPOM FISCAL_________*")
        print("TIPO DE CARNE: PICANHA")
        print("QUANTIDADE DE CARNE:", qts, "KG")
        print("PREÇO TOTAL:", picanha, "R$")
        print("TIPO DE PAGAMENTO NO CARTÃO:", metodoPagamento.upper())
        print("VALOR COM DESCONTO (5%):", picanhaDesconto, "R$")
        print("VALOR A PAGAR", picanhaDesconto, "R$")

else:
    print("Produto invalido")