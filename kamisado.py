from tkinter import*
from random import*

class fenetre_choix_pion:
      def __init__(self, type_partie, joueur_blanc, joueur_noir):

            self.type_partie = type_partie
            self.joueur_blanc = joueur_blanc
            self.joueur_noir = joueur_noir

            self.fenetre_choix_pion = Tk()
            self.fenetre_choix_pion.geometry("425x100")
            self.fenetre_choix_pion.title("Choix")
            self.couleur = ""
            self.choix_pion = StringVar()
            
            label = Label(self.fenetre_choix_pion, textvariable=self.choix_pion)
            label.pack()
            self.choix_pion.set (str(self.joueur_blanc.pseudo) + ", vous jouez les pions blancs, \n choissisez quel pion vous voulez déplacer en premier lieu")
            
            self.afficher_boutons()
            self.fenetre_choix_pion.mainloop()

      def afficher_boutons(self):

            pion_orange = Button(self.fenetre_choix_pion, background="#f5530c", command=lambda: self.renvoyer_couleur_pion("orange"))
            pion_orange.place(x=20, y=50, width = 30, height = 30)


            pion_bleu = Button(self.fenetre_choix_pion, background="#3231d9", command=lambda: self.renvoyer_couleur_pion("bleu"))
            pion_bleu.place(x=70, y=50, width = 30, height = 30)

            pion_mauve = Button(self.fenetre_choix_pion, background="#6e0062", command=lambda: self.renvoyer_couleur_pion("mauve"))
            pion_mauve.place(x=120, y=50, width = 30, height = 30)

            pion_rose = Button(self.fenetre_choix_pion, background="#e5169a", command=lambda: self.renvoyer_couleur_pion("rose"))
            pion_rose.place(x=170, y=50, width = 30, height = 30)
            
            pion_jaune = Button(self.fenetre_choix_pion, background="#dce30c", command=lambda: self.renvoyer_couleur_pion("jaune"))
            pion_jaune.place(x=220, y=50, width = 30, height = 30)
            
            pion_rouge = Button(self.fenetre_choix_pion, background="#df1717", command=lambda: self.renvoyer_couleur_pion("rouge"))
            pion_rouge.place(x=270, y=50, width = 30, height = 30)

            pion_vert = Button(self.fenetre_choix_pion, background="#148622", command=lambda: self.renvoyer_couleur_pion("vert"))
            pion_vert.place(x=320, y=50, width = 30, height = 30)

            pion_brun = Button(self.fenetre_choix_pion, background="#7c3819", command=lambda: self.renvoyer_couleur_pion("brun"))
            pion_brun.place(x=370, y=50, width = 30, height = 30)

      def renvoyer_couleur_pion(self, couleur):
            self.fenetre_choix_pion.destroy()
            self.couleur = couleur
            
            if self.type_partie == "simple" :
                  ma_partie = partie_simple(self.couleur, self.joueur_blanc, self.joueur_noir)

            elif self.type_partie == "standard" :
                  ma_partie = partie_standard(self.couleur, self.joueur_blanc, self.joueur_noir)

            elif self.type_partie == "longue" :
                  ma_partie = partie_longue(self.couleur, self.joueur_blanc, self.joueur_noir)

            else :
                  ma_partie = partie_marathon(self.couleur, self.joueur_blanc, self.joueur_noir)

            ma_partie.jouer_partie()
                  
########################################################################################################################################################################################

