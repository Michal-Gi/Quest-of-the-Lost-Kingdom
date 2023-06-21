class Character:
    """
        Klasa Character reprezentuje postać w grze. Postać posiada określone atrybuty, takie jak punkty zdrowia (hp),
        punkty many (mp), wytrzymałość (stamina) oraz zadawane obrażenia (damage). Postać posiada również atrybut
        'immunity_time', który reprezentuje czas odporności na obrażenia.

        Atrybuty:
            hp (int): Punkty zdrowia postaci.
            mp (int): Punkty many postaci.
            stamina (int): Wytrzymałość postaci.
            damage (int): Obrażenia zadawane przez postać.
            immunity_time (int): Czas odporności na obrażenia.

        Metody:
            get_hurt(self, damage): Metoda odpowiadająca za otrzymanie obrażeń przez postać.
                                    Obrażenia są zadawane tylko, gdy 'immunity_time' wynosi 0,
                                    w przeciwnym razie postać jest odporna na obrażenia.
                                    Po otrzymaniu obrażeń, 'immunity_time' jest ustawiane na 60.
        """
    def __init__(self, hp, mp, stamina, damage):
        self.hp = hp
        self.mp = mp
        self.stamina = stamina
        self.damage = damage
        self.immunity_time = 0

    def get_hurt(self, damage):
        if self.immunity_time == 0:
            self.hp -= damage
            self.immunity_time = 60