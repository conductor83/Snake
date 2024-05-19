yacheika_size = 21  # pixel

field_height = 25  # cells
field_width = 25  # cells

x = field_height // 2
y = field_width // 2
vx = 0
vy = 0

window_size_x = yacheika_size * (field_width-1)
window_size_y = yacheika_size * (field_height-1)


def calc_gx(doska_x):
    return doska_x * yacheika_size


def calc_gy(doska_y):
    return window_size_y - doska_y * yacheika_size


def calc_gpos(doska_x, doska_y):
    return calc_gx(doska_x), calc_gy(doska_y)
