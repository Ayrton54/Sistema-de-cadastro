from cProfile import label
import re
from tkinter import *
from tkinter import Tk,StringVar,ttk
from tkinter import messagebox
from turtle import fd
from PIL import Image,ImageTk
from tkcalendar import Calendar,DateEntry
from datetime import date
from view import *
from tkinter import filedialog as fd

#cores
c00 ="#f5f0b8"
c01 ="#f5eeee"#branco
c02 ="#f2f055"#amarelo
c03 ="#84c7e2"#azul claro
c04 = "#03c78a"#verde
c05 ="#df2a2a"#vermelho
c06="#da6523"#laranja
c07 ="#040404"#preto
c08 ="#1b2eec"#azul forte

#Criando janela
janela =Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=c01)
janela.resizable(width=False,height=False)

style =ttk.Style(janela)
style.theme_use("clam")

#Criando Frames

frameCima = Frame(janela,width=1043,height=50,bg=c01,relief=FLAT)
frameCima.grid(row=0,column=0)

#frame meio
framemeio = Frame(janela,width=1043,height=303,pady=20, bg=c01,relief=FLAT)
framemeio.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)
#Frame abaixo
framebaixo = Frame(janela,width=1043,height=300, bg=c01,relief=FLAT)
framebaixo.grid(row=2,column=0,pady=0,padx=1,sticky=NSEW)

#criando funcões----------------------------------------------------
global tree
#funcões inseir
def inseir():
    global imagem,imagem_string,l_imagem
    nome = e_nome.get()
    local = e_local.get()
    Descrição = e_Descrição.get()
    model = e_model.get()
    data = e_cal.get()
    valor = e_valor.get()
    serie = e_serie.get()
    imagem = imagem_string

    lista_inserir = [nome,local,Descrição,model,data,valor,serie,imagem]

    for i in lista_inserir:
        if i =='':
            messagebox.showerror('Erro','Preencha todos os campos ')
            return
    inserir_form(lista_inserir)

    messagebox.showinfo('Sucesso','Os dados foram inseridos com sucesso')

    e_nome.delete(0,'end')
    e_local.delete(0,'end')
    e_Descrição.delete(0,'end')
    e_model.delete(0,'end')
    e_cal.delete(0,'end')
    e_valor.delete(0,'end')
    e_serie.delete(0,'end')
    mostrar()    
    
# Atualizar
def atualizar():
    global imagem,imagem_string,l_imagem
    try: 
        treev_dados = tree.focus()
        tree_dicionario = tree.item(treev_dados)
        treev_lista = tree_dicionario['values']

        valor = treev_lista[0]

        e_nome.delete(0,'end')
        e_local.delete(0,'end')
        e_Descrição.delete(0,'end')
        e_model.delete(0,'end')
        e_cal.delete(0,'end')
        e_valor.delete(0,'end')
        e_serie.delete(0,'end')   


        id = int(treev_lista[0])
        e_nome.insert(0,treev_lista[1])
        e_local.insert(0,treev_lista[2])
        e_Descrição.insert(0,treev_lista[3])
        e_model.insert(0,treev_lista[4])
        e_cal.insert(0,treev_lista[5])
        e_valor.insert(0,treev_lista[6])
        e_serie.insert(0,treev_lista[7]) 
        imagem_string = treev_lista[8]


        def update():
            global imagem,imagem_string,l_imagem

            nome = e_nome.get()
            local = e_local.get()
            Descrição = e_Descrição.get()
            model = e_model.get()
            data = e_cal.get()
            valor = e_valor.get()
            serie = e_serie.get()
            imagem = imagem_string

            if imagem == '':
                imagem =e_serie.insert(0,treev_lista[7]) 

            lista_atualizar = [nome, local, Descrição, model, data, valor,
            serie, imagem,id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror('Erro','Preencha todos os campos')
                    return
            atualizar_(lista_atualizar)
            messagebox.showinfo('Sucesso','Os dados foram atualizados com sucesso')

            e_nome.delete(0,'end')
            e_local.delete(0,'end')
            e_Descrição.delete(0,'end')
            e_model.delete(0,'end')
            e_cal.delete(0,'end')
            e_valor.delete(0,'end')
            e_serie.delete(0,'end') 

            btn_confirmar.destroy()
            mostrar()

        btn_confirmar =Button(framemeio,command=update,text='  Confirmar'.upper(),width=13,overrelief=RIDGE ,font=('Ivy 8 bold'),bg=c03,fg=c07)
        btn_confirmar.place(x=330,y=185)
    except IndexError:
        messagebox.showerror('Erro','selecione um dos dados da tabela')
    

# Deletar
def deletar():
    
    try: 
        treev_dados = tree.focus()
        tree_dicionario = tree.item(treev_dados)
        treev_lista = tree_dicionario['values']

        valor = treev_lista[0]

        deletar_([valor])
       
        messagebox.showinfo('Sucesso','Os dados foram deltados com sucesso')
        mostrar()
    except IndexError:
        messagebox.showerror('Erro','selecione um dos dados da tabela')
    

#função para escolher imagem
global imagem,imagem_string,l_imagem
def escolher_img():
    global imagem,imagem_string,l_imagem
    imagem =fd.askopenfilename()
    imagem_string = imagem
    #abrindo imagem
    imagem=Image.open(imagem)
    imagem=imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(framemeio,image=imagem, bg=c01,fg=c07)
    l_imagem.place(x=700,y=10)

# função veer imagem
def ver_imagem():
    global imagem,imagem_string,l_imagem
    treev_dados = tree.focus()
    tree_dicionario = tree.item(treev_dados)
    treev_lista = tree_dicionario['values']

    valor = [int(treev_lista[0])]
    iten = ver_item(valor)
    imagem = iten[0][8]

    #abrindo imagem
    imagem=Image.open(imagem)
    imagem=imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(framemeio,image=imagem, bg=c01,fg=c07)
    l_imagem.place(x=700,y=10)

#primeiro frame
#abrindo imagem
app_img=Image.open("imagens/img.png")
app_img=app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima,image=app_img, text=" Inventário",width=900,compound=LEFT,relief=RAISED,anchor=NW,font=('Verdana 20 bold'),bg=c01,fg=c07)
app_logo.place(x=0,y=0)

