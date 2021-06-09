class Judge(object):
    def __init__(self, Rekin, Rybka):
        self.Rekin = rekin
        self.Rybka = Rybka
        self.score = [0, 0]

        pygame.font.init()
        font_path = pygame.font.match_font('arial')
        self.font = pygame.font.Font(font_path, 64)


    def update_Score(self, SCREEN_HEIGHT):

        #PRZYDZIELA PUNKTY

         if self.Rekin.rect.y < 0:
            self.score[0] += 1
        elif self.Rekin.rect.y > SCREEN_HEIGHT:
            self.score[1] += 1

    def draw_text(self, surface,  text, x, y):

        #Rysuje wskazany tekst we wskazanym miejscu

        text = self.font.render(text, True, (150, 150, 150))
        rect = text.get_rect()
        rect.center = x, y
        surface.blit(text, rect)

    def draw_on(self, surface):

        #Aktualizuje i rysuje wyniki

        height = self.screen.surface.get_height()
        self.update_score(height)

        width = self.screen.surface.get_width()
        self.draw_text(surface, "Rekin: {}".format(self.score[0]), width/2, height * 0.3)
        self.draw_text(surface, "Rybka: {}".format(self.score[1]), width/2, height * 0.7)
