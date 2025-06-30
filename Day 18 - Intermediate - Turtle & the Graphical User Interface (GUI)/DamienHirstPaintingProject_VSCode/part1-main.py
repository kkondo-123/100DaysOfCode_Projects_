"""
Name: Kana Kondo
Date: 2025-06-30-Mon
Course: 100 Days of Code Day 18
Description: Hirst Painting Project Part 1
"""

###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

import colorgram

'''
Step 1) Installed colorgram 1.2.0 and downloaded package
    Colorgram: https://pypi.org/project/colorgram.py/

Step 2) Installed PIP
Link: https://www.youtube.com/watch?v=p6CH6T9HIa0&t=67s
    With Python Version 3.13.1
    In zsh Terminal, typed: curl https://bootstrap.pypa.io/pip/3.8/get-pip.py -o get-pip.py
    Then typed: python3 get-pip.py 
        A file called get-pip.py appeared
    Updated by typing: pip3 install --upgrade pip
    Checked version using: pip3 --version

Step 3) Folder organization
Link: https://stackoverflow.com/questions/67507969/visual-studio-code-cant-find-my-python-module-ive-installes-with-pip
Make sure the main.py and image.jpg is in the same folder as the unzipped folder of colorgram 
    with the folder name "obskyr-colorgram.py-8b07c38" (colorgram package) but not inside the 
    folder name "colorgram" subfolder.
Then, I tested to see if I could place my main.py and image.jpg wherever I want to.
    It worked.

'''


rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
    
    # rgb_colors.append(color.rgb)

print(rgb_colors)
'''
Result: [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
Link to check color: https://www.w3schools.com/colors/colors_rgb.asp
Closer to 255 = Probably white color -> Take out rgb tuples that are close to white color to use in painting
Edited result: [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

'''

