import datetime
 
# pssd means password, ussnm is username
def user_information(ussnm, pssd):  
    name = input("enter your name please: ")
    address = input("your address")
    age = input("Your age please")
    ussnm_ = ussnm+" task.txt"
    f = open(ussnm_, 'a')
    f.write(pssd)
    f.write("\nName: ")
    f.write(name)
    f.write('\n')
    f.write("Address :")
 
    f.write(address)
    f.write('\n')
    f.write("Age :")
    f.write(age)
    f.write('\n')
    f.close()
 
 
def signup():
    print("Coloque o nome de usuário de sua conta")
    username = input("Nome:  ")
    password = input("Senha:  ")
    user_information(username, password)
    print("Prossiga com o Login")
    login()
 
 
def login():
    print("Insira seu nome de usuário ")
    user_nm = input("Insira aqui: ")
     
    # Password as entered while logging in
    pssd_wr = (input("Insira sua senha"))+'\n'
    try:
        usernm = user_nm+" task.txt"
        f_ = open(usernm, 'r')
         
        # variable 'k' contains the password as saved
        # in the file
        k = f_.readlines(0)[0]
        f_.close()
         
        # Checking if the Password entered is same as 
        # the password saved while signing in
        if pssd_wr == k:   
            print(
                "1--to view your data \n2--To add task \n3--Update\
                task \n4--VIEW TASK STATUS")
            a = input()
             
            if a == '1':
                view_data(usernm)
            elif a == '2':
                # add task
                task_information(usernm)
            elif a == '3':
                task_update(user_nm)
            elif a == '4':
                task_update_viewer(user_nm)
            else:
                print("Variável inválida. Tente novamente")
        else:
            print("Sua senha está errada. Tente novamente")
            login()
 
    except Exception as e:
        print(e)
        login()
 
 
def view_data(username):
    ff = open(username, 'r')
    print(ff.read())
    ff.close()
 
 
def task_information(username):
    print("Insira a quantidade de tarefas desejadas.")
    j = int(input())
    f1 = open(username, 'a')
     
    for i in range(1, j+1):
        task = input("Insira a tarefa")
        target = input("Insira a meta")
        pp = "TASK "+str(i)+' :'
        qq = "TARGET "+str(i)+" :"
         
        f1.write(pp)
        f1.write(task)
        f1.write('\n')
        f1.write(qq)
        f1.write(target)
        f1.write('\n')
        print("Deseja parar? Caso não, aperte espaço.")
        s = input()
        if s == ' ':
            break
    f1.close()
 
 
def task_update(username):
    username = username+" TASK.txt"
    print("Insira tarefas concluídas ")
    task_completed = input()
     
    print("Insira tarefas não concluídas")
    task_not_started = input()
     
    print("Insira tarefas no qual está fazendo agora.")
    task_ongoing = input()
     
    fw = open(username, 'a')
    DT = str(datetime.datetime.now())
    fw.write(DT)
    fw.write("\n")
    fw.write("TAREFA COMPLETA \n")
    fw.write(task_completed)
    fw.write("\n")
    fw.write("TAREFA EM ANDAMENTO \n")
    fw.write(task_ongoing)
    fw.write("\n")
    fw.write("NÃO COMEÇADA\n")
    fw.write(task_not_started)
    fw.write("\n")
 
 
def task_update_viewer(username):
    ussnm = username+" TASK.txt"
    o = open(ussnm, 'r')
    print(o.read())
    o.close()
 
 
if __name__ == '__main__':
    print("BEM VINDO AO GERENCIADOR DE TAREFAS")
    print("É sua primeira vez usando este programa?")
    a = int(input("Digite 1 se for, se não digite 0 ::"))
    if a == 1:
        signup()
    elif a == 0:
        login()
    else:
        print("Você digitou algo inválido.")