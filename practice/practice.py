#import requests
#import pandas as pd
#import sqlite3
#import sqlite3
#print('volume')
#v =input()
#print('distance')
#y=input()
#
#
#v=float(v)
#y=float(y)
#
#
#output_classic=0.0
#output_nexgen=0.0
#
#if float(y)<1:
#    output_classic=float(v)*0.10/1000
#    output_nexgen=float(v)*0.10/1000
#    print(output_classic)
#    print(output_nexgen)
#  
#else:
#    output_classic=float(v)*0.10*(1-(y-1)*0.1)/1000
#    output_nexgen=float(v)*0.10*(1-(y-1)*0.05)/1000
#    print(output_classic)
#    print(output_nexgen)
  



#volAqua= float(input(" The volume of the aquarium  is :"))
#distAqua=float(input("The distance from the bottom of the aquarium to the pump is : "))
#typePump= str(input("The type of pump (classic/next generation) is :"))
#
#def outputflow(volAqua,distAqua,typePump):
#	if typePump == "classic" : 
#		flow = volAqua/10
#		if distAqua > 1 :
#			flow = flow*(1 - 0.1*distAqua)
#
#	elif typePump == "next generation" :
#		flow = volAqua/10
#		if distAqua > 1 :
#			flow = flow*(1 - 0.05*distAqua)
#
#	return flow 
#
#def convertflow(flow):
#	return flow/1000
#
#print(convertflow(outputflow(volAqua,distAqua,typePump)))
#


#import sqlite3
#d=sqlite3.connect('database_group43.db', isolation_level=None)
#querydelete='''
#			DELETE 
#			FROM Product 
#			WHERE Product_ID=3
#			'''
#print(querydelete)
#d.execute(querydelete)
#
#



#a=[]
#print(a)
#
#if not a:
#	print('empty')
#
