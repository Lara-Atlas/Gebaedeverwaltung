# Basisklasse
class Gebaeude:
    def __init__(self, adresse="unbekannt", preis=0.0, baujahr=0):
        self.__adresse = adresse
        self.__preis = preis
        self.__baujahr = baujahr

    def get_adresse(self):
        return self.__adresse

    def set_adresse(self, value):
        self.__adresse = value

    def get_preis(self):
        return self.__preis

    def set_preis(self, value):
        self.__preis = value

    def get_baujahr(self):
        return self.__baujahr

    def set_baujahr(self, value):
        self.__baujahr = value

    def get_daten(self):
        return (f"Adresse: {self.__adresse}\n"
                f"Preis: {self.__preis}\n"
                f"Baujahr: {self.__baujahr}")

# Abgeleitete Klasse Wohnhaus
class Wohnhaus(Gebaeude):
    def __init__(self, adresse="unbekannt", preis=0.0, baujahr=0, anzahl_wohnungen=0):
        super().__init__(adresse, preis, baujahr)
        self.__anzahl_wohnungen = anzahl_wohnungen

    def get_anzahl_wohnungen(self):
        return self.__anzahl_wohnungen

    def set_anzahl_wohnungen(self, value):
        self.__anzahl_wohnungen = value

    def get_daten(self):
        return super().get_daten() + f"\nAnzahl Wohnungen: {self.__anzahl_wohnungen}"

# Abgeleitete Klasse Lagerhalle
class Lagerhalle(Gebaeude):
    def __init__(self, adresse="unbekannt", preis=0.0, baujahr=0, lagerflaeche=0.0):
        super().__init__(adresse, preis, baujahr)
        self.__lagerflaeche = lagerflaeche

    def get_lagerflaeche(self):
        return self.__lagerflaeche

    def set_lagerflaeche(self, value):
        self.__lagerflaeche = value

    def get_daten(self):
        return super().get_daten() + f"\nLagerfläche: {self.__lagerflaeche} m²"

# Neue Klasse Krankenhaus
class Krankenhaus(Gebaeude):
    def __init__(self, adresse="unbekannt", preis=0.0, baujahr=0, anzahl_raeume=0, anzahl_personal=0):
        super().__init__(adresse, preis, baujahr)
        self.__anzahl_raeume = anzahl_raeume
        self.__anzahl_personal = anzahl_personal

    def get_anzahl_raeume(self):
        return self.__anzahl_raeume

    def set_anzahl_raeume(self, value):
        self.__anzahl_raeume = value

    def get_anzahl_personal(self):
        return self.__anzahl_personal

    def set_anzahl_personal(self, value):
        self.__anzahl_personal = value

    def get_daten(self):
        return (super().get_daten() +
                f"\nAnzahl Räume: {self.__anzahl_raeume}" +
                f"\nAnzahl Personal: {self.__anzahl_personal}")

# --- Beispielnutzung ---
wohnhaus = Wohnhaus("Musterstraße 5", 350000, 1998, 10)
lagerhalle = Lagerhalle("Industriestraße 12", 500000, 2005, 1200)
krankenhaus = Krankenhaus("Gesundheitsweg 1", 2000000, 2015, 50, 200)