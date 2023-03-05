# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 01:24:20 2023

@author: Daryl
"""

def tri_par_fusion(list):
    newliste=[]
    if len(list)%2==0:     
        if len(list)>1:
            n1=len(list)//2
            liste1=sorted(list[:n1])
            liste2=sorted(list[n1:])
        i,j=0,0
        while i<len(liste1) and j<len(liste2):
            if liste1[i]<liste2[j]:
                newliste.append(liste1[i])
                i=i+1   
            else:
                newliste.append(liste2[j])
                j=j+1
        newliste+=liste1[i:]
        newliste+=liste2[j:]
        return newliste
    else:
        print("Entrez un nombre d'éléments paire")  
                
list=[100,45,9,2]
newliste=tri_par_fusion(list)
print(newliste)

        
        
    