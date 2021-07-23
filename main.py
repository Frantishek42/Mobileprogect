from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder

Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (600, 900)

def get_formulaR(Rpr, U1, U2, U3,):

    Riz = float(round(Rpr * ((U1 / (U2 + U3))-1), 1))
    R = str(Riz,)
    return {'finish_R': R,}

def get_formula(Ps, Pf, T, Pn,):

    H2 = float(round(((24 * (Ps - Pf)) / (T * (Pn + 1))) * 100, 10))
    h2 = str(H2,)
    return {'finish': h2,}

class FistWindow(Screen):
    pass

class FormulaR(Screen):
    def calculate_R(self):

        try:
            Rpr = int(self.text_inputRpr.text)
            U1 = int(self.text_inputU1.text)
            U2 = int(self.text_inputU2.text)
            U3 = int(self.text_inputU3.text)

        except:
            Rpr = ""
            U1 = ""
            U2 = ""
            U3 = ""

        if (self.text_inputU1.text > "0"):

            if (self.text_inputU2.text > "0"):

                formulaR = get_formulaR(Rpr, U1, U2, U3)
                r = float(formulaR.get('finish_R'))

                if r >= 2:

                    self.finish_R.color = (0, 1, 0, 1)
                    self.finish_R.text = formulaR.get('finish_R') + ' кОм' + " хорошая"

                else:

                    self.finish_R.color = (1, 0, 0, 1)
                    self.finish_R.text = formulaR.get('finish_R') + ' кОм' + " плохая"

                if r >= 1000:

                    self.finish_R.color = (0, 1, 0, 1)
                    r2 = str(round(r / 1000, 1))
                    self.finish_R.text = r2 + ' мОм' + " хорошая"

    def clear_widgets(self, children=None):

        self.text_inputRpr.text = ''
        self.text_inputU1.text = ''
        self.text_inputU2.text = ''
        self.text_inputU3.text = ''
        self.finish_R.text = ''

class FormulaH2(Screen):

    def calculate(self ):

        try:
            Ps = float(self.text_inputPs.text)
            Pf = float(self.text_inputPf.text)
            Pn = float(self.text_inputPn.text)
            T = int(self.text_inputT.text)

        except:
            Ps = ""
            Pf = ""
            T = ""
            Pn = ""

        if (self.text_inputT.text > "0"):

            formula = get_formula(Ps, Pf, T, Pn)
            h2 = float(formula.get('finish'))

            if h2 <=  5 :

                self.finish.color = (0, 1, 0, 1)
                self.finish.text = formula.get('finish') + '%' + " норма"

            else:

                self.finish.color = (1, 0, 0, 1)
                self.finish.text = formula.get('finish') + '%' + " превышено"



    def clear_widgets(self, children=None):

        self.text_inputPs.text = ''
        self.text_inputPf.text = ''
        self.text_inputPn.text = ''
        self.text_inputT.text = ''
        self.finish.text = ''

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('box1.kv')

class MyApp(App):
    title = "Формулы"
    def build(self):
        self.icon = 'myicon.png'
        return kv

if __name__ == '__main__':
    MyApp().run()
