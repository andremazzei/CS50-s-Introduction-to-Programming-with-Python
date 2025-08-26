from fpdf import FPDF


def main():
    name = get_name()
    shirtificate(name)


def get_name():
    name = input("Name: ")
    return name

def shirtificate(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 40)
    pdf.cell(text='CS50 Shirtificate', center=True, align='C', h=60)
    pdf.image("shirtificate.png", x="C", y=70, h=180)
    pdf.set_font("helvetica", "B", 20)
    pdf.set_text_color("#ffffff")
    pdf.cell(text=f"{name} took CS50", center=True, align='C', h=250)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
