# Xadrez
### Acesso aos artefatos de gerenciamento e planejamento do projeto
[Google Drive](https://drive.google.com/drive/folders/1SsH0biSJyUlAqar0ZKFkENHfKmZAPPcP?usp=sharing)

## Como executar o jogo
### Executando o arquivo main.py pelo terminal
Assumindo que você já tem o python instalado na sua máquina, caso não, siga as instruções no [site oficial](https://www.python.org/downloads/).

Após isso, devemos instalar as dependências do projeto:
#### Windows:
`pip install pygame`
#### macOS:
`python3 -m pip install pygame`
#### Linux:
`pip3 install pygame`

Depois disso, podemos rodar o arquivo main.py estando na raiz do projeto:

#### Windows:
`python main.py`
#### macOS:
`python3 main.py`
#### Linux:
`python3 main.py`

### Criando um executável através do PyInstaller

O PyInstaller é um módulo Python que pode ser usado para criar executáveis a partir de scripts Python. Portanto pode-se criar um único arquivo que pode ser executado em qualquer sistema que tenha o Python instalado, sem a necessidade de instalar bibliotecas ou dependências adicionais.

### Instalando o PyInstaller
Para instalar o PyInstaller, deve-se usar os seguintes comandos:
#### Windows:
`pip install pyinstaller`

#### Linux:
`pip3 install pyinstaller`

### Criando um executável
Para criar um executável a partir de um script Python, deve-se usar o seguinte comando:
`pyinstaller -n Xadrez -F -w main.py`

Isso irá criar uma pasta chamada dist no mesmo diretório do seu script Python. A pasta conterá um arquivo executável chamado Xadrez.exe (no Windows) ou Xadrez (no Linux). Após isto, é necessário copiar a pasta assets para dentro da pasta dist.

**Observação (Linux):**

No Linux, pode ser necessário executar o seguinte comando antes de criar seu executável:

`export LD_LIBRARY_PATH=/usr/local/lib/python3.8/site-packages`

Caso encontre algum problema ao criar um executável com o PyInstaller, consulte a [documentação do PyInstaller](https://pyinstaller.readthedocs.io/en/stable/) para obter ajuda.
