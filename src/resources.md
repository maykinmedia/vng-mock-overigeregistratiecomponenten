# Resources

Dit document beschrijft de (RGBZ-)objecttypen die als resources ontsloten
worden met de beschikbare attributen.


## InzageVerzoek

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_2.0/doc/objecttype/inzageverzoek)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| uuid |  | string | nee | C​R​U​D |
| inzageWmo | Indicatie Inzage WMO | boolean | nee | C​R​U​D |
| inzageJeugd | Indicatie Inzage Jeugd | boolean | nee | C​R​U​D |
| inzageParticipatie | Indicatie Inzage Participatie | boolean | nee | C​R​U​D |
| inzageVeiligheidskamer | Indicatie Inzage Veiligheidskamer | boolean | nee | C​R​U​D |
| inzageSchuldhulpverlening | Indicatie Inzage Schuldhulpverlening | boolean | nee | C​R​U​D |
| inzageOverigeRegelingen | Indicatie Inzage Overige regelingen | boolean | nee | C​R​U​D |
| onderwerpOverigeRegelingen | Onderwerp bij Overige Regelingen | string | nee | C​R​U​D |
| inzageAlgemeen | Indicatie Inzage Algemeen | boolean | nee | C​R​U​D |
| redenInzageAlgemeen | Reden Algemeen | string | nee | C​R​U​D |
| antwoordPerEmail | Indicatie Antwoord per e-mail | boolean | nee | C​R​U​D |

## NatuurlijkPersoon

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_2.0/doc/objecttype/natuurlijkpersoon)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url |  | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| bsn |  | string | ja | C​R​U​D |
| naam |  | string | ja | C​R​U​D |
| telefoonnummer |  | string | ja | C​R​U​D |
| email |  | string | nee | C​R​U​D |

## MeldingOpenbareRuimte

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_2.0/doc/objecttype/meldingopenbareruimte)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url |  | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| hoofdcategorie |  | string | ja | C​R​U​D |
| subcategorie |  | string | ja | C​R​U​D |
| locatieBeschrijving | Aanvullende omschrijving locatie | string | nee | C​R​U​D |
| data |  | string | nee | C​R​U​D |

## ProductOfDienst

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_2.0/doc/objecttype/productofdienst)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url |  | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| naam |  | string | ja | C​R​U​D |
| omschrijving |  | string | nee | C​R​U​D |
| webpagina |  | string | nee | C​R​U​D |

## NietNatuurlijkPersoon

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_2.0/doc/objecttype/nietnatuurlijkpersoon)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url |  | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| rsin | Het door een kamer toegekend uniek nummer voor de INGESCHREVEN NIET-NATUURLIJK PERSOON | string | ja | C​R​U​D |
| statutaireNaam | Naam van de niet-natuurlijke persoon zoals deze is vastgelegd in de statuten (rechtspersoon) of in de vennootschapsovereenkomst is overeengekomen (Vennootschap onder firma of Commanditaire vennootschap). | string | nee | C​R​U​D |
| datumAanvang | De datum van aanvang van de NIET-NATUURLIJK PERSOON | string | ja | C​R​U​D |
| datumBeeindiging | De datum van beëindiging van de NIET-NATUURLIJK PERSOON. | string | nee | C​R​U​D |

## Adres

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_2.0/doc/objecttype/adres)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| id |  | integer | nee | ~~C~~​R​~~U~~​~~D~~ |
| straatnaam | De officiële straatnaam zoals door het bevoegd gemeentelijk orgaan is vastgesteld, zo nodig ingekort conform de specificaties van de NEN 5825. | string | ja | C​R​U​D |
| postcode |  | string | ja | C​R​U​D |
| woonplaatsnaam |  | string | ja | C​R​U​D |
| huisnummer |  | string | ja | C​R​U​D |
| huisletter |  | string | nee | C​R​U​D |
| huisnummertoevoeging |  | string | nee | C​R​U​D |

## VerblijfsObject

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_2.0/doc/objecttype/verblijfsobject)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url |  | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| identificatie |  | string | ja | C​R​U​D |


* Create, Read, Update, Delete
