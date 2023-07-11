import sys
sys.path.extend(['/Users/rodrigo/Code/Output/Stub'])

a = 'U25L15D12r45u27'

from Stub_SVG import *

my_screen = Screen()
p = Pen()
# print(p)
d = DrawRelative(p, my_screen)
# d.process_draw(a)
# print(f"Draw List: {d.step_list}")
# d.process_coordinates()
# print(f"Coordinates List: {d.coordinates_list}")
# print(p)
t = Text(my_screen)

d.draw(a)
t.write("This is a test", 100, 100, 12)

save(my_screen.screen, OUTPUT_FILE)