################################################3
#
#
#
# PROGRAMA PARA MIGRAR XLS para base de dados Postgres
# 28/04/2023
#
# Teste em 05/05/2023 (final)
# 04/09/2023 - railway
#
################################################3
import psycopg2
import xml.etree.ElementTree as ET
import os
import re
pasta = 'dados/anglo/M9'

##################################################################################################

#con = psycopg2.connect(host='containers-us-west-116.railway.app', database='railway', user='postgres', password='4s42HrhMxBIiqe9gC3LS', port=6628)
con = psycopg2.connect(host='localhost', database='teste_dds', user='postgres', password='admin', port=5432)

def retornaDataHora():
    listaDatas =[]
    for channel_summary in root.findall("./Transect"):
        #print (channel_summary.findtext("StartDateTime"))
        #startDateTimeList = channel_summary.findtext("StartDateTime")
        listaDatas.append(channel_summary.findtext("StartDateTime"))
        listaDatas.append(channel_summary.findtext("EndDateTime"))
        #print ("valor 0 = ", listaDatas[0])
        #print ("valor 1 = ", listaDatas[1])
    print("---------------------")
    print (listaDatas)
    print("---------------------")
    return listaDatas

def numTrancept():
    for numTrancept in root.findall("./ChannelSummary/Other"):
        print (numTrancept.findtext("NumberofTransects"))
    return  numTrancept.findtext("NumberofTransects")

##################################################################################################

##################################################################################################
def qrev (sequenciaFromNextVal):
    print ("CHEGOU RESULTS => ", sequenciaFromNextVal)

    for channel_summary in root.findall("./ChannelSummary/Other"):
        MeanWidth = channel_summary.findtext("MeanWidth")
        #print (channel_summary.findtext("MeanWidth"))

        WidthCOV = channel_summary.findtext("WidthCOV")
        #print (channel_summary.findtext("WidthCOV"))

        MeanArea = channel_summary.findtext("MeanArea")
        #print (channel_summary.findtext("MeanArea"))

        AreaCOV = channel_summary.findtext("AreaCOV")
        #print (channel_summary.findtext("AreaCOV"))

        MeanBoatSpeed = channel_summary.findtext("MeanBoatSpeed")
                        #print (channel_summary.findtext("MeanBoatSpeed"))

        MeanQoverA = channel_summary.findtext("MeanQoverA")
        #print (channel_summary.findtext("MeanQoverA"))

        MeanCourseMadeGood = channel_summary.findtext("MeanCourseMadeGood")
        #print (channel_summary.findtext("MeanCourseMadeGood"))

        MeanFlowDirection = channel_summary.findtext("MeanFlowDirection")
        #print (channel_summary.findtext("MeanFlowDirection"))

        MeanDepth = channel_summary.findtext("MeanDepth")
        #print (channel_summary.findtext("MeanDepth"))

        MaximumDepth = channel_summary.findtext("MaximumDepth")
        #print (channel_summary.findtext("MaximumDepth"))

        MaximumWaterSpeed = channel_summary.findtext("MaximumWaterSpeed")
        #print (channel_summary.findtext("MaximumWaterSpeed"))

        NumberofTransects = channel_summary.findtext("NumberofTransects")
        #print (channel_summary.findtext("NumberofTransects"))

        Duration = channel_summary.findtext("Duration")
        #print (channel_summary.findtext("Duration"))

        LeftQPer = channel_summary.findtext("LeftQPer")
        #print (channel_summary.findtext("LeftQPer"))

        RightQPer = channel_summary.findtext("RightQPer")
        #print (channel_summary.findtext("RightQPer"))

        InvalidCellsQPer = channel_summary.findtext("InvalidCellsQPer")
        print (channel_summary.findtext("InvalidCellsQPer"))

        InvalidEnsQPer = channel_summary.findtext("InvalidEnsQPer")
        print (channel_summary.findtext("InvalidEnsQPer"))

        UserRating = channel_summary.findtext("InvalidEnsQPer")
        #print (channel_summary.findtext("UserRating"))

        DischargePPDefault = channel_summary.findtext("DischargePPDefault")
        #print (channel_summary.findtext("DischargePPDefault"))
        sql = "select "

        #con = psycopg2.connect(host='localhost', database='ALM', user='postgres', password='conecta123')
        cur = con.cursor()

        sql = "INSERT INTO qrev values (nextval('qrev_id_seq')," + MeanWidth + "," + WidthCOV + "," + MeanArea + ","+ AreaCOV + "," +  MeanBoatSpeed + "," + MeanQoverA + "," + MeanCourseMadeGood + ","+ MeanFlowDirection + "," + MeanDepth + "," + MaximumDepth + "," + MaximumWaterSpeed + "," + NumberofTransects + "," + Duration + "," + LeftQPer + "," + RightQPer + "," + InvalidCellsQPer + "," + InvalidEnsQPer + "," + UserRating + "," + DischargePPDefault + "," + int(sequenciaFromNextVal) + ")"
        print (sql)
        cur.execute(sql)
        con.commit()

