
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys
try:
	from PyQt4.QtCore import *				# Moteur contrôle Qt
	from PyQt4.QtGui import *				# IHM Qt
except:
	import time						# Gestion heures système
	for i in range(1, 11):
		print("PyQt non installé - A vérifier (%d/10)", i)
	time.sleep(5)
	sys.exit(1)
# try
 
class QtAppli(
		QApplication):					# Objet hérité
	"Fenêtre de l'application"
 
	# Constructeur fenêtre
	def __init__(
			self,					# Instance objet
			argv,					# Arguments programme
			transFile=None):			# Fichier de traduction
 
		# Message de contrôle
		print("Python version %s - QtAppli (qt v%s, pyqt_v%s)" , (
			sys.version,
			QT_VERSION_STR,
			PYQT_VERSION_STR
		))
 
		# Appel constructeur de l'objet hértié
		QApplication.__init__(self, argv)
		
		# Translations
		if transFile != None:
			self.__trans=QTranslator()
			self.installTranslator(self.__trans)
			self.__trans.load(transFile)
		#if
 
		# Widget principale
		self.__mainWid=QMainWindow()
		self.__mainWid.setCentralWidget(QWidget(self.__mainWid))
		self.__mainWid.statusBar()
 
		# Titre
		self.__mainWid.setWindowTitle(
			self.trUtf8(
				"Vérification Qt (v%1)",
				"Note: titre de la fenêtre",
			).arg(QT_VERSION_STR)
		)
 
		# Le bouton
		btn=QPushButton(
			self.trUtf8(
				"Surtout ne pas cliquer là !!!",
				"Note: titre du bouton",
			),
			self.__mainWid.centralWidget()
		)
		self.connect(
			btn,
			SIGNAL("clicked()"),
			self.__slotAction,
		)
 
		# Le bouton version
		ver=QPushButton(
			self.trUtf8(
				"A propos de Qt",
				"Note: titre du bouton",
			)
		)
		self.connect(
			ver,
			SIGNAL("clicked()"),
			self.__slotQt,
		)
 
		# Pour quitter
		quit=QPushButton(
			self.trUtf8(
				"Quitter",
				"Note: titre du bouton",
			)
		)
		self.connect(
			quit,
			SIGNAL("clicked()"),
			self.__mainWid,
			SLOT("close()"),
		)
		
		# Rangement des éléments
		mainLayout=QVBoxLayout(self.__mainWid.centralWidget())
		mainLayout.addWidget(btn)
		mainLayout.addWidget(ver)
		mainLayout.addWidget(quit)
	# __init__()
 
	# Affichage et lancement application
	def run(
			self):					# Instance objet
		self.__mainWid.show()
		self.exec_()
	# run()
 
	# Slot qui affiche une fenêtre avec un texte
	def __slotAction(
			self):					# Instance objet
 
		print("%s.__slotAction" % self.__class__.__name__)
 
		# Sous-fenêtre
		dial=QDialog(self.__mainWid.centralWidget())
		dial.setModal(True)
		dial.setWindowTitle(
			self.trUtf8(
				"Félicitations, Qt fonctionne parfaitement !!!",
				"Note: titre de la fenêtre",
			)
		)
 
		# Widget principale
		mainLayout=QVBoxLayout(dial)
 
		# Texte à la con
		lab=QLabel(
			self.trUtf8(
				"<center><font size='+5'>C'était écrit <u><font color='red'>SURTOUT</font></u> ne pas cliquer !!!</font><br>Et l'autre gros con, qu'est-ce qu'il fait ? Il clique !!!</center>",
				"Note: texte de la fenêtre",
			)
		)
		mainLayout.addWidget(lab)
 
		# Bouton
		btn=QPushButton(
			self.trUtf8(
				"Félicitations, Qt fonctionne parfaitement !!!",
				"Note: titre du bouton",
			)
		)
		btn.connect(
			btn,
			SIGNAL("clicked()"),
			dial,
			SLOT("close()"),
		)
		mainLayout.addWidget(btn)
 
		# Affichage sous-fenêtre
		dial.show()
	# __slotAction()
 
	# Slot qui affiche la version de Qt
	def __slotQt(
			self):					# Instance objet
 
		print("%s.__slotQt" % self.__class__.__name__)
 
		# Fenêtre "A propos de Qt"
		QMessageBox.aboutQt(
			self.__mainWid,
			self.trUtf8(
				"à propos de Qt...",
				"Note: titre de la fenêtre",
			),
		)
	# __slotQt()
# class QtAppli
 
if __name__ == "__main__":
	# Lancement appli
	Appli=QtAppli(
		sys.argv,
		# "nom_du_fichier_de_traduction_éventuel",
	)
	Appli.run()
