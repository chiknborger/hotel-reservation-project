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


## Innstallasjon

1. Clone the repository:
   ```bash
   git clone https://github.com/chiknborger/hotel-reservation-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repo-name
   ```
3. Install dependencies:
   ```bash
   npm install
   # or: pip install -r requirements.txt
   ```

```
