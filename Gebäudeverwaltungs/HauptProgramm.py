import Gebäudeverwaltung as g


if __name__ == "__main__":

    wohnhaus =g.Wohnhaus("Musterstraße 5",350000,1998,10 ) # type: ignore
    print(wohnhaus.get_daten())
    
    lagerhalle =g.Lagerhalle("Industriestraße 12", 500000, 2005, 1200) # type: ignore
    print(lagerhalle.get_daten())
   
    krankenhaus =g.Krankenhaus("Gesundheitsweg 1", 2000000, 2015, 50, 200) # type: ignore
    print(krankenhaus.get_daten())