
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
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, f1_score, cohen_kappa_score


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def main(argv):
	
	help = """Este script e responsavel por realizar a predicao
		de uma ou varias imagens. Recebe como parametro o caminho
		absoluto da imagem ou o diretorio contendo todas as imagens
		a serem preditas.

		Args:
			-m <CAMINHO_DA_IMAGEM> : apenas uma imagem
			-d <CAMINHO_DO_DIRETORIO> : varias imagens
			"""
	
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
			imagens.append(im) # insere face an lista
				
		print('Imagens carregadas com sucesso!')
		print('Quantidade de imagens: ',len(imagens))
		return imagens

	# verificando paramentros
	flag = False
	if sys.argv[1] == '-h':
		print (help)
		#print ('classificar_emocao.py -m <CAMINHO_DA_IMAGEM')
		sys.exit()
	elif sys.argv[1] =='-m':
		path = sys.argv[2]
	elif sys.argv[1] =='-d':
		path = sys.argv[2]
		flag = True
	else:
		print('Verifique o caminho da imagens ou do diretório.')
		print('digite: <file> <-h> para obte ajuda.')
		sys.exit(2)
	
	# lista de emoções conhecidas pelo sistemas
	classes_emocoes = ['alegria', 'desgosto', 'desprezo', 'medo', 'neutral', 'raiva', 'surpresa', 'tristeza']
	# importando a imagem e redimensionando
	shape = (98,98)
	
	print('*' * 50)
	if flag:
		print('Importando imagens:',path)
		imagens = carregar_imagens(path) # Abrir imagens
		if imagens is None:
			print('Imagem invalida" verifique o caminho da imagem.')
			exit()
		else:
			
			faces = []
			for img in imagens:			
				# cria uma aray numpy com uma lista de lista contendo os pixels da imagem
				pixel_values = np.array(list(img.getdata()))
				# redimensiona os pixels para formato 98x98
				pixel_values = pixel_values.reshape(shape)
				faces.append(pixel_values)

			array_pixels = faces
			print()
			print("Configurando o array de pixels para procesamento da rede...\n")
			dados_empilhados = np.stack(array_pixels)
			print(dados_empilhados.shape)

			# O framework theano trabalha com a quantidade de canais 
			# de cores a frente da dimesão da imagem
			if K.image_data_format() == 'channels_first': # = th
				shape = (1, 98, 98)
				#shape = (1, img_cols, img_rows)
				print("Trabalhando com theano:", shape)
			# O framework tensorflow trabalha com a quantidade de canais
			# de cores apos a dimesão da imagem
			else:  # channel_last = tf
				shape = (98, 98, 1)
				print("Trabalhando com tensorflow:", shape)

			# configurando o shape para 4D
			X_test = dados_empilhados.reshape((dados_empilhados.shape[0],) + shape).astype('float32')

			print('Novo formato dos pixles da imagem: ',X_test.shape)
			# cada pixels é normalizado = pixel = pixel / 255
			X_test /= 255
			print("Preparacao da imagem completa!\n")
	else:
		print('Importando imagem:',path)
		img = Image.open(path) # Abrir imagem
		if img is None:
			print('Imagem invalida" verifique o caminho da imagem.')
			exit()
		else:
			img = img.resize(shape, Image.ANTIALIAS)
			img = img.convert('L') # coverte imagem para escala de cinza.
			print('Imagem importada com sucesso!\n')
			print('*' * 50)
		
		# cria uma aray numpy com uma lista de lista contendo os pixels da imagem
		pixel_values = np.array(list(img.getdata()))
		# redimensiona os pixels para formato 98x98
		pixel_values = pixel_values.reshape(shape)

		array_pixels = pixel_values
		print("Formato dos pixels da imagens: {}".format((array_pixels.shape)))
		print()
		print("Configurando o array de pixels para procesamento da rede...\n")
		dados_empilhados = np.stack(array_pixels)

		# O framework theano trabalha com a quantidade de canais 
		# de cores a frente da dimesão da imagem
		if K.image_data_format() == 'channels_first': # = th
			shape = (1, 98, 98)
			#shape = (1, img_cols, img_rows)
			print("Trabalhando com theano:", shape)
		# O framework tensorflow trabalha com a quantidade de canais
		# de cores apos a dimesão da imagem
		else:  # channel_last = tf
			shape = (98, 98, 1)
			print("Trabalhando com tensorflow:", shape)

		# configurando o shape para 4D
		X_test = dados_empilhados.reshape((1,) + shape).astype('float32')

		print('Novo formato dos pixles da imagem: ',X_test.shape)
		# cada pixels é normalizado = pixel = pixel / 255
		X_test /= 255
		print("Preparacao da imagem completa!\n")
	
	print('*' * 50)
	# Carregando o modelo salvo
	# Lendo o modelo salvo em arquivo para um novo modelo
	MODELO_SALVO_JSON = 'deep_emotive_model_t10_faces.json'
	print("Carregando o modelo...")
	json_file = open(MODELO_SALVO_JSON, 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	print('Modelo carregado com sucesso!\n')
	
	MELHORES_PESOS = './pesos/pesos_teste_10-266-0.96.3.hdf5'
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
	
	y_probabilidade = loaded_model.predict(X_test, batch_size=32, verbose=1)
	predicted = [np.argmax(prob) for prob in y_probabilidade]
	
	# print(y_probabilidade[0])
	# imagem classificada
	if flag:
		#print(classification_report(np.argmax(y_probabilidade, axis=1), predicted, target_names=classes_emocoes))
		predicoes = [classes_emocoes[x] for x in predicted]
		probs = [prob for prob in y_probabilidade]
		
		for index, emocao in enumerate(predicted):
			print('Imagem {}, probabilidade da emocao: {}:\t %.2f%%'.format(index, classes_emocoes[emocao]) % np.max(probs[index]))
		
		#print(predicoes)
		#print('Classificando imagens...\n')
		#for index, p in enumerate(predicted):
		#	for i, emocao in enumerate(classes_emocoes):
		#			if i == 3:
		#				print('probabilidade da emocao: {}:\t\t %.2f%%'.format(emocao) % y_probabilidade[index][i])
		#			elif i == 5:
		#				print('probabilidade da emocao: {}:\t\t %.2f%%'.format(emocao) % y_probabilidade[index][i])
		#			else:
		#				print('probabilidade da emocao: {}:\t%.2f%%'.format(emocao) % y_probabilidade[index][i])
		#	print()
		#	print('Emocao classificada pela rede:',classes_emocoes[p])
		#	print()
		print('*' * 50)
			
	else:
		print('Classificando a imagem...\n')
		# probabilidade das emoções
		for i, emocao in enumerate(classes_emocoes):
			if i == 3:
				print('probabilidade da emocao: {}:\t\t %.2f%%'.format(emocao) % y_probabilidade[0][i])
			elif i == 5:
				print('probabilidade da emocao: {}:\t\t %.2f%%'.format(emocao) % y_probabilidade[0][i])
			else:
				print('probabilidade da emocao: {}:\t%.2f%%'.format(emocao) % y_probabilidade[0][i])
		print()
		print('Emocao classificada pela rede:',classes_emocoes[predicted[0]])
		print()
		print('*' * 50)
	
if __name__ == '__main__':
	print()
	print('*' * 50)
	print('Prototipo DeepEmotive')
	print('Modulo de classificacao de emocao de uma imagem.\n')
	print('*' * 50)
	main(sys.argv[1:])