class joueur:
      def __init__ (self, pseudo, equipe):
            self.pseudo = pseudo
            self.equipe = equipe
            self.point_de_victoire = 0

      def gagner_point_de_victoire (self, point_victoire_gagne) :
            self.point_de_victoire += point_victoire_gagne

      def choisir_case (self, cases_possibles, pions, cases): 
            """
            Méthode qui regarde parmi les possibilité si certaine menrait l'autre équipe à la victoire et choisi sa case en fonction de ça
            """
            cases_non_perdante = []
            for case in cases_possibles :
                  couleur = case.couleur
                  for pion in pions :
                        if pion.code_couleur == couleur :
                              deplacements_pion_adverse = pion.trouver_possibilites_deplacement (pions, cases)
                              for case_adverse in deplacements_pion_adverse :
                                    if (case_adverse.numero > 9) and (case_adverse.numero < 57) :
                                          cases_non_perdante.append(case_adverse)

            if cases_non_perdante == [] :
                  case_choisie = choice(cases_possibles)

            else :
                  case_choisie = choice(cases_non_perdante)

            return (case_choisie)

########################################################################################################################################################################################

class cases:
      """Classe qui instancie une case."""
      def __init__ (self, numero, couleur):

            self.numero = numero
            self.coordonnee_X = (self.numero-1) % 8
            self.coordonnee_Y = ((self.numero-1)//8)+1
            self.couleur = couleur

      def verifier_disponibilite (self, pions):
            disponible = True
            for pion in pions :
                  if pion.case.numero == self.numero :
                        disponible = False

            return (disponible)

########################################################################################################################################################################################

class pions_tour_dragon (object):
      """Classe qui instancie un pion."""

      def __init__(self, equipe, couleur, code_couleur, case):
            self.equipe = equipe
            self.couleur = couleur
            self.code_couleur = code_couleur
            self.case = case

            self.case_disponible = []

            self.image = "Skin1/Tour_Dragon/" + str(self.equipe) + "_" + str(self.couleur) + ".png"
            self.limite_deplacement = 7
            # self.oshi_max = 0
            self.points_victoire = 1
            

      def trouver_possibilites_deplacement (self, pions, cases):
            if str(self.equipe) == "blanc" :
                  # cases disponible en ligne droite
                  nombre_cases_dans_deplacement = 0
                  x_case_base = (self.case.coordonnee_X)
                  y_case_base = (self.case.coordonnee_Y + 1)

                  while nombre_cases_dans_deplacement < self.limite_deplacement :
                        nombre_cases_dans_deplacement += 1
                        while y_case_base < 9 :
                              case_a_regarder = cases[((8*(y_case_base-1)) + x_case_base)]
                              if (case_a_regarder.verifier_disponibilite(pions)) == False :
                                    y_case_base = 9
                              else :
                                    self.case_disponible.append(case_a_regarder)
                                    y_case_base += 1

                  # cases disponible sur la diagonale droite
                  nombre_cases_dans_deplacement = 0
                  y_case_base = (self.case.coordonnee_Y + 1)
                  x_case_base += 2

                  while nombre_cases_dans_deplacement < self.limite_deplacement :
                        nombre_cases_dans_deplacement += 1
                        while (x_case_base < 9) and (y_case_base < 9) :
                              case_a_regarder = cases[((8*(y_case_base-1)) + x_case_base)-1]
                              if (case_a_regarder.verifier_disponibilite(pions)) == False :
                                    y_case_base = 9

                              else :
                                    self.case_disponible.append(case_a_regarder)
                                    y_case_base += 1
                                    x_case_base += 1
                        

                  # cases disponible sur la diagonale gauche
                  nombre_cases_dans_deplacement = 0
                  x_case_base = (self.case.coordonnee_X - 1)
                  y_case_base = (self.case.coordonnee_Y + 1)
                  
                  while nombre_cases_dans_deplacement < self.limite_deplacement :
                        nombre_cases_dans_deplacement += 1
                        
                        while (x_case_base >= 0) and (y_case_base >= 0):
                              case_a_regarder = cases[((8*(y_case_base-1)) + x_case_base)]
                              
                              if (case_a_regarder.verifier_disponibilite(pions)) == False :
                                    y_case_base = -1

                              else :
                                    self.case_disponible.append(case_a_regarder)
                                    y_case_base += 1
                                    x_case_base -= 1
                  

            else :
                  # cases disponible en ligne droite
                  nombre_cases_dans_deplacement = 0
                  x_case_base = (self.case.coordonnee_X)
                  y_case_base = (self.case.coordonnee_Y - 1)

                  while y_case_base < 9 :
                        case_a_regarder = cases[((8*(y_case_base-1)) + x_case_base)]
                        if (case_a_regarder.verifier_disponibilite(pions)) == False :
                              y_case_base = 9
                        else :
                              self.case_disponible.append(case_a_regarder)
                              y_case_base -= 1
                  
                  # cases disponible sur la diagonale droite
                  nombre_cases_dans_deplacement = 0
                  y_case_base = (self.case.coordonnee_Y - 1)
                  x_case_base += 2

                  while (x_case_base < 9) and (y_case_base < 9) :
                        case_a_regarder = cases[((8*(y_case_base-1)) + x_case_base)-1]
                        if (case_a_regarder.verifier_disponibilite(pions)) == False :
                              y_case_base = 9

                        else :
                              self.case_disponible.append(case_a_regarder)
                              y_case_base -= 1
                              x_case_base += 1

                  # cases disponible sur la diagonale gauche
                  nombre_cases_dans_deplacement = 0
                  x_case_base = (self.case.coordonnee_X - 1)
                  y_case_base = (self.case.coordonnee_Y - 1)

                  while (x_case_base >= 0) and (y_case_base >= 0):
                        case_a_regarder = cases[((8*(y_case_base-1)) + x_case_base)]
                        if (case_a_regarder.verifier_disponibilite(pions)) == False :
                              y_case_base = -1

                        else :
                              self.case_disponible.append(case_a_regarder)
                              y_case_base -= 1
                              x_case_base -= 1

            return (self.case_disponible)

            # def effectuer_un_oshi (self) :
                  
                  
########################################################################################################################################################################################

class sumo (pions_tour_dragon):
      def __init__ (self, equipe, couleur, code_couleur, case) :
            pions_tour_dragon.__init__(self, equipe, couleur, code_couleur, case)

            self.image = "Skin1/Sumo/" + str(self.equipe) + "_" + str(self.couleur) + ".png"
            self.limite_deplacement = 5
            self.oshi_max = 1
            self.points_victoire = 2
            
########################################################################################################################################################################################

class double_sumo (pions_tour_dragon):
      def __init__ (self, equipe, couleur, code_couleur, case) :
            pions_tour_dragon.__init__(self, equipe, couleur, code_couleur, case)

            self.image = "Skin1/Double_Sumo/" + str(self.equipe) + "_" + str(self.couleur) + ".png"
            self.limite_deplacement = 3
            self.oshi_max = 2
            self.points_victoire = 4

########################################################################################################################################################################################

class triple_sumo (pions_tour_dragon):
      def __init__ (self, equipe, couleur, code_couleur, case) :
            pions_tour_dragon.__init__(self, equipe, couleur, code_couleur, case)

            self.image = "Skin1/Triple_Sumo/" + str(self.equipe) + "_" + str(self.couleur) + ".png"
            self.limite_deplacement = 1
            self.oshi_max = 3
            self.points_victoire = 8

########################################################################################################################################################################################

class plateaux(Tk) :
      """Classe qui instancie un plateau."""
      
      def __init__ (self, la_partie, liste_case, liste_pions) :
            Tk.__init__(self)
            self.title("damier")
            self.canvas = Canvas(self, width=650, height=650)
            self.canvas.place(x=25,y=25)
            self.clique = False
            self.case_choisie = None
            self.la_partie=la_partie
            self.compteur_canvas = 1
                  
      def cliquer (self, evenement):
            self.widget = evenement.widget
            self.widget = str(self.widget)
            self.case_choisie = self.cases_possibles[self.compteur_canvas-int(self.widget[16:(len(self.widget))])]
        
            self.la_partie.jouer_manche()
            


      def afficher_case_possible (self, pion):
            self.cases_possibles = pion.trouver_possibilites_deplacement(self.la_partie.liste_pions, self.la_partie.liste_case)
            #numero_canvas = 1
            liste_canvas_case_possible = []
            for num_canvas in range (1, len(self.cases_possibles)):
                  liste_canvas_case_possible.append ("canvas_case_possible_" + str(num_canvas))
                  liste_canvas_case_possible[-1] = Canvas(self.canvas, height=70, width=70, bg=self.cases_possibles[num_canvas-1].couleur, borderwidth = 3)
                  liste_canvas_case_possible[-1].grid(column = self.cases_possibles[num_canvas-1].coordonnee_X, row = self.cases_possibles[num_canvas-1].coordonnee_Y)
                  self.compteur_canvas += 1
                  liste_canvas_case_possible[-1].bind("<Button-1>", self.cliquer)

      def afficher_plateau (self) :
            liste_canvas = []
            for numero in range (1, 65):
                  liste_canvas.append("canvas" + str(numero))
                  liste_canvas[-1] = Canvas(self.canvas, height=70, width=70, bg=self.la_partie.liste_case[numero-1].couleur, borderwidth = 10)
                  self.compteur_canvas += 1
                  liste_canvas[-1].grid(column = self.la_partie.liste_case[numero-1].coordonnee_X, row = self.la_partie.liste_case[numero-1].coordonnee_Y)

      def afficher_pions (self) :
            for pion in self.la_partie.liste_pions :
                  self.canvas_case = Canvas(self.canvas, height=70, width=70, bg=(pion.case.couleur), borderwidth = 10)
                  self.compteur_canvas += 1
                  self.image = PhotoImage (master=self.canvas_case, file = (pion.image))
                  self.canvas_case.create_image(47, 47, image=self.image)
                  self.canvas_case.image = self.image
                  self.canvas_case.grid(column = pion.case.coordonnee_X, row = pion.case.coordonnee_Y)

      def replacer_pions (self) :

            # blanc
            numero_case = 0
            for case in self.la_partie.liste_case :
                  place_pion_dans_liste = 0
                  for pion in self.la_partie.liste_pions :
                        if (pion.case == case) and (pion.equipe == "blanc") :
                              self.la_partie.liste_pions[place_pion_dans_liste].case = self.la_partie.liste_case[numero_case]
                              numero_case += 1
                        place_pion_dans_liste += 1    

            # noir    

            numero_case = 63
            for case in self.la_partie.liste_case :
                  place_pion_dans_liste = 0
                  for pion in self.la_partie.liste_pions :
                        if (pion.case == case) and (pion.equipe == "noir") :
                              self.la_partie.liste_pions[place_pion_dans_liste].case = self.la_partie.liste_case[numero_case]
                              numero_case -= 1
                        place_pion_dans_liste += 1


                        



########################################################################################################################################################################################
                

class partie_simple (object):
      """Classe qui instancie une partie."""

      def __init__ (self, pion_a_deplacer, joueur_blanc, joueur_noir) :

            self.pion_a_deplacer = pion_a_deplacer
            self.joueur_blanc = joueur_blanc
            self.joueur_noir = joueur_noir
            self.joueur = self.joueur_blanc
            self.points_victoire_pour_gagner = 1
            
            self.liste_case = []
            self.liste_pions = []
            
            self.liste_couleur = ["orange", "bleu", "mauve", "rose", "jaune", "rouge", "vert", "brun"]
            self.dictionnaire_codes_couleur = {"orange" : "#f5530c", "bleu" : "#3231d9", "mauve" : "#6e0062", "rose" : "#e5169a", "jaune" : "#dce30c", "rouge" : "#df1717", "vert" : "#148622", "brun" : "#7c3819"}
            self.creer_cases()
            self.creer_pions()
            self.mon_plateau = plateaux(self,self.liste_case, self.liste_pions)
            self.mon_plateau.geometry("800x800")

            for pion in self.liste_pions :
                  if (pion.equipe == "blanc") and (pion.couleur == self.pion_a_deplacer):
                        self.pion_a_deplacer = pion

      def creer_cases (self) :
            for numero_case in range (1, 65):
                  self.liste_case.append("case_" + str(numero_case))
                  if numero_case % 9 == 1 :
                        self.liste_case[-1] = cases(numero_case, self.dictionnaire_codes_couleur["orange"])
                  elif numero_case in [2, 13, 24, 27, 38, 41, 52, 63] :
                        self.liste_case[-1] = cases(numero_case, self.dictionnaire_codes_couleur["bleu"])
                  elif numero_case in [3, 16, 21, 26, 39, 44, 49, 62] :
                        self.liste_case[-1] = cases(numero_case, self.dictionnaire_codes_couleur["mauve"])
                  elif numero_case in [4, 11, 18, 25, 40, 47, 54, 61] :
                        self.liste_case[-1] = cases(numero_case, self.dictionnaire_codes_couleur["rose"])
                  elif numero_case in [5, 14, 23, 32, 33, 42, 51, 60] :
                        self.liste_case[-1] = cases(numero_case, self.dictionnaire_codes_couleur["jaune"])     
                  elif numero_case in [6, 9, 20, 31, 34, 45, 56, 59] :
                        self.liste_case[-1] = cases(numero_case, self.dictionnaire_codes_couleur["rouge"])
                  elif numero_case in [7, 12, 17, 30, 35, 48, 53, 58] :
                        self.liste_case[-1] = cases(numero_case, self.dictionnaire_codes_couleur["vert"])
                  else :
                        self.liste_case[-1] = cases(numero_case, self.dictionnaire_codes_couleur["brun"])

      def creer_pions (self) :
            for nombre_de_pions in range (0, 16) :
                  if nombre_de_pions < 8 :
                        self.liste_pions.append("blanc_" + self.liste_couleur[nombre_de_pions])
                        self.liste_pions[-1] = pions_tour_dragon ("blanc", self.liste_couleur[nombre_de_pions], self.dictionnaire_codes_couleur[self.liste_couleur[nombre_de_pions]], self.liste_case[nombre_de_pions])
                  else :
                        self.liste_pions.append("noir_" + self.liste_couleur[nombre_de_pions-8])
                        self.liste_pions[-1] = pions_tour_dragon ("noir", self.liste_couleur[nombre_de_pions-8], self.dictionnaire_codes_couleur[self.liste_couleur[nombre_de_pions-8]], self.liste_case[-nombre_de_pions+7])

      def gagner_manche (self):

            if self.joueur == self.joueur_blanc :
                  self.joueur_blanc.gagner_point_de_victoire(self.pion_a_deplacer.point_victoire_gagne)
                  place_pion_dans_liste = 0
            
            for pion in self.liste_pions :
                  if (pion.equipe == self.pion_a_deplacer.equipe) and (pion.couleur == self.pion_a_deplacer.couleur) :
                        self.liste_pions[place_pion_dans_liste].evoluer()
                  place_pion_dans_liste += 1

            self.mon_plateau.replacer_pions()
      
      def jouer_manche (self) :
            case_choisie = self.mon_plateau.case_choisie

            # Déplacement de pion
            place_pion_dans_liste = 0
            for pion in self.liste_pions :
                  if (pion.equipe == self.pion_a_deplacer.equipe) and (pion.couleur == self.pion_a_deplacer.couleur) :
                       self.liste_pions[place_pion_dans_liste].case = case_choisie
                  place_pion_dans_liste += 1

            # Regarde si le joueur gagne la manche

            if case_choisie.numero in [1, 2, 3, 4, 5, 6, 7, 8, 64, 63, 62, 61, 60, 59, 58, 57]:
                  self.gagner_manche() 
                  self.mon_plateau.afficher_plateau()
                  self.mon_plateau.afficher_pions()

            # Changement de joueur

      
            if self.joueur == self.joueur_blanc :
                  self.joueur = self.joueur_noir

            else :
                  self.joueur = self.joueur_blanc

            for pion in self.liste_pions :
                  if (pion.equipe == self.joueur.equipe) and (pion.code_couleur == self.mon_plateau.case_choisie.couleur) :
                        self.pion_a_deplacer = pion

            self.mon_plateau.afficher_plateau()
            self.mon_plateau.afficher_pions()         
            self.mon_plateau.afficher_case_possible(self.pion_a_deplacer)
            

      def jouer_partie (self) :

            self.mon_plateau.afficher_plateau()
            self.mon_plateau.afficher_pions()

            if self.joueur_blanc.pseudo == "bot" :
                  couleur_pion_a_deplacer = choice(["orange", "bleu", "rose", "rouge", "jaune", "brun", "vert", "mauve"])

                  for pion in self.liste_pions :
                      if (pion.equipe == "blanc") and (pion.code_couleur == couleur_pion_a_deplacer) :
                        self.pion_a_deplacer = pion

                  liste_case_possibles = self.pion_a_deplacer.trouver_possibilites_deplacement (self.liste_pions, self.liste_case)
                  
                  for pion in self.liste_pions :
                        if (pion.equipe == "noir") and (pion.code_couleur == self.pion_a_deplacer.code_couleur) :
                              self.pion_a_deplacer = pion

                  case_choisie = self.joueur.choisir_case (liste_case_possibles, self.liste_pions)

                  for pion in self.liste_pions :
                        if (pion.equipe == "blanc") and (pion.code_couleur == self.pion_a_deplacer.code_couleur) :
                              self.liste_pions[(pion.numero) - 1].case = case_choisie

            self.mon_plateau.afficher_plateau()
            self.mon_plateau.afficher_pions()         

            self.mon_plateau.afficher_case_possible(self.pion_a_deplacer)
            self.mon_plateau.mainloop()
      

########################################################################################################################################################################################

class partie_standard (partie_simple):
      """Classe qui instancie une partie."""

      def __init__ (self,premier_pion, joueur_blanc, joueur_noir) :
            partie_simple.__init__ (self, premier_pion, joueur_blanc, joueur_noir)

            self.points_victoire_pour_gagner = 3

########################################################################################################################################################################################

class partie_longue (partie_simple):
      """Classe qui instancie une partie."""

      def __init__ (self,premier_pion, joueur_blanc, joueur_noir) :
            partie_simple.__init__ (self, premier_pion, joueur_blanc, joueur_noir)

            self.points_victoire_pour_gagner = 7

########################################################################################################################################################################################

class partie_marathon (partie_simple):
      """Classe qui instancie une partie."""

      def __init__ (self, premier_pion, joueur_blanc, joueur_noir) :
            partie_simple.__init__ (self, premier_pion, joueur_blanc, joueur_noir)

            self.points_victoire_pour_gagner = 15

########################################################################################################################################################################################
def lancer_une_partie (type_partie, joueur_blanc, joueur_noir):
      if joueur_blanc.pseudo == "bot" :
            pion_a_deplacer = choice(["orange", "vert", "mauve", "jaune", "bleu", "brun", "rose", "rouge"])
            if type_partie == "simple" :
                  ma_partie = partie_simple(pion_a_deplacer, joueur_blanc, joueur_noir)

            elif type_partie == "standard" :
                  ma_partie = partie_standard(pion_a_deplacer, joueur_blanc, joueur_noir)

            elif type_partie == "longue" :
                  ma_partie = partie_longue(pion_a_deplacer, joueur_blanc, joueur_noir)

            else :
                  ma_partie = partie_marathon(pion_a_deplacer, joueur_blanc, joueur_noir)

            ma_partie.jouer_partie()
      else :
            choix_pion = fenetre_choix_pion(type_partie, joueur_blanc, joueur_noir)

lancer_une_partie("simple", joueur("Lisane", "blanc"), joueur("bot", "noir"))
