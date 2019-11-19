import pygame
import random
import time
from math import *

pygame.init()

display_x = 1040
display_y = 680

aircraft_carrier_image_false = pygame.image.load("Aircraft_Carrier_False.png")
aircraft_carrier_image_true = pygame.image.load("BattleshipAircraft_Carrier_True.png")
cruiser_image_false = pygame.image.load("BattleshipCruiser_False.png")
cruiser_image_true = pygame.image.load("BattleshipCruiser_True.png")
submarine_image_false = pygame.image.load("BattleshipSubmarine_False.png")
submarine_image_true = pygame.image.load("BattleshipSubmarine_True.png")
destroyer_image_false = pygame.image.load("BattleshipDestroyer_False.png")
destroyer_image_true = pygame.image.load("BattleshipDestroyer_True.png")

aircraft_carrier_button_image = pygame.image.load("BattleshipAircraft_Carrier_button.png")
cruiser_button_image = pygame.image.load("BattleshipCruiser_button.png")
submarine_button_image = pygame.image.load("BattleshipSubmarine_button.png")
destroyer_button_image = pygame.image.load("BattleshipDestroyer_button.png")

aircraft_carrier_button_onclick = pygame.image.load("BattleshipAircraft_Carrier_button_onclick.png")
cruiser_button_onclick = pygame.image.load("BattleshipCruiser_button_onclick.png")
submarine_button_onclick = pygame.image.load("BattleshipSubmarine_button_onclick.png")
destroyer_button_onclick = pygame.image.load("BattleshipDestroyer_button_onclick.png")

miss_cell = pygame.image.load("BattleshipMiss_cell.png")
hit_cell = pygame.image.load("BattleshipHit_cell.png")

orient_true = pygame.image.load("Battleshiporient_true.png")
orient_false = pygame.image.load("Battleshiporient_false.png")
orient_none = pygame.image.load("Battleshiporient_none.png")

replay_button_image = pygame.image.load("BattleshipReplay_button.png")
replay_button_onclick = pygame.image.load("BattleshipReplay_button_onclick.png")
quit_button_image = pygame.image.load("BattleshipQuit_button.png")
quit_button_onclick = pygame.image.load("BattleshipQuit_button_onclick.png")

win_badge = pygame.image.load("BattleshipWin_badge.png")
lost_badge = pygame.image.load("BattleshipLost_badge.png")

homepage = pygame.image.load("BattleshipHomepage.png")
play_button_image = pygame.image.load("BattleshipPlay_button_1.png")
how_to_button_image = pygame.image.load("BattleshipHow_to_play.png")
back_to_menu_button_image = pygame.image.load("BattleshipBack_to_menu.png")

turn_image = pygame.image.load("BattleshipTurn.png")

guest_image = pygame.image.load("BattleshipGuest.png")
computer_image = pygame.image.load("BattleshipComputer.png")

x = display_x / 26
y = display_y / 17

black = (0, 0, 0)
back_blue = (30, 149, 189)
white = (255, 255, 255)
sea_blue = (89, 96, 112)
red = (255, 0, 0)
green = (0, 232, 0)

Display = pygame.display.set_mode((display_x, display_y))

pygame.display.set_caption("Battleship")

font = pygame.font.SysFont("Arial", 14)

