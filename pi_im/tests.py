from django.test import TestCase
from image_srv import settings

from pi_im.models import ReferenceImg, ResourceAnalyse, AnalyseResults

def fill_db_references(references_data):
    for elem in references_data:
        ref = ReferenceImg(img_name=elem["img_name"], img_desc=elem["img_desc"])
        ref.save()

ref_data = [
    {"img_name": "obj1__5.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__10.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__15.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__20.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__25.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__30.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__35.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__40.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__45.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__50.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__55.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__60.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__65.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__70.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__75.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__80.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__85.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__90.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__95.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj1__100.png", "img_desc": "Dristan Cold médicament."},
    {"img_name": "obj3__5.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__10.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__15.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__20.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__25.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__30.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__35.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__40.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__45.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__50.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__55.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__60.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__65.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__70.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__75.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__80.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__85.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__90.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__95.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj3__100.png", "img_desc": "Jouet bateau jaune."},
    {"img_name": "obj5__5.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__10.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__15.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__20.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__25.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__30.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__35.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__40.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__45.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__50.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__55.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__60.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__65.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__70.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__75.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__80.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__85.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__90.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__95.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj5__100.png", "img_desc": "Rolaids médicament."},
    {"img_name": "obj7__5.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__10.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__15.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__20.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__25.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__30.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__35.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__40.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__45.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__50.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__55.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__60.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__65.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__70.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__75.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__80.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__85.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__90.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__95.png", "img_desc": "Arizona canette."},
    {"img_name": "obj7__100.png", "img_desc": "Arizona canette."},
    {"img_name": "obj9__5.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__10.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__15.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__20.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__25.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__30.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__35.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__40.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__45.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__50.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__55.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__60.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__65.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__70.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__75.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__80.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__85.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__90.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__95.png", "img_desc": "OralB fil dentaire."},
    {"img_name": "obj9__100.png", "img_desc": "OralB fil dentaire."},
]


fill_db_references(ref_data)

print()
print("===== ReferenceImg =====")
for o in ReferenceImg.objects.all():
    print(o)
print()
print("===== ResourceAnalyse =====")
for o in ResourceAnalyse.objects.all():
    print(o)
print()
print("===== AnalyseResults =====")
for o in AnalyseResults.objects.all():
    print(o)



