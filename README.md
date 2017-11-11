# DEEP-EMOTIVE

## Trabalho de conclusão de curso - Ciência da Computação  - FURB - 2017
### Autor: Diogenes Ademir Domingos<br>

Deep-Emotive é um protótipo para reconhecer e classificar as expressões faciais das emoções, alegria, desgosto, medo, raiva, surpresa,
tristeza, consideradas por Ekman et al. (1987), como básicas e universais, utilizando técnicas já consolidadas das áreas de 
Processamento Digital de Imagem e Visão Computacional. Estas técnicas são combinadas com uma nova abordagem, considerada a mais avançada
no reconhecimento visual de objetos através do aprendizado de máquina, o Aprendizado Profundo ou Deep Learning.

<p>A proposta inicial deste trabalho foi desenvolver um protótipo capaz de reconhecer automaticamente as seis emoções básicas e universais: 
raiva; desgosto; medo; alegria; tristeza; surpresa, através da análise de expressões faciais. Para tanto, foram utilizadas imagens oriundas
da base de dados Cohn-Kanade AU-Coded Expression Database Version 2 (LUCEY et. al. 2010).</p>

<p>Foi utilizado a linguagem de programação Python, a ferramenta Jupyter Notebook, assim com os frameworks Keras, OpenCV, Scikit Learn, 
Numpy, Matplotlib.</p>

<p>O trabalho proposto alcançou os objetivos pré-estabelecidos, bem como, apresenta resultados positivos, além do esperado. 
Este foi capaz de reconhecer e segmentar automaticamente uma face na imagem utilizando técnicas de visão computacional. 
As faces segmentadas deram origem a uma nova base de dados. O trabalho desenvolvido implementou um classificador de emoções capaz de 
<b>reconhecer oito emoções, alcançando 98,71% de precisão</b>. As duas emoções reconhecidas e que não estavam na proposta inicial são desprezo 
e neutra. Para tanto, foi criado uma rede neural convolucional, utilizando a topologia do Aprendizado Profundo, que realizou a 
extração de características relevantes para o reconhecimento das emoções.</p>

<p>Adicionalmente, foi implementada a técnica de Transferência de Aprendizado, com o objetivo de validar o aprendizado obtido pelo 
classificador de emoções proposto, bem como para investigar suas limitações. Os resultados obtidos foram satisfatórios quando 
aplicado a transferência de aprendizado na base de dados Japanese Female Facial Expression (JAFFE), atingindo uma <b>precisão de 97.67%</b>. 
O JAFFE possui imagens similares a base de dados utilizadas para o treinamento da rede DeepEmotive. 
Com este resultado é possível concluir que o DeepEmotive é eficaz no reconhecimento automático de expressões faciais de outras 
bases de dados que sejam relativamente similares a base de dados utilizada para o mesmo, porém não se limitando somente a esta. 
Este pode auxiliar a comunidade tecnológica na geração de novos algoritmos computacionais, que, baseado nesta arquitetura reconhece 
automaticamente as emoções através de expressões faciais.</p>

<p>Uma limitação apresentada pelo protótipo pode ser observada quando a técnica de transferência de aprendizado é aplicada 
na base de dados Facial Expression Recognition 2013 (FER-2013). O protótipo apresentou baixa assertividade, alcançado <b>60.71% de 
precisão.</b> Uma das razões da baixa assertividade é que a base de dados FER-2013 possui imagens dissimilares às bases de dados citadas anteriormente, 
contendo imagens com problemas que ainda são desafiadores para a área de visão computacional, como oclusão e ruido. No entanto, 
o resultado foi superior à taxa de escolha randômica de 50%.</p>

<p>Outra limitação apresentada no desenvolvimento do protótipo é o alto custo computacional requerido para aplicação da técnica de 
aprendizado profundo, necessitando um bom background para o processamento. Os testes desempenhados neste trabalho possuíam tempo duração, 
na fase de treinamento, variando entre 1 hora, para a pior taxa de precisão e 1 dia, 10 horas, 14 minutos, e 8 segundos para a melhor taxa.
Isto limitou a quantidade de características que a rede é capaz de aprender, visto que, para que fosse possível a execução do algoritmo, 
as imagens precisam estar em baixa escala e também utilizando apenas um canal de cor.</p>

<p>Conclui-se que a técnica de aprendizado profundo de máquina pode ser utilizada para a identificação de emoções através de expressões
faciais em imagens 2D, com um percentual fidedigno de acurácia. Tornando assim desnecessária a marcação explicita dos pontos relevantes
a serem extraídos para obter o conhecimento, fase que é realizada por um especialista no domínio do problema.
O trabalho proposto também disponibiliza um modelo de predição treinado, o qual através do conhecimento adquirido, pode predizer emoções
em imagens de face humana. A criação do modelo preditivo agrega também relevância social ao protótipo, podendo ser utilizado em diversas 
áreas da sociedade, como por exemplo nas áreas de entretenimento, auxiliando na interação homem máquina, no marketing, através da 
informação do estado emocional dos clientes para auxiliar na venda, e no monitoramento de pacientes, predizendo sintomas que possuam 
correlação com o estado emocional, como a depressão.</p>