user_cells_ref = ['0121', '0122', '0123', '0124', '0125', '0126', '0127', '0128', '0129', '0130', '0221', '0222', '0223', '0224', '0225', '0226', '0227', '0228', '0229', '0230', '0321', '0322', '0323', '0324', '0325', '0326', '0327', '0328', '0329', '0330', '0421', '0422', '0423', '0424', '0425', '0426', '0427', '0428', '0429', '0430', '0521', '0522', '0523', '0524', '0525', '0526', '0527', '0528', '0529', '0530', '0621', '0622', '0623', '0624', '0625', '0626', '0627', '0628', '0629', '0630', '0721', '0722', '0723', '0724', '0725', '0726', '0727', '0728', '0729', '0730', '0821', '0822', '0823', '0824', '0825', '0826', '0827', '0828', '0829', '0830', '0921', '0922', '0923', '0924', '0925', '0926', '0927', '0928', '0929', '0930', '1021', '1022', '1023', '1024', '1025', '1026', '1027', '1028', '1029', '1030']
AI_cells_ref = ['1121', '1122', '1123', '1124', '1125', '1126', '1127', '1128', '1129', '1130', '1221', '1222', '1223', '1224', '1225', '1226', '1227', '1228', '1229', '1230', '1321', '1322', '1323', '1324', '1325', '1326', '1327', '1328', '1329', '1330', '1421', '1422', '1423', '1424', '1425', '1426', '1427', '1428', '1429', '1430', '1521', '1522', '1523', '1524', '1525', '1526', '1527', '1528', '1529', '1530', '1621', '1622', '1623', '1624', '1625', '1626', '1627', '1628', '1629', '1630', '1721', '1722', '1723', '1724', '1725', '1726', '1727', '1728', '1729', '1730', '1821', '1822', '1823', '1824', '1825', '1826', '1827', '1828', '1829', '1830', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']

user_unused_cells = ['0121', '0122', '0123', '0124', '0125', '0126', '0127', '0128', '0129', '0130', '0221', '0222', '0223', '0224', '0225', '0226', '0227', '0228', '0229', '0230', '0321', '0322', '0323', '0324', '0325', '0326', '0327', '0328', '0329', '0330', '0421', '0422', '0423', '0424', '0425', '0426', '0427', '0428', '0429', '0430', '0521', '0522', '0523', '0524', '0525', '0526', '0527', '0528', '0529', '0530', '0621', '0622', '0623', '0624', '0625', '0626', '0627', '0628', '0629', '0630', '0721', '0722', '0723', '0724', '0725', '0726', '0727', '0728', '0729', '0730', '0821', '0822', '0823', '0824', '0825', '0826', '0827', '0828', '0829', '0830', '0921', '0922', '0923', '0924', '0925', '0926', '0927', '0928', '0929', '0930', '1021', '1022', '1023', '1024', '1025', '1026', '1027', '1028', '1029', '1030']
AI_unused_cells = ['1121', '1122', '1123', '1124', '1125', '1126', '1127', '1128', '1129', '1130', '1221', '1222', '1223', '1224', '1225', '1226', '1227', '1228', '1229', '1230', '1321', '1322', '1323', '1324', '1325', '1326', '1327', '1328', '1329', '1330', '1421', '1422', '1423', '1424', '1425', '1426', '1427', '1428', '1429', '1430', '1521', '1522', '1523', '1524', '1525', '1526', '1527', '1528', '1529', '1530', '1621', '1622', '1623', '1624', '1625', '1626', '1627', '1628', '1629', '1630', '1721', '1722', '1723', '1724', '1725', '1726', '1727', '1728', '1729', '1730', '1821', '1822', '1823', '1824', '1825', '1826', '1827', '1828', '1829', '1830', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']

user_used_cells = []
AI_used_cells = []

top_edge = ["0221", "0321", "0421", "0521", "0621", "0721", "0821", "0921"]
right_edge = ["1022", "1023", "1024", "1025", "1026", "1027", "1028", "1029"]
left_edge = ["0122", "0123", "0124", "0125", "0126", "0127", "0128", "0129"]
bottom_edge = ["0230", "0330", "0430", "0530", "0630", "0730", "0830", "0930"]

AI_hit_cells = []
user_hit_cells = []

AI_missed_cells = []
user_missed_cells = []

AI_targeted = []

last_click = ""

font = pygame.font.SysFont("Arial", 8)

class board:
    def __init__(self, pos_x, pos_y, cells_x, cells_y, cell_width_x, cell_width_y, Display, board_color, line_color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.cells_x = cells_x
        self.cells_y = cells_y
        self.cell_width_x = cell_width_x
        self.cell_width_y = cell_width_y
        self.board_color = board_color
        self.line_color = line_color
        self.display = Display
        pygame.draw.rect(self.display, self.board_color, [self.pos_x, self.pos_y, self.cells_x*self.cell_width_x, self.cells_y*self.cell_width_y])
        for x in range(self.pos_x, (self.pos_x + (self.cells_x*self.cell_width_x)), self.cell_width_x):
            for y in range(self.pos_y, (self.pos_y + (self.cells_y*self.cell_width_y)), self.cell_width_y):
                pygame.draw.rect(self.display, self.line_color, [x, y, self.cell_width_x, self.cell_width_y], 1)
        pygame.display.update()
    def draw_lines_again(self):
        for x in range(self.pos_x, (self.pos_x + (self.cells_x*self.cell_width_x)), self.cell_width_x):
            for y in range(self.pos_y, (self.pos_y + (self.cells_y*self.cell_width_y)), self.cell_width_y):
                pygame.draw.rect(self.display, self.line_color, [x, y, self.cell_width_x, self.cell_width_y], 1)
        pygame.display.update()

class button:
    def __init__(self, pos_x, pos_y, size_x, size_y, onclickfunction, image, state = True):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.state = state
        self.onclick = onclickfunction
        self.image = image
        if self.state:
            Display.blit(self.image, (pos_x, pos_y))

    def on_click(self):
        if not self.state:
            return -1
        else:
            self.onclickfunction()

    def set_false_state(self):
        self.state = False
        pygame.draw.rect(Display, back_blue, [self.pos_x, self.pos_y, self.size_x, self.size_y])

    def set_true_state(self):
        self.state = True
        print "Checkpoint"
        Display.blit(self.image, (self.pos_x, self.pos_y))

    def cell_cover(self):
        l = []
        for i in range(self.pos_x, self.pos_x + self.size_x, x):
            for j in range(self.pos_y, self.pos_y + self.size_y, y):
                l.append((i, j))
        return l

class ship:
    def __init__(self, pos_x, pos_y, orient, length, user_trigger = False):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.orient = orient
        self.length = length
        self.occupied = []
        if self.orient:
            for i in range(pos_x, pos_x + self.length):
                if len(str(i)) == 1:
                    i = "0" + str(i)
                else:
                    i = str(i)
                self.occupied.append(i + str(pos_y))
        elif not self.orient:
            for j in range(pos_y, pos_y + self.length):
                if len(str(pos_x)) == 1:
                    i = str(0) + str(pos_x)
                else:
                    i = str(pos_x)
                self.occupied.append(i + str(j))
        if not user_trigger:
            for i in self.occupied:
                AI_unused_cells.remove(i)
                AI_used_cells.append(i)
        if user_trigger:
            for i in self.occupied:
                user_unused_cells.remove(i)
                user_used_cells.append(i)

    def __str__(self):
        return str(self.orient) + " " + str(self.pos_x) + " " + str(self.pos_y)

    @staticmethod
    def calculate_usable_cells(orient, length):
        if orient == None:
            pass
        unusable = []
        usable = []
        if orient:
            for i in AI_used_cells:
                xc = int(i[0:2])
                yc = (i[2:4])
                for j in range(xc - length + 1, xc):
                    print j
                    if len(str(j)) == 1:
                        j = "0" + str(j)
                    unusable.append(str(j) + yc)
        if not orient:
            for i in AI_used_cells:
                xc = i[0:2]
                yc = int(i[2:4])
                for j in range(yc - length + 1, yc):
                    unusable.append(xc + str(j))
        for i in AI_cells_ref:
            if i not in unusable and i not in AI_used_cells:
                if orient:
                    if int(i[1]) < 12 - length and int(i[0:2]) != 20:
                        usable.append(i)
                if not orient:
                    if int(i[3]) < 12 - length and int(i[2:4]) != 30:
                        usable.append(i)
        return usable

    @staticmethod
    def calculate_usable_cells_user(orient, length):
        print orient
        if orient == None:
            return -1
        usable = []
        unusable = []
        if orient:
            for i in user_used_cells:
                xc = int(i[0:2])
                yc = i[2:4]
                for j in range(xc - length + 1, xc):
                    if len(str(j)) == 1:
                        j = "0" + str(j)
                    unusable.append(str(j) + yc)
        if not orient:
            for i in user_used_cells:
                xc = i[0:2]
                yc = int(i[2:4])
                for j in range(yc - length + 1, yc):
                    unusable.append(xc + str(j))
        for i in user_cells_ref:
            if i not in unusable and i not in user_used_cells:
                if orient:
                    if int(i[1]) < 12 - length and int(i[0:2]) != 10:
                        usable.append(i)
                if not orient:
                    if int(i[3]) < 12 - length and int(i[2:4]) != 30:
                        usable.append(i)
        print "Usable", usable
        print "Unusable", unusable
        return usable
    """

    @staticmethod
    def calculate_usable_cells_user(orient, length):
        if orient == None:
            return -1
        usable = []
        unusable = []
        if orient:
            for i in user_used_cells:
                xc = i[0:2]
                yc = int(i[2:4])
                for j in range(yc - length + 1, yc):
                    unusable.append(xc + str(j))
    """

    def preview(orient, length, pos):
        pass

class aircraft_carrier(ship):
    def __init__(self, pos_x, pos_y, orient, user_trigger = False):
        if len(str(pos_x)) == 1:
            pos_x = "0" + str(pos_x)
        if len(str(pos_y)) == 1:
            pos_y = "0" + str(pos_y)
        pos_x = int(pos_x)
        pos_y = int(pos_y)
        ship.__init__(self, pos_x, pos_y, orient, 5, user_trigger)

class cruiser(ship):
    def __init__(self, pos_x, pos_y, orient, user_trigger = False):
        if len(str(pos_x)) == 1:
            pos_x = "0" + str(pos_x)
        if len(str(pos_y)) == 1:
            pos_y = "0" + str(pos_y)
        pos_x = int(pos_x)
        pos_y = int(pos_y)
        ship.__init__(self, pos_x, pos_y, orient, 4, user_trigger)

class submarine(ship):
    def __init__(self, pos_x, pos_y, orient, user_trigger = False):
        if len(str(pos_x)) == 1:
            pos_x = "0" + str(pos_x)
        if len(str(pos_y)) == 1:
            pos_y = "0" + str(pos_y)
        pos_x = int(pos_x)
        pos_y = int(pos_y)
        ship.__init__(self, pos_x, pos_y, orient, 3, user_trigger)

class destroyer(ship):
    def __init__(self, pos_x, pos_y, orient, user_trigger = False):
        if len(str(pos_x)) == 1:
            pos_x = "0" + str(pos_x)
        if len(str(pos_y)) == 1:
            pos_y = "0" + str(pos_y)
        pos_x = int(pos_x)
        pos_y = int(pos_y)
        ship.__init__(self, pos_x, pos_y, orient, 2, user_trigger)

def qsequence():
    pygame.quit()
    quit()

def blank_function():
    pass

def message_to_screen(x, y, msg, color):
    msg = str(msg)
    screen_text = font.render(msg, True, color)
    Display.blit(screen_text, [x, y])

def cell_to_x_and_y(cell):
    a = int(cell[0:2])
    b = int(cell[2:4])
    if a < 11:
        a = (a + 1)*x
    else:
        a = (a + 3)*x
    b = (b - 19)*y
    return (a, b)

def x_and_y_to_cell(t):
    a = t[0]
    b = t[1]
    if floor(a/x) < 13:
        m = str(int(floor(a/x)) - 1)
        if len(m) == 1:
            m = "0" + m
    else:
        m = str(int(floor(a/x)) - 3)
    n = str(int(floor(b/y)) + 19)
    return (m + n)

def top_corner(t):
    a = t[0]
    b = t[1]
    at = x * (a/x)
    bt = y * (b/y)
    return (at, bt)

def cell_int_to_str(cell_int):
    if len(cell_int) == 3:
        return "0" + (cell_int)
    return (cell_int)

def aircraft_carrier_button_click():
    global last_click
    if aircraft_carrier_button.state == True:
        last_click = "Aircraft Carrier"
        Display.blit(aircraft_carrier_button_onclick, (3*x, 13*y))
    return 5

def cruiser_button_click():
    global last_click
    if cruiser_button.state == True:
        last_click = "Cruiser"
        Display.blit(cruiser_button_onclick, (5*x, 13*y))
    return 4

def submarine_button_click():
    global last_click
    if submarine_button.state == True:
        last_click = "Submarine"
        Display.blit(submarine_button_onclick, (8*x, 13*y))
    return 3

def destroyer_button_click():
    global last_click
    if destroyer_button.state == True:
        last_click = "Destroyer"
        Display.blit(destroyer_button_onclick, (10*x, 13*y))
    return 2

def AI_Ship_Set():
    orient_5 = random.choice([0, 1])
    usable = ship.calculate_usable_cells(orient_5, 5)
    a = random.randrange(0, len(usable) - 1)
    ship_5 = aircraft_carrier(int(usable[a][0:2]), int(usable[a][2:4]), orient_5)

    orient_4 = random.choice([0, 1])
    usable = ship.calculate_usable_cells(orient_4, 4)
    a = random.randrange(0, len(usable) - 1)
    ship_4 = cruiser(int(usable[a][0:2]), int(usable[a][2:4]), orient_4)

    orient_3 = random.choice([0, 1])
    usable = ship.calculate_usable_cells(orient_3, 3)
    a = random.randrange(0, len(usable) - 1)
    ship_3 = submarine(int(usable[a][0:2]), int(usable[a][2:4]), orient_3)

    orient_2 = random.choice([0, 1])
    usable = ship.calculate_usable_cells(orient_2, 2)
    a = random.randrange(0, len(usable) - 1)
    ship_2 = destroyer(int(usable[a][0:2]), int(usable[a][2:4]), orient_2)

def user_ship_set():
    global last_click
    global buttons
    last_click_orient = None
    while True:
        for event in pygame.event.get():
            print event
            if last_click_orient == None:
                Display.blit(orient_none, (6.5*x, 14*y))
            elif last_click_orient:
                Display.blit(orient_true, (6.5*x, 14*y))
            elif not last_click_orient:
                Display.blit(orient_false, (6.5*x, 14*y))
            if event.type == 2:
                if event.scancode == 72 or event.scancode == 80:
                    last_click_orient = False
                if event.scancode == 75 or event.scancode == 77:
                    last_click_orient = True
            """
            if event.type == 4:
                if last_click == "Aircraft Carrier":
                    ship.preview(last_click_orient, 5, x_and_y_to_cell(top_corner(event.pos)))
                if last_click == "Cruiser":
                    ship.preview(last_click_orient, 4, x_and_y_to_cell(top_corner(event.pos)))
                if last_click == "Submarine":
                    ship.preview(last_click_orient, 3, x_and_y_to_cell(top_corner(event.pos)))
                if last_click == "Destroyer":
                    ship.preview(last_click_orient, 2, x_and_y_to_cell(top_corner(event.pos)))
            """
            if event.type == 5:
                print top_corner(event.pos)
                print x_and_y_to_cell(event.pos)
                if top_corner(event.pos) in back_to.cell_cover():
                    back_to.onclick()
                if event.button == 1:
                    if (x_and_y_to_cell(event.pos)) == "0232":
                        aircraft_carrier_button_click()
                    if (x_and_y_to_cell(event.pos)) == "0432":
                        cruiser_button_click()
                    if (x_and_y_to_cell(event.pos)) == "0732":
                        submarine_button_click()
                    if (x_and_y_to_cell(event.pos)) == "0932":
                        destroyer_button_click()
                print last_click
                print last_click_orient
                print ship.calculate_usable_cells_user(last_click_orient, 5)
                if last_click == "Aircraft Carrier":
                    try:
                        if x_and_y_to_cell(event.pos) in ship.calculate_usable_cells_user(last_click_orient, 5):
                            aircraft_carrier(int(x_and_y_to_cell(event.pos)[0:2]), int(x_and_y_to_cell(event.pos)[2:4]), last_click_orient, True)
                            last_click = None
                            aircraft_carrier_button.set_false_state()
                            if last_click_orient:
                                Display.blit(aircraft_carrier_image_true, top_corner(event.pos))
                            elif not last_click_orient:
                                Display.blit(aircraft_carrier_image_false, top_corner(event.pos))
                    except TypeError:
                        pass
                if last_click == "Cruiser":
                    try:
                        if x_and_y_to_cell(event.pos) in ship.calculate_usable_cells_user(last_click_orient, 4):
                            cruiser(int(x_and_y_to_cell(event.pos)[0:2]), int(x_and_y_to_cell(event.pos)[2:4]), last_click_orient, True)
                            last_click = None
                            cruiser_button.set_false_state()
                            if last_click_orient:
                                Display.blit(cruiser_image_true, top_corner(event.pos))
                            if not last_click_orient:
                                Display.blit(cruiser_image_false, top_corner(event.pos))
                    except TypeError:
                        pass
                if last_click == "Submarine":
                    try:
                        if x_and_y_to_cell(event.pos) in ship.calculate_usable_cells_user(last_click_orient, 3):
                            submarine(int(x_and_y_to_cell(event.pos)[0:2]), int(x_and_y_to_cell(event.pos)[2:4]), last_click_orient, True)
                            last_click = None
                            submarine_button.set_false_state()
                            if last_click_orient:
                                Display.blit(submarine_image_true, top_corner(event.pos))
                            if not last_click_orient:
                                Display.blit(submarine_image_false, top_corner(event.pos))
                    except TypeError:
                        pass
                if last_click == "Destroyer":
                    try:
                        if x_and_y_to_cell(event.pos) in ship.calculate_usable_cells_user(last_click_orient, 2):
                            destroyer(int(x_and_y_to_cell(event.pos)[0:2]), int(x_and_y_to_cell(event.pos)[2:4]), last_click_orient, True)
                            last_click == None
                            destroyer_button.set_false_state()
                            if last_click_orient:
                                Display.blit(destroyer_image_true, top_corner(event.pos))
                            if not last_click_orient:
                                Display.blit(destroyer_image_false, top_corner(event.pos))
                    except TypeError:
                        pass
            if event.type == 12:
                qsequence()
            temp = []
            for i in [destroyer_button, aircraft_carrier_button, submarine_button, cruiser_button]:
                if i.state == False:
                    temp.append(1)
            print temp
            if len(temp) == 4:
                pygame.display.update()
                return -1
            pygame.display.update()

def check_cell(cell, user_trigger = False):
    if user_trigger:
        if cell in AI_used_cells:
            return 1
    elif not user_trigger:
        if cell in user_used_cells:
            return 1
    return 0

def around_cell_str_function(integer):
    if len(str(integer)) != 2:
        return "0" + str(integer)
    else:
        return str(integer)

def around_cell(cell):
    if cell == "0121":
        around = ["0122", "0221"]
    if cell == "1021":
        around = ["1022", "0921"]
    if cell == "0130":
        around = ["0129", "0230"]
    if cell == "1030":
        around = ["1029", "0929"]
    x = int(cell[0:2])
    y = int(cell[2:4])
    a1 = x - 1
    a2 = x + 1
    b1 = y - 1
    b2 = y + 1
    x = around_cell_str_function(x)
    y = around_cell_str_function(y)
    a1 = around_cell_str_function(a1)
    a2 = around_cell_str_function(a2)
    b1 = around_cell_str_function(b1)
    b2 = around_cell_str_function(b2)
    if cell in top_edge:
        around = [a1 + y, a2 + y, x + b2]
    if cell in bottom_edge:
        around = [a1 + y, a2 + y, x + b1]
    if cell in left_edge:
        around = [x + b1, x + b2, a2 + y]
    if cell in right_edge:
        around = [x + b1, x + b2, a1 + y]
    else:
        around = [x + b1, x + b2, a1 + y, a2 + y]
    return around

def redef_targets():
    global AI_targeted
    AI_targeted = []
    for i in AI_hit_cells:
        xc = int(i[0:2])
        yc = int(i[2:4])
        if cell_int_to_str(str(xc - 1) + str(yc)) in AI_hit_cells and cell_int_to_str(str(xc - 2) + str(yc)) not in AI_hit_cells and cell_int_to_str(str(xc - 2) + str(yc)) not in AI_missed_cells:
            AI_targeted.append(cell_int_to_str(str(xc - 2) + str(yc)))
        if cell_int_to_str(str(xc + 1) + str(yc)) in AI_hit_cells and cell_int_to_str(str(xc + 2) + str(yc)) not in AI_hit_cells and cell_int_to_str(str(xc + 2) + str(yc)) not in AI_missed_cells:
            AI_targeted.append(cell_int_to_str(str(xc + 2) + str(yc)))
        if cell_int_to_str(str(xc) + str(yc - 1)) in AI_hit_cells and cell_int_to_str(str(xc) + str(yc - 2)) not in AI_hit_cells and cell_int_to_str(str(xc) + str(yc - 2)) not in AI_missed_cells:
            AI_targeted.append(cell_int_to_str(str(xc) + str(yc - 2)))
        if cell_int_to_str(str(xc) + str(yc + 1)) in AI_hit_cells and cell_int_to_str(str(xc) + str(yc + 2)) not in AI_hit_cells and cell_int_to_str(str(xc) + str(yc + 2)) not in AI_missed_cells:
            AI_targeted.append(cell_int_to_str(str(xc) + str(yc + 2)))

def AI_move():
    Display.blit(turn_image, (23*x, y))
    pygame.display.update()
    pygame.time.wait(1000)
    global AI_targeted
    global user_cells_ref
    global AI_hit_cells
    global AI_missed_cells
    availible = []
    for i in user_cells_ref:
        if i not in AI_hit_cells and i not in AI_missed_cells:
            availible.append(i)
    if AI_targeted == []:
        a = random.randrange(0, len(availible) - 1)
        if check_cell(availible[a]):
            AI_hit_cells.append(availible[a])
            for i in around_cell(availible[a]):
                if i in availible:
                    AI_targeted.append(i)
            b = availible[a]
            Display.blit(hit_cell, (cell_to_x_and_y(b)[0], cell_to_x_and_y(b)[1]))
            pygame.draw.rect(Display, back_blue, [23*x, y, x, y])
            return 1
        else:
            AI_missed_cells.append(availible[a])
            b = availible[a]
            pygame.draw.rect(Display, back_blue, [23*x, y, x, y])
            Display.blit(miss_cell, (cell_to_x_and_y(b)[0], cell_to_x_and_y(b)[1]))
            return 0
    if AI_targeted != []:
        t = AI_targeted[0]
        if check_cell(t):
            AI_hit_cells.append(t)
            redef_targets()
            Display.blit(hit_cell, (cell_to_x_and_y(t)[0], cell_to_x_and_y(t)[1]))
            pygame.draw.rect(Display, back_blue, [23*x, y, x, y])
            return 1
        else:
            AI_missed_cells.append(t)
            AI_targeted.remove(t)
            Display.blit(miss_cell, (cell_to_x_and_y(t)[0], cell_to_x_and_y(t)[1]))
            pygame.draw.rect(Display, back_blue, [23*x, y, x, y])
            return 0


def user_move():
    global user_missed_cells
    global user_hit_cells
    global AI_cells_ref
    Display.blit(turn_image, (11*x, y))
    while True:
        for event in pygame.event.get():
            if event.type == 5:
                if top_corner(event.pos) in back_to.cell_cover():
                    back_to.onclick()
                if event.button == 1:
                    if x_and_y_to_cell(top_corner(event.pos)) in AI_cells_ref and x_and_y_to_cell(top_corner(event.pos)) not in user_hit_cells and x_and_y_to_cell(top_corner(event.pos)) not in user_missed_cells:
                        if check_cell(x_and_y_to_cell(event.pos), True):
                            Display.blit(hit_cell, (top_corner(event.pos)[0], top_corner(event.pos)[1]))
                            user_hit_cells.append(x_and_y_to_cell(event.pos))
                            pygame.draw.rect(Display, back_blue, [11*x, y, x, y])
                            pygame.display.update()
                            return 0
                        else:
                            Display.blit(miss_cell, (top_corner(event.pos)[0], top_corner(event.pos)[1]))
                            user_missed_cells.append(x_and_y_to_cell(event.pos))
                            pygame.draw.rect(Display, back_blue, [11*x, y, x, y])
                            pygame.display.update()
                            return 1
            if event.type == 12:
                qsequence()
            pygame.display.update()

def GameLoop():
    global aircraft_carrier_button
    global cruiser_button
    global submarine_button
    global destroyer_button
    global AI_hit_cells
    global user_hit_cells
    global AI_used_cells
    global user_used_cells

    Display.fill(back_blue)

    b1 = board(2*x, 2*y, 10, 10, x, y, Display, sea_blue, black)
    b2 = board(14*x, 2*y, 10, 10, x, y, Display, sea_blue, black)

    Display.blit(guest_image, (5*x, y))
    Display.blit(computer_image, (17*x, y))

    for i in buttons:
        if i in [destroyer_button, aircraft_carrier_button, submarine_button, cruiser_button, back_to]:
            i.set_true_state()
        else:
            i.set_false_state

    print aircraft_carrier_button.state

    GameExit = False
    GameOver = False

    AI_Ship_Set()
    user_ship_set()

    turn = random.randrange(0, 2, 1)

    while not GameExit:
        while GameOver:
            for event in pygame.event.get():
                if event.type == 5:
                    if x_and_y_to_cell(event.pos) in ["1232", "1332", "1432"]:
                        Display.blit(replay_button_onclick, (15*x, 13*y))
                    if x_and_y_to_cell(event.pos) in ["1732", "1832", "1932"]:
                        Display.blit(quit_button_onclick, (20*x, 13*y))
                    if top_corner(event.pos) in back_to.cell_cover():
                        back_to.onclick()
                if event.type == 6:
                    if x_and_y_to_cell(event.pos) in ["1232", "1332", "1432"]:
                        replay.onclick()
                    if x_and_y_to_cell(event.pos) in ["1732", "1832", "1932"]:
                        qbutton.onclick()
                if event.type == 12:
                    qsequence()
                pygame.display.update()
        AI_hit_cells.sort()
        user_used_cells.sort()
        user_hit_cells.sort()
        AI_used_cells.sort()
        if not turn:
            AI_move()
            pygame.display.update()
            turn = 1
        if AI_hit_cells == user_used_cells:
            GameOver = True
            replay.set_true_state()
            qbutton.set_true_state()
            LW = False
            Display.blit(lost_badge, (15*x, 15*y))
            pygame.display.update()
            continue
        if turn:
            user_move()
            turn = 0
        AI_hit_cells.sort()
        user_used_cells.sort()
        user_hit_cells.sort()
        AI_used_cells.sort()
        if user_hit_cells == AI_used_cells:
            GameOver = True
            replay.set_true_state()
            qbutton.set_true_state()
            LW = True
            Display.blit(win_badge, (15*x, 15*y))
            pygame.display.update()
            continue

        pygame.display.update()

def Home_Screen():
    for i in buttons:
        if i not in [play1, how_to]:
            i.set_false_state()
    Display.blit(homepage, (0, 0))
    play1.set_true_state()
    how_to.set_true_state()
    while True:
        for event in pygame.event.get():
            if event.type == 5:
                if top_corner(event.pos) in play1.cell_cover():
                    play1.onclick()
                if top_corner(event.pos) in how_to.cell_cover():
                    how_to.onclick()
            if event.type == 12:
                qsequence()
            pygame.display.update()

def How_to_play():
    for i in buttons:
        if i not in [play2, back_to]:
            i.set_false_state()
    Display.blit(homepage, (0, 0))
    play2.set_true_state()
    back_to.set_true_state()
    while True:
        for event in pygame.event.get():
            if event.type == 5:
                if top_corner(event.pos) in play2.cell_cover():
                    play2.onclick()
                if top_corner(event.pos) in back_to.cell_cover():
                    back_to.onclick()
            if event.type == 12:
                qsequence()
            pygame.display.update()

aircraft_carrier_button = button(3*x, 13*y, x, y, aircraft_carrier_button_click, aircraft_carrier_button_image, False)
cruiser_button = button(5*x, 13*y, x, y, cruiser_button_click, cruiser_button_image, False)
submarine_button = button(8*x, 13*y, x, y, submarine_button_click, submarine_button_image, False)
destroyer_button = button(10*x, 13*y, x, y, destroyer_button_click, destroyer_button_image, False)

replay = button(15*x, 13*y, 3*x, y, GameLoop, replay_button_image, False)
qbutton = button(20*x, 13*y, 3*x, y, qsequence, quit_button_image, False)

play1 = button(12*x, 3*y, 4*x, 4*y, GameLoop, play_button_image, False)
how_to = button(12*x, 7*y, 4*x, 2*y, How_to_play, how_to_button_image, False)

play2 = button(22*x, 13*y, 4*x, 4*y, GameLoop, play_button_image, False)
back_to = button(0, 15*y, 4*x, 2*y, Home_Screen, back_to_menu_button_image, False)

buttons = [aircraft_carrier_button, cruiser_button, submarine_button, destroyer_button, how_to, back_to, play1, play2, replay, qbutton]

Home_Screen()
