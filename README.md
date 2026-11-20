# Hotel Reservation Project

Et command-line hotell reservasjonssystem skrevet i Python. Brukere kan registrere, logge inn og booke rom.

## Features

- **Registration and login:** lag en konto og logg inn med e-post og passord
- **Input validation:** navn, e-poster, telefonnummre og passord er sjekket med CVS-filen, og programmet spør igjen dersom de ikke er funnet
- **Romadministrasjon (admin):** lage, redigere, slette og liste rom
- **Søke etter ledige rom (bruker):** se hvilke rom som er ledige mellom to datoer
- **Booking (bruker):** book et rom og se totalprisen (med 12% mva ;))
- **Ingen dobbeltbooking:** et rom kan ikke bookes to ganger på samme dato
- **Lagret data:** informasjon lagres i CSV-filene


## Installasjon


   ```bash
   git clone https://github.com/chiknborger hotel-reservation-project.git
   cd hotel-reservation-project
   ```
Run:
```bash
python3 main.py
```
Første gang du kjører programmet, ber det deg opprette administratorkontoen. Etter det blir alle som registrerer seg vanlige brukere.

## Prosjektplan
Prosjektet ble planlagt i et Gantt-diagram (other-files/plan-hotelproject.xlsx)

## Mulige forbedringer
- Avbestille en reservasjon og vise "mine bookinger"
- En PDF-regning når brukeren logger ut
- Hashed passorder
- Flere detaljer om rommene





