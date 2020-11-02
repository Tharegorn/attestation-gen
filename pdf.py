from fpdf import FPDF
import json
from datetime import datetime
from qr import qrCode
import os

def titles(self):
    self.set_xy(0.0, 0.0)
    self.set_font('Arial', 'B', 16)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, align='C',
              txt="ATTESTATION DE DÉPLACEMENT DÉROGATOIRE", border=0)

def cross(self, x, y):
    self.set_xy(x, y)
    self.set_font('Arial', '', 15)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0,
              txt="X", border=0)

def rects(self, re):
    if (re == "travail"):
        cross(self, 30.0, 58.0)
    if (re == "sante"):
        cross(self, 30.0, 91.0)
    if (re == "famille"):
        cross(self, 30.0, 103.0)
    if (re == "handicap"):
        cross(self, 30.0, 115.0)
    if (re == "convocation"):
        cross(self, 30.0, 147.0)
    if (re == "missions"):
        cross(self, 30.0, 157.0)
    if (re == "enfants"):
        cross(self, 30.0, 167.0)
    if (re == "achats"):
        cross(self, 30.0, 76.0)
    if (re == "sport_animaux"):
        cross(self, 30.0, 130.0)
    self.rect(30.0, 75.0, 6.0, 6.0, 'B')
    self.rect(30.0, 93.0, 6.0, 6.0, 'B')
    self.rect(30.0, 108.0, 6.0, 6.0, 'B')
    self.rect(30.0, 120.0, 6.0, 6.0, 'B')
    self.rect(30.0, 132.0, 6.0, 6.0, 'B')
    self.rect(30.0, 147.0, 6.0, 6.0, 'B')
    self.rect(30.0, 164.0, 6.0, 6.0, 'B')
    self.rect(30.0, 174.0, 6.0, 6.0, 'B')
    self.rect(30.0, 184.0, 6.0, 6.0, 'B')

def cre(self, x, y, ctt):
    self.set_xy(x, y)
    self.set_font('Arial', '', 6)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0,
              txt=ctt, border=0)

def cre_cell(self, x, y, ctt):
    self.set_xy(x, y)
    self.set_font('Arial', '', 10)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0,
              txt=ctt, border=0)


def reasons(self):
    # travail
    cre_cell(self, 50.0, 55.0,
             "Déplacement entre le domicile et le lieu d'exercice de l'activité professionnelle ou un")
    cre_cell(self, 50.0, 59.0,
             "établissement d'enseignement ou de formation, déplacements professionnels ne pouvant")
    cre_cell(self, 50.0, 63.0,
             "être différés 2 , déplacements pour un concours ou un examen.")
    # achats
    cre_cell(self, 50.0, 73.0,
             "Déplacements pour effectuer des achats de fournitures nécessaires à l'activité")
    cre_cell(self, 50.0, 76.0,
             "professionnelle, des achats de première nécessité 3 dans des établissements dont les")
    cre_cell(self, 50.0, 79.0,
             "activités demeurent autorisées, le retrait de commande et les livraisons à domicile.")
    # santé
    cre_cell(self, 50.0, 89.0,
             "Consultations, examens et soins ne pouvant être assurés à distance et l'achat de")
    cre_cell(self, 50.0, 92.0,
             "médicaments.")
    # famillial
    cre_cell(self, 50.0, 102.0,
             "Déplacements pour motif familial impérieux, pour l'assistance aux personnes vulnérables")
    cre_cell(self, 50.0, 105.0,
             "et précaires ou la garde d'enfants.")
    # handicap
    cre_cell(self, 50.0, 115.0,
             "Déplacement des personnes en situation de handicap et leur accompagnant.")
    # sport animaux
    cre_cell(self, 50.0, 125.0,
             "Déplacements brefs, dans la limite d'une heure quotidienne et dans un rayon maximal")
    cre_cell(self, 50.0, 128.0,
             "d'un kilomètre autour du domicile, liés soit à l'activité physique individuelle des")
    cre_cell(self, 50.0, 131.0,
             "personnes, à l'exclusion de toute pratique sportive collective et de toute proximité avec")
    cre_cell(self, 50.0, 134.0,
             "d'autres personnes, soit à la promenade avec les seules personnes regroupées dans un")
    cre_cell(self, 50.0, 137.0,
             "même domicile, soit aux besoins des animaux de compagnie.")
    # justice
    cre_cell(self, 50.0, 147.0,
             "Convocation judiciaire ou administrative et pour se rendre dans un service public")
    # missions
    cre_cell(self, 50.0, 157.0,
             "Participation à des missions d'intérêt général sur demande de l'autorité administrative")
    # enfants
    cre_cell(self, 50.0, 167.0,
             "Déplacement pour chercher les enfants à l'école et à l'occasion de leurs activités")
    cre_cell(self, 50.0, 170.0,
             "périscolaires.")


