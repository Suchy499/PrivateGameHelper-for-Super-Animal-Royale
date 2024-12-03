import os

if __name__ == "__main__":
    qrc_header = \
    "<!DOCTYPE RCC><RCC version=\"1.0\">\n\t<qresource>\n"
    qrc_footer = \
    "\t</qresource>\n</RCC>"

    path = os.path.dirname(__file__)
    images = ""

    with open(os.path.join(path, "rc_images.qrc"), "w") as f:
        f.write(qrc_header)
        for dirpath, dirnames, filenames in os.walk(rf"{path}\images"):
            for f_name in filenames:
                f.write(f"\t\t<file>images/{f_name}</file>\n")
        f.write(qrc_footer)
    
    os.system(rf'pyside6-rcc "{path}\rc_images.qrc" -o "{path}\rc_images.py"')