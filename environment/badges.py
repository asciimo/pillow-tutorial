from PIL import Image
from PIL import ImageDraw
import json

def load_employees(path):
    with open(path) as f:
        data = json.load(f)
        return data.get("employees")

def get_badge_filename(employee):
    raw_filename = "%s_%s_%s.png" % (employee.get("id"), employee.get("last_name"), employee.get("first_name"))
    return "".join(c for c in raw_filename if (c.isalnum() or c in "_.")).lower()

def main():
    template = Image.open("src/badge.png")
    employees = load_employees("src/employees.json")
    for employee in employees:
        print("Processing %s %s" % (employee.get("first_name"), employee.get("last_name")))
        output_filename = get_badge_filename(employee)
        employee_badge = template.copy()
        employee_photo = Image.open("src/%s" % employee.get("photo"))
        employee_badge.paste(employee_photo, (185, 216))

        employee_name = employee.get("first_name")

        draw = ImageDraw.Draw(employee_badge)
        print(draw)
        text_width, text_height = draw.textsize(employee_name)
        draw.text(
            ((employee_badge.width/2 - text_width/2), employee_badge.height/2),
            employee_name,
            (0,0,0))

        employee_badge.save("dist/%s" % output_filename)

if __name__ == "__main__":
    main()
