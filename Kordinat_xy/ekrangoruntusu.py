from PIL import ImageGrab

# Ekranın sol üstünden sağ altına kadar olan bir bölgeyi yakala
screenshot = ImageGrab.grab(bbox=(11, 59, 283, 278))  # Bu değerleri ihtiyaca göre ayarlayın

# Yakalanan ekran görüntüsünü kaydet
screenshot.save('screenshot.png')

# Yakalanan ekran görüntüsünü göster
screenshot.show()