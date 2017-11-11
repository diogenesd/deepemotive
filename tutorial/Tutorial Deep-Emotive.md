# TUTORIAL DEEP-EMOTIVE #

DEEP-EMOTIVE
Trabalho de conclusão de curso - Ciência da Computação - FURB - 2017
Autor: Diogenes Ademir Domingos
Contato: k.fus@hotmail.com

## Este tutorial serve como referência para execução do protótipo DEEP-EMOTIVE.

### Download do protótipo
1. Os fontes do protótipo estão disponíveis no github: https://github.com/diogenesd/deepemotive<br>
2. Realizar o download via comandos git ou zip

### Download da base de dados
1. Base de dados utilizada no desenvolvimento do protótipo: http://www.consortium.ri.cmu.edu/ckagree/<br>
	1.1 Criar oito pastas. Cada pasta representa uma emoção da base de dados.<br>
	1.2 Inserir as pastas criadas no diretório `./imagens`
	<dl>
	  <dt>--Alegria</dt>
		<dd>--file_alegria_01.jpg</dd>
		<dd>--file_alegria_02.jpg</dd>
		<dd>...</dd>
	  <dt>--Tristeza</dt>
		<dd>--file_tristeza_01.jpg</dd>
		<dd>...</dd>
	 <dt>...</dt>
	</dl>
2. Bases de dados utilizada para transferência de aprendizado<br>
	2.1 Download da base de dados JAFFE: http://www.kasrl.org/jaffe.html<br>
		2.1.2 Colar esta base de dados para o diretório: `./transfer learning/jaffeimages/original.`<br>
	2.2 Download da base de dados FER2013: https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data.<br>
		2.2.1 Colar esta base de dados para o diretório: `./transfer learning/fer2013.`<br>

	
### Instalar gerenciador de pacotes.
1. Instalar o gerenciado de pacotes Anaconda: https://www.anaconda.com/download/<br>
2. Configuar Anaconda como variável de ambiente **(path)** do sistema operacional<br>
	2.1 Setar no path a pasta: `~/<usuario>/Anaconda3/Scripts`<br>

### Criar ambientes de trabalho
1. Criar o ambiente de virtual de trabalho do fluxo principal:<br>
	1.1 Abrir um terminal de comando<br>
	1.2 Navegar até o diretório de configuração: `cd ~/<dir_protótipo>/config`<br>
	1.3 Executar o comando: `conda create -f deepemotive.yml`<br>
2. Criar o ambiente de virtual de trabalho da segmentação de faces:<br>
	2.1 Abrir um terminal de comando<br>
	2.2 Navegar até o diretório de configuração: `cd ~/<dir_protótipo>/config`<br>
	2.3 Executar o comando: `conda create -f segmentacao.yml`<br>
3. Para maiores informações de gerenciamento de ambientes virtuais: https://conda.io/docs/user-guide/tasks/manage-environments.html<br>

### Download da biblioteca OpenCV
1. Realizar o download da biblioteca: http://opencv.org<br>
2. Abrir um terminal de comando<br>
	2.1 Navegar até o diretório do protótipo: `cd ~/<dir_protótipo>/`<br>
2. Colar os fontes da biblioteca OpenCV para a pasta **./opencv/** no diterório do protótipo<br>

### Caso ocorra algum problema de dependencia de biblioteca
1. Instalar requirequirements<br>
	1.1 Abrir um terminal de comando<br>
	1.2 Navegar até o diretório de configuração: `~/<dir_protótipo>/config`<br>
	1.3 Ativar ambimente de segmentacao: **(Plataforma Windows)** `activate deepemotive`<br>
	1.4 Executar o comando: `pip install -r requirements.txt`<br>

### Executar a segmentação da faces
1 Ativar o ambiente de trabalho de segmentacao<br>
	1.1 Abrir um terminal de comando<br>
	1.2 Navegar até o diretório do protótipo: `cd ~/<dir_protótipo>/`<br>
	1.3 Ativar ambimente de segmentacao: **(Plataforma Windows)** `activate segmentacao`<br>
	1.4 Para ativar o ambiente em outro sistemas operacionais consulte: https://conda.io/docs/user-guide/tasks/manage-environments.html<br>
2. Executar o Jupyter Notebook no diretório do protótipo<br>
	2.1 Com o ambiente ativo executar o comando: `jupyter notebook`<br>
	2.2 Será aberto uma pagina de internet com o home do protótipo<br>
3. Abrir script de segmentacao<br>
	3.1 abrir arquivo: **DeepEmotive - Detecção da face.ipynb**<br>
4. Seguir o script passo passo<br>

### Executar o fluxo principal
1 Ativar o ambiente de trabalho de deepemotive<br>
	1.1 Abrir um terminal de comando<br>
	1.2 Navegar até o diretório do protótipo: `cd ~/<dir_protótipo>/`<br>
	1.3 Ativar ambimente de segmentacao: **(Plataforma Windows)** `activate deepemotive`<br>
	1.4 Para ativar o ambiente em outro sistemas operacionais consulte: https://conda.io/docs/user-guide/tasks/manage-environments.html<br>
2. Executar o Jupyter Notebook no diretório do protótipo<br>
	2.1 Com o ambiente ativo executar o comando: `jupyter notebook`<br>
	2.2 Será aberto uma pagina de internet com o home do protótipo<br>
3. Abrir script de segmentacao<br>
	3.1 Abrir arquivo: **DeepEmotive - Fluxo Principal.ipynb**<br>
4. Seguir o script passo passo<br>

### Executar a transferência de aprendizado
1. Deve estar ativado o ambiente de trabalho deepemotive<br>
2. Executar o Jupyter Notebook no diretório do protótipo, caso necessário<br>
	2.1 Com o ambiente ativo executar o comando: `jupyter notebook`<br>
	2.2 Será aberto uma pagina de internet com o home do protótipo<br>
3. Abrir script de transferência de aprendizado<br>
	3.1 Abrir arquivo: **DeepEmotive - Transfer Learning - FER2013.ipynb**<br>
	3.2 Abrir arquivo: **DeepEmotive - Transfer Learning - JAFFE.ipynb**<br>
4. Seguir o script passo passo<br>

## DEMO ##

Para utilizar o demo deve seguir os procedimentos abaixo.<br>
Para este procedimento é necessário que a rede neural já esteja treinada.<br>
Será utilizado os pesos do treino realizado pela rede DEEP-EMOTIVE.<br>

### Executar script DEMO ###
1. Abrir um terminal de comando
2. Navegar até o diretório do protótipo: `cd ~/<dir_protótipo>/`
3. Ativar ambimente de segmentacao: **(Plataforma Windows)** `activate deepemotive`
4. Reconhecer uma imagem:
	4.1 Executar o script **"classificar_emocao"**: `python classificar_emocao.py -m "<caminho_da_imagem_a_ser_reconhecida>"`
5. Reconhecer várias imagens:
	5.1 Executar o script **"classificar_emocao"**: `python classificar_emocao.py -d "<caminho_do_diretório_de_imagens_a_serem_reconhecidas>"`
