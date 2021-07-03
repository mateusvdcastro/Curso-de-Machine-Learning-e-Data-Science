# -*- coding: utf-8 -*-
"""Disparos de Email.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dYDMxhmxGhpwqgY06gKAS-o0exbefbNd
"""
# esse código pode ser feito mais facilmente no google Colab que linka com o google drive
# pip install openpyxl
import xlrd
import pandas as pd

tabela_vendas = pd.read_excel("Vendas.xlsx", engine='openpyxl')

tabela_faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
tabela_faturamento = tabela_faturamento.sort_values(by='Valor Final', ascending=False)

tabela_quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

ticket_medio = (tabela_faturamento['Valor Final'] / tabela_quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Medio'})
print(ticket_medio)


def enviar_email(nome_loja, tabela):
    import smtplib
    import email.message
    server = smtplib.SMTP('smtp.gmail.com:587')
    # editar linha abaixo
    corpo_email = f"""                         
    <p>Prezados, </p>
    <p>Segue relatório de vendas </p>
    {tabela.to_html()}   
    <p> Qualquer dúvida estou à disposição </p>
    """
    # editar linha abaixo
    msg = email.message.Message()
    msg['Subject'] = f"Mateus Castro- {nome_loja}"

    # Fazer antes (apenas na 1ª vez): Ativar Aplicativos não Seguros.
    # Gerenciar Conta Google -> Segurança -> Aplicativos não Seguros -> Habilitar
    # Caso mesmo assim dê o erro: smtplib.SMTPAuthenticationError: (534,
    # Você faz o login no seu e-mail e depois entra em: https://accounts.google.com/DisplayUnlockCaptcha
    msg['From'] = 'mateusvc1124@gmail.com'
    msg['To'] = 'mateusvc11@gmail.com'
    password = "1424738wsE"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# enviar para a diretoria uma tabela mais ampla
tabela_completa_diretoria = tabela_faturamento.join(tabela_quantidade).join(ticket_medio)
enviar_email('Castro Company', tabela_completa_diretoria)

# enviar para as demais 25 lojas
lista_lojas = tabela_vendas['ID Loja'].unique()

for loja in lista_lojas:
    tabela_loja = tabela_vendas.loc[tabela_vendas['ID Loja'] == loja, ['ID Loja', 'Quantidade', 'Valor Final']]
    resumo_loja = tabela_loja.groupby('ID Loja').sum()
    resumo_loja['Ticket Medio'] = resumo_loja['Valor Final'] / tabela_loja['Quantidade']
    enviar_email(loja, resumo_loja)
