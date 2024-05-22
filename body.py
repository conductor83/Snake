from doska import field_height, field_width


vx = 0
vy = 0

body_arr=[(field_height // 2, field_width // 2), None, None]
head_idx = 0
tail_idx = 0
grow = 5

def calc_snake_len():
    if head_idx > tail_idx:
        return head_idx - tail_idx + 1
    else:
        return len(body_arr) - (tail_idx - head_idx) + 1

