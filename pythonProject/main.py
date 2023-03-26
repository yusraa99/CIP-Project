from experta import *
import ast


class Expert(KnowledgeEngine):
    token = ""
    rsi1 = 0

    @DefFacts()
    def needed_data(selbtcf):
        yield Fact(make_dicision='true')

    @Rule(Fact(make_dicision='true'), NOT(Fact(name=W())), salience=1000)
    def ask_token(self):
        self.token = input("What's the token you want do analys?\n")
        self.token = self.token.lower()
        self.declare(Fact(token=self.token))

    @Rule(Fact(make_dicision='true'), NOT(Fact(dicision=W())), NOT(Fact(rsi1=W())), salience=800)
    def value_rsi1(self):
        self.rsi1 = input("\nwhat is the value of RSI ? (number between 1-120) \n")
        self.declare(Fact(rsi1=self.rsi1))
        xrsi = int(self.rsi1)
        if (xrsi >= 75):
            self.declare(Fact(dicision='sell'))

        elif (xrsi < 35):
            self.declare(Fact(dicision='buy'))

    @Rule(Fact(make_dicision='true'), NOT(Fact(dicision=W())), NOT(Fact(trend=W())), salience=960)
    def broken_trend(self):
        self.trend = input("\nIs there any broken Trends ? (yes rising trend, yes down trend or None) \n")
        self.trend = self.trend.lower()
        self.declare(Fact(trend=self.trend.strip().lower()))

    @Rule(Fact(trend='yes rising trend'), salience=958)
    def broke_rise(self):
        self.declare(Fact(dicision='sell'))

    @Rule(Fact(trend='yes down trend'), salience=956)
    def broke_down(self):
        self.declare(Fact(dicision='buy'))

    @Rule(Fact(make_dicision='true'), NOT(Fact(dicision=W())), NOT(Fact(IsModel=W())), salience=954)
    def Model_exist(self):
        self.IsModel = input("\nIs there any model? (yes, no) \n")
        self.declare(Fact(IsModel=self.IsModel.strip().lower()))
        if (self.IsModel == 'yes'):
            self.declare(Fact(IsModel='yes'))

    @Rule(Fact(make_dicision='true'), Fact(IsModel='yes'), NOT(Fact(Model=W())), salience=953)
    def Model_type(self):
        self.Model = input('\nWhat is the model? (Flag, Head and neck, W, M, Three down tringles, Three up tringles)\n')
        self.Model = self.Model.lower()
        self.declare(Fact(Model=self.Model.strip().lower()))
        if (
                self.Model == 'flag' or self.Model == 'w' or self.Model == 'head and neck' or self.Model == 'three down tringles'):
            self.declare(Fact(dicision='buy'))

        elif (self.Model == 'm' or self.Model == 'three up tringles'):
            self.declare(Fact(dicision='sell'))

    @Rule(Fact(make_dicision='true'), NOT(Fact(dicision=W())), NOT(Fact(Resistance=W())), salience=940)
    def BreakThrow(self):
        self.Resistance = input("\nIs there break resistance? (yes, no) \n")
        self.Resistance = self.Resistance.lower()
        self.declare(Fact(Resistance=self.Resistance.strip().lower()))

    @Rule(Fact(Resistance='yes'), salience=938)
    def broken_resistance(self):
        self.declare(Fact(dicision='buy'))

    @Rule(Fact(make_dicision='true'), NOT(Fact(dicision=W())), NOT(Fact(Support=W())), salience=920)
    def BreakDown(self):
        self.Support = input("\nIs there break Support? (yes, no) \n")
        self.Support = self.Support.lower()
        self.declare(Fact(Support=self.Support.strip().lower()))

    @Rule(Fact(Support='yes'), salience=918)
    def broken_support(self):
        self.declare(Fact(dicision='sell'))

    @Rule(Fact(make_dicision='true'), NOT(Fact(dicision=W())), NOT(Fact(Volume=W())), salience=910)
    def Def_Volume(self):
        self.Volume = input("\nWhat's the volume last 24 Hours? [0,100]\n")
        self.Volume = self.Volume
        self.declare(Fact(Volume=self.Volume))

        xvolume = int(self.Volume)
        if (xvolume >= 75):
            self.declare(Fact(dicision='sell'))

    @Rule(Fact(make_dicision='true'), NOT(Fact(dicision=W())), NOT(Fact(BOLL=W())), salience=900)
    def place_of_BOLL(self):
        self.BOLL = input("\nIS the price nearly to the up or down Average? (up, down, none)\n")
        self.BOLL = self.BOLL.lower()
        self.declare(Fact(BOLL=self.BOLL.strip().lower()))
        if (self.BOLL == 'up'):
            self.declare(Fact(dicision='sell'))
        elif (self.BOLL == 'down'):
            self.declare(Fact(dicision='buy'))

    @Rule(Fact(make_dicision='true'), NOT(Fact(dicision=W())), salience=-1)
    def unmatched(self):
        self.declare(Fact(dicision='\nYou have to wait for any changes in inicators!! '))

    @Rule(Fact(make_dicision='true'), Fact(dicision=MATCH.dicision), salience=1)
    def getDicision(self, dicision):
        print(dicision)


engine = Expert()
engine.reset()
engine.run()