####################################################################################################################################################################################################


def retornaSequencia():
    cur = con.cursor()
    seq_qrev_data = "SELECT last_value FROM qrev_data_id_seq"
    data = []
    cur.execute(seq_qrev_data,data)
    results = cur.fetchone()
    #loop to print all the fetched details
    for r in results:
        print(r)
        print("Total number of rows in the table:", r)
        ############# Poula a tabela qrev
    return r

####################################################################################################################################################################################################
def populaQrev():
                     for channel_summary in root.findall("./ChannelSummary/Other"):
                        MeanWidth = channel_summary.findtext("MeanWidth")
                        #print (channel_summary.findtext("MeanWidth"))

                        WidthCOV = channel_summary.findtext("WidthCOV")
                        #print (channel_summary.findtext("WidthCOV"))

                        MeanArea = channel_summary.findtext("MeanArea")
                        #print (channel_summary.findtext("MeanArea"))

                        AreaCOV = channel_summary.findtext("AreaCOV")
                        #print (channel_summary.findtext("AreaCOV"))

                        MeanBoatSpeed = channel_summary.findtext("MeanBoatSpeed")
                                        #print (channel_summary.findtext("MeanBoatSpeed"))

                        MeanQoverA = channel_summary.findtext("MeanQoverA")
                        #print (channel_summary.findtext("MeanQoverA"))

                        MeanCourseMadeGood = channel_summary.findtext("MeanCourseMadeGood")
                        #print (channel_summary.findtext("MeanCourseMadeGood"))

                        MeanFlowDirection = channel_summary.findtext("MeanFlowDirection")
                        #print (channel_summary.findtext("MeanFlowDirection"))

                        MeanDepth = channel_summary.findtext("MeanDepth")
                        #print (channel_summary.findtext("MeanDepth"))

                        MaximumDepth = channel_summary.findtext("MaximumDepth")
                        #print (channel_summary.findtext("MaximumDepth"))

                        MaximumWaterSpeed = channel_summary.findtext("MaximumWaterSpeed")
                        #print (channel_summary.findtext("MaximumWaterSpeed"))

                        NumberofTransects = channel_summary.findtext("NumberofTransects")
                        #print (channel_summary.findtext("NumberofTransects"))

                        Duration = channel_summary.findtext("Duration")
                        #print (channel_summary.findtext("Duration"))

                        LeftQPer = channel_summary.findtext("LeftQPer")
                        #print (channel_summary.findtext("LeftQPer"))

                        RightQPer = channel_summary.findtext("RightQPer")
                        #print (channel_summary.findtext("RightQPer"))

                        InvalidCellsQPer = channel_summary.findtext("InvalidCellsQPer")
                        #print (channel_summary.findtext("InvalidCellsQPer"))

                        InvalidEnsQPer = channel_summary.findtext("InvalidEnsQPer")
                        #print (channel_summary.findtext("InvalidEnsQPer"))

                        UserRating = channel_summary.findtext("InvalidEnsQPer")
                        #print (channel_summary.findtext("UserRating"))

                        DischargePPDefault = channel_summary.findtext("DischargePPDefault")
                        #print (channel_summary.findtext("DischargePPDefault"))

                        sql_qrev = "INSERT INTO qrev values (nextval('qrev_id_seq'::regclass), '" + MeanWidth + "' , '" + WidthCOV + "','" + MeanArea + "','"+ AreaCOV + "','" +  MeanBoatSpeed + "','" + MeanQoverA + "','" + MeanCourseMadeGood + "','"+ MeanFlowDirection + "','" + MeanDepth + "','" + MaximumDepth + "','" + MaximumWaterSpeed + "','" + NumberofTransects + "','" + Duration + "','" + LeftQPer + "','" + RightQPer + "','" + InvalidCellsQPer + "','" + InvalidEnsQPer + "','" + UserRating + "','" + DischargePPDefault + "', " + str(retornaSequencia()) + ")"

                        print (sql_qrev)
                        cur.execute(sql_qrev)
                        #con.commit()

