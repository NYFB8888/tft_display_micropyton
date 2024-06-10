Example showing ESP32 IP etc.

from tft_display import TFT_Display

tft = TFT_Display()
tft.SetColor(255,255,255)
tft.SetCursor(3,3)
tft.Print(station.ifconfig()[0])
tft.SetCursor(3,4)
tft.Print(station.ifconfig()[1])
tft.SetCursor(3,5)
tft.Print(station.ifconfig()[2])
tft.SetCursor(3,6)
tft.Print(station.ifconfig()[3])

