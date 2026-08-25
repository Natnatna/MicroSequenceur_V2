# MicroSequenceur_V2
MicroSequenceur_V2 est une amélioration de MicroSequenceur.
Créer pour un raspberry pico, sur le modél Eurorack pour offrir un maximum de polyvalance.
Par défaut une plage allant de 60 a 260 bpm et une sync-in/sync-out pour le rendre compatible avec d'autres sequenceurs ou autres instruments.
Ce sequenceur repose sur le systéme d'une matrice de 8 line avec du 1/1t, 1/2t et 1/4t.
Posséde une Attack modulable.

Sous license CC-BY-NC-SA


## Instalation

### 1)    Liste des composants :
* Raspberry Pico ou équivalent supportant MicroPython
* 64 interrupteurs
* 15 transistor NPN 2N904
* 15 résistance 1K Ohm
* 2 potentiomètre 
* 1 LED indicateur BPM
* 8 LED indicateur Line
* 8 résistance 100 Ohm

Optionnel:
* 56 LED 3v indicateur Temp
* 56 diode
* 1 résistance 680 Ohm
### 2)    Firmware :
MicroPython installer sur la carte

### 3)    Branchement :
->Se référencer au schéma [Schema pdf](Microsequenceur_V2.pdf)
![Schéma png](Microsequenceur_V2.png "img schema")

Line_1:
![](IMG_20260820_202822.jpg "Line")
Montage avec LED indicateur (optionnel):
![](IMG_20260824_161829~2.jpg "LED indicateur sur Line")
vérifiez que le circuit soit correct avec le fichier test [test_line.py](TEST/test_line.py) et [test_line_complite.py](TEST/test_line_complite.py) pour la condition semi-réel
## Utilisation
Polyvalente pour Modular System
