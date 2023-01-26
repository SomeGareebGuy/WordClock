import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import time

class Time(Label):
	def updateTime(self, *args):
		t = time.asctime()

		String1 = "[font=Courier]I    T    L    I    S    A    S    A    M    P    M\n\n"
		String2 = "A    C    Q    U    A    R    T    E    R    D    C\n\n"
		String3 = "T    W    E    N    T    Y    F    I    V    E    X\n\n"
		String4 = "H    A    L    F    S    T    E    N    F    T    O\n\n"
		String5 = "P    A    S    T    E    R    U    N    I    N    E\n\n"
		String6 = "O    N    E    S    I    X    T    H    R    E    E\n\n"
		String7 = "F    O    U    R    F    I    V    E    T    W    O\n\n"
		String8 = "E    I    G    H    T    E    L    E    V    E    N\n\n"
		String9 = "S    E    V    E    N    T    W    E    L    V    E\n\n"
		String10 = "T    E    N    S    E    O'    C    L    O    C    K[/font]"

		word = list(t)
		song = []
		n = 11
	
		while n < 13:
			song.append(word[n])
			n += 1

		preUri = ''.join([str(elem) for elem in song])
		hour = int(preUri)
		
		song = []
		n = 14
	
		while n < 16:
			song.append(word[n])
			n += 1

		preUri = ''.join([str(elem) for elem in song])
		minute = int(preUri)

		a = 1
		while a < 2:
			if hour < 12:
				if hour < 6:
					if hour < 3:
						if hour == 1:
							if minute < 35:
								String6 = "[color=ff3333]O    N    E[/color]    S    I    X    T    H    R    E    E\n\n"
							else:
								String7 = "F    O    U    R    F    I    V    E    [color=ff3333]T    W    O[/color]\n\n"
						elif hour == 2:
							if minute < 35:
								String7 = "F    O    U    R    F    I    V    E    [color=ff3333]T    W    O[/color]\n\n"
							else:
								String6 = "O    N    E    S    I    X    [color=ff3333]T    H    R    E    E[/color]\n\n"
						else:
							if minute < 35:
								String9 = "S    E    V    E    N    [color=ff3333]T    W    E    L    V    E[/color]\n\n"
							else:
								String6 = "[color=ff3333]O    N    E[/color]    S    I    X    T    H    R    E    E\n\n"
					else:
						if hour == 3:
							if minute < 35:
								String6 = "O    N    E    S    I    X    [color=ff3333]T    H    R    E    E[/color]\n\n"
							else:
								String7 = "[color=ff3333]F    O    U    R[/color]    F    I    V    E    T    W    O\n\n"
						elif hour == 4:
							if minute < 35:
								String7 = "[color=ff3333]F    O    U    R[/color]    F    I    V    E    T    W    O\n\n"
							else:
								String7 = "F    O    U    R    [color=ff3333]F    I    V    E[/color]    T    W    O\n\n"
						else:
							if minute < 35:
								String7 = "F    O    U    R    [color=ff3333]F    I    V    E[/color]    T    W    O\n\n"
							else: 
								String6 = "O    N    E    [color=ff3333]S    I    X[/color]    T    H    R    E    E\n\n"
				else:
					if hour < 9:
						if hour == 6:
							if minute < 35:
								String6 = "O    N    E    [color=ff3333]S    I    X[/color]    T    H    R    E    E\n\n"
							else:
								String9 = "[color=ff3333]S    E    V    E    N[/color]    T    W    E    L    V    E\n\n"
						elif hour == 7:
							if minute < 35:
								String9 = "[color=ff3333]S    E    V    E    N[/color]    T    W    E    L    V    E\n\n"
							else:
								String8 = "[color=ff3333]E    I    G    H    T[/color]    E    L    E    V    E    N\n\n"
						else:
							if minute < 35:
								String8 = "[color=ff3333]E    I    G    H    T[/color]    E    L    E    V    E    N\n\n"
							else:
								String5 = "P    A    S    T    E    R    U    [color=ff3333]N    I    N    E[/color]\n\n"
					else:
						if hour == 9:
							if minute < 35:
								String5 = "P    A    S    T    E    R    U    [color=ff3333]N    I    N    E[/color]\n\n"
							else:
								String10 = "[color=ff3333]T    E    N[/color]    S    E    C    C    L    O    C    K[/font]"
						elif hour == 10:
							if minute < 35:
								String10 = "[color=ff3333]T    E    N[/color]    S    E    O'    C    L    O    C    K[/font]"
							else:
								String8 = "E    I    G    H    T    [color=ff3333]E    L    E    V    E    N[/color]\n\n"
						else:
							if minute < 35:
								String8 = "E    I    G    H    T    [color=ff3333]E    L    E    V    E    N[/color]\n\n"
							else:
								String9 = "S    E    V    E    N    [color=ff3333]T    W    E    L    V    E[/color]\n\n"
				a+=1

			else:
				hour = hour - 12

		b = 1
		while b < 2:
			if minute < 35:
				if minute < 20:
					if minute < 5:
						if hour == 10 or hour == 22:
							String1 = "[font=Courier][color=ff3333]I    T[/color]    L    [color=ff3333]I    S[/color]    A    S    A    M    P    M\n\n"
							String10 = "[color=ff3333]T    E    N[/color]    S    E    [color=ff3333]O'    C    L    O    C    K[/color][/font]"
							b+=1 
						else:
							String1 = "[font=Courier][color=ff3333]I    T[/color]    L    [color=ff3333]I    S[/color]    A    S    A    M    P    M\n\n"
							String10 = "T    E    N    S    E    [color=ff3333]O'    C    L    O    C    K[/color][/font]"
							b+=1
					elif minute < 10:
						if hour == 9 or hour == 21 :
							String5 = "[color=ff3333]P    A    S    T[/color]    E    R    U    [color=ff3333]N    I    N    E[/color]\n\n"
						else:
							String5 = "[color=ff3333]P    A    S    T[/color]    E    R    U    N    I    N    E\n\n"
						String3 = "T    W    E    N    T    Y    [color=ff3333]F    I    V    E[/color]    X\n\n"
					elif minute < 15:
						if hour == 9 or hour == 21 :
							String5 = "[color=ff3333]P    A    S    T[/color]    E    R    U    [color=ff3333]N    I    N    E[/color]\n\n"
						else:
							String5 = "[color=ff3333]P    A    S    T[/color]    E    R    U    N    I    N    E\n\n"
						String4 = "H    A    L    F    S    [color=ff3333]T    E    N[/color]    F    T    O\n\n"
					else:
						String2 = "A    C    [color=ff3333]Q    U    A    R    T    E    R[/color]    D    C\n\n"
						if hour == 9 or hour == 21 :
							String5 = "[color=ff3333]P    A    S    T[/color]    E    R    U    [color=ff3333]N    I    N    E[/color]\n\n"
						else:
							String5 = "[color=ff3333]P    A    S    T[/color]    E    R    U    N    I    N    E\n\n"
				else:
					if minute < 25:
						String3 = "[color=ff3333]T    W    E    N    T    Y[/color]    F    I    V    E    X\n\n"
						if hour == 9 or hour == 21 :
							String5 = "[color=ff3333]P    A    S    T[/color]    E    R    U    [color=ff3333]N    I    N    E[/color]\n\n"
						else:
							String5 = "[color=ff3333]P    A    S    T[/color]    E    R    U    N    I    N    E\n\n"
					elif minute < 30:
						String3 = "[color=ff3333]T    W    E    N    T    Y    F    I    V    E[/color]    X\n\n"
						if hour == 9 or hour == 21 :
							String5 = "[color=ff3333]P    A    S    T[/color]    E    R    U    [color=ff3333]N    I    N    E[/color]\n\n"
						else:
							String5 = "[color=ff3333]P    A    S    T[/color]    E    R    U    N    I    N    E\n\n"
					else:
						String4 = "[color=ff3333]H    A    L    F[/color]    S    T    E    N    F    T    O\n\n"
						if hour == 9 or hour == 21 :
							String5 = "[color=ff3333]P    A    S    T[/color]    E    R    U    [color=ff3333]N    I    N    E[/color]\n\n"
						else:
							String5 = "[color=ff3333]P    A    S    T[/color]    E    R    U    N    I    N    E\n\n"
			else:
				if minute < 40:
					String3 = "[color=ff3333]T    W    E    N    T    Y    F    I    V    E[/color]    X\n\n"
					String4 = "H    A    L    F    S    T    E    N    F    [color=ff3333]T    O[/color]\n\n"
				elif minute < 45:
					String3 = "[color=ff3333]T    W    E    N    T    Y[/color]    F    I    V    E    X\n\n"
					String4 = "H    A    L    F    S    T    E    N    F    [color=ff3333]T    O[/color]\n\n"
				elif minute < 50:
					String2 = "A    C    [color=ff3333]Q    U    A    R    T    E    R[/color]    D    C\n\n"
					String4 = "H    A    L    F    S    T    E    N    F    [color=ff3333]T    O[/color]\n\n"
				elif minute < 55:
					String4 = "H    A    L    F    S    [color=ff3333]T    E    N[/color]    F    [color=ff3333]T    O[/color]\n\n"
				else:
					String3 = "T    W    E    N    T    Y    [color=ff3333]F    I    V    E[/color]    X\n\n"
					String4 = "H    A    L    F    S    T    E    N    F    [color=ff3333]T    O[/color]\n\n"
			b+=1

		self.text = String1 + String2 + String3 + String4 + String5 + String6 + String7 + String8 + String9 + String10
		self.markup = True

class HelloWorldApp(App):
	def build(self):
		t = Time()
		Clock.schedule_interval(t.updateTime, 1)
		return(t)
		
		

if __name__ == '__main__':
	HelloWorldApp().run()