# segundo frame
#Criando entradas
l_nome =Label(framemeio,text='Nome',height=1,anchor=NW,font=('Ivy 10 bold'),bg=c01,fg=c07)
l_nome.place(x=10,y=10)
e_nome =Entry(framemeio,width=30,justify='left',relief='solid')
e_nome.place(x=130,y=11)

l_local =Label(framemeio,text='local',height=1,anchor=NW,font=('Ivy 10 bold'),bg=c01,fg=c07)
l_local.place(x=10,y=40)
e_local=Entry(framemeio,width=30,justify='left',relief='solid')
e_local.place(x=130,y=41)

l_Descrição =Label(framemeio,text='Descrição',height=1,anchor=NW,font=('Ivy 10 bold'),bg=c01,fg=c07)
l_Descrição.place(x=10,y=70)
e_Descrição =Entry(framemeio,width=30,justify='left',relief='solid')
e_Descrição.place(x=130,y=71)


l_model =Label(framemeio,text='Marca/modelo',height=1,anchor=NW,font=('Ivy 10 bold'),bg=c01,fg=c07)
l_model.place(x=10,y=100)
e_model =Entry(framemeio,width=30,justify='left',relief='solid')
e_model.place(x=130,y=101)

l_cal =Label(framemeio,text='Data da compra',height=1,anchor=NW,font=('Ivy 10 bold'),bg=c01,fg=c07)
l_cal.place(x=10,y=130)
e_cal =DateEntry(framemeio,width=12,bg=c03,bordewidth=2,year=2022)
e_cal.place(x=130,y=131)

l_valor =Label(framemeio,text='Valor do produto',height=1,anchor=NW,font=('Ivy 10 bold'),bg=c01,fg=c07)
l_valor.place(x=10,y=160)
e_valor =Entry(framemeio,width=30,justify='left',relief='solid')
e_valor.place(x=130,y=161)

l_serie =Label(framemeio,text='Número de série',height=1,anchor=NW,font=('Ivy 10 bold'),bg=c01,fg=c07)
l_serie.place(x=10,y=190)
e_serie =Entry(framemeio,width=30,justify='left',relief='solid')
e_serie.place(x=130,y=191)

#criando botões---------------


