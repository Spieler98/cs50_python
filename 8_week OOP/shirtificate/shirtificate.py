from fpdf import FPDF


def main():
    name = input("Name: ").strip()
    if name:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", "", size=48)
        pdf.cell(text="CS50 Shirtificate", h=40, center=True)
        pdf.image("shirtificate.png", x=5, y=60, w=200)
        pdf.set_font("helvetica", "", size=26)
        pdf.set_text_color(255,255,255)
        pdf.cell(text=name+" took CS50", h=240, center=True)
        pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()