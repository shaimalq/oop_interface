from abc import ABC, abstractmethod
class produit :
    _nbr=0
    def __init__(self , reference , desig , pv , pA , stock) :
        self._reference = reference
        self._desig = desig
        self._pv = pv
        self._pA = pA
        self._stock = stock
        produit._nbr +=1

    @property
    def  refence(self):
        return self._reference
    @refence.setter
    def refence( self ,refence):
        self._reference =refence

    @property
    def  pv(self):
        return self._pv
    @pv.setter
    def pv( self ,pv):
        self._pv =pv

    @property
    def  pA(self):
        return self._pA
    @pA.setter
    def pA ( self ,pA):
        self._pA = pA

    @property
    def desig (self):
     return self._desig
    @desig.setter
    def desig( self ,desig):
        self._desig  =desig

    @property
    def stock (self):
        return self._stock
    @stock.setter
    def stock (self ,stock):
        self._stock = stock

    def __str__(self):
     return f"reference: {self._reference}, designation: {self._desig}, prix d'achat: {self._pA}, prix de vente: {self._pv} , stock:{self._stock}"
    
    def __eq__(self, other):
        if self._reference == other._reference:
            return True


class commande :
    import time 
    def __init__( self , date , quantite):
        self._date = date 
        self ._quantite = quantite
    
    @property
    def date (self):
        return self._date 
    @date.setter
    def date (self ,date ):
        self._date = date 

    @property
    def quantite (self):
        return self._quantite
    @date.setter
    def quatite (self ,quantite ):
        self._quantie = quantite

    def __str__(self):
     return f"date de creation: {self._date}, designation:{self._quantie}"
  
p1 = produit("0111224","" ,"120 dh" ,"100 dh","12" )
c1 =commande("12-06-2023" , "12 kg")

print(c1.__str__)
  
    

    


   