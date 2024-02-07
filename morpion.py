import tkinter as tk


# impossibre fermer root1 quand win
# probleme avec bg black
# peut être faire un bouton rejouer sur le root2

class Morpion:
    def __init__(self):
        # partie logique
        self.matrix = [["_","_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

        self.root = tk.Tk()
        self.root.configure(background='white')
        self.buttons = []
        self.control = 1
        

        for i in range(9):
            button = tk.Button(self.root,
                               width=25,
                               height=15,
                               font=50,
                               text="",
                               bg='black',
                               fg='white',
                               command=lambda index=i: self.button(index))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)
        self.root.mainloop()

        

    def change_button_text(self, index: int) -> None:
        if self.buttons[index]['text'] != "":
            return
        if 0 <= index < len(self.buttons):
            self.buttons[index].config(text=self.wich_text(index))
    


    # command du bouton
    def button(self, index: int) -> None:
        self.change_button_text(index)

    def play(self, index: int, text: str):
        test = 0
        self.matrix[index//3][index%3] = text
        if self.check_win(self.matrix):
            if self.control == 1:
                winner = "X"
            else:
                winner = "O"
            print(f"Bravo joueur {winner} c'est gagné")
            self.root.quit()
            test = 1
        if test == 1:
            self.root_win = tk.Tk()            
            self.new_method(winner)


    def new_method(self, winner):
        self.label_win = tk.Label(self.root,
                                        height=100,
                                        width = 100,
                                        text = f"Bravo au joueur {winner}, c'est gagné",
                                        fg='white',
                                        bg='white'
                                        )
        self.root_win.mainloop()
            
    




    # choisi le texte à mettre entre O ou X 
    def wich_text(self, index: int) -> str:
        text = ""
        if self.control == 1:
            text = "O"
              
        if self.control == -1:
            text = "X"
        self.control *= -1
        self.play(index, text)
        return text

    # check win in any cases: 
    def check_lign(self, m):
        for i in range(3):
            sommel = ""
            for j in range(3):
                sommel += m[i][j]
            if all(char == sommel[0] for char in sommel) and sommel[0] != '_':
                return True
        return False


    def check_column(self, m):
        for i in range(3):
            sommec = ""
            for j in range(3):
                sommec += m[j][i]
            if all(char == sommec[0] for char in sommec) and sommec[0] != '_':
                return True
        return False

    def check_diagonal(self, m):
        somme_d1 = ""
        somme_d2 = ""
        for i in range(3):
            somme_d1 += m[i][i]
            somme_d2 += m[2 - i][i]
        
        if all(char == somme_d1[0] for char in somme_d1) and somme_d1[0] != '_':   
            return True
        if all(char == somme_d2[0] for char in somme_d2) and somme_d2[0] != '_':   
            return True     
        return False
        
    def check_win(self, m):
        if self.check_column(m):
            return True
        if self.check_lign(m):
            return True
        if self.check_diagonal(m):
            return True
        return False
    


if __name__ == "__main__":
    Morpion()

