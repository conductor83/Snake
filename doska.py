yacheika_size = 21  # pixel

field_height = 25  # cells
field_width = 25  # cells

x = field_height // 2
y = field_width // 2
vx = 0
vy = 0

def calc_gx(fx):
    return (fx - field_width // 2) *yacheika_size-yacheika_size//7
def calc_gy(fy):
    return (fy - field_height // 2) *yacheika_size+yacheika_size//4

