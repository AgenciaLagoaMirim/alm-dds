		##############################################################
#
# Script para migrar os dados do equipamento SL
# da Agência da Lagoa Mirim
# Arquivo nome ex: '2019_06_06_HS-SL-SG-02.dat'
#
# Coloca os dados diretamente na base de dados pelo postgres
# juntando a data no formato timestamp.
#
# Version 1.0 (7/03/2023 mateus@ufpel.edu.br
# Version 1.1 (27/04/2023 mateus@ufpel.edu.br
#
##############################################################
import os
import re
import psycopg2

pasta = 'dados/anglo/SL'

con = psycopg2.connect(host='localhost', database='teste_dds', user='postgres', password='admin', port=5432)
#con = psycopg2.connect(host='containers-us-west-116.railway.app', database='railway', user='postgres', password='4s42HrhMxBIiqe9gC3LS', port=6628)

cur = con.cursor()

for diretorio, subpastas, arquivos in os.walk(pasta):
	#print ('***********************')
	#print (len(arquivos));
	#print ('***********************')
	for i in range (len(arquivos)):
		#print (os.path.join(diretorio)+'/'+arquivos[i])
		file_name = (os.path.join(diretorio)+'/'+arquivos[i])
		#print file_name
		#print ('---------------------')
		with open(os.path.join(diretorio)+'/'+arquivos[i],'r', encoding='utf-8',errors='ignore') as f:
			content = f.readlines()
			#print (content)
			for j in range(len(content)):
				if (j != 0 ):
					#print(content[j])

					result = re.sub(r"\s+",",",content[j])

					ano = result.split(",")[0]
					mes = result.split(',')[1]
					dia = result.split(',')[2]
					hora = result.split(',')[3]
					minuto = result.split(',')[4]
					segundo = result.split(',')[5]

					date_time = ano + "-" + mes + "-" + dia + " " + hora + ":" + minuto + ":" + segundo
					#date_time = ano+mes+dia+hora+minuto+segundo
					print ("Date Time = [" + date_time + "] " + "Erro linha " + str(j))

					dados =  result[19:]

					#result = result[:-1]
					dados = dados[:-1]
					#sql =  "INSERT INTO sl_sg VALUES ('" + date_time + "'" +  dados + ",nextval('sl_sg_id_seq')," + "2" +");"

					#
					# o número 1 é referente siteinformation (id)
					#
					sql =  "INSERT INTO sl_sg VALUES (nextval('sl_sg_id_seq'), TIMESTAMP '" + date_time + "'  AT TIME ZONE 'UTC'" +  dados + ",1,'" + file_name + "'," + str(j) + ")"

					print ("linha i j ",i,j, "no aquivo: "+ arquivos[i])

					print (sql)
					cur.execute(sql)
					con.commit()

					#print(j)
		#print('Processando arquivo ',i, os.path.join(diretorio)+'/'+arquivos[i], 'Total de registros = ',j)
