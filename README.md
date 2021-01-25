# Questão 1

# Questão 2
> Procedimentos realizados em uma máquina Windows 10 com o Virtual Box. O procedimento é semelhante caso use uma distribuição linux com Virtual Box.

1. Instale o VirtualBox na máquina ( https://www.virtualbox.org/wiki/Downloads ).

2. Baixe o minishift ( https://github.com/minishift/minishift/releases ) e descompacte-o na raiz do seu drive ou diretório de sua preferência. 

3. Execute o prompt de comando ou powershell como administrador. 
No Windows, isso pode ser feito apertando o botão Windows + R, depois digitando cmd e apertando ctrl+shift+enter.

4. Com o terminal aberto, execute os comandos abaixo. Por exemplo, caso tenha descompactado na raiz do drive C:
```
C:\WINDOWS\system32>cd c:\minishift-1.34.3-windows-amd64
c:\minishift-1.34.3-windows-amd64>.\minishift.exe config set vm-driver virtualbox
c:\minishift-1.34.3-windows-amd64>.\minishift.exe start
```

> O processo pode demorar um bom tempo para ser finalizado. Após término, a plataforma minishift estará instalada.

5. Para facilitar os comandos a seguir, é necessário adicionar os comandos minishift e oc no PATH do Windows. Abra novamente a janela de executar com o botão Windows + R e digite `sysdm.cpl`. Na janela a seguir, clique na aba `Avançado` e depois em `Variáveis de Ambiente`.

Na janela `Variáveis do Sistema`, clique na linha PATH e depois em editar.

Clique em Novo e adicione o diretório do minishift e do oc. A imagem abaixo mostra um exemplo dos dois diretórios adicionados. Para o diretório do executável oc, não se esqueça de trocar para o seu usuário:

6. Abra um novo terminal como administrador e verifique se os caminhos foram adicionados corretamente. 
Ao digitar minishift status, ele deve retornar informações sobre o minishift.


7. Crie um novo projeto. Por exemplo, para se criar um projeto com o nome nexxees:
C:\>oc new-project nexxees 

8. Crie uma nova aplicação. Ela foi criada usando como base o exemplo do minishift, com as variáveis trocadas para o repositório atual:
C:\>oc new-app -f https://raw.githubusercontent.com/vbrake/nexxees/master/nginx.json

9. Ao final da criação, aparecerá no terminal uma url. O arquivo json pedido pela questão pode ser acessado digitando /nexxees.json ao final da url. Por exemplo, caso a url retornada seja a da imagem abaixo:

Deve-se digitar http://nginx-example-nexxees.192.168.99.101.nip.io/nexxees.json .

