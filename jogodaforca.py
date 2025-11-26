#Criando um jogo da forca
import random

def jogo_daforca(): 
    print("\nVoce selecionou o jogo da forca!! Deseja continuar? (s/n)") #mensagem inicial do game
    
    resposta = input(">>").lower() #interação com o usuário/ defini uma variável interativa 

    if resposta == "s": #se a resposta for "s"
        print("Oba, então vamos iniciar o game!!") 
    else: #mas se não...
        print("Que pena, mas volte sempre que quiser.")
    
    palavras = ["programador", "tecnologia", "notebook", "internet"] #abri uma variável lista, para definiar quais seriam as palavras do jogo.
    palv_jogo = random.choice(palavras) #essa função random choice irá sortear uma das palavras que eu pré defini na variávle acima.

    palavra_oculta = ["_" for _ in palv_jogo] #sublinhando cada letra da palavra sorteada

    print("A palavra da vez já foi sorteada para voçe adivinhar!!") #avisando o usuário que a palavra foi sorteada
    print("Palavra:", " ".join(palavra_oculta))
    print("Agora você deve iniciar as advinhações! Digite as letras até descobrir a palavra!")

    tentativas = 6
    palavras_certas = []
    palavras_erradas = []

    while "_" in palavra_oculta and tentativas > 0: #abrindo um laço com while
        letra = input("\nDigite uma letra: ").lower() 
        if letra in palv_jogo:
            if letra in palavras_certas:
                print(f"você já descobriu essa letra!")
            else:
                print("É isso aí!! \nLetra descoberta.")
                palavras_certas.append(letra)
                for indice, l in enumerate(palv_jogo):
                    if l == letra:
                        palavra_oculta[indice] = letra
        else:
            if letra in palavras_erradas:
                print(f"Você já digitou a letra {letra} e não há ela na palavra.")
            else:
                print("Essa letra não tem na palavra, tente novamente!")
                palavras_erradas.append(letra)
                tentativas -= 1  #diminui as tentativas
        
        #Mostrando o progresso da palavra para o usuário.
        print("\nPalavra", " ".join(palavra_oculta))
        print(f"\nAs tentativas restantes são: {tentativas}")
    
    if "_" not in palavra_oculta:
        print(f"\nParabéns!! Você venceu o game e descobriu a palavra que é: {palv_jogo}")
    else:
        print(f"Infelizmente as suas tentativas acabaram... \nMas a palavra era: {palv_jogo}")

jogo_daforca() 