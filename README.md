Per questo esame ho utilizzato una struttura quanto più possibile modulare senza andare troppo fuori traccia richiesta.

Ho implementato questi esercizi seguendo il principio della Separazione delle Preoccupazioni (SOC), dell'Astrazione e delle Responsabilità Singole.
Ho diviso logica business (MovieMethods.py) e persistenza dei dati (MovieLibrary)
Ho utilizzato l'incapsulamento creando la classe Movie con inmetodi per la sua traduzione in dizionari e instanza.
Tenendo in mente il DRY e spero il keep it simple, ho seguito cosa richiesto aggiungendo all'inizializzazione del costruttore della classe MovieLibrary, oltre a json_file e movies, 
movie_methods per riuscire a dare questa struttura.
Ho pensato alla pulizia e validazione delle stringhe, ma soprattuto ho usato il Type Hinting 
