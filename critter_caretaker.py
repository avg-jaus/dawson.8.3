# Моя зверюшка
# Виртуальный питомец, о котором пользователь может заботиться
#
# Программа «Моя зверюшка» доработана так, что пользователь сам решает, сколько еды скормить
# зверюшке и сколько времени потратить на игру с ней в условных единицах.
# В зависимости от передаваемых величин зверюшка неодинаково быстро насыщается и веселеет.
#
# В программе «Моя зверюшка» создан своего рода «черный ход» - способ увидетЬ точные значения
# числовых атрибутов объекта.
# В меню сделан секретный пункт 9, который подсказка не отражает, если пользователь его выбирает,
# то на экран выводится объект.
# Реализовано с помощью специального метода _str_().

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name         # имя зверюшки
        self.hunger = hunger     # уровень голода
        self.boredom = boredom   # уровень уныния

    """ Увеличивает уровень голода и уныния """
    def __pass_time(self):
        self.hunger += 1         # увеличить уровень голода
        self.boredom += 1        # увеличить уровень уныния

    """ Отражает самочувствие игрушки """
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m
    
    """ Беседуем с хозяином """
    def talk(self):
        print("Меня зовут", self.name, "и сейчас я чувствую себя", self.mood, "\n")
        self.__pass_time()
        
    """ Едим """    
    def eat(self, food = 4):
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
        
    """ Играем"""
    def play(self, fun = 4):
        print("Yиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Kaк вы назовете свою зверюшку?: ")
    crit = Critter(crit_name)
    amount_of_food = 0                                         # количество еды
    amount_of_boredom = 0                                      # количество уныния

    choice = None  
    while choice != "0":
        print \
        ("""
        Моя зверюшка
    
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)
    
        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свиданья.")

        # беседа со зверюшкой
        elif choice == "1":
            crit.talk()
        
        # кормление зверюшки
        elif choice == "2":
            # Запрос количества еды и вызов метода с уменьшением чувства голода
            amount_of_food = int(input("Сколько еды дадим зверюшке - " + crit.name + "?:"))
            crit.eat(amount_of_food)
         
        # игра со зверюшкой
        elif choice == "3":
            # Запрос количества времени игры и вызов метода уменьшения уровня уныния
            amount_of_boredom = int(input("Как долго поиграем со зверюшкой - " + crit.name + "?:"))           
            crit.play(amount_of_boredom)

        # непонятный пользовательский ввод
        else:
            print("\nИзвините. в меню нет пункта.")

main()

