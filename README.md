# IP-Tracker-Datenbank
Eine Datenbank für IP-Adressen und deren Standorte. Es können sich derzeit maximal 10 Clients verbinden, man kann jedoch innhalb des Scripts variieren. Beachte jedoch, dass das jeweilige Gerät die Anzahl von generierten Threads auch verarbeiten muss! -> Multithreading Server
# IP-Tracker
Das db.py Script sucht nach der vom Client angeforderten IP und dessen Standort usw. 
Diese Informationen werden der IP entnommen: 

    [Hostname]
    [IP]
    [Land]
    [Bundesland]
    [Stadt]
# Verschlüsselte Datenübertragung

Die Datenübertragung zwischen der Datenbank und den Endbenutzer (Client) erfolgt über eine AES-128-Bit Verschlüsselung, welche durch das 
Python Modul Fernet erstellt wird. Der Schlüssel wird zu Beginn des Startens vom Server-Script angezeigt.
