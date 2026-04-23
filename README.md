# Emoji Cipher ✨

Uma aplicação web moderna e divertida, desenvolvida em Python com o micro-framework **Flask**. O Emoji Cipher permite transformar textos comuns em mensagens secretas compostas inteiramente por emojis, e vice-versa. 

Foi construído com uma interface premium e responsiva, focada na experiência do usuário, contendo suporte a Dark Mode, Glassmorphism e layouts específicos para impressão física.

## 🚀 Funcionalidades

- **Criptografia (Texto → Emojis):** Mapeia letras (A-Z) e números (0-9) para emojis pré-definidos. Os espaços são mantidos intactos para facilitar a leitura das palavras formadas, e caracteres não mapeados são ignorados automaticamente.
- **Descriptografia (Emojis → Texto):** Realiza o caminho reverso, traduzindo sequências de emojis perfeitamente de volta para a linguagem legível.
- **Dicionário Interativo:** Exibe a tabela de correspondência (Alfabeto vs. Emoji) dinamicamente logo abaixo da conversão, para rápida consulta.
- **Modo Impressão Inteligente:** Layout preparado via `@media print`. Ao tentar imprimir a tela, a aplicação oculta os botões, cabeçalhos e fundos coloridos, gerando uma folha branca limpa contendo apenas a mensagem secreta e a legenda do dicionário.

## 🏗️ Arquitetura

O projeto foi organizado utilizando conceitos de **Clean Architecture**, visando testabilidade e separação de responsabilidades:
- **`src/domain/`**: Núcleo da lógica de negócios. Contém as regras do Alfabeto (`EmojiAlphabet`) e as engrenagens da Cifra (`EmojiCipher`), totalmente isolados da interface gráfica.
- **`src/application/`**: Casos de uso e orquestração. Define o dicionário de mapeamento padrão e fornece serviços limpos para a camada superior.
- **`src/presentation/`**: A interface de usuário. Configura a API e o servidor Flask (`web.py`), os templates HTML e os ativos estáticos (CSS Vanilla, JS Vanilla).

## 🛠️ Instalação e Execução Local

### Pré-requisitos
- Python 3.12+

### Passo a Passo

1. **Clone o repositório e acesse a pasta:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd emoji-cipher
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o servidor de desenvolvimento:**
   ```bash
   flask --app src.presentation.web run --port=5000 --debug
   ```

5. Abra o navegador em `http://127.0.0.1:5000/`.

## 🧪 Rodando os Testes

A lógica de domínio e de conversão é testada de ponta a ponta com **pytest**.
Com o ambiente virtual ativado, basta rodar:
```bash
pytest tests/
```

## ☁️ Hospedagem / Produção

O projeto está configurado e pronto para produção, possuindo suporte nativo a servidores WSGI modernos por meio da biblioteca `gunicorn` e pelo ponto de entrada `wsgi.py` criado na raiz do repositório.

Para rodar localmente como se estivesse em um servidor de produção:
```bash
gunicorn wsgi:app
```

---
*Desenvolvido com carinho para codificar mensagens de forma lúdica!*
