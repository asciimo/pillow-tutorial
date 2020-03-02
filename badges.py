from PIL import Image
import json

def load_employees(path):
    with open(path) as f:
        data = json.load(f)
        return data.get("employees")

def main():
    employees = load_employees("src/employees.json")
    for employee in employees:
        print("%s %s" % (employee.get("first_name"), employee.get("last_name")))
        im = Image.open("src/%s" % employee.get("photo"))
        im.save("dist/%s" % employee.get("photo").replace(".jpg", ".png"))

if __name__ == "__main__":
    main()
