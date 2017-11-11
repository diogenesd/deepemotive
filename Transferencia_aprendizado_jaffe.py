
# coding: utf-8

# encoding: UTF-8
# Copyright Diogenes Ademir Domingos 2017
# Authored by Diogenes Ademir Domingos (k.fus@hotamil.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# biblioteca para trabalhar com imagens
from PIL import Image
import numpy as np
import sys,getopt
from keras.models import model_from_json, load_model
from keras import backend as K
from keras import optimizers
import os

# para criação do dataset em x_train, x teste
from sklearn.model_selection import train_test_split
# Modulo Scikit-Learn para montar a matriz de confusão
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, f1_score, cohen_kappa_score
# Importando Lib de utilidades (https://keras.io/utils/)
from keras.utils import np_utils
# modulo de callback para parar o treinamento na melhor opção
from keras.callbacks import EarlyStopping, ModelCheckpoint


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def main(argv):
	
	help = """Transferência de aprendiado.
		Este script e responsavel por realizar a predicao
		de uma ou varias imagens em uma base de teste não treinada.
		Recebe como parametro o caminho do diretorio contendo 
		todas as imagens a serem preditas.

		Args:
			-d <CAMINHO_DO_DIRETORIO> : varias imagens
			"""
	
	def identificar_emocao(filename):
		""" Esta função é responsável criar os descritores
			da base de dados JAFFE. Recebe o nome do arquivo
			e extrai o descritor.

			Args:
				filename (string): nome do arquivo

			Returns:
				int : descritor da emoção na imagem
			"""
		em = filename.split('.')
		if em[1][:2] == "AN":
			return 0
		elif em[1][:2] == "DI":
			return 1
		elif em[1][:2] == "FE":
			return 2
		elif em[1][:2] == "HA":
			return 3
		elif em[1][:2] == "NE":
			return 4
		elif em[1][:2] == "SA":
			return 5
		elif em[1][:2] == "SU":
			return 6
	
	def carregar_imagens(path):
		""" Esta função é responsável por importar as imagens para 
			o protótipo. Recebe como entrada o caminho do diretório
			onde as imagens estão localizadas. Retorna uma lista 
			de tuplas de duas posições. A primeira posição é o
			objeto de imagem e a segunda é a emoção da imagem.

			Args:
				path (string): caminho do diretório onde as imagens 
				estão localizadas.

			Returns:
				tuple (len=2): tupla contendo objeto imagem e emoção.
		"""  
		imagens = [] # lista para guardar as faces segmentadas
		files = [f for f in os.listdir(path)]
		
		print('Carregando imagens...')
		for file in files:  # para cada imagem
			
			path_img = path + '\\' + file #caminho absoluto
			im = Image.open(path_img) # obj PIL
			im = im.resize(shape, Image.ANTIALIAS)
			im = im.convert('L') # coverte imagem para escala de cinza.
			imagens.append((im, identificar_emocao(file))) # insere face an lista
				
		print('Imagens carregadas com sucesso!')
		print('Quantidade de imagens: ',len(imagens))
		return imagens
	
	# Função auxiliar para extrair os pixels da imagem
	def get_pixels_image(imagem):
		pixel_values = np.array(list(imagem.getdata()))
		pixel_values = pixel_values.reshape((img_cols,img_rows))
		#print(type(pixel_values))
		return pixel_values
	
	# verificando paramentros
	flag = False
	if sys.argv[1] == '-h':
		print (help)
		#print ('classificar_emocao.py -m <CAMINHO_DO_DIRETORIO')
		sys.exit()
	elif sys.argv[1] =='-d':
		path = sys.argv[2]
	else:
		print('Verifique o caminho da imagens ou do diretório.')
		print('digite: <file> <-h> para obte ajuda.')
		sys.exit(2)
	
	# lista de emoções conhecidas pelo sistemas
	classes_emocoes = ['raiva','desgosto','medo','alegria','neutra','tristeza','surpresa']
	# importando a imagem e redimensionando
	img_cols,img_rows = 98,98
	shape = (98,98)
	
	print('*' * 50)

	print('Importando imagens:',path)
	imagens = carregar_imagens(path) # Abrir imagens
	
	if imagens is None:
		print('Verifique o caminho da imagens ou do diretório.')
		print('digite: <file> <-h> para obte ajuda.')
		sys.exit(2)
	else:
		### EXTRAIR PIXELS DA IMAGEM ###
		# Criando a conjunto de dados
		data = []
		array_emocoes = []

		print("Extraindo os dados...")
		# para cada imagem
		for imagem in range(len(imagens)):
			# extrai o array de pixels
			data.append(get_pixels_image(imagens[imagem][0]))
			# extrai a emocao
			array_emocoes.append(imagens[imagem][1])
		 
		print("Quantidade de imagens extraidas:",len(data))
		print("Quantidade de emocoes extraidas:",len(array_emocoes))
	
	# empilha a tupla de imagens: data = (quantidade, largara, altura)
	print("Empilhando conjunto imagem para tupla: (quantidade, largara, altura)...")
	data = np.stack(data)

	# empilha a tupla de emocoes: data = (quantidade, )
	print("Empilhando conjunto emocoes para tupla: (quantidade,)...")
	labels = np.stack(array_emocoes)

	print("Extracão de dados completa!")
	print("Formato das imagens:", data.shape)
	print("Formato das emocoes:", labels.shape)
	print()
	
	# organizando dados para trabalhar com o keras
	(X, y) = (data, labels)
	
	print('Separando os dados em grupo de treino e teste...')
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state= len(imagens))

	print('Imagens separadas para treino: ',X_train.shape)
	print('Imagens separadas para teste: ',X_test.shape)
	print('Emoções separadas para treino: ',y_train.shape)
	print('Emoções separadas para teste: ',y_test.shape)
	
	### CONFIGURAR SHAPE PARA DEEP LEARNING ###
	print("Adicionando a quantidade de canais de cores na estrutura de dados...")
	# O framework theano trabalha com a quantidade de canais de cores a frente da dimesão da imagem
	if K.image_data_format() == 'channels_first': # = th
		shape = (1, img_cols, img_rows)
		#shape = (1, img_cols, img_rows)
		print("Trabalhando com theano")
		
	# O framework tensorflow trabalha com a quantidade de canais de cores apos a dimesão da imagem
	else:  # channel_last = tf
		shape = (img_cols, img_rows, 1)
		#shape = (img_cols, img_rows, 1)
		print("Trabalhando com tensorflow")
	print("Novo formato para estrutura de dados contendo o canal de cor: ",shape)

	# configurando o shape para 4D
	# Alterando o formato dos dados incluindo a estrutura com canal de cor
	print('Alterando o formato das imagens colocando a estrutura com canal de cor...')
	X_train = X_train.reshape((X_train.shape[0],) + shape).astype('float32')
	X_test = X_test.reshape((X_test.shape[0],) + shape).astype('float32')
	print('Novo formato das imagens separadas para treino: ',X_train.shape)
	print('Novo formato das imagens separadas para teste: ',X_test.shape)

	print('Novo formato dos pixles da imagem: ',X_test.shape)
	X_train /= 255
	X_test /= 255
	print("Preparacao da imagem completa!\n")
	
	# Criando a classificação
	# Converte um vetor de classe (inteiros) em matriz de classe verdade (binária).
	print('Criando a matriz de classificação binária...')

	# Classificando imagens
	Y_train = np_utils.to_categorical(y_train)
	# classificando as emocoes
	Y_test = np_utils.to_categorical(y_test)

	# verificando a quantidade de classes encontradas para as imagens
	num_classes = Y_train.shape[1]
	print('Classes encontradas para imagens: ', num_classes)

	# Visualizando alguns dados da matriz verdade das classes 
	num_emocoes = Y_test.shape[1]
	print('Classes encontradas para emocoes: ', num_emocoes)
	
	# adicionando coluna on-hot para a emoção desprezo que não tem nessa database
	# ultima coluna sempre sera 0

	# Cria a coluna
	extra_on_hot_Y_train = np.zeros(len(Y_train)).astype('float32')
	extra_on_hot_Y_test = np.zeros(len(Y_test)).astype('float32')

	# Adiciona a matriz já existente
	Y_train = np.hstack((Y_train, np.atleast_2d(extra_on_hot_Y_train).T))
	Y_test = np.hstack((Y_test, np.atleast_2d(extra_on_hot_Y_test).T))

	print(Y_train[0:5])
	print(Y_test[0:5])
	print(Y_test.shape)
	print(Y_train.shape)
	
	
	### CARREGAR MODELO DEEPEMOTIVE ###
	print('*' * 50)
	# Carregando o modelo salvo
	# Lendo o modelo salvo em arquivo para um novo modelo
	MODELO_SALVO_JSON = './modelos/deep_emotive_model_t10_faces.json'
	print("Carregando o modelo...")
	json_file = open(MODELO_SALVO_JSON, 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	print('Modelo carregado com sucesso!\n')
	
	### CARREGAR MELHORES PESOS DE TTREINAMENTO DA REDE DEEPEMOTIVE ###
	MELHORES_PESOS = '/pesos/pesos_teste_10-266-0.96.3.hdf5'
	# Carregando o melhor pesos do checkout para para o novo modelo
	print("Carregando os melhores pesos...")
	loaded_model.load_weights(MELHORES_PESOS)
	# Compilando o modelo que estava salvo
	# lr: taxa de aprendizado
	# decay: tamanho do passo da caída do gradiente
	adam = optimizers.Adam(lr=1e-3, decay=1e-5)    
	# Copilando o modelo
	# métrica de reconhecimento será precisão.
	loaded_model.compile(loss = 'categorical_crossentropy', 
						optimizer = adam, metrics = ['accuracy'])
	print("Carregamento dos melhores pesos completo!\n")
	print('*' * 50)

	#loaded_model.summary()

	# Utilizando o modelo para predição.
	# Verifica a probabilidade de ser uma das 8 emoções
	# Criar lista on-hot das predições.
	# Selecionando o indice da predição
	print('*' * 50)
	
	print('*' * 50)
	print("Congelando as camadas convolucionais para que não sejam treinadas...\n")
	# resetando o treino anterior
	for layer in loaded_model.layers:
		 layer.trainable = False
		 
	print('Verificando se configurou corretamente!')
	loaded_model.summary()
	print('*' * 50)
	
	### TREINANDO O CLASSIFICADOR ###
	# chekpoint para salvar o mehlor aprendizado enter as epocas
	filepath="./pesos/checkpoint-transfer-learning-jaffe-{epoch:02d}-{val_acc:.2f}.hdf5"
	checkpoint = ModelCheckpoint(filepath,  # caminho para o modelo salvo
								 monitor= 'val_acc', # qual parametro vai acompanhar
								 verbose=0, # verbosity - 0 or 1
								 save_best_only= True, # sobreescreve o modelo apenas se for o melhor
								 mode='auto') # dependecia de acorco com o monitor
	
	callback_list = [checkpoint]
	
	print("Treinando o classificador...")
	history = loaded_model.fit(X_train, Y_train, validation_data=(X_test, Y_test), callbacks=callback_list, epochs=30, batch_size=128, verbose=0)
	print('Treinanmeto finalizado!')
	
	MELHOR_PESO = './pesos/checkpoint-transfer-learning-jaffe-29-0.97.67.hdf5'
	# Carregando o melhor pesos do checkout para para o novo modelo
	print("Carregando os melhores pesos...")
	loaded_model.load_weights(MELHOR_PESO)

	# Compilando o modelo que estava salvo
	# lr: taxa de aprendizado
	# decay: tamanho do passo da caída do gradiente
	adam = optimizers.Adam(lr=1e-3, decay=1e-5)    

	# Copilando o modelo
	# Função de apredizado será cross-entropy (https://en.wikipedia.org/wiki/Cross_entropy)
	# métrica de reconhecimento será precisão.
	loaded_model.compile(loss = 'categorical_crossentropy', optimizer = adam, metrics = ['accuracy'])
	print("Carregamento dos melhores pesos completo!")
	
	# Avaliando a precisção do modelo carregado depois do fit

	print('Metricas do Modelo: {}'.format(loaded_model.metrics_names))
	loaded_model_metricas = loaded_model.evaluate(X_test, Y_test, verbose=1)
	print("Erro de: %.2f%%" % (100-loaded_model_metricas[1]*100))
	print("Precisão de: %.2f%%" % (loaded_model_metricas[1]*100))
	
	y_probabilidade = loaded_model.predict(X_test, batch_size=32, verbose=1)
	predicted = [np.argmax(prob) for prob in y_probabilidade]
	
	# Verificando a precisão por classe
	# precision= A precisão é a razão onde é o número de positivos verdadeiros e o número de falsos positivos
	# recall= O recall é a razão onde é o número de positivos verdadeiros e o número de falsos negativos
	# f1-score= A média harmônica ponderada da precisão e recall
	# support= O suporte é o número de ocorrências de cada classe verdade

	print(classification_report(np.argmax(Y_test, axis=1), predicted, target_names=classes_emocoes))
	
	
if __name__ == '__main__':
	print()
	print('*' * 50)
	print('Prototipo DeepEmotive')
	print('Modulo de Transferencia de aprendizado.\n')
	print('*' * 50)
	main(sys.argv[1:])




