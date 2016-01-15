# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 14:59:41 2016

@author: yanelly
"""

from sklearn import preprocessing
import csv as csv 

import pandas


import numpy as np 
import os 

os.getcwd()  # obtener dir
os.chdir("/home/yanelly/Escritorio/tarea1") # cambiarlo



# Open up the csv file in to a Python object
data_file = open('data.csv', 'rb')
data_file_object = csv.reader(data_file)
header = data_file_object.next()  # The next() command just skips the 
                                 

data=[]
aux = 0                    # Create a variable called 'data'.
for row in data_file_object:
    if not aux == 1:
        data.append(row[1:])
    aux = aux + 1
data = np.array(data) 


count = 0
for reg in data:                  
        
    #fecha de nacimiento
    fecha = [] 
    row = reg[2]
    row = row.strip() 
    dia = row[0:2]
    sep = row[2]
    if not sep.isdigit():
        mes = row[3:5]
        aux_a = row[6:]
        anio = aux_a[-2:]
    else:
        mes = int(row[2:4])
        if mes < 12:
            mes = row[2:4]
            aux_a = row[4:]
            anio = aux_a[-2:]
        else:
            mes = "0" + row[2:3]
            aux_a = row[3:]
            anio = aux_a[-2:]
    fechaC = dia + "/" + mes + "/" + anio
    reg[2] = fechaC
    
    #edades  
    row = reg[3] 
    reg[3] = row[0:3] 
    
    #corregir estado civil
    estado_civil = reg[4]
    if estado_civil[0] == "C" or estado_civil[0] == "U":
        reg[4]= 2
    if estado_civil[0] == "S":
        reg[4]= 1
    if estado_civil[0] == "V":
        reg[4]= 3
    
    #sexo
    sexo = reg[5]
    if sexo[0] == "F":
        reg[5] = 1
    else:
        reg[5] = 0
    
    #escuela
    escuela =  reg[6]
    if escuela[0] == "B":
        reg[6] = 1 
    else:
        reg[6] = 0 
       
        
    #modalidad de ingreso
    modalidad_i = reg[8]
    if modalidad_i[0] == "P":
        reg[8]= 1
    if modalidad_i[0] == "A":
        reg[8]= 2
    if modalidad_i[0] == "C":
        reg[8]= 3
        
    #semestre que cursa
    semestre = reg[9]
    if len(semestre)>2 and semestre[1].isdigit():
        reg[9] = semestre[0:2]
    else:
        reg[9] = semestre[0]
      
    
    #ha cambiado de direccion
    cambio_dir = reg[10]
    motivo = reg[11]
    if len(cambio_dir) < 3 and cambio_dir[0] == "S":
        reg[10] = motivo        
          
    #promedio      
    promedio = reg[16]
    if len(promedio)>2 and promedio[1] != "." and promedio[2] != ".":
        reg[16] = promedio[0:2] + "." + promedio[2:]
     
    #eficiencia
    eficiencia = reg[17]
    if len(eficiencia)>1 and eficiencia[1] != ".":
        reg[17] = "0." + eficiencia[0:]
    
    #Tesis, trabajode grado, pasantias
    tesis = reg[20]
    cantidad = reg[21]
    if not tesis.isdigit():
        if tesis[0] == "N":
            reg[20] = 0
        else:
            if len(cantidad)>0:
                if cantidad[0] == "P":
                    reg[20] = 1
                if cantidad[0] == "S":
                    reg[20] = 2
                if cantidad[0] == "M":
                    reg[20] = 3
               
    #2526  viviendda mientras estudia AA AB
    vivienda = reg[25]
    alquiler1 = reg[26]
    alquiler2 = reg[43]
    direccion = reg[27]
    if vivienda[0] == "H" or vivienda[0] == "R":
        reg[25] = vivienda + " (" + direccion + ")"
        if not alquiler1.isdigit():
            alquiler1 = alquiler2
    else:
        alquiler1 = 0
    reg[43] = alquiler1
       
    #solicitud de beneficio
    solicitud = reg[29]
    beneficio = reg[30]
    if solicitud[0] == "S":
        reg[29] = beneficio

    #actividad q genere beneficio
    actividad = reg[31]   
    tipo = reg[32]
    if actividad[0] == "S":
        reg[31] = tipo
                
    #beca  imputar Por sustitución por un valor de tendencia central #####
    beca_inc = 0
    beca_cor = 0
    beca = reg[33]
    if beca < 1000 or beca > 2500:
        beca_inc = beca_inc + 1
    else:
        beca_cor = beca_cor + 1
    
    #aporte responsable academico
    aporte_resp = reg[34]
    if not aporte_resp.isdigit():
        reg[34] = 0
        
    #aporte familiares
    aporte_fam = reg[35]
    if not aporte_fam.isdigit():
        reg[35] = 0
    
    #ingreso por actividades
    ingreso_act = reg[36]
    if not ingreso_act.isdigit():
        reg[36] = 0
        
    #alimentacion 
    alim = reg[38]
    if not alim.isdigit():
        reg[38] = 0
  

    #ransporte
    transporte = reg[39]
    if not transporte.isdigit():
        reg[39] = 0
    
    #gastos medicos
    gastos_med = reg[40]
    if not gastos_med.isdigit():
        reg[40] = 0
        
    #gastos odontologicos
    gastos_od = reg[41]
    if not gastos_od.isdigit():
        reg[41] = 0
    
    #gastos personales
    gastos_pers = reg[42]
    if not gastos_pers.isdigit():
        reg[42] = 0

    #recreacion
    recreacion = reg[45]
    if not recreacion.isdigit():
        reg[45] = 0  
    
    #otros gastos
    otros_gastos = reg[46]
    if not otros_gastos.isdigit():
        reg[46] = 0  

    #ingreso responsable academico AZ
    ing_resp = reg[50]
    ing_resp = ing_resp.replace(" ", "")
    ing_resp = ing_resp.replace("bs","")
    ing_resp = ing_resp.replace(",",".")
    if not ing_resp.isdigit():
        aux = ing_resp.split(".")
        tam = len(aux)
        if tam == 1:
            ing_resp = 0
        if tam == 3:
            ing_resp = aux[0] + aux[1] + "." + aux[2]
        if tam == 2:
            if len(aux[1])>2:
                ing_resp = aux[0] + aux[1]
    reg[50]= ing_resp
    
    #otros ingresos de responsabe academico
    otros_i= reg[51]
    if len(otros_i) == 0:
        reg[51] = 0
    else: 
        otros_i = otros_i.replace(" ", "")
        otros_i = otros_i.replace(",", ".")
        otros_i = otros_i.replace("bs","")
    if not otros_i.replace(".", "", 1).isdigit():
        reg[51] = 0  
    
    #vivienda 53
    vivienda_r= reg[53]
    if len(vivienda_r) == 0:
        reg[53] = 0
    else: 
        vivienda_r= vivienda_r.replace(" ", "")
        vivienda_r= vivienda_r.replace(",", ".")
        vivienda_r= vivienda_r.replace("bs","")
    if not vivienda_r.replace(".", "", 1).isdigit():
        reg[53] = 0  
    
    #alimentacion 54
    alimentacion_r= reg[54]
    if len(alimentacion_r) == 0:
        reg[54] = 0
    else: 
        alimentacion_r= alimentacion_r.replace(" ", "")
        alimentacion_r= alimentacion_r.replace(",", ".")
        alimentacion_r= alimentacion_r.replace("bs","")
    if not alimentacion_r.replace(".", "", 1).isdigit():
        reg[54] = 0  

    #transporte 55
    transporte_r= reg[55]
    if len(transporte_r) == 0:
        reg[55] = 0
    else: 
        transporte_r= transporte_r.replace(" ", "")
        transporte_r= transporte_r.replace(",", ".")
        transporte_r= transporte_r.replace("bs","")
    if not transporte_r.replace(".", "", 1).isdigit():
        reg[55] = 0  
    
    #gastos medicos
    gastosmed_r= reg[56]
    if len(gastosmed_r) == 0:
        reg[56] = 0
    else: 
        gastosmed_r= gastosmed_r.replace(" ", "")
        gastosmed_r= gastosmed_r.replace(",", ".")
        gastosmed_r= gastosmed_r.replace("bs","")
        if not gastosmed_r.replace(".", "", 1).isdigit():
            reg[56] = 0  
        else:
            reg[56] = gastosmed_r
   
    #odontologicos
    gastosod_r= reg[57]
    if not gastosod_r.isdigit():
        reg[57] = 0


    #educativos
    educativo_r= reg[58]
    if not educativo_r.isdigit():
        reg[58] = 0
    
    #servicios publcios
    servicios_r= reg[59]
    if not servicios_r.isdigit():
        reg[59] = 0
 

    #condominio    
    condominio_r= reg[60]
    condominio_r = condominio_r.strip() 
    condominio_r= condominio_r.replace(" ", "")
    condominio_r= condominio_r.replace(",", ".")
    condominio_r= condominio_r.replace("bs","")  
    if len(condominio_r) == 0:
        reg[60] = 0
    else: 
        if not condominio_r.replace(".", "", 1).isdigit():
            reg[60] = 0
        else:
            reg[60] = condominio_r
        

    #otros gastos
    otrosgastos_r= reg[61]
    if len(otrosgastos_r) == 0:
        reg[61] = 0
    else: 
        otrosgastos_r= otrosgastos_r.replace(" ", "")
        otrosgastos_r= otrosgastos_r.replace(",", ".")
        otrosgastos_r= otrosgastos_r.replace("bs","")
    if not otrosgastos_r.replace(".", "", 1).isdigit():
        reg[61] = 0  



minable = open("minable.csv", "wb")
minable_obj = csv.writer(minable)
minable_obj.writerow(["CI", "Fecha.Nacimiento", "Estado.Civil", "Sexo","Escuela", "Año.de.Ingreso.UCV",	"Modalidad.de.Ingreso.UCV",	"Semestre.que.cursa",	"Ha.cambiado.de.dirección",	"Num.materias.aprobadas.semestre.anterior",	"Num.materias.retiradas.semestre.anterior",	"Num.de.materias.reprobadas.semestre.anterior","Promedio.ponderado.aprobado", "Eficiencia",	"Si.reprobó.una.o.más.materias.indique.el.motivo","Num.materias.inscritas.semestre.en.curso",	"Realizado.tesis.trabajo.de.grado.o.pasantías","Procedencia","Lugar.donde.reside.mientras.estudia",	"Personas.con.las.que.vive.mientras.estudia", "Tipo.de.vivienda.donde.reside.mientras.estudia",		"Ha.solicitado.otro.beneficio.en.la.universidad", "Esta.realizando.alguna.actividad.que.le.genere.ingresos.", "Monto.mensual.de.la.beca","Aporte.mensual.que.le.brinda.su.responsable.económico",	"Aporte.mensual.que.recibe.de.familiares.o.amigos",	"Ingreso.mensual.por.actividades.a.destajo.o.por.horas", "Alimentación","Transporte.público","Gastos.médicos","Gastos.odontológicos","Gastos.personales","Residencia.o.habitación.alquilada","Materiales.de.estudio","Recreación","Otros.gastos","Quién.es.su.responsable.económico",	"Carga.familiar","Ingreso.mensual.responsable.económico","Otros.ingresos","Vivienda.resp.economico","Alimentación.resp.economico","Transporte.resp.economico","Gastos.médicos.resp.economico","Gastos.odontológicos",	"Gastos.educativos.resp.eco","Servicios.públicos"	, "Condominio","Otros.gastos.resp.econm",	"Opinión.de.nuestros.usuarios..para.mejorar.la.calidad.de.los.servicios.ofrecidos.por.el.Dpto..de.Trabajo.Social.OBE","Sugerencias.y.recomendaciones.para.mejorar.nuestra.atención"])




for row in data:
                       
    minable_obj.writerow(np.concatenate((row[1:3], row[4:11], row[13:21], row[22:26], row[29:30], row[31:32], row[33:37],row[38:47], row[48:52], row[53:62], row[63:65]), axis=0))

    
minable.close()
data_file.close()



