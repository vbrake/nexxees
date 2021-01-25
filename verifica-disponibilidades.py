import urllib.request
import subprocess
import os
import json
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
_email = ''
_msg = MIMEMultipart()

#Executa comando para descobrir qual url da aplicacao e cria url com o json
_output = subprocess.run(['oc', 'get', 'route', 'nginx-example', "--template='{{ .spec.host }}'"], stdout=subprocess.PIPE, universal_newlines=True)
_output.stdout = "http://" + _output.stdout.strip("'") + "/nexxees.json"

#Verifica se url esta no ar. Caso esteja, salva quais servicos estao down. 
#Caso nao esteja, finaliza script com descricao de erro.
try:
  with urllib.request.urlopen(_output.stdout) as f:
    _json = f.read().decode('utf-8')
    _json = json.loads(_json)
    for key, value in _json['service'].items():
      if value == 'down':
        _email += str("Servico " + key + " esta fora do ar." + '\n')
except urllib.error.URLError as e:
  _erro = "Erro ao acessar json: " + e.reason + ". Finalizando script..."
  sys.exit(_erro)

#Comandos para se conectar ao email e enviar mensagem indicando quais servicos estao down.
_server = smtplib.SMTP('smtp.gmail.com: 587')
_server.starttls()
_msg['Subject'] = "Servicos down"
_msg['From'] = "alertanxs@gmail.com"
_msg['To'] = "alertanxs@gmail.com"
_msg.attach(MIMEText(_email, 'plain'))
_server.login(_msg['From'], "nexxeesprovapratica")
_server.sendmail(_msg['From'], _msg['To'], _email)
_server.quit()
 
print("Email enviado com sucesso para %s" % (_msg['To']))
