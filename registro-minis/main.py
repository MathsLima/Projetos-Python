import tkinter as tk
import mysql.connector
from tkinter import ttk

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'miniaturas',
)
cursor = conexao.cursor()

bg = "#34495E"
letras = "#FDFEFE"

class App:
    #configura o metodo da classe principal
    def __init__(self, root):
        #tela inicial
        self.root = root
        self.root.title('Registro Miniaturas')
        self.root.geometry("300x225")
        self.root.resizable(width=False, height=False)

        #conteiner principal
        self.container_principal = tk.Frame(root)
        self.container_principal.pack(expand=True, fill="both")
        self.container_principal.configure(background=bg  )

        #serve para armazenar o tamanho do menu
        self.tamanho_inicial = "300x225"

        #variavel que aramzena a treeview
        self.treeview_pagina_2 = None

        #inicia a tela inicial com o menu
        self.tela_inicial()
        self.resultados = self.consulta()
    
    #funcao para alterar as paginas
    def muda_janela(self):
        for widget in self.container_principal.winfo_children():
            widget.destroy()
    

    #tela inicial com o menu
    def tela_inicial(self):
        self.muda_janela()

        label_tela_inicial = tk.Label(self.container_principal, text="Sistema de Cadastro de Miniaturas", font=('Calibri', 13), bg=bg, fg=letras)
        label_tela_inicial.place(width=250, height=40, x=25, y=10)

        botao_pagina_1 = tk.Button(self.container_principal, text="Cadastrar Miniatura", command=self.pagina_1)
        botao_pagina_1.place(width=200, height=40, x=50, y=60)

        botao_pagina_2 = tk.Button(self.container_principal, text="Consultar Coleção", command=self.pagina_2)
        botao_pagina_2.place(width=200, height=40, x=50, y=110)

        botao_pagina_3 = tk.Button(self.container_principal,text="Excluir Miniatura", command=self.pagina_3)
        botao_pagina_3.place(width=200, height=40, x=50, y=160)

        #deixa com o menu com o tamanho inicial
        self.root.geometry(self.tamanho_inicial)


    #pagina de cadastro de miniaturas
    def pagina_1(self):
        self.muda_janela()
        self.root.geometry("485x350")

        label_titulo = tk.Label(self.container_principal, text="Cadastrar Miniaturas", font=('Calibri', 18), bg=bg, fg=letras)
        label_titulo.place(width=300, height=25, x=100, y=15)

        botao_voltar = tk.Button(self.container_principal, text="⬅ Voltar", command=self.tela_inicial)
        botao_voltar.place(width=65, height=25, x=400, y=15)

        label_modelo = tk.Label(self.container_principal, text="Modelo:", font=('Calibri', 15), bg=bg, fg=letras)
        label_modelo.place(width=75, height=30, x=25, y=75)

        input_modelo = tk.Entry(self.container_principal)
        input_modelo.place(width=250, height=30, x=125, y=75)

        label_cor = tk.Label(self.container_principal, text="Cor:", font=('Calibri', 15), bg=bg, fg=letras)
        label_cor.place(width=75, height=30, x=8, y=125)

        input_cor = tk.Entry(self.container_principal)
        input_cor.place(width=250, height=30, x=125, y=125)

        label_marca = tk.Label(self.container_principal, text="Marca:", font=('Calibri', 15), bg=bg, fg=letras)
        label_marca.place(width=75, height=30, x=17, y=175)

        input_marca = tk.Entry(self.container_principal)
        input_marca.place(width=250, height=30, x=125, y=175)

        label_colecao = tk.Label(self.container_principal, text="Coleção:", font=('Calibri', 15), bg=bg, fg=letras)
        label_colecao.place(width=75, height=30, x=22, y=225)

        input_colecao = tk.Entry(self.container_principal)
        input_colecao.place(width=250, height=30, x=125, y=225)

        adicionar = tk.Button(self.container_principal, text="Adicionar na coleção", 
                              font=('Calibri', 15),
                              command=lambda: [self.adicionar_miniatura(input_modelo.get(), input_cor.get(), input_marca.get(), input_colecao.get()),
                                               input_modelo.delete("0", "end"), 
                                               input_cor.delete("0", "end"),
                                               input_marca.delete("0", "end"),
                                               input_colecao.delete("0", "end"),
                                               self.alerta_inserido()])
        
        adicionar.place(width=200, height=30, x=150, y=280)


    def pagina_2(self):
        self.muda_janela()
        self.root.geometry("600x400")

        label_titulo = tk.Label(self.container_principal, text="Consulta de Miniaturas", font=('Calibri', 18), bg=bg, fg=letras)
        label_titulo.place(width=300, height=25, x=150, y=15)

        botao_voltar = tk.Button(self.container_principal, text="⬅ Voltar", command=self.tela_inicial)
        botao_voltar.place(width=75, height=25, x=510, y=15)

        #se existe uma treeview ela é destruida antes de criar uma nova 
        if self.treeview_pagina_2:
            self.treeview_pagina_2.destroy()
        
        self.treeview_pagina_2 = self.treeview()
        self.scrollbar(self.treeview_pagina_2)

        # quantidade = self.quantidade()
        label_quantidade = tk.Label(self.container_principal, text=f'Quantidade: {len(self.resultados)}', font=('Calibri', 15), bg=bg, fg=letras)
        label_quantidade.place(width=300, height=25, x=150, y=40)


    def pagina_3(self):
        self.muda_janela()
        self.root.geometry("350x300")

        label_titulo = tk.Label(self.container_principal, text="Deletar Miniatura", font=('Calibri', 18), bg=bg, fg=letras)
        label_titulo.place(width=300, height=25, x=0, y=15)
        
        label_id = tk.Label(self.container_principal, text="Digite o ID", font=('Calibri', 15), bg=bg, fg=letras)
        label_id.place(width=100, height=30, x=125, y=75)

        input_id = tk.Entry(self.container_principal)
        input_id.place(width=100, height=30, x=125, y=115)

        deletar = tk.Button(self.container_principal, text="Deletar", 
                              font=('Calibri', 15),
                              command=lambda: [self.deletar(input_id.get()),
                                                input_id.delete("0", "end"),
                                                self.alerta_deletado()])
        
        deletar.place(width=100, height=30, x=125, y=175)
        
        botao_voltar = tk.Button(self.container_principal, text="⬅ Voltar", command=self.tela_inicial)
        botao_voltar.place(width=75, height=25, x=260, y=15)

    
    #funcao para adicionar miniaturas no banco de dados
    def adicionar_miniatura(self, modelo, cor, marca, colecao):
        comando = f'INSERT INTO minis (modelo, cor, marca, colecao) VALUES ("{modelo}", "{cor}", "{marca}", "{colecao}")'
        cursor.execute(comando)
        conexao.commit()
    

    #funcao para consultar o banco
    def consulta(self):
        comando = f'SELECT * FROM minis'
        cursor.execute(comando)
        return cursor.fetchall()
    

    #funcao para criar a treeview
    def treeview(self):
        tv = ttk.Treeview(self.container_principal)    
        tv['show'] = 'headings'
        
        estilo = ttk.Style(self.root)
        estilo.theme_use('clam')

        tv["columns"] = ("INDEX", "ID", "Modelo", "Cor", "Marca", "Colecao")

        for column_name in tv["columns"]:
            tv.column(column_name, width=50, minwidth=50, anchor=tk.CENTER)
            tv.heading(column_name, text=column_name, anchor=tk.CENTER)

        for i, root in enumerate(self.resultados):
            tv.insert('', i, text='batata', values=(i, root[0], root[1], root[2], root[3], root[4]))

        tv.place(width=530, height=300, x=30, y=75)

        return tv

    def deletar(self, id):
        comando = f'DELETE from minis WHERE idminis = {id} '
        cursor.execute(comando)
        conexao.commit()

    def scrollbar(self, treeview):
        scrollbar = ttk.Scrollbar(self.container_principal, orient="vertical", command=treeview.yview)
        scrollbar.place(x=560, y=75, height=300)
        
        treeview.configure(yscrollcommand=scrollbar.set)
    

    def alerta_inserido(self):
        popup  =tk.Toplevel(self.root)
        popup.geometry("200x80")
        popup.title("Alerta")
        popup.resizable(width=False, height=False)
        mensagem_popup = tk.Label(popup, text="Miniatura inserida!", font=('Calibri', 13))
        mensagem_popup.pack(pady=10)
        botao_ok = tk.Button(popup, text="OK", command=popup.destroy)
        botao_ok.pack()
    

    def alerta_deletado(self):
        popup  =tk.Toplevel(self.root)
        popup.geometry("200x80")
        popup.title("Alerta")
        popup.resizable(width=False, height=False)
        mensagem_popup = tk.Label(popup, text="Miniatura Deletada!", font=('Calibri', 13))
        mensagem_popup.pack(pady=10)
        botao_ok = tk.Button(popup, text="OK", command=popup.destroy)
        botao_ok.pack()
    
#inicia a aplicacao e fecha conexao com banco
root = tk.Tk()
app = App(root)
root.mainloop()
cursor.close()
conexao.close()
