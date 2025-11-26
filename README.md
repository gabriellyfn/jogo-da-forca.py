# 🪢 Jogo da Forca – Python

Este projeto é uma implementação simples e divertida do clássico **Jogo da Forca**, desenvolvida em Python. O objetivo é adivinhar uma palavra secreta sorteada aleatoriamente antes que as tentativas acabem.

---

## 🎮 Como o jogo funciona

1. O usuário é perguntado se deseja iniciar o jogo.
2. Uma palavra é sorteada automaticamente de uma lista.
3. O jogador tenta adivinhar a palavra digitando uma letra por vez.
4. O jogador possui **6 tentativas** para errar.
5. O jogo mostra:

   * As letras já descobertas
   * As letras erradas
   * As tentativas restantes
   * O progresso da palavra sendo revelada

---

## 🧠 Lógica principal

* Utilização do módulo `random` para sortear palavras.
* A palavra secreta é representada inicialmente por `_`.
* O jogador tenta letras até:

  * acertar toda a palavra **(vitória)**
  * ou acabar as tentativas **(derrota)**.
* Verificações importantes:

  * Se a letra existe na palavra
  * Se já foi digitada antes
  * Se deve atualizar a palavra oculta

---

## 📌 Estrutura do código

### ✔️ Sorteio da palavra

```
palavras = ["programador", "tecnologia", "notebook", "internet"]
palv_jogo = random.choice(palavras)
```

### ✔️ Criação dos underlines

```
palavra_oculta = ["_" for _ in palv_jogo]
```

### ✔️ Loop principal

```
while "_" in palavra_oculta and tentativas > 0:
    letra = input("\nDigite uma letra: ").lower()
```

### ✔️ Atualização da palavra

```
for indice, l in enumerate(palv_jogo):
    if l == letra:
        palavra_oculta[indice] = letra
```

---

## ▶️ Como executar

1. Certifique-se de ter Python instalado.
2. Clone o repositório:

   ```sh
   git clone https://github.com/gabriellyfn/jogo-da-forca.py.git
   ```
3. Execute o programa:

   ```sh
   python jogo_da_forca.py
   ```

---

## 💡 Possíveis melhorias

* Adicionar interface gráfica.
* Criar níveis de dificuldade.
* Permitir que o usuário cadastre palavras.
* Mostrar desenho da forca visualmente.

---

## 🧑‍💻 Autora

Projeto desenvolvido por **gabriellyfn** como prática de Python.
