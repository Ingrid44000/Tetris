import pygame


colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0)]


class Case:
    def __init__(self, x, y, couleur):
        self.x = x
        self.y = y
        self.couleur = couleur

    def afficher(self, surface):
        pygame.draw.rect(surface, self.couleur, pygame.Rect(self.x*40, self.y*40, 40, 40), 3)
        pygame.display.flip()
        
    def colorier_case(self,surface, couleur = (0,255,0)):
        pygame.draw.rect(surface, couleur, pygame.Rect(self.x * 40, self.y * 40, 40, 40))
        pygame.display.flip()
    
         
class Grille():
    def __init__(self, hauteur, largeur):
        self.grille = [[Case(x,y, couleur = (255,255,255)) for x in range(largeur)] for y in range(hauteur)]
        self.hauteur = hauteur
        self.largeur = largeur
        
          
        
    def affichergrille(self, surface):
        for sousliste in self.grille:
            for case in sousliste:
                case.afficher(surface)
                
    def find_case(self, x,y) :
        return self.grille[x][y]
                
        
        
# class Figure:
    
#     def __init__(self, x, y, shape):
#         self.x = x
#         self.y = y
#         self.shape = shape
#         self.color = random.choice(colors) # You can choose different colors for each shape
#         self.rotation = 0
    

def main():
    pygame.init()
    surface = pygame.display.set_mode((650,750))
    
    
    grille = Grille(18, 10)
    grille.affichergrille(surface)
    case = grille.find_case(5,2)
    case.colorier_case(surface)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("haut")
                if event.key == pygame.K_DOWN:
                    print("bas")
                if event.key == pygame.K_LEFT:
                    print("gauche")
                if event.key == pygame.K_RIGHT:
                    print("droite")




main()