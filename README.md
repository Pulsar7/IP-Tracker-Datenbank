# IP-Tracker-Datenbank
Eine Datenbank für IP-Adressen und deren Standorte
# IP-Tracker
Das db.py Script sucht nach der vom Client angeforderten IP und dessen Standort usw. 
Diese Information wird angezeigt: 

    [Hostname]
    [IP]
    [Land]
    [Bundesland]
    [Stadt]
# Verschlüsselte Datenübertragung

Die Datenübertragung zwischen der Datenbank und den Endbenutzer (Client) erfolgt über eine AES-128-Bit Verschlüsselung, welche durch das 
Python Modul Fernet erstellt wird. Der Schlüssel wird zu Beginn des Startens vom Server-Script angezeigt.
