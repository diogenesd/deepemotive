# TUTORIAL INSTALAÇÃO DEEP-EMOTIVE #

DEEP-EMOTIVE
Trabalho de conclusão de curso - Ciência da Computação - FURB - 2017
Autor: Diogenes Ademir Domingos
Contato: k.fus@hotmail.com

## Este tutorial serve como referência para execução do protótipo DEEP-EMOTIVE.

### Download do protótipo
1. Os fontes do protótipo estão disponíveis no github: https://github.com/diogenesd/deepemotive
	1.1 realizar o download via comandos git ou zip

### Download da base de dados
1. Base de dados utilizada no desenvolvimento do protótipo: http://www.consortium.ri.cmu.edu/ckagree/
	1.1 Separar imagens. Cada uma das oito emoção em uma pasta distinta.
		--Alegria
			--file_alegria_01.jpg
			--file_alegria_02.jpg
			...
		--Tristeza
			--file_tristeza_01.jpg
			...
		....
	1.2 Inserir as as pastas criadas no diretório ./imagens
2. Bases de dados utilizada para transferência de aprendizado
	2.1 Download da base de dados JAFFE: http://www.kasrl.org/jaffe.html
	2.1.1 Copiar esta base de dados para o diretório: ./transfer learning/jaffeimages/original
	2.2 Download da base de dados FER2013: https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data
	2.2.1 Copiar esta base de dados para o diretório: ./transfer learning/fer2013

	
### Instalar gerenciador de pacotes.
1. Instalar o gerenciado de pacotes Anaconda: https://www.anaconda.com/download/
2. Configuar Anaconda como variavel de ambiente (path) do sistema operacional
	2.1 Setar no path a pasta: ~/<User>/Anaconda3/Scripts

### Criar ambientes de trabalho
1. Criar o ambiente de virtual de trabalho do fluxo principal:	
	1.1 Abrir um terminal de comando
	1.2 Navegar até o diretório de configuração: ~/<dir_protótipo>/config
	1.3 Executar o comando: conda create -f deepemotive.yml
2. Criar o ambiente de virtual de trabalho da segmentação de faces:
	2.1 Abrir um terminal de comando	
	2.2 Navegar até o diretório de configuração: ~/<dir_protótipo>/config
	2.3 Executar o comando: conda create -f segmentacao.yml
3. Para maiores informações de gerenciamento de ambientes virtuais: https://conda.io/docs/user-guide/tasks/manage-environments.html

### Download da biblioteca OpenCV
1. Realizar o download da biblioteca: http://opencv.org
2. Copiar os fontes da biblioteca OpenCV para a pastas ./opencv no diterório do protótipo

### Caso ocorra algum problema de dependencia de biblioteca
1. Instalar requirequirements 
	1.1 Abrir um terminal de comando
	1.2 Navegar até o diretório de configuração: ~/<dir_protótipo>/config
	1.3 Ativar ambimente de segmentacao: (Plataforma Windows) activate deepemotive
	1.4 Executar o comando: pip install -r requirements.txt

### Executar a segmentação da faces
1 Ativar o ambiente de trabalho de segmentacao
	1.1 Abrir um terminal de comando
	1.2 Navegar até o diretório onde esta os fontes do protótipo
	1.3 Ativar ambimente de segmentacao: (Plataforma Windows) activate segmentacao
	1.4 Para ativar o ambiente em outro sistemas operacionais consulte: https://conda.io/docs/user-guide/tasks/manage-environments.html
2. Executar o Jupyter Notebook no diretório do protótipo
	2.1 Com o ambiente ativo executar o comando: jupyter notebook
	2.2 Será aberto uma pagina de internet com o home do protótipo
3. Abrir script de segmentacao
	3.1 abrir arquivo: DeepEmotive - Detecção da face.ipynb
4. Seguir o script passo passo

### Executar o fluxo principal
1 Ativar o ambiente de trabalho de deepemotive
	1.1 Abrir um terminal de comando
	1.2 Navegar até o diretório onde esta os fontes do protótipo
	1.3 Ativar ambimente de segmentacao: (Plataforma Windows) activate deepemotive
	1.4 Para ativar o ambiente em outro sistemas operacionais consulte: https://conda.io/docs/user-guide/tasks/manage-environments.html
2. Executar o Jupyter Notebook no diretório do protótipo
	2.1 Com o ambiente ativo executar o comando: jupyter notebook
	2.2 Será aberto uma pagina de internet com o home do protótipo
3. Abrir script de segmentacao
	3.1 Abrir arquivo: DeepEmotive - Fluxo Principal.ipynb
4. Seguir o script passo passo

### Executar a transferência de aprendizado
1. Deve estar ativado o ambiente de trabalho deepemotive
2. Executar o Jupyter Notebook no diretório do protótipo, caso necessário
	2.1 Com o ambiente ativo executar o comando: jupyter notebook
	2.2 Será aberto uma pagina de internet com o home do protótipo
3. Abrir script de transferência de aprendizado
	3.1 Abrir arquivo: DeepEmotive - Transfer Learning - FER2013.ipynb
	3.2 DeepEmotive - Transfer Learning - JAFFE.ipynb
4. Seguir o script passo passo	