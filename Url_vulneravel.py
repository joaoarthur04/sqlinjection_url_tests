import sys
import urllib
import urllib.request

argumento = sys.argv

def analise(fullurl):
    #Adicionar o caminho do arquivo
    arquivo = open('lista.txt', 'r')
    #Adicionar o caminho do arquivo
    logsfile = open('log_sqlinjection.txt', 'a')
    #linhas = arquivo.readlines()
    #print(linhas)
    print("##### Script created by ---- João Arthur ---######\n ###--Contact: joaoarthur04@hotmail.com --###")
    print("##### Date: ###")
    print("## Site:", fullurl ,"##")
    for linha in arquivo:
        #conteudoLinha = print(linha)
        try:
            resp = urllib.request.urlopen(fullurl + linha)
            body = resp.read()
            fullbody = body.decode('utf-8')
            #print(body)

            if "You have an error in your SQL syntax" in fullbody:
                print("Comando: "+ fullurl + linha +" -------- VULNERAVEL SQL injection! --------\n")
                logsfile.write("Url Vulneravel : " + fullurl + linha + "\n")
            else:
                print("Comando: "+ fullurl + linha +"-------- NÃO VULNERAVEL SQL injection! --------\n")
        except:
                print("Erro de URL")



if argumento[1]:
    print('Site para analise: ', argumento[1])
    resultado = analise(argumento[1])

else:
    print("Digite a url")
