import tkinter as tk

# Fonction pour effectuer les calculs
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Erreur: {e}"

# Fonction pour gérer les clics sur les boutons
def on_button_click(value):
    current_text = entry.get()
    if value == "=":
        result = evaluate_expression(current_text)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice")

# Création de l'entrée pour afficher les expressions et les résultats
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Définition des boutons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Création des boutons et ajout à la grille
row, col = 1, 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 18),
              command=lambda b=button: on_button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Exécution de la boucle principale de l'application
root.mainloop()
if __name__ == "__main__":
    main()