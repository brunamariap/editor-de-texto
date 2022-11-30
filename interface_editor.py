import keyboard
from tkinter import *
from doubly_linked_list import DoublyLinkedList

master = Tk()
master.title('Editor de texto')
master.geometry('954x650+317+34')
master.wm_resizable() #não permitir que a tela possa ser redimensionada

def limpar():
    text_description.delete('1.0', END)
    lista.clear()

# criação de frames
frame_description = Frame(master, bg="#85B777")
frame_description.place(width=801, height=579, x=12, y=21)

#criação da barra lateral, scroll
barra_lateral1 = Scrollbar(frame_description) #subir e descer o texto
barra_lateral1.pack(side=RIGHT, fill=Y)

# criação das caixas de texto
text_description = Text(frame_description, font=('Calibri', 16), selectbackground='#F5F799', selectforeground='black', wrap=WORD, undo=True, yscrollcommand=barra_lateral1.set)
text_description.place(width=784, height=579, x=0, y=0)

#configurando a barra lateral
barra_lateral1.config(command=text_description.yview) #associa a barra lateral ao texto que ela representa, a função faz a barra aumentar enquanto o texto diminui e diminuir se o texto aumenta

# Criação dos botões
bt2 = Button(master, text="Limpar", font=("Calibri", 16), background='white', command=limpar)
bt2.place(width=80, height=52, x=834, y=123)

lista = DoublyLinkedList()

alphabet = 'abcdefghijklmnopqrstuvwxyzç'
keyboard.block_key('up')
keyboard.block_key('down')
def press_backspace(event):
    lista.delete_last()
    print()
    lista.print_list()

def press_right(event):
    lista.mover('right')
    print()
    lista.print_list()

def press_left(event):
    lista.mover('left')
    print()
    lista.print_list()

def key_press(event):
    key = event.char
    if key in alphabet or key in alphabet.upper() or ' ':
        lista.insert(key)
        print()
    lista.print_list()

master.bind('<Key>', key_press) # Vincula uma função a uma tecla pressionada
master.bind("<BackSpace>", press_backspace)
master.bind("<Right>", press_right)
master.bind("<Left>", press_left)

master.mainloop()
#lista.print_list()