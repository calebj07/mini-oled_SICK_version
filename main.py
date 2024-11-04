import OLED12864_I2C

def draw_s(x, y):
    OLED12864_I2C.pixel(x + 1, y + 2, 1)
    OLED12864_I2C.pixel(x + 2, y + 2, 1)
    OLED12864_I2C.pixel(x + 3, y + 2, 1)
    OLED12864_I2C.pixel(x + 0, y + 3, 1)
    OLED12864_I2C.pixel(x + 1, y + 4, 1)
    OLED12864_I2C.pixel(x + 2, y + 4, 1)
    OLED12864_I2C.pixel(x + 3, y + 5, 1)
    OLED12864_I2C.pixel(x + 2, y + 6, 1)
    OLED12864_I2C.pixel(x + 1, y + 6, 1)
    OLED12864_I2C.pixel(x + 0, y + 6, 1)

def draw_i(x, y):
    OLED12864_I2C.pixel(x + 0, y + 2, 1)
    OLED12864_I2C.pixel(x + 0, y + 4, 1)
    OLED12864_I2C.pixel(x + 0, y + 5, 1)
    OLED12864_I2C.pixel(x + 0, y + 6, 1)

def draw_c(x, y):
    OLED12864_I2C.pixel(x + 1, y + 2, 1)
    OLED12864_I2C.pixel(x + 2, y + 2, 1)
    OLED12864_I2C.pixel(x + 0, y + 3, 1)
    OLED12864_I2C.pixel(x + 0, y + 4, 1)
    OLED12864_I2C.pixel(x + 0, y + 5, 1)
    OLED12864_I2C.pixel(x + 1, y + 6, 1)
    OLED12864_I2C.pixel(x + 2, y + 6, 1)

def draw_k(x, y):
    OLED12864_I2C.pixel(x + 0, y + 0, 1)
    OLED12864_I2C.pixel(x + 0, y + 1, 1)
    OLED12864_I2C.pixel(x + 0, y + 2, 1)
    OLED12864_I2C.pixel(x + 0, y + 3, 1)
    OLED12864_I2C.pixel(x + 0, y + 4, 1)
    OLED12864_I2C.pixel(x + 0, y + 5, 1)
    OLED12864_I2C.pixel(x + 0, y + 6, 1)
    OLED12864_I2C.pixel(x + 3, y + 2, 1)
    OLED12864_I2C.pixel(x + 2, y + 3, 1)
    OLED12864_I2C.pixel(x + 1, y + 4, 1)
    OLED12864_I2C.pixel(x + 2, y + 5, 1)
    OLED12864_I2C.pixel(x + 3, y + 6, 1)
draw_s(1, 0)
draw_i(6, 0)
draw_c(8, 0)
draw_k(12, 0)