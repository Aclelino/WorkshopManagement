from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QTableWidget


# Carrega o arquivo QtDesing

app = QtWidgets.QApplication([])
ui = uic.loadUi('lib/cadastroCliente.ui')

# tamando da tabela geometry

ui.tableWidget.setGeometry(100,100,300,200)



def btSalvar():

    # coleta os dados escrito na caixa de texto 

    nome = ui.lineEditNome.text()
    cpf = ui.lineEditCpf.text()
    endereco = ui.lineEditEndereco.text()
    telefone = ui.lineEditTelefone.text()
    email = ui.lineEditEmail.text()

    # tranforma os dados em uma lista

    dados = [nome,cpf,endereco,telefone,email]
    select_Row = ui.tableWidget.currentRow() # linha selecionada da tabela
    # numero da linha
    print(select_Row)
    if select_Row != -1:
        print("cadastro eDITADO")
        row = select_Row

        ui.tableWidget.setRowCount(1 + row ) # soma o numero da linha
        ui.tableWidget.setColumnCount(len(dados)) # conta o numero de colunas
        ui.tableWidget.setItem(row,0,QTableWidgetItem(dados[0]))
        ui.tableWidget.setItem(row,1,QTableWidgetItem(dados[1]))
        ui.tableWidget.setItem(row,2,QTableWidgetItem(dados[2]))
        ui.tableWidget.setItem(row,3,QTableWidgetItem(dados[3]))
        ui.tableWidget.setItem(row,4,QTableWidgetItem(dados[4]))

    elif select_Row == -1:

        row = ui.tableWidget.rowCount() # linha
        ui.tableWidget.setRowCount(1 + row)  # soma o numero da linha
        ui.tableWidget.setColumnCount(len(dados))  # conta o numero de colunas
        ui.tableWidget.setItem(row, 0, QTableWidgetItem(dados[0]))
        ui.tableWidget.setItem(row, 1, QTableWidgetItem(dados[1]))
        ui.tableWidget.setItem(row, 2, QTableWidgetItem(dados[2]))
        ui.tableWidget.setItem(row, 3, QTableWidgetItem(dados[3]))
        ui.tableWidget.setItem(row, 4, QTableWidgetItem(dados[4]))

    # limpar os dados na caixa de texto 
   
    ui.lineEditNome.setText("")
    ui.lineEditCpf.setText("")
    ui.lineEditEndereco.setText("")
    ui.lineEditTelefone.setText("")
    ui.lineEditEmail.setText("")



def deletRow():
    select_row = ui.tableWidget.currentRow()
    if select_row > -1:
        ui.tableWidget.removeRow(select_row)
        print(select_row + 1 ,'coluna removida',)


def edit():
    
    select_row = ui.tableWidget.currentRow() # Mosta a linha selecionada
    nome = ui.tableWidget.item(select_row,0)
    cpf = ui.tableWidget.item(select_row, 1)
    endereco = ui.tableWidget.item(select_row, 2)
    telefone = ui.tableWidget.item(select_row, 3)
    email = ui.tableWidget.item(select_row, 4)

    if nome is not None:
        nome = nome.text()
        ui.lineEditNome.setText(str(nome))
    if cpf is not None:
        cpf = cpf.text()
        ui.lineEditCpf.setText(str(cpf))

    if endereco is not None:
        endereco = endereco.text()
        ui.lineEditEndereco.setText(str(endereco))

    if telefone is not None:
        telefone = telefone.text()
        ui.lineEditTelefone.setText(str(telefone))

    if email is not None:
        email = email.text()
        ui.lineEditEmail.setText(str(email))



  
# Acao do Botao Salvar 
    
ui.btSalvar.clicked.connect(btSalvar)
ui.btExcluir.clicked.connect(deletRow)
ui.btEditar.clicked.connect(edit)

# inicia o loop da tela

ui.show()
app.exec_()