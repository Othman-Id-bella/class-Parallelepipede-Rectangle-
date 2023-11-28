class Rectangle:
    _Nbrrect=0
    def __init__(self,largeur=0,longueur=0):
        self._longueur=longueur
        self._largeur=largeur
        Rectangle._Nbrrect+=1

    def getLongueur(self):
        return self._longueur
    
    def setLongueur(self,Lon):
         self._longueur=Lon
    
    
    def getLargeur(self):
        return self._largeur
    
    def setLargeur(self,Lar):
        self._largueur=Lar
    
    def getNbrrec():
        return Rectangle._Nbrrect
    
    def Equal(self,other):
        if (self.getLargeur()==other.getLargeur()) and ( self.getLongueur()==other.getLongueur()):
            return True
        else:
            return False
    
    def Peremetre(self):
        return ( self.getLongueur()+self.getLargeur())*2
    
    def Surface(self):
        return  self._longueur*self._largeur
    
    def ToString(self):
        return f"(longueur={self.getLongueur()},largeur= {self.getLargeur()})"


class Parallelepipede(Rectangle):
    _NbrPara=0
    def __init__(self, largeur=0, longueur=0,hauteur=0):
        super().__init__(largeur, longueur)
        self._hauteur=hauteur
        Parallelepipede._NbrPara+=1

    def gethauteur(self):
        return self._hauteur
    
    def setHauteur(self,Hau):
        self._hauteur=Hau

    def getNbrPara():
        return Parallelepipede._NbrPara
    
    def Surface(self):
        return  (self.getLongueur()*2)+(self.getLargeur()*2)+(self.gethauteur()*2)
    
    def Volume(self):
        return  self.getLongueur()*self.getLargeur()*self.gethauteur()
    
    def ToString(self):
        return f"(longueur={ self.getLongueur()},largeur= {self.getLargeur()},Hauteur={self.gethauteur()})"
    
    def Equal(self,other):
        if (self.getLargeur()==other.getLargeur()) and ( self.getLongueur()==other.getLongueur()) and (self.gethauteur()==other.gethauteur()):
            return True
        else:
            return False
        
Rec1=Rectangle(12,5)
Rec2=Rectangle(2,5)
print(Rec1.ToString(),Rec2.ToString())
print(Rec1.Equal(Rec2))
print("peremetre de Rectangle1 est:",Rec1.Peremetre(),"suface est:",Rec1.Surface())
print("peremetre de Rectangle1 est:",Rec2.Peremetre(),"suface est:",Rec2.Surface())
print("nbr;",Rectangle._Nbrrect)
par1=Parallelepipede(2,5,3)
par2=Parallelepipede(2,5,3)
print(par1.ToString(),par2.ToString())
print(par1.Equal(par2))
print("peremetre de Rectangle1 est:",par1.Peremetre(),"suface est:",par1.Surface())
print("peremetre de Rectangle1 est:",par2.Peremetre(),"suface est:",par2.Surface())
print("nbr;",Parallelepipede._NbrPara)