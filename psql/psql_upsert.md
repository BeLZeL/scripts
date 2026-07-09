https://neon.com/postgresql/tutorial/upsert
https://wiki.postgresql.org/wiki/UPSERT

Table avec valeurs initiales :

```
account | log_date   | currency | deposit
--------|------------|----------|---------------------
123     | 2024-01-01 | EUR      | 1000.00
```

Résultat qu'on va vouloir upsert dans la BDD (ici même account et log_date) :

```
account | log_date   | currency | deposit
--------|------------|----------|---------------------
123     | 2024-01-01 | USD      | 1500.00
```

```
INSERT INTO table 
    (account, log_date, currency, deposit)
VALUES (%s, %s, %s, %s)
ON CONFLICT (account, log_date) DO UPDATE SET
    currency = EXCLUDED.currency,
    deposit = EXCLUDED.deposit
```

EXCLUDED est un mot clef pour récupérer les résultats de la nouvelle requête

```
-- Résultat après upsert :
account | log_date   | currency | deposit
--------|------------|----------|---------------------
123     | 2024-01-01 | USD      | 1500.00  <-- Mise à jour
```
