Program umožňující automatické vyplnění docházky v sep systému na základě CSV vstupu.

Již je konec unavného a opakovaného vyplňování strediska a lokality, stačí jen vyplnit CSV soubor a nechat program, aby za vás vyplnil docházku.

## Instalace

1. Stáhněte si tento repozitář
2. Nainstalujte si python3
3. Nainstalujte si potřebné knihovny pomocí `pip install -r requirements.txt`
4. V souboru sep_autofill.py nezbytné údaje pro vaši identifikaci v sep systému - USER_ID, ID_STREDISKA apod.

## Zápis dat do CSV souboru

### Formát CSV souboru

CSV soubor musí mít následující formát:

```
datum;cas_od;cas_do;project_id
```

datum - formát YYYY-MM-DD

cas_od - formát HH:MM

cas_do - formát HH:MM

project_id - ID projektu, který chcete vyplnit projektu může byt v jeden den více, musí být odděleny čárkou (viz příklad níže). Seznam projektů a jejich ID najdete v souboru projects.py, kde můžete také přidat do pole pomocnou zkratku projektu.

Za zkratku projektu je možné přidat poznámku oddělenou pomlčkou (viz příklad níže).
V rámci textu poznámky tedy pomlčku již nepoužívat.

```


například:

```

2023-06-01;8:00;16:30;SUDB-vyrovnani plosek
2023-06-02;8:00;16:30;2212.2
2023-06-02;8:00;16:30;2212.2-test vypoctu,Office-vyplneni dochazky

```


## Change log

2023-08-02 - Přidána možnost vyplnit poznámku k projektu
```
