import tkinter as tk
import sqlite3


conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL
    )
''')

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

def cadastrar_produto():
    nome = nome_entry.get()
    preco = float(preco_entry.get())
    quantidade = int(quantidade_entry.get())

    produto = Produto(nome, preco, quantidade)
    salvar_produto(produto)
    print("Produto cadastrado com sucesso!")

   
    nome_entry.delete(0, tk.END)
    preco_entry.delete(0, tk.END)
    quantidade_entry.delete(0, tk.END)

def salvar_produto(produto):
    cursor.execute('''
        INSERT INTO produtos (nome, preco, quantidade)
        VALUES (?, ?, ?)
    ''', (produto.nome, produto.preco, produto.quantidade))
    conn.commit()

def exibir_produtos():
    produtos_listbox.delete(0, tk.END)
    cursor.execute('SELECT * FROM produtos')
    for row in cursor:
        produto = Produto(row[1], row[2], row[3])
        produtos_listbox.insert(tk.END, f"Nome: {produto.nome}, Preço: {produto.preco}, Quantidade: {produto.quantidade}")

window = tk.Tk()
window.title("Cadastramento de Produtos")


nome_label = tk.Label(window, text="Nome:")
nome_label.pack()
nome_entry = tk.Entry(window)
nome_entry.pack()

preco_label = tk.Label(window, text="Preço:")
preco_label.pack()
preco_entry = tk.Entry(window)
preco_entry.pack()

quantidade_label = tk.Label(window, text="Quantidade:")
quantidade_label.pack()
quantidade_entry = tk.Entry(window)
quantidade_entry.pack()

cadastrar_button = tk.Button(window, text="Cadastrar", command=cadastrar_produto)
cadastrar_button.pack()

produtos_listbox = tk.Listbox(window)
produtos_listbox.pack()

exibir_produtos_button = tk.Button(window, text="Exibir Produtos", command=exibir_produtos)
exibir_produtos_button.pack()


window.mainloop()


conn.close()