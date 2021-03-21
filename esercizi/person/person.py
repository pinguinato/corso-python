# la Classe Person

class Person:
    def __init__(self, nome, cognome, telefono, email):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono
        self.email = email
    
    def stampa_nome_persona(self):
        return self.nome
    
    def stampa_cognome_persona(self):
        return self.cognome
    
    def stampa_telefono_persona(self):
        return self.telefono
    
    def stampa_email_persona(self):
        return self.email
    
    #def stampa_persona(self):
    #    return self.stampa_nome_persona , " " , self.stampa_cognome_persona
        
persona = Person("Roberto", "Gianotto")

print(persona.stampa_nome_persona())