def body(self, av, re):
    now = datetime.now()
    with open("profiles/" + av.lower() + ".json") as json_file:
        data = json.load(json_file)
        first = data["prenom"]
        last = data["nom"]
        date = data["datenaissance"]
        place = data["lieunaissance"]
        add = data["adresse"]
        city = data["ville"]
        code = data["codepostal"]
    self.set_xy(0.0, 5.0)
    self.set_font('Arial', '', 10)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, align='C',
              txt="En application du décret n°2020-1310 du 29 octobre 2020 prescrivant les mesures générales", border=0)
    self.set_xy(0.0, 8.0)
    self.set_font('Arial', '', 10)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, align='C',
              txt="nécessaires pour faire face à l'épidémie de Covid19 dans le cadre de l'état d'urgence sanitaire", border=0)
    cre_cell(self, 23.0, 15.0, "Je soussigné(e),")
    cre_cell(self, 23.0, 20.0, "Mme/M. : " + first + " " + last)
    cre_cell(self, 23.0, 25.0, "Né(e) le : " + date)
    cre_cell(self, 23.0, 30.0, "Deumeurant : " + add + " " + code + " " + city)
    cre_cell(self, 83.0, 25.0, "à : " + place)
    cre_cell(self, 23.0, 35.0,
             "certifie que mon déplacement est lié au motif suivant (cocher la case) autorisé par le décret")
    cre_cell(self, 23.0, 40.0,
             "n°2020-1310 du 29 octobre 2020 prescrivant les mesures générales nécessaires pour faire face à")
    cre_cell(self, 23.0, 45.0,
             "l'épidémie de Covid19 dans le cadre de l'état d'urgence sanitaire 1 :")
    reasons(self)
    rects(self, re)
    cre_cell(self, 23.0, 180.0, "Fait à : " + city)
    cre_cell(self, 23.0, 185.0, "Le : " + now.strftime("%D"))
    cre_cell(self, 83.0, 185.0, "à : " + now.strftime("%H:%M"))
    cre_cell(self, 23.0, 190.0,
             "(Date et heure de début de sortie à mentionner obligatoirement)")
    cre_cell(self, 23.0, 195.0, "Signature :")
    qrCode("Cree le: " + now.strftime("%D") + " a " + now.strftime("%H:%M") + ";\n\
     Nom: " + last + ";\n\
     Prenom: " + first + ";\n\
     Naissance: " + date + " a " + place + ";\n\
     Adresse: " + add + " " + code + " " + city + ";\n\
     Sortie: " + now.strftime("%D") + " a " + now.strftime("%H:%M") + ";\n\
     Motifs: " + re + "\n\
    ")
    self.image("./qr.png", 150.0, 200.0, 50.0, 50.0, "png")
    cre(self, 23.0, 205.0, "1  Les personnes souhaitant bénéficier de l'une de ces exceptions doivent se munir s'il y a lieu, lors de leurs")
    cre(self, 25.0, 208.0, "déplacements hors de leur domicile, d'un document leur permettant de justifier que le déplacement considéré entre")
    cre(self, 25.0, 211.0, "dans le champ de l'une de ces exceptions.")
    cre(self, 23.0, 214.0, "2  A utiliser par les travailleurs non-salariés, lorsqu'ils ne peuvent disposer d'un justificatif de déplacement établi par leur")
    cre(self, 25.0, 217.0, "employeur.")
    cre(self, 23.0, 220.0, "3  Y compris les acquisitions à titre gratuit (distribution de denrées alimentaires...) et les déplacements liés à la")
    cre(self, 25.0, 223.0, "perception de prestations sociales et au retrait d'espèces.")

def maker(profile, re):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    titles(pdf)
    body(pdf, profile, re)
    pdf.output(profile + '.pdf', 'F')
    os.remove("./qr.png")