####################################################################################################################################################################################################

def ChannelSummary():
    for channel_summary in root.findall("./ChannelSummary/Discharge"):

        Top = channel_summary.findtext("Top")
        Middle = channel_summary.findtext("Middle")
        Bottom =channel_summary.findtext("Bottom")
        Left = channel_summary.findtext("Left")
        Right = channel_summary.findtext("Right")
        Total = channel_summary.findtext("Total")
        MovingBedPercentCorrection = channel_summary.findtext("MovingBedPercentCorrection")
    sql_channel_summary = "INSERT INTO channelsummary values (nextval('channelsummary_id_seq'::regclass), " +  Top +  ","  +  Middle +  "," + Bottom +   ","  +  Left +  ","  + Right +  "," + Total + "," + MovingBedPercentCorrection + "," + str(retornaSequencia()) + ")"
    cur.execute(sql_channel_summary)
    print ("sql_channel_summary = ", sql_channel_summary)


######### MAIN ---------------------------------
#con = psycopg2.connect(host='localhost', database='alm-dds', user='postgres', password='conecta123')
#con = psycopg2.connect(host='containers-us-west-202.railway.app', database='railway', user='postgres', password='JNnkxoZnLc1Vpw8fMZQp', port=7942)
cur = con.cursor()
for diretorio, subpastas, arquivos in os.walk(pasta):
    for i in range (len(arquivos)):
        #print (os.path.join(diretorio)+'/'+arquivos[i])
        print ('---------------------')
        #with open(os.path.join(diretorio)+'/'+arquivos[i],'r') as f:
        print (pasta + '/'+ arquivos[i])
        tree = ET.parse(pasta + '/'+ arquivos[i])
        root = tree.getroot()
        print ("------------")
        numTrancept()
        listaDatas = retornaDataHora()

        startdate,starttime = listaDatas[0].split(' ') #Data e Hora do inicio da medida
        enddate,endtime = listaDatas[-1].split(' ')    #Data e Hora do fim da medida

        #sql_qrev_data = "INSERT INTO qrev_data values (nextval('qrev_data_id_seq'), '" +  arquivos[i]  +  "'," + numTrancept() +  ", '"  +  startdate + "' , '" + enddate +  "' , '"+starttime + "' , '" + endtime + "',1 )"
        sql_qrev_data = "INSERT INTO qrev_data values (nextval('qrev_data_id_seq'), '" +  arquivos[i]  +  "'," + numTrancept() +  ", '"  +  startdate + " " + starttime + "' , '"  + enddate + " " + endtime + "',1 )"

        print (" >>>>>>>>> " + sql_qrev_data + "<<<<<<<<<<<<<<" )

        cur.execute(sql_qrev_data)

        ChannelSummary()
        populaQrev()

    con.commit()
    cur.close()

