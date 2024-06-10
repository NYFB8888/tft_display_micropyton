from time import sleep
from lib.ili9488 import Display, color565
from machine import Pin, SPI
from lib.xglcd_font import XglcdFont
import random


class TFT_Display(XglcdFont, Display):
    x = 0
    y = 0
    color = 0xFFFF
    backgrund = 0
    def __init__(self):
        spi = SPI(1, baudrate=60000000, sck=Pin(12), mosi=Pin(11))
        self.display = Display(spi, dc=Pin(5), cs=Pin(10), rst=Pin(6), width=480, height = 320, rotation = 180)
        self.defaultFont = XglcdFont('lib/fonts/Liberation_Sans27x36.c', 27, 36, 46, 12 )
        self.display.clear(0)
        
    def Print(self,text):
        self.display.draw_text(self.x, self.y, text, self.defaultFont, self.color)
    
    def FontHeight(self):
        return self.defaultFont.height
    
    def	FontWidth(self):
        return self.defaultFont.width
    
    def SetColor(self,blue,green,red):
        self.color = color565(blue,green,red)
    
    def DrawCircle(self,x,y,r):
        self.display.draw_circle(x, y, r, self.color)
    
    def DrawEllipse(self,x,y,a,b,):
        self.display.draw_ellipse(x, y, a, b, self.color)
    
    def SetCursor(self, x, y):
        if x+x*self.FontWidth() < self.display.width:
            self.x = x * self.FontWidth()
        if y+y*self.FontHeight() < self.display.height:
            self.y = y * self.FontHeight()
        
    def SetFont(self,font_name, width, height, start_letter, counter_letter):
        self.defaultFont = XglcdFont(font_name, width, height, start_letter, counter_letter )
        self.display.clea(0)
        self.x=0
        self.y=0
        
    def FillCircle(self, x, y, r):
         self.display.fill_circle(0, 0, r, self.color)
    
    def FillEllipse(self, x, y, a, b ):
        self.display.fill_ellipse(x, y, a, b, self.color)
            
    def FillHRect(self, x, y, w, h ):
        self.display.fill_hrect(x,y,w,h, self.color)
        
    def FillRectangle(self,x,y,w,h):
        self.display.fill_rectangle( x, y, w, h, self.color)
    
    def FillPolygon(self,sides,x,y,r,rotate=0):
        self.display.fill_polygon(sides, x, y, r, self.color, rotate=rotate)
    
    def FillVRect(self,x,y,w,h):
        self.display.fill_vrect(x, y, w, h, self.color)
    
    def DrwaHLine(self,x,y,w):
        self.display.draw_hline( x, y, w, self.color)
    
    def DrawVLine(self, x, y, h ):
        self.display.draw_vline( x, y, h, self.color)
            
    def DrawLine( self,x1, y1, x2, y2):
        self.display.draw_line( x1, y1, x2, y2, self.color)
    
    def DrawLines(self, coords):
        self.display.draw_lines(coords, self.color)
    
    def DrawPixel(self, x, y):
        self.display.draw_pixel( x, y, self.color)        
        
    def DrawPolygon(self, sides, x, y, r, rotate=0):
        self.display.draw_polygon( x, y, r, self.color, rotate=rotate)
        
    def DrawRectangle(self, x, y, w, h):
        self.display.draw_rectangle( x, y, w, h, self.color)
        
    def DrawSprite( self,buf, x, y, w, h):
        self.display.draw_sprite(buf, x, y, w, h)

    def DrawImage(self, path, x=0, y=0, w=480, h=320):
        self.display.draw_image(path,x,y,w,h);
        
    def DrawLetter(self, x, y, letter, font,  landscape = True):
        self.display.draw_letter( x, y, letter, self.font, self.color, landscape = landscape)
   