#botão carregar
l_carregar =Label(framemeio,text='Imagem do item',height=1,anchor=NW,font=('Ivy 10 bold'),bg=c01,fg=c07)
l_carregar.place(x=10,y=220)
btn_carregar =Button(framemeio,command=escolher_img,width=29, text='CARREGAR',compound=CENTER,overrelief=RIDGE ,anchor=CENTER,font=('Ivy 8'),bg=c00,fg=c07)
btn_carregar.place(x=130,y=221)

#Botão add
add_img=Image.open("imagens/add.png")
add_img=add_img.resize((20,20))
add_img = ImageTk.PhotoImage(add_img)

btn_add =Button(framemeio,command=inseir,text='  Adicionar'.upper(),image=add_img,width=95,compound=LEFT,anchor=NW,overrelief=RIDGE ,font=('Ivy 8'),bg=c04,fg=c07)
btn_add.place(x=330,y=10)

#Botão atualizar
atualizar_img=Image.open("imagens/atualizar.png")
atualizar_img=atualizar_img.resize((20,20))
atualizar_img = ImageTk.PhotoImage(atualizar_img)

btn_atualizar =Button(framemeio,command=atualizar,text='  Atualizar'.upper(),image=atualizar_img,width=95,compound=LEFT,anchor=NW,overrelief=RIDGE ,font=('Ivy 8'),bg=c03,fg=c07)
btn_atualizar.place(x=330,y=50)

#Botão delete
delete_img=Image.open("imagens/delete.png")
delete_img=delete_img.resize((20,20))
delete_img = ImageTk.PhotoImage(delete_img)

btn_delete =Button(framemeio,command=deletar,text='  delete'.upper(),image=delete_img,width=95,compound=LEFT,anchor=NW,overrelief=RIDGE ,font=('Ivy 8'),bg=c05,fg=c07)
btn_delete.place(x=330,y=90)

#Botão ver item
item_img=Image.open("imagens/item.png")
item_img=item_img.resize((20,20))
item_img = ImageTk.PhotoImage(item_img)

btn_item =Button(framemeio,command=ver_imagem,text='  Ver item'.upper(),image=item_img,width=95,compound=LEFT,anchor=NW,overrelief=RIDGE ,font=('Ivy 8'),bg=c01,fg=c07)
btn_item.place(x=330,y=217)

# Valor total , quantidade
# valor total
l_total =Label(framemeio,text='',width=14,height=2,anchor=CENTER,font=('Ivy 17 bold'),bg=c06,fg=c07)
l_total.place(x=450,y=15)
l_total_ =Label(framemeio,text=' Valor total de todos os produtos    ',height=1,anchor=NW,font=('Ivy 9 bold'),bg=c06,fg=c07)
l_total_.place(x=450,y=0)

#quantidade
l_qtd =Label(framemeio,text='',width=14,height=2,anchor=CENTER,font=('Ivy 17 bold'),bg=c06,fg=c07)
l_qtd.place(x=450,y=90)
l_qtd_ =Label(framemeio,text=' Quantidade total de produtos          ',height=1,anchor=CENTER,font=('Ivy 9 bold'),bg=c06,fg=c07)
l_qtd_.place(x=450,y=83)


# Descrições

def mostrar():
        global tree

        tabela_head = ['#Item','Nome',  'local','Descrição', 'Marca', 'Data da compra',"valor da compra", 'Número de série']

        
        lista_itens =ver_form()
 
        tree = ttk.Treeview(framebaixo, selectmode="extended",columns=tabela_head, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(framebaixo, orient="vertical", command=tree.yview)

        # horizontal scrollbar
        hsb = ttk.Scrollbar(framebaixo, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')
        framebaixo.grid_rowconfigure(0, weight=12)

        hd=["center","center","center","center","center","center","center", 'center']
        h=[40,150,100,160,130,100,100, 100]
        n=0

        for col in tabela_head:
            tree.heading(col, text=col.title(), anchor=CENTER)
            # adjust the column's width to the header string
            tree.column(col, width=h[n],anchor=hd[n])
            n+=1


        # inserindo os itens dentro da tabela
        for item in lista_itens:
            tree.insert('', 'end', values=item)

        quantidade=[]
 
        for iten in lista_itens:  
            
            quantidade.append(iten[6])
            
        Total_valor = sum(quantidade)
    
        Total_itens = len(quantidade)


        l_total['text']='R$ {:,.2f}'.format(Total_valor)
        l_qtd['text'] =  Total_itens
        



mostrar()




janela.mainloop()

