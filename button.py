class Button:
    def __init__(self, xpos, ypos, width, height, color, text, textColor):
        self.text = text
        self.textColor = textColor
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.color = color
        self.enable = True

    def draw(self, pg, screen):
        font = pg.font.SysFont('Corbel', 20)
        t = font.render(self.text, True, self.textColor)
        pg.draw.rect(screen, self.color, [self.xpos, self.ypos, self.width, self.height])
        textSize = len(self.text)
        screen.blit(t, (self.xpos + self.width / 2 - (textSize / 2) * 7, self.ypos + self.height / 2 - 10))
    
    def hasButtonClicked(self, xmouse, ymouse):
        if self.xpos <= xmouse <= self.xpos + self.width and self.ypos <= ymouse <= self.ypos + self.height:
            return True
        return False