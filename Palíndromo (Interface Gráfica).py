import tkinter as tk
from tkinter import messagebox

def verificar_palindromo():
    palavra = entrada.get().strip()
    if palavra == palavra[::-1] and palavra:
        resultado = f"'{palavra}' é um Palíndromo!"
    elif not palavra:
        resultado = "Por favor, insira uma palavra!"
    else:
        resultado = f"'{palavra}' não é um Palíndromo."
    
    messagebox.showinfo("Resultado", resultado)

# Criando a janela principal
janela = tk.Tk()
janela.title("Verificador de Palíndromo")
janela.geometry("400x300")  # Tamanho da janela
janela.configure(bg="#f0f0f0")  # Cor de fundo

# Estilo de fonte
font_style = ("Arial", 14)

# Criando um rótulo
rotulo = tk.Label(janela, text="Digite uma palavra:", font=font_style, bg="#f0f0f0", fg="#333")
rotulo.pack(pady=20)

# Criando uma caixa de entrada
entrada = tk.Entry(janela, font=font_style, width=25, bd=2, relief=tk.SUNKEN)
entrada.pack(pady=10)

# Criando um botão
botao = tk.Button(janela, text="Verificar", command=verificar_palindromo, font=font_style, bg="#4CAF50", fg="white", bd=0, padx=10)
botao.pack(pady=20)

# Criando um rótulo de instrução
instrucoes = tk.Label(janela, text="Pressione o botão para verificar.", font=font_style, bg="#f0f0f0", fg="#666")
instrucoes.pack(pady=10)

# Executando a aplicação
janela.mainloop()
