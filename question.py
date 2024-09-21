#Trivia Game
#Philip Weinthal U71401206 (Driver/Navigator)
#Description - This program can be used to play a game of trivia via its trivia bank.
class questionClass():
    def __init__(self, question, a1, a2, a3, a4, ca):
        self.__question = question
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__ca = ca
    def __str__(self):
        printStr=''
        printStr+=self.__question+'\n'
        printStr+=self.__a1+'\n'
        printStr+=self.__a2+'\n'
        printStr+=self.__a3+'\n'
        printStr+=self.__a4
        return printStr
    def get_question(self):
        return self.__question
    def get_a1(self):
        return self.__a1
    def get_a2(self):
        return self.__a2
    def get_a3(self):
        return self.__a3
    def get_a4(self):
        return self.__a4
    def get_ca(self):
        return self.__ca
    def set_question(self,question):
        self.__question = question
    def set_a1(self,a1):
        self.__a1 = a1
    def set_a2(self,a2):
        self.__a2 = a2
    def set_a3(self,a3):
        self.__a3 = a3
    def set_a4(self,a4):
        self.__a4 = a4
    def set_ca(self,ca):
        self.__ca = ca
