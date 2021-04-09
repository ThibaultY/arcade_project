if overlap_x > 0 and overlap_y > 0:  # quadrant 1
    if cercle.change_x > 0:
        cercle.change_x *= -1
    if cercle.change_y > 0:
        cercle.change_y *= -1
elif overlap_x < 0 and overlap_y > 0:  # quadrant 2
    if cercle.change_x < 0:
        cercle.change_x *= -1
    if cercle.change_y > 0:
        cercle.change_y *= -1
elif overlap_x < 0 and overlap_y < 0:  # quadrant 3
    if cercle.change_x < 0:
        cercle.change_x *= -1
    if cercle.change_y < 0:
        cercle.change_y *= -1
elif overlap_x > 0 and overlap_y < 0:  # quadrant 4
    if cercle.change_x > 0:
        cercle.change_x *= -1
    if cercle.change_y < 0:
        cercle.change_y *= -1