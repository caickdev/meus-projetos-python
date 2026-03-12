import yagmail

def enviar_email_com_anexo(
    destinatario,
    assunto,
    corpo,
    caminho_anexo=None,
    remetente=None,
    senha_app=None
):
    """
    Envia e-mail simples ou com anexo usando yagmail + Gmail.
    - destinatario: e-mail do receptor (str ou lista)
    - assunto: título do e-mail
    - corpo: texto do corpo (pode ser HTML se quiser)
    - caminho_anexo: caminho completo do arquivo (ex: 'produtos_com_desconto.csv')
    """
    # Configurações - NÃO COMMIT NO GITHUB!
    if remetente is None:
        remetente = "emailremetente@gmail.com"  # Mude para o seu
    if senha_app is None:
        senha_app = "senha"  # A de 16 caracteres!

    # Cria o cliente yagmail
    yag = yagmail.SMTP(remetente, senha_app)

    # Envia
    try:
        yag.send(
            to=destinatario,
            subject=assunto,
            contents=corpo,
            attachments=caminho_anexo if caminho_anexo else None
        )
        print(f"E-mail enviado com sucesso para {destinatario}!")
    except Exception as e:
        print(f"Erro ao enviar: {e}")

# Teste simples (rode isso primeiro!)
if __name__ == "__main__":
    destinatario_teste = "emaildestinatario@gmail.com"  # Mude para um e-mail seu ou de teste
    assunto = "Teste de Automação Python - Relatório de Descontos"
    corpo = """
    Olá!

    Aqui vai um relatório automático gerado com Python.
    Anexo: produtos_com_desconto.csv

    Economize tempo com automações como essa! 🚀

    Abraços,
    Caick (Python Automations)
    """
    anexo = "produtos_com_desconto.csv"  # O CSV que você gerou antes (na mesma pasta)

    enviar_email_com_anexo(destinatario_teste, assunto, corpo, anexo)