import pandas as pd
from datetime import datetime
import email.message
import smtplib
from time import sleep
import pyautogui as pg
from flask import Flask, request, jsonify
from flask_cors import CORS
from logica import process_data


# pg.hotkey('win', 'r')
# pg.write('cmd')
# pg.press('enter')
# sleep(0.5)
# pg.write('ipconfig')
# pg.press('enter')
# sleep(0.3)
# pg.write('hostname')
# pg.press('enter')





# Criar uma instância da aplicação Flask
app = Flask(__name__)
CORS(app)

# Definir o endpoint para a rota '/dados'
@app.route('/dados', methods=['POST'])
def receber_dados():
    # Verificar se os dados foram enviados corretamente como JSON
    if request.is_json:
        # Obter os dados enviados no corpo da requisição
        dados = request.json
        resultado = process_data(dados)  # Chama a função de lógica para processar os dados
        return jsonify(resultado)
        # Processar os dados como desejado (nesse exemplo, apenas retornamos os dados recebidos)
    else:
        return jsonify({"mensagem": "Dados inválidos"}), 400
    

@app.route('/')
def hello():
    return'hello world'

# Rodar o servidor da API localmente na porta 5000
if __name__ == '__main__':
    app.run()







# vendas_df = pd.read_excel(r"C:\Users\HenriquePaganiTorres\OneDrive - TECMES\Área de Trabalho\Python\Projetos teste\Reservar.xlsx")

# empresas = ''

# for row, index in vendas_df.iterrows():
#     #print(row)
#     empresas = index[2]
#     print(empresas)
#     data_venda = index[3]
#     #print(data_venda)
#     data_formatada = data_venda.strftime("%d-%m-%Y")
#     print(data_formatada)





# def enviar_email():
#     corpo_email = f"""<p>Vai nada irmao<p>"""

#     msg = email.message.Message()
#     msg['Subject'] = "Instalação CATIA V5"
#     msg['From'] = 'henrique.pgtorres44@gmail.com'
#     msg['To'] = 'gustavo.pellegrina@tecmes.com.br'
#     password = 'pbtbxecyyhfaqymg'
#     msg.add_header('Content-type', 'text/html')
#     msg.set_payload(corpo_email)

#     s = smtplib.SMTP('smtp.gmail.com: 587')
#     s.starttls()

#     s.login(msg['From'], password)
#     s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))

# enviar_email()


    




