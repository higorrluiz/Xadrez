# Xadrez
### Acesso aos artefatos de gerenciamento e planejamento do projeto
[Google Drive](https://drive.google.com/drive/folders/1SsH0biSJyUlAqar0ZKFkENHfKmZAPPcP?usp=sharing)

## Criando um executável através do PyInstaller

O PyInstaller é um módulo Python que pode ser usado para criar executáveis a partir de scripts Python. Portanto pode-se criar um único arquivo que pode ser executado em qualquer sistema que tenha o Python instalado, sem a necessidade de instalar bibliotecas ou dependências adicionais.

### Instalando o PyInstaller
Para instalar o PyInstaller, deve-se usar os seguintes comandos:
#### Windows:
`pip install pyinstaller`
#### macOS:
`python3 -m pip install pyinstaller`
#### Linux:
`pip3 install pyinstaller`

### Criando um executável
Para criar um executável a partir de um script Python, deve-se usar o seguinte comando:
`pyinstaller -n Xadrez -F -w main.py`

Isso irá criar uma pasta chamada dist no mesmo diretório do seu script Python. A pasta conterá um arquivo executável chamado Xadrez.exe (no Windows) ou Xadrez (no macOS e Linux). Após isto, é necessário copiar a pasta assets para dentro da pasta dist.

**Observação (macOS e Linux):**
No macOS, pode ser necessário executar o seguinte comando antes de criar seu executável:

`export DYLD_LIBRARY_PATH=/usr/local/opt/python/lib`

No Linux, pode ser necessário executar o seguinte comando antes de criar seu executável:

`export LD_LIBRARY_PATH=/usr/local/lib/python3.8/site-packages`

Caso encontre algum problema ao criar um executável com o PyInstaller, consulte a [documentação do PyInstaller](https://pyinstaller.readthedocs.io/en/stable/) para obter ajuda.
