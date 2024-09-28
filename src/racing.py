import customtkinter
import re
import pywinctl
import keyboard
import time
import math
import pyperclip
from typing import Literal
from images import Images
from CTkMessagebox import CTkMessagebox
from functions import *
from widgets import *

class Racing(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("600x600")
        self.title("Private Game Helper - Racing")
        self.resizable(False, False)
        self.banana_count: int = 0
        
        Text(self, text="Hamball Racing", font="title", place=(20, 20))
        
        # Settings
        Text(self, text="Map:", place=(20, 60))
        self.map_select = OptionMenu(self, values=["Super Stage GP", "Penguin Palace GP", "Pyramid GP"], width=175, command=self.change_map, place=(20, 90))
        Text(self, text="Host ID:", place=(300, 60))
        self.host_id_entry = Entry(self, width=175, placeholder_text="e.g. 1", place=(300, 90))
        Text(self, text="Selected Map", font="title", place=(20, 160))
        self.selected_map_image = Image(self, image=Images.SUPER_STAGE_GP, width=500, height=300, place=(50, 190))
        self.selected_map_author = Text(self, text="Map by:\nDeltaEagle84", justify="center", place=(230, 500))
        
        Button(self, text="Start Match", command=self.start_match, place=(20, 555))
        
        Settings.update(self=Settings)
    
    def change_map(self, value: Literal["Super Stage GP", "Penguin Palace GP", "Pyramid GP"]) -> None:
        match value:
            case "Super Stage GP":
                self.selected_map_image.configure(image=Images.SUPER_STAGE_GP)
                self.selected_map_author.configure(text="Map by:\n DeltaEagle84")
            case "Penguin Palace GP":
                self.selected_map_image.configure(image=Images.PENGUIN_PALACE_GP)
                self.selected_map_author.configure(text="Map by:\n UmbraCuticus")
            case "Pyramid GP":
                self.selected_map_image.configure(image=Images.PYRAMID_GP)
                self.selected_map_author.configure(text="Map by:\n UmbraCuticus")
    
    def validate_host(self, value: str) -> bool:
        pattern = r"^[0-9]{1}[a-zA-Z ]{0}|^[0-9]{2}[a-zA-Z ]{0}"
        if re.fullmatch(pattern, value) is None:
            return False
        return True
    
    def spawn_bananas(self, amount: int) -> None:
        send_commands(f"banana {amount}")
        time.sleep(KEY_DELAY*8)
        press_throwable()
        self.banana_count = 10
    
    def lay_banana(self, x_player: int, y_player: int, direction: Literal["N", "S", "E", "W"] = "N") -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window_rect = sar_window.getClientFrame()
        window_top_left_x, window_top_left_y = sar_window_rect[0], sar_window_rect[1]
        window_width: int = sar_window_rect[2] - window_top_left_x
        x_position, y_position = sar_window.center
        offset: int = 50
        
        size_ratio: float = window_width / 1920
        if size_ratio != 1:
            y_position: int = int(x_position * size_ratio)
            y_position: int = int(y_position * size_ratio)
            offset: int = int(offset * size_ratio)
        
        match direction:
            case "N":
                y_position -= offset
            case "S":
                y_position += offset
            case "E":
                x_position += offset
            case "W":
                x_position -= offset
        
        click_x: int = window_top_left_x + x_position
        click_y: int = window_top_left_y + y_position
        
        sar_window.activate()
        pyperclip.copy(f"/tele {self.host_id_entry.get()} {x_player} {y_player}")
        keyboard.send("\n")
        time.sleep(KEY_DELAY)
        keyboard.send("ctrl+v")
        time.sleep(KEY_DELAY)
        keyboard.send("\n")
        if self.banana_count <= 0:
            self.spawn_bananas(10)
        time.sleep(KEY_DELAY*8)
        press_throwable()
        mouse_click(click_x, click_y)
        self.banana_count -= 1
    
    def lay_zip(self, x_player: int, y_player: int, x_mouse: int, y_mouse: int) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window_rect = sar_window.getClientFrame()
        window_top_left_x, window_top_left_y = sar_window_rect[0], sar_window_rect[1]
        window_width: int = sar_window_rect[2] - window_top_left_x
        
        size_ratio: float = window_width / 1920
        if size_ratio != 1:
            x_mouse = int(x_mouse * size_ratio)
            y_mouse = int(y_mouse * size_ratio)
        
        click_x: int = window_top_left_x + x_mouse
        click_y: int = window_top_left_y + y_mouse
        
        sar_window.activate()
        send_commands(f"tele {self.host_id_entry.get()} {x_player} {y_player}", "zip", delay=8)
        time.sleep(KEY_DELAY*16)
        press_use()
        time.sleep(KEY_DELAY*8)
        press_throwable()
        mouse_click(click_x, click_y)
    
    def break_boxes(self, x_player: int, y_player: int, x_mouse: int, y_mouse: int) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window_rect = sar_window.getClientFrame()
        window_top_left_x, window_top_left_y = sar_window_rect[0], sar_window_rect[1]
        window_width: int = sar_window_rect[2] - window_top_left_x
        
        size_ratio: float = window_width / 1920
        if size_ratio != 1:
            x_mouse = int(x_mouse * size_ratio)
            y_mouse = int(y_mouse * size_ratio)
        
        click_x: int = window_top_left_x + x_mouse
        click_y: int = window_top_left_y + y_mouse
        
        sar_window.activate()
        send_commands(f"tele {self.host_id_entry.get()} {x_player} {y_player}")
        press_melee()
        mouse_click(click_x, click_y)
    
    def spawn_hamball(self, x: int, y: int) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"tele {self.host_id_entry.get()} {x} {y}", "hamball")
    
    def get_curve_coordinates(self, x_center: int, y_center: int, radius: int, angle: int, quarter: Literal["NW", "NE", "SW", "SE"], num_of_bananas: int, reverse: bool = False) -> list[tuple[int, int]]:
        angle_increase: float = angle / num_of_bananas
        points_on_curve: list[tuple[int, int]] = []
        match quarter:
            case "NW":
                for i in range(num_of_bananas):
                    x: int = int(x_center - radius * math.cos(math.radians(angle_increase * (i + 1))))
                    y: int = int(y_center + radius * math.sin(math.radians(angle_increase * (i + 1))))
                    points_on_curve.append((x, y))
            case "NE":
                for i in range(num_of_bananas):
                    x: int = int(x_center + radius * math.cos(math.radians(angle_increase * (i + 1))))
                    y: int = int(y_center + radius * math.sin(math.radians(angle_increase * (i + 1))))
                    points_on_curve.append((x, y))
            case "SW":
                for i in range(num_of_bananas):
                    x: int = int(x_center - radius * math.cos(math.radians(angle_increase * (i + 1))))
                    y: int = int(y_center - radius * math.sin(math.radians(angle_increase * (i + 1))))
                    points_on_curve.append((x, y))
            case "SE":
                for i in range(num_of_bananas):
                    x: int = int(x_center + radius * math.cos(math.radians(angle_increase * (i + 1))))
                    y: int = int(y_center - radius * math.sin(math.radians(angle_increase * (i + 1))))
                    points_on_curve.append((x, y))
        if reverse:
            points_on_curve.reverse()
        return points_on_curve
    
    def start_match(self) -> None:
        # Guard clauses
        if self.validate_host(self.host_id_entry.get()) is False:
            CTkMessagebox(self, message="Invalid host ID")
            return
        
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        if open_window("Super Animal Royale") is False:
            return
        
        # Startup commands
        send_commands("allitems", "emus", "hamballs", "gasoff", "ziplines", "startp", "god all")
        send_commands("yell Welcome to hamball racing!",
                      "yell Please jump out of the eagle as soon as possible")
        
        time.sleep(20)
        press_use()
        time.sleep(2)
        press_use()
        time.sleep(10)
        self.banana_count: int = 0
        match self.map_select.get():
            case "Super Stage GP":
                self.break_boxes(1572, 1210, 1050, 343)
                self.break_boxes(663, 1840, 1050, 343)
                self.break_boxes(795, 1840, 1050, 343)
                self.break_boxes(932, 1840, 1050, 343)
                self.break_boxes(1337, 1692, 1050, 343)
                self.break_boxes(1715, 1506, 1050, 343)
                self.break_boxes(1340, 1641, 1050, 343)
                self.lay_banana(1574, 1406, "E")
                self.lay_banana(1574, 1396, "E")
                self.lay_banana(1574, 1386, "E")
                self.lay_banana(1574, 1337, "E")
                self.lay_banana(1574, 1327, "E")
                for i in range(1277, 1157, -20):
                    self.lay_banana(1574, i, "E")
                for i in range(1574, 1534, -20):
                    self.lay_banana(i, 1177, "S")
                for i in range(1520, 770, -20):
                    self.lay_banana(i, 1171, "S")
                for i in range(1171, 1261, 20):
                    self.lay_banana(790, i, "W")
                self.lay_banana(710, 1264, "S")
                for i in range(624, 474, -20):
                    self.lay_banana(i, 1285, "S")
                self.lay_banana(474, 1287, "S")
                self.lay_banana(464, 1289, "S")
                self.lay_banana(454, 1292, "S")
                self.lay_banana(444, 1297, "S")
                self.lay_banana(434, 1303, "S")
                self.lay_banana(425, 1311, "S")
                self.lay_banana(417, 1319, "S")
                self.lay_banana(410, 1329, "S")
                self.lay_banana(404, 1340, "S")
                self.lay_banana(399, 1350, "S")
                self.lay_banana(396, 1360, "S")
                self.lay_banana(395, 1370, "S")
                for i in range(1370, 1750, 20):
                    self.lay_banana(406, i, "W")
                for x, y in self.get_curve_coordinates(500, 1743, 103, 80, "NW", 8):
                    self.lay_banana(x+10, y, "W")
                for i in range(492, 1100, 20):
                    self.lay_banana(i, 1834, "N")
                for x, y in self.get_curve_coordinates(1103, 1745, 100, 90, "NE", 8, reverse=True):
                    self.lay_banana(x, y-10, "N")
                for x, y in self.get_curve_coordinates(1255, 1750, 53, 90, "SW", 5):
                    self.lay_banana(x, y-10, "N")
                for i in range(1267, 1367, 20):
                    self.lay_banana(i, 1687, "N")
                for i in range(1598, 1748, 20):
                    self.lay_banana(i, 1687, "N")
                for i in range(1687, 1577, -20):
                    self.lay_banana(1734, i, "E")
                for x, y in self.get_curve_coordinates(1638, 1585, 106, 65, "SE", 7):
                    self.lay_banana(x-10, y, "E")
                for x, y in self.get_curve_coordinates(1635, 1433, 50, 90, "NW", 4, reverse=True):
                    self.lay_banana(x-10, y, "E")
                for i in range(1398, 1218, -20):
                    self.lay_banana(1543, i, "W")
                for i in range(1523, 1483, -20):
                    self.lay_banana(i, 1203, "N")
                for i in range(1460, 820, -20):
                    self.lay_banana(i, 1203, "N")
                for i in range(1218, 1258, 20):
                    self.lay_banana(817, i, "E")
                for i in range(1260, 1340, 20):
                    self.lay_banana(817, i, "E")
                self.lay_banana(762, 1340, "N")
                self.lay_banana(664 , 1340, "N")
                self.lay_banana(604 , 1316, "N")
                self.lay_banana(594 , 1316, "N")
                self.lay_banana(552 , 1316, "N")
                for x, y in self.get_curve_coordinates(497, 1378, 50, 90, "SW", 5, reverse=True):
                    self.lay_banana(x-10, y, "E")
                self.lay_banana(437, 1467, "E")
                self.lay_banana(437, 1477, "E")
                self.lay_banana(437, 1571, "E")
                self.lay_banana(437, 1581, "E")
                self.lay_banana(437, 1622, "E")
                self.lay_banana(437, 1632, "E")
                self.lay_banana(437, 1677, "E")
                for i in range(1708, 1747, 20):
                    self.lay_banana(437, i, "E")
                for x, y in self.get_curve_coordinates(504, 1742, 57, 40, "NW", 3):
                    self.lay_banana(x-10, y, "E")
                for i in range(489, 519, 20):
                    self.lay_banana(i, 1802, "S")
                for i in range(545, 1095, 20):
                    self.lay_banana(i, 1802, "S")
                for x, y in self.get_curve_coordinates(1098, 1737, 55, 90, "NE", 4, reverse=True):
                    self.lay_banana(x+10, y, "W")
                for x, y in self.get_curve_coordinates(1257, 1745, 105, 65, "SW", 6):
                    self.lay_banana(x+10, y, "W")
                for i in range(1273, 1373, 20):
                    self.lay_banana(i, 1653, "S")
                for x, y in self.get_curve_coordinates(1630, 1438, 96, 60, "NW", 5):
                    self.lay_banana(x+10, y, "W")
                self.lay_banana(1542, 1437, "W")
                self.lay_banana(1542, 1427, "W")
                self.lay_zip(1574, 1410, 760, 530)
                self.spawn_hamball(1550, 1422)
                self.spawn_hamball(1570, 1422)
                self.spawn_hamball(1550, 1432)
                self.spawn_hamball(1570, 1432)
            case "Penguin Palace GP":
                self.break_boxes(1651, 3660, 1050, 343)
                self.break_boxes(1583, 3651, 1050, 343)
                self.break_boxes(1620, 3540, 1050, 343)
                self.break_boxes(2153, 3563, 800, 800)
                self.lay_zip(2030, 3452, 970, 850)
                self.lay_banana(2050, 3407, "S")
                self.lay_banana(2070, 3407, "S")
                for x, y in self.get_curve_coordinates(2097, 3502, 105, 90, "SE", 9, reverse=True):
                    self.lay_banana(x+10, y, "W")
                for i in range(3500, 3700, 20):
                    self.lay_banana(2190, i, "E")
                for i in range(3715, 3755, 20):
                    self.lay_banana(2190, i, "E")
                self.lay_banana(2303, 3865, "E")
                self.lay_banana(2284, 3952, "N")
                self.lay_banana(2117, 3943, "N")
                self.lay_banana(2052, 3943, "N")
                self.lay_banana(1991, 3863, "N")
                self.lay_banana(1991, 3861, "S")
                for i in range(1950, 1770, -20):
                    self.lay_banana(i, 3870, "N")
                self.lay_banana(1790, 3870, "W")
                self.lay_banana(1790, 3840, "W")
                self.lay_banana(1790, 3820, "W")
                self.lay_banana(1773, 3786, "W")
                self.lay_banana(1763, 3765, "W")
                self.lay_banana(1763, 3745, "W")
                self.lay_banana(1740, 3700, "W")
                self.lay_banana(1725, 3685, "W")
                self.lay_banana(1710, 3670, "W")
                self.lay_banana(1692, 3662, "W")
                self.lay_banana(1662, 3652, "N")
                self.lay_banana(1642, 3652, "N")
                self.lay_banana(1602, 3652, "N")
                self.lay_banana(1582, 3652, "N")
                self.lay_banana(1514, 3646, "N")
                for i in range(3652, 3613, -20):
                    self.lay_banana(1482, i, "W")
                self.lay_banana(1511, 3570, "W")
                self.lay_banana(1521, 3555, "W")
                self.lay_banana(1541, 3540, "W")
                self.lay_banana(1574, 3546, "S")
                self.lay_banana(1612, 3529, "W")
                self.lay_banana(1612, 3529, "S")
                self.lay_banana(1704, 3529, "S")
                self.lay_banana(1724, 3529, "S")
                self.lay_banana(1787, 3494, "S")
                self.lay_banana(1805, 3494, "S")
                self.lay_banana(1823, 3494, "S")
                for i in range(3459, 3379, -20):
                    self.lay_banana(1912, i, "W")
                self.lay_banana(1966, 3407, "S")
                self.lay_banana(2003, 3407, "S")
                for i in range(1950, 2090, 20):
                    self.lay_banana(i, 3440, "N")
                for x, y in self.get_curve_coordinates(2095, 3505, 55, 90, "SE", 5, reverse=True):
                    self.lay_banana(x+10, y, "W")
                for i in range(3500, 3700, 20):
                    self.lay_banana(2158, i, "W")
                for i in range(3715, 3755, 20):
                    self.lay_banana(2158, i, "W")
                self.lay_banana(2161, 3776, "W")
                self.lay_banana(2165, 3788, "W")
                self.lay_banana(2203, 3800, "W")
                self.lay_banana(2210, 3819, "W")
                self.lay_banana(2215, 3829, "W")
                self.lay_banana(2220, 3839, "W")
                self.lay_banana(2230, 3855, "W")
                self.lay_banana(2235, 3865, "W")
                self.lay_banana(2240, 3875, "W")
                self.lay_banana(2240, 3896, "W")
                self.lay_banana(2235, 3903, "W")
                self.lay_banana(2230, 3910, "W")
                self.lay_banana(2203, 3934, "S")
                self.lay_banana(2194, 3937, "S")
                self.lay_banana(2185, 3940, "S")
                self.lay_banana(2163, 3940, "S")
                self.lay_banana(2155, 3937, "S")
                self.lay_banana(2146, 3934, "S")
                self.lay_banana(2120, 3910, "E")
                self.lay_banana(2115, 3903, "E")
                self.lay_banana(2110, 3896, "E")
                self.lay_banana(2110, 3875, "E")
                self.lay_banana(2115, 3865, "E")
                self.lay_banana(2120, 3855, "E")
                for i in range(2125, 2025, -20):
                    self.lay_banana(i, 3857, "S")
                for i in range(1950, 1830, -20):
                    self.lay_banana(i, 3860, "S")
                self.lay_banana(1830, 3693, "S")
                self.lay_banana(1820, 3689, "S")
                self.lay_banana(1810, 3685, "S")
                self.lay_banana(1770, 3647, "E")
                self.lay_banana(1760, 3642, "E")
                self.lay_banana(1750, 3637, "E")
                self.lay_banana(1740, 3644, "S")
                self.lay_banana(1730, 3644, "S")
                self.lay_banana(1720, 3644, "S")
                self.lay_banana(1710, 3644, "S")
                self.lay_banana(1580, 3644, "S")
                self.lay_banana(1565, 3644, "S")
                self.lay_banana(1555, 3568, "N")
                self.lay_banana(1568, 3568, "N")
                self.lay_banana(1580, 3568, "N")
                self.lay_banana(1642, 3568, "N")
                self.lay_banana(1705, 3568, "N")
                self.lay_banana(1715, 3574, "N")
                self.lay_banana(1725, 3580, "N")
                self.lay_banana(1735, 3586, "N")
                self.lay_banana(1745, 3592, "N")
                self.lay_banana(1761, 3592, "E")
                self.lay_banana(1771, 3582, "E")
                self.lay_banana(1781, 3572, "E")
                self.lay_banana(1791, 3562, "E")
                self.lay_banana(1801, 3552, "E")
                self.lay_banana(1811, 3542, "E")
                self.lay_banana(1895, 3535, "E")
                self.lay_banana(1904, 3525, "E")
                self.lay_banana(1913, 3515, "E")
                self.lay_banana(1929, 3489, "E")
                self.lay_banana(1935, 3479, "E")
                self.spawn_hamball(2020, 3430)
                self.spawn_hamball(2020, 3410)
                self.spawn_hamball(2010, 3430)
                self.spawn_hamball(2010, 3410)
            case "Pyramid GP":
                self.break_boxes(1576, 2801, 800, 400)
                self.break_boxes(1588, 2804, 800, 400)
                self.break_boxes(1576, 2811, 800, 400)
                for i in range(2652, 2592, -20):
                    self.lay_banana(1435, i, "E")
                self.lay_banana(1437, 2616, "S")
                for i in range(0, 40, 10):
                    self.lay_banana(1424-i, 2567-i, "S")
                self.lay_banana(1380, 2529, "S")
                self.lay_banana(1308, 2497, "S")
                self.lay_banana(1321, 2497, "S")
                for i in range(1394, 1434, 10):
                    self.lay_banana(i, 2514, "N")
                for i in range(2522, 2492, -10):
                    self.lay_banana(1438, i, "E")
                for i in range(2480, 2420, -20):
                    self.lay_banana(1397, i, "W")
                for i in range(1397, 1497, 20):
                    self.lay_banana(i, 2444, "S")
                for x, y in self.get_curve_coordinates(1503, 2534, 100, 90, "SE", 10, reverse=True):
                    self.lay_banana(x, y+10, "S")
                for i in range(2528, 2568, 20):
                    self.lay_banana(1592, i, "E")
                for i in range(2568, 2628, 20):
                    self.lay_banana(1600, i, "E")
                for i in range(0, 40, 10):
                    self.lay_banana(1496+i, 2477+i, "W")
                for i in range(0, 30, 10):
                    self.lay_banana(1543+i, 2524+i, "W")
                self.lay_banana(1563, 2554, "W")
                self.lay_banana(1563, 2588, "W")
                self.lay_banana(1563, 2608, "W")
                self.lay_banana(1573, 2618, "W")
                self.lay_banana(1583, 2628, "W")
                self.lay_banana(1583, 2644, "W")
                self.lay_banana(1583, 2660, "W")
                self.lay_banana(1610, 2618, "E")
                for i in range(2628, 2724, 16):
                    self.lay_banana(1620, i, "E")
                self.lay_banana(1632, 2737, "E")
                for i in range(0, 30, 10):
                    self.lay_banana(1693+(i*2), 2743+i, "W")
                self.lay_banana(1719, 2771, "E")
                self.lay_banana(1717, 2781, "N")
                for i in range(1698, 1663, -5):
                    self.lay_banana(i, 2781, "N")
                for i in range(2816, 2876, 10):
                    self.lay_banana(1710, i, "E")
                self.lay_banana(1655, 2866, "N")
                for i in range(0, 40, 10):
                    self.lay_banana(1610-i, 2860-i, "N")
                self.lay_banana(1611, 2820, "E")
                self.lay_banana(1611, 2810, "E")
                for i in range(1582, 1622, 10):
                    self.lay_banana(i, 2773, "N")
                for i in range(2806, 2836, 10):
                    self.lay_banana(1469, i, "E")
                for i in range(2760, 2780, 10):
                    self.lay_banana(1508, i, "E")
                for i in range(2771, 2781, 5):
                    self.lay_banana(1459, i, "E")
                for i in range(2730, 2790, 20):
                    self.lay_banana(1410, i, "W")
                for i in range(1451, 1461, 5):
                    self.lay_banana(i, 2710, "S")
                for i in range(1477, 1492, 5):
                    self.lay_banana(i, 2710, "S")
                for i in range(2678, 2698, 10):
                    self.lay_banana(1398, i, "W")
                for i in range(2652, 2612, -20):
                    self.lay_banana(1360, i, "E")
                self.lay_banana(1374, 2603, "W")
                self.lay_banana(1311, 2586, "N")
                self.lay_zip(1376, 2608, 1300, 540)
                self.spawn_hamball(1395, 2618)
                self.spawn_hamball(1415, 2618)
                self.spawn_hamball(1395, 2608)
                self.spawn_hamball(1415, 2608)