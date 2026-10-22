# Gold-label review sheet (clean chunks)

One section per concept. Mark **Decision** (approve / reject / edit). Chunk ids are described in `docs/CHUNK_IDS.md`: `<pdf>/s<section>/<article>`; `[title]` is the text inside the PDF the chunk belongs to (code vs. decree/convention). Candidates are lexical hits for the French question over the chunks of the gold source: evidence, not truth. Retrieved results are shown for **dev** concepts only.

---
## penal_theft  (dev)

- `q001` [fr, penal, concept] Quelle est la peine pour le vol ?
- `q013` [fr, penal, article_lookup] Que dit l'article 258 du code pénal ?
- `q041` [fr, unfiltered, cross_domain] Quelle est la peine pour le vol ?
- `q047` [ar, penal, concept] ما هي عقوبة السرقة؟
- `q066` [ar, unfiltered, cross_domain] ما هي عقوبة السرقة؟
- `q068` [en, penal, concept] What is the penalty for theft?
- `q085` [en, unfiltered, cross_domain] What is the penalty for theft?

**Current gold** → chunks

- `PenalFr/s02/258` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 258.- Quiconque soustrait frauduleusement une chose qui ne lui appartient pas est coupable de vol. Est assimilée au vol, l'utilisation frauduleuse d'eau, de gaz, d'électricité au détriment des concessionnaires.
- `PenalFr/s02/260` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 260 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, le vol commis avec la réunion des cinq circonstances suivantes : 1) à l'aide de violences graves ou de menaces de violences graves envers la victime ou ses proches, 2) à l'aide d'escalade ou d'ouvertur
- `PenalFr/s02/261` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 261 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de vingt ans de prison, le vol commis à l'aide de l'une des deux premières circonstances édictées par l'article précédent.
- `PenalFr/s02/262` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 262 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de douze ans de prison, le vol commis avec la réunion des trois dernières circonstances prévues à l'article 260.

**Corpus candidates** (BM25 over PenalFr.pdf; query terms: peine vol)

- gold `PenalFr/s02/258` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 258.- Quiconque soustrait frauduleusement une chose qui ne lui appartient pas est coupable de vol. Est assimilée au vol, l'utilisation frauduleuse d'eau, de gaz, d'électricité au détriment des (6.1)
-      `PenalFr/s02/265` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 265.- Tout individu coupable de vol peut être condamné aux peines accessoires prévues par l'article 5 du présent code. (5.4)
- gold `PenalFr/s02/262` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 262 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de douze ans de prison, le vol commis avec la réunion des trois dernières circonstances prévues à l'article 260. (5.0)
- gold `PenalFr/s02/261` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 261 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de vingt ans de prison, le vol commis à l'aide de l'une des deux premières circonstances édictées par l'article précédent. (4.9)
-      `PenalFr/s02/274` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confectionné, sciemment, un instrument destiné à commettre u (4.3)
-      `PenalFr/s02/266` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 266.- Ne constitue pas un vol, la soustraction commise par les ascendants de quelque degré qu’ils soient au préjudice de leurs enfants, à moins que l'objet soustrait n'appartienne pour partie  (3.9)
-      `PenalFr/s02/270` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 270.- Sont considérés comme armes, au sens de l'article 260, tous instruments fabriqués pour l'attaque ou la défense des personnes. Sont également considérés comme armes, les bâtons, rasoirs,  (3.9)
- gold `PenalFr/s02/260` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 260 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, le vol commis avec la réunion des cinq circonstances suivantes : 1) à l'aide de violences graves ou d (3.1)

**Retrieved** (top-6, dev only)

- `q001` [fr]
    -   `PenalFr/s02/264` Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   `PenalFr/s02/61-quater` Article 61 quater. (Ajouté par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l
    -   `PenalFr/s02/129` Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   `PenalFr/s02/274` Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confection
    -   `PenalFr/s02/263` Article 263.- Est puni de dix ans d’emprisonnement l’auteur du vol commis : 1°- au cours d'un incendie ou après une explosion, inondation, naufrage, a
    -   `PenalFr/s02/186` Article 186 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de quinze ans d'emprisonnement, celui qui contrefait ou altère des monnaies en
- `q013` [fr]
    - ✓ `PenalFr/s02/258` Article 258.- Quiconque soustrait frauduleusement une chose qui ne lui appartient pas est coupable de vol. Est assimilée au vol, l'utilisation fraudul
- `q041` [fr]
    -   `PenalFr/s02/264` Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   `PenalFr/s02/61-quater` Article 61 quater. (Ajouté par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l
    -   `PenalFr/s02/129` Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   `PenalFr/s02/274` Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confection
    -   `PenalFr/s02/186` Article 186 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de quinze ans d'emprisonnement, celui qui contrefait ou altère des monnaies en
    -   `PenalFr/s02/190` Article 190.- Est puni de trois ans d'emprisonnement, quiconque aura coloré les monnaies ayant cours légal en Tunisie ou les monnaies étrangères, dans
- `q047` [ar]
    -   `PenalFr/s02/61-quater` Article 61 quater. (Ajouté par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l
    -   `PenalFr/s02/264` Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   `PenalFr/s02/295` Article 295.- Est puni des peines prévues à l'article 291du présent code, quiconque, amène, frauduleusement, autrui à quitter le territoire tunisien e
    -   `PenalFr/s02/274` Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confection
    -   `PenalFr/s02/129` Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   `PenalFr/s02/61-ter` Article 61 ter. (Ajouté par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l'ar
- `q066` [ar]
    -   `PenalFr/s02/61-quater` Article 61 quater. (Ajouté par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l
    -   `PenalFr/s02/264` Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   `PenalFr/s02/295` Article 295.- Est puni des peines prévues à l'article 291du présent code, quiconque, amène, frauduleusement, autrui à quitter le territoire tunisien e
    -   `CommerceFr/s01/411-ter` Article 411 ter. (Ajouté par la loi n° 85-82 du 11 août 1985) Est puni d'un an d'emprisonnement et d'une amende de 500 dinars : - Celui qui émet un ch
    -   `PenalFr/s02/274` Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confection
    -   `PenalFr/s02/129` Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
- `q068` [en]
    -   `PenalFr/s02/61-quater` Article 61 quater. (Ajouté par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l
    -   `PenalFr/s02/264` Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   `PenalFr/s02/295` Article 295.- Est puni des peines prévues à l'article 291du présent code, quiconque, amène, frauduleusement, autrui à quitter le territoire tunisien e
    -   `PenalFr/s02/274` Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confection
    - ✓ `PenalFr/s02/262` Article 262 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de douze ans de prison, le vol commis avec la réunion des trois dernières circ
    -   `PenalFr/s02/247` Article 247.- Est puni de six mois d’emprisonnement et de deux cent quarante dinars d’amende, quiconque, se sera rendu coupable de diffamation. Est pu
- `q085` [en]
    -   `PenalFr/s02/264` Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   `PenalFr/s02/295` Article 295.- Est puni des peines prévues à l'article 291du présent code, quiconque, amène, frauduleusement, autrui à quitter le territoire tunisien e
    -   `PenalFr/s02/274` Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confection
    - ✓ `PenalFr/s02/262` Article 262 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de douze ans de prison, le vol commis avec la réunion des trois dernières circ
    -   `PenalFr/s02/129` Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   `PenalFr/s02/263` Article 263.- Est puni de dix ans d’emprisonnement l’auteur du vol commis : 1°- au cours d'un incendie ou après une explosion, inondation, naufrage, a

**Suggested change:** Add 263 (theft committed during fire/explosion etc., 10 years) and 264 ("tous autres vols", 5 years): both are theft penalties in the corpus, and 264 is the single most frequent 'wrong' result in the v1 baseline.

- add chunks: PenalFr/s02/263, PenalFr/s02/264
- drop chunks: none
- proposed gold:
    - article 258 `Article 258` → `PenalFr/s02/258`
        > Article 258.- Quiconque soustrait frauduleusement une chose qui ne lui appartient pas est coupable de vol. Est assimilée au vol, l'utilisation fraudul
    - article 260 `Article 260 (Modifié par la loi n° 89-23` → `PenalFr/s02/260`
        > Article 260 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, le vol commis avec la réunion des cinq circonstance
    - article 261 `Article 261` → `PenalFr/s02/261`
        > Article 261 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de vingt ans de prison, le vol commis à l'aide de l'une des deux premières cir
    - article 262 `Article 262` → `PenalFr/s02/262`
        > Article 262 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de douze ans de prison, le vol commis avec la réunion des trois dernières circ
    - NEW article 263 `Article 263` → `PenalFr/s02/263`
        > Article 263.- Est puni de dix ans d’emprisonnement l’auteur du vol commis : 1°- au cours d'un incendie ou après une explosion, inondation, naufrage, a
    - NEW article 264 `Article 264` → `PenalFr/s02/264`
        > Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_homicide  (test)

- `q002` [fr, penal, concept] Qu'est-ce que le meurtre ?
- `q014` [fr, penal, article_lookup] Que dit l'article 201 ?
- `q049` [ar, penal, concept] ما هي عقوبة القتل العمد؟
- `q069` [en, penal, concept] What is the penalty for murder?

**Current gold** → chunks

- `PenalFr/s02/201` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 201.- Est puni de mort, quiconque aura, par quelque moyen que ce soit, commis volontairement et avec préméditation un homicide.
- `PenalFr/s02/202` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 202.- La préméditation consiste dans le dessein, formé avant l'action, d'attentat à la personne d'autrui.
- `PenalFr/s02/203` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 203.- Est puni de mort, l’auteur de parricide. Est qualifié parricide, le meurtre des ascendants quel qu’en soit le degré.

**Corpus candidates** (BM25 over PenalFr.pdf; query terms: meurtre)

- gold `PenalFr/s02/203` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 203.- Est puni de mort, l’auteur de parricide. Est qualifié parricide, le meurtre des ascendants quel qu’en soit le degré. (6.3)
-      `PenalFr/s02/205` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 205 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni d'emprisonnement à vie le coupable de meurtre dans tous les cas non prévus par les articles ci-dessus. (6.0)
-      `PenalFr/s02/211` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 211 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de deux ans de prison, le meurtre commis par la mère sur son enfant à sa naissance ou immédiatement après. (5.9)
-      `PenalFr/s02/72` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 72.- Est puni de mort, l’auteur de l'attentat ayant pour but de changer la forme du gouvernement, d'inciter les gens à s'armer les uns contre les autres ou à provoquer le désordre, le meurtre  (5.3)
-      `PenalFr/s02/101-quater` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 101 quater (Ajouté art.2 D.L n° 2011-106 du 22 octobre 2011) . - Est exempt des peines encourues pour les actes mentionnés à l'article 101 bis du présent code, le fonctionnaire public ou assim (2.3)

**Retrieved:** _hidden (test concept)_

**Suggested change:** Add 204 (homicide preceded/accompanied by another offence: death) and 205 (meurtre in all cases not provided above: life imprisonment): they define/penalise murder directly. 201-203 unchanged.

- add chunks: PenalFr/s02/204, PenalFr/s02/205
- drop chunks: none
- proposed gold:
    - article 201 `Article 201` → `PenalFr/s02/201`
        > Article 201.- Est puni de mort, quiconque aura, par quelque moyen que ce soit, commis volontairement et avec préméditation un homicide.
    - article 202 `Article 202` → `PenalFr/s02/202`
        > Article 202.- La préméditation consiste dans le dessein, formé avant l'action, d'attentat à la personne d'autrui.
    - article 203 `Article 203` → `PenalFr/s02/203`
        > Article 203.- Est puni de mort, l’auteur de parricide. Est qualifié parricide, le meurtre des ascendants quel qu’en soit le degré.
    - NEW article 204 `Article 204` → `PenalFr/s02/204`
        > Article 204 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de mort, l’auteur de l'homicide volontaire lorsque l’homicide a été précédé, a
    - NEW article 205 `Article 205` → `PenalFr/s02/205`
        > Article 205 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni d'emprisonnement à vie le coupable de meurtre dans tous les cas non prévus par

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_corruption  (test)

- `q003` [fr, penal, concept] Quelle est la peine pour la corruption ?
- `q048` [ar, penal, concept] ما هي عقوبة الرشوة؟
- `q071` [en, penal, concept] What is the penalty for bribery?

**Current gold** → chunks

- `PenalFr/s02/84` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 84 (Modifié par la loi n° 98-33 du 23 mai 1998).- Si le fonctionnaire public ou assimilé a provoqué la corruption, la peine prévue à l'article 83 de ce code sera portée au double.
- `PenalFr/s02/85` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 85 (Modifié par la loi n° 98-33 du 23 mai 1998).- Si le fonctionnaire public ou assimilé a accepté des dons, promesses, présents ou avantages de quelque nature que ce soit en récompense d'actes qu'il a accomplis et qui sont liés à sa fonction, mais non sujet à contre partie, ou d'un acte qu'
- `PenalFr/s02/86` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 86 (Abrogé par la loi n° 1998-33 du 23 mai 1998) .

**Corpus candidates** (BM25 over PenalFr.pdf; query terms: peine corruption)

-      `PenalFr/s02/147` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 147 (Modifié par la loi n° 89-23 du 27 février 1989).- Est augmentée d'un an, la peine du condamné à l'emprisonnement à temps qui s'est évadé ou tenté de s'évader. S'il y a eu violence, bris d (6.5)
- gold `PenalFr/s02/84` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 84 (Modifié par la loi n° 98-33 du 23 mai 1998).- Si le fonctionnaire public ou assimilé a provoqué la corruption, la peine prévue à l'article 83 de ce code sera portée au double. (6.2)
-      `PenalFr/s02/89` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 89 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni, le juge corrompu, de la même peine prononcée contre le prévenu par l'effet de la corruption, à condition que la peine prononcée  (5.6)
-      `PenalFr/s02/148` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 148.- Celui qui, en dehors du cas prévu à l'article 111, procure ou facilite l'évasion d'un détenu, est puni de l'emprisonnement pendant 1 an, s'il a usé de violences ou de menaces ou fourni d (5.3)
-      `PenalFr/s02/146` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 146.- Tout prévenu qui s'évade du lieu de sa détention ou se délivre des mains de ses gardiens à l'aide de violences, de menaces ou de bris de prison est puni d'un emprisonnement d'un an. La t (5.2)
-      `PenalFr/s02/92` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 92 (Modifié par la loi n° 98-33 du 23 mai 1998).- La peine est d'un an d'emprisonnement et de mille dinars d'amende, si la tentative de corruption n'a eu aucun effet. Elle est de deux ans d'em (5.1)
-      `PenalFr/s02/94` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 94.- Dans tous les cas de corruption, les choses données ou reçues sont confisquées au profit de l'Etat. Section III - La concussion (5.0)
-      `PenalFr/s02/93` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 93.- Est absous le corrupteur ou l'intermédiaire qui, avant toute poursuite, révèle volontairement le fait de corruption et, en même temps, en rapporte la preuve. (4.8)

**Retrieved:** _hidden (test concept)_

**Suggested change:** Remove 86: its heading says 'Abrogé par la loi n° 1998-33' (empty article). Add 83 (fonctionnaire who agrees to offers/promises, i.e. passive corruption) and 91 (person who corrupted or attempted to corrupt, 5 years). 84-85 unchanged.

- add chunks: PenalFr/s02/83, PenalFr/s02/91
- drop chunks: PenalFr/s02/86
- proposed gold:
    - NEW article 83 `Article 83` → `PenalFr/s02/83`
        > Article 83 (Modifié par la loi n° 98-33 du 23 mai 1998).- Toute personne ayant la qualité de fonctionnaire public ou assimilé conformément aux disposi
    - article 84 `Article 84` → `PenalFr/s02/84`
        > Article 84 (Modifié par la loi n° 98-33 du 23 mai 1998).- Si le fonctionnaire public ou assimilé a provoqué la corruption, la peine prévue à l'article
    - article 85 `Article 85` → `PenalFr/s02/85`
        > Article 85 (Modifié par la loi n° 98-33 du 23 mai 1998).- Si le fonctionnaire public ou assimilé a accepté des dons, promesses, présents ou avantages 
    - NEW article 91 `Article 91` → `PenalFr/s02/91`
        > Article 91 (Modifié par la loi n° 98-33 du 23 mai 1998).- Est punie de cinq ans d'emprisonnement et de cinq mille dinars d'amende, toute personne qui 

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_fraud  (test)

- `q004` [fr, penal, concept] Quelle est la peine pour l'escroquerie ?
- `q050` [ar, penal, concept] ما هي عقوبة الاحتيال؟
- `q070` [en, penal, concept] How is fraud punished?

**Current gold** → chunks

- `PenalFr/s02/291` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 291 (Modifié par le décret du 8 octobre 1935).- Est puni de cinq ans d’emprisonnement et de deux mille quatre cents dinars d’amende, quiconque, soit en faisant usage de faux noms ou de fausses qualités, soit en employant des ruses ou artifices propres à persuader de l'existence de fausses en

**Corpus candidates** (BM25 over PenalFr.pdf; query terms: peine escroquerie)

-      `PenalFr/s02/290` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 290.- Est puni de deux ans d’emprisonnement, le commerçant qui s'est réduit à l'insolvabilité par sa prodigalité ou par des spéculations hasardeuses ne rentrant pas dans le cercle ordinaire de (5.9)
-      `PenalFr/s02/292` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 292.- Est assimilé à l'escroquerie et puni des peines prévues à l'article précédent, le fait : 1) de vendre, hypothéquer, mettre en gage ou louer des biens dont on n'a pas le droit de disposer (5.0)
-      `PenalFr/s02/6` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 6.- Le présent code détermine pour chaque infraction le maximum de la peine encourue. Le minimum de chaque peine est déterminé par ses articles 14 et 16. (1.5)
-      `PenalFr/s02/54` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 54.- Lorsque le même fait constitue plusieurs infractions, la peine encourue pour l'infraction entraînant la peine la plus forte est seule prononcée. (1.5)
-      `PenalFr/s02/15-quater` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 15 quater (ajouté par la loi n°2009-68 du 12 août 2009).- La peine de réparation pénale tend à remplacer la peine d'emprisonnement prononcée par le tribunal par une réparation pécuniaire que d (1.5)
-      `PenalFr/s02/43` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 43 (Modifié par la loi n° 89-23 du 27 février 1989 et la loi n° 95-93 du 9 novembre 1995).- La loi pénale est applicable aux délinquants âgés de plus de treize ans révolus et moins de dix huit (1.4)
-      `PenalFr/s02/34` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 34 (Modifié par la loi n° 89-23 du 27 février 1989).- La peine de mort, lorsqu'elle est applicable aux auteurs principaux d'une infraction, est remplacée à l'égard des complices qui se sont re (1.4)
-      `PenalFr/s02/123` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 123.- La peine prononcée contre l’auteur de rébellion parmi les prisonniers s'ajoute à celle qu’il est entrain de purger. Si l’auteur de la rébellion est en état de détention préventive, la pe (1.4)

**Retrieved:** _hidden (test concept)_

**Suggested change:** Add 292: 'assimilé à l'escroquerie et puni des peines prévues à l'article précédent'. 291 is anchored to the main article (two fragment chunks also carry number 291).

- add chunks: PenalFr/s02/292
- drop chunks: none
- proposed gold:
    - article 291 `Article 291 (Modifié par le décret du 8 octobre 1935)` → `PenalFr/s02/291`
        > Article 291 (Modifié par le décret du 8 octobre 1935).- Est puni de cinq ans d’emprisonnement et de deux mille quatre cents dinars d’amende, quiconque
    - NEW article 292 `Article 292` → `PenalFr/s02/292`
        > Article 292.- Est assimilé à l'escroquerie et puni des peines prévues à l'article précédent, le fait : 1) de vendre, hypothéquer, mettre en gage ou lo

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_breach_of_trust  (test)

- `q005` [fr, penal, concept] Qu'est-ce que l'abus de confiance ?

**Current gold** → chunks

- `PenalFr/s02/297` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 297.- Est puni de trois ans d’emprisonnement et de deux cent quarante dinars d’amende, quiconque détourne ou dissipe, tente de détourner ou dissiper au préjudice des propriétaires, possesseurs ou détenteurs, des effets, deniers, marchandises, billets, quittances ou tous autres écrits contena

**Corpus candidates** (BM25 over PenalFr.pdf; query terms: abus confiance)

-      `PenalFr/s02/296` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 296 (Modifié par le décret du 18 avril 1946).- Est puni des peines prévues à l'article 291, celui qui, prétendant connaître le lieu où se trouvent des objets ou des animaux égarés ou volés, se (10.2)
-      `PenalFr/s02/178` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 178.- Dans les cas prévus à la présente section, il est fait application des peines accessoires édictées par l'article 5. Section XVII – De la contrefaçon et abus de sceau (5.6)
-      `PenalFr/s02/100` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 100 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de dix ans d'emprisonnement et d'une amende de mille dinars tout fonctionnaire public ou assimilé qui soustrait, détourne, ou su (4.3)
-      `PenalFr/s02/233` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 233 (Abrogé par le décret du 26 mai 1949 et ajouté par la loi 64-34 du 2 juillet 1964).- La peine sera d'un emprisonnement de trois à cinq ans et d'une amende de cinq cents à mille dinars dans (3.4) ABROGATED
-      `PenalFr/s02/321-bis` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 321 bis (Ajouté par la loi organique n° 2001-43 du 3 mai 2001, portant modification du code de la presse).- Quiconque voudra exercer, sur la voie publique ou en tout autre lieu public ou privé (2.6)
-      `PenalFr/s02/32` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 32.- Est considéré complice et puni comme tel : 1°- celui qui, par dons, promesses, menaces, abus d'autorité ou de pouvoir, machinations, artifices coupables, a provoqué à l'action ou donné de (2.2)

**Retrieved:** _hidden (test concept)_

**Suggested change:** No change; only anchored to the real heading (297 is the abus de confiance article).

- add chunks: none
- drop chunks: none
- proposed gold:
    - article 297 `Article 297` → `PenalFr/s02/297`
        > Article 297.- Est puni de trois ans d’emprisonnement et de deux cent quarante dinars d’amende, quiconque détourne ou dissipe, tente de détourner ou di

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_defamation  (dev)

- `q006` [fr, penal, concept] Que dit la loi sur la diffamation ?

**Current gold** → chunks

- `PenalFr/s02/245` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 245.- Il y a diffamation dans toute allégation ou imputation publique d'un fait qui porte atteinte à l'honneur ou à la considération d'une personne ou d'un corps constitué. La preuve du fait diffamatoire peut être établie dans les cas prévus à l'article 57 du code de la presse.
- `PenalFr/s02/246` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 246.- Il y a calomnie : 1) lorsque le fait diffamatoire a été judiciairement déclaré non établi, 2) lorsque le prévenu ne peut rapporter la preuve dudit fait dans le cas où la loi l'y autorise. La calomnie est punissable même si les imputations ont été faites par écrits non rendus publics, m

**Corpus candidates** (BM25 over PenalFr.pdf; query terms: diffamation)

- gold `PenalFr/s02/245` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 245.- Il y a diffamation dans toute allégation ou imputation publique d'un fait qui porte atteinte à l'honneur ou à la considération d'une personne ou d'un corps constitué. La preuve du fait d (5.9)
-      `PenalFr/s02/247` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 247.- Est puni de six mois d’emprisonnement et de deux cent quarante dinars d’amende, quiconque, se sera rendu coupable de diffamation. Est puni d'un an d’emprisonnement et de deux cent quaran (5.5)
-      `PenalFr/s02/15-bis` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 15 bis (Ajouté par la loi n° 99-89 du 2 août 1999).- Dans le cas où le tribunal prononce une peine de prison ferme d’une durée ne dépassant pas un an, il peut la remplacer dans le même jugemen (1.3)

**Retrieved** (top-6, dev only)

- `q006` [fr]
    -   `PenalFr/s00/1` Article premier.- Les textes promulgués ci-après, sous le titre de « code pénal tunisien », seront en vigueur, devant les tribunaux tunisiens, le 1er 
    -   `PenalFr/s02/295` Article 295.- Est puni des peines prévues à l'article 291du présent code, quiconque, amène, frauduleusement, autrui à quitter le territoire tunisien e
    -   `PenalFr/s02/129` Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   `PenalFr/s02/61` Article 61 (Modifié par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l'articl
    -   `PenalFr/s02/188` Article 188 (Modifié par la loi n° 89-23 du 27 février 1989).- Sont punis d'emprisonnement à vie ceux qui ont contrefait ou falsifié les billets de ba
    -   `PenalFr/s02/185` Article 185 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, celui qui contrefait ou altère la monnaie fiduciair

**Suggested change:** Add 247: it is the penalty article ('Est puni de six mois d'emprisonnement ... diffamation'); 245 defines diffamation, 246 defines calomnie. 247 is a frequent 'wrong' result in v1 because it is in fact relevant.

- add chunks: PenalFr/s02/247
- drop chunks: none
- proposed gold:
    - article 245 `Article 245` → `PenalFr/s02/245`
        > Article 245.- Il y a diffamation dans toute allégation ou imputation publique d'un fait qui porte atteinte à l'honneur ou à la considération d'une per
    - article 246 `Article 246` → `PenalFr/s02/246`
        > Article 246.- Il y a calomnie : 1) lorsque le fait diffamatoire a été judiciairement déclaré non établi, 2) lorsque le prévenu ne peut rapporter la pr
    - NEW article 247 `Article 247` → `PenalFr/s02/247`
        > Article 247.- Est puni de six mois d’emprisonnement et de deux cent quarante dinars d’amende, quiconque, se sera rendu coupable de diffamation. Est pu

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_rape  (test)

- `q007` [fr, penal, concept] Comment est puni le viol ?
- `q051` [ar, penal, concept] ما هي عقوبة الاغتصاب؟

**Current gold** → chunks

- `PenalFr/s02/227` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 227 (Modifié par la loi n° 85-9 du 7 mars 1985 et par la loi n° 89-23 du 27 février 1989).- Est puni de mort : 1) le crime de viol commis avec violence, usage ou menace d'usage d'arme. 2) le crime de viol commis même sans usage des moyens précités sur une personne âgée de moins de dix ans ac
- `PenalFr/s02/227-bis` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 227 bis (Ajouté par la loi n° 1958 du 4 mars 1958 et modifié par la loi n° 69-21 du 27 mars 1969 et modifié par la loi n° 89-23 du 27 février 1989).- Est puni d'emprisonnement pendant six ans, celui qui fait subir sans violence, l'acte sexuel à un enfant de sexe féminin âgé de moins de quinz

**Corpus candidates** (BM25 over PenalFr.pdf; query terms: puni viol)

- gold `PenalFr/s02/227` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 227 (Modifié par la loi n° 85-9 du 7 mars 1985 et par la loi n° 89-23 du 27 février 1989).- Est puni de mort : 1) le crime de viol commis avec violence, usage ou menace d'usage d'arme. 2) le c (10.4)
-      `PenalFr/s02/213` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 213 (Modifié par la loi n° 95-93 du 9 novembre 1995).- L'auteur est puni de douze ans d'emprisonnement si par suite de l'abandon prévu à l'article 212 du code pénal, l'enfant ou l'incapable es (2.0)
-      `PenalFr/s02/247` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 247.- Est puni de six mois d’emprisonnement et de deux cent quarante dinars d’amende, quiconque, se sera rendu coupable de diffamation. Est puni d'un an d’emprisonnement et de deux cent quaran (2.0)
-      `PenalFr/s02/63` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 63.- L'attentat contre la vie du chef de l'État est puni de mort. (2.0)
-      `PenalFr/s02/206` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 206.- Est puni de cinq ans d'emprisonnement, celui qui, sciemment, aide à un suicide. (1.9)
-      `PenalFr/s02/121` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 121.- Est puni comme s'il avait participé à la rébellion, quiconque l'a provoquée, soit par des discours tenus dans des lieux ou réunions publics, soit par placards, affiches ou écrits imprimé (1.9)
-      `PenalFr/s02/37` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 37.- Nul ne peut être puni que pour un fait accompli intentionnellement, sauf dans les cas spécialement prévus par la loi. (1.9)
-      `PenalFr/s02/203` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 203.- Est puni de mort, l’auteur de parricide. Est qualifié parricide, le meurtre des ascendants quel qu’en soit le degré. (1.8)

**Retrieved:** _hidden (test concept)_

**Suggested change:** No change in articles; anchors separate 227 and 227 bis (same law, both about rape / sexual acts without violence).

- add chunks: none
- drop chunks: none
- proposed gold:
    - article 227 `Article 227 (Modifié par la loi n° 85-9` → `PenalFr/s02/227`
        > Article 227 (Modifié par la loi n° 85-9 du 7 mars 1985 et par la loi n° 89-23 du 27 février 1989).- Est puni de mort : 1) le crime de viol commis avec
    - article 227 `Article 227 bis` → `PenalFr/s02/227-bis`
        > Article 227 bis (Ajouté par la loi n° 1958 du 4 mars 1958 et modifié par la loi n° 69-21 du 27 mars 1969 et modifié par la loi n° 89-23 du 27 février 

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_harassment  (test)

- `q008` [fr, penal, concept] Quelle est la sanction du harcèlement sexuel ?

**Current gold** → chunks

- `PenalFr/s02/226` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 226.- Est puni de six mois d'emprisonnement et de quarante huit dinars d’amende, quiconque se sera, sciemment, rendu coupable d'outrage public à la pudeur.
- `PenalFr/s02/226-bis` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 226 bis (Ajouté par la loi n° 2004-73 du 2 août 2004).- Est puni de six mois d’emprisonnement et d’une amende de mille dinars quiconque porte publiquement atteinte aux bonnes mœurs ou à la morale publique par le geste ou la parole ou gène intentionnellement autrui d’une façon qui porte attei
- `PenalFr/s02/226-ter` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 226 ter (Ajouté par la loi n° 2004-73 du 2 août 2004).- Est puni d’un an d’emprisonnement et d’une amende de trois mille dinars celui qui commet le harcèlement sexuel. Est considéré comme harcèlement sexuel toute persistance dans la gène d’autrui par la répétition d’actes ou de paroles ou de
- `PenalFr/s02/226-quater` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 226 quater (Ajouté par la loi n° 2004-73 du 2 août 2004).- Les peines prévues aux deux articles précédents ne préjudicient pas à l’application des peines plus sévères prévues pour d’autres infractions. Les poursuites ne peuvent être exercées qu’à la demande du ministère public sur la base d’

**Corpus candidates** (BM25 over PenalFr.pdf; query terms: sanction harcèlement sexuel)

- gold `PenalFr/s02/226-ter` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 226 ter (Ajouté par la loi n° 2004-73 du 2 août 2004).- Est puni d’un an d’emprisonnement et d’une amende de trois mille dinars celui qui commet le harcèlement sexuel. Est considéré comme harc (13.3)
-      `PenalFr/s02/319` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 319.- Sont passibles des mêmes peines, les auteurs de rixes et ceux qui se livrent à des voies de fait ou à des violences n'entraînant pour la santé d'autrui aucune conséquence sérieuse ou dur (4.6)
-      `PenalFr/s02/227-bis` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 227 bis (Ajouté par la loi n° 1958 du 4 mars 1958 et modifié par la loi n° 69-21 du 27 mars 1969 et modifié par la loi n° 89-23 du 27 février 1989).- Est puni d'emprisonnement pendant six ans, (3.5)
-      `PenalFr/s02/15-ter` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 15 ter (Ajouté par la loi n° 99-89 du 2 août 1999).- Pour remplacer la peine d'emprisonnement par la peine de travail d’intérêt général, il est exigé que l’inculpé soit présent à l’audience, q (3.1)
-      `PenalFr/s02/248` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 248 (Modifié par la loi n° 58-73 du 4 juillet 1958).- Est puni de deux à cinq ans d'emprisonnement et de sept cent vingt dinars d’amende, quiconque aura, par quelque moyen que ce soit, fait un (2.7)

**Retrieved:** _hidden (test concept)_

**Suggested change:** Narrow: the harassment article is 226 ter ('commet le harcèlement sexuel', 1 year + 3000 dinars). 226 (outrage public à la pudeur) and 226 bis (atteinte aux bonnes moeurs) are different offences. Keep 226 quater (rules attached to the two preceding articles).

- add chunks: none
- drop chunks: PenalFr/s02/226, PenalFr/s02/226-bis
- proposed gold:
    - article 226 `Article 226 ter` → `PenalFr/s02/226-ter`
        > Article 226 ter (Ajouté par la loi n° 2004-73 du 2 août 2004).- Est puni d’un an d’emprisonnement et d’une amende de trois mille dinars celui qui comm
    - article 226 `Article 226 quater` → `PenalFr/s02/226-quater`
        > Article 226 quater (Ajouté par la loi n° 2004-73 du 2 août 2004).- Les peines prévues aux deux articles précédents ne préjudicient pas à l’application

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_self_defence  (test)

- `q009` [fr, penal, concept] Qu'est-ce que la légitime défense ?
- `q052` [ar, penal, concept] ما هو الدفاع الشرعي؟
- `q072` [en, penal, concept] What counts as self-defence?

**Current gold** → chunks

- `PenalFr/s02/39` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 39.- Il n'y a pas d'infraction lorsque l'auteur y a été contraint par une circonstance qui exposait sa vie ou celle de l’un de ses proches à un danger imminent, et lorsque ce danger ne pouvait être autrement détourné. Sont considérés comme proches : 1°- les ascendants et descendants, 2°- les

**Corpus candidates** (BM25 over PenalFr.pdf; query terms: légitime défense)

-      `PenalFr/s02/276` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 276.- Est puni de six mois de prison celui qui, ayant été précédemment condamné à une peine corporelle pour un attentat contre la propriété, est trouvé en possession de numéraire, valeurs ou o (5.6)
-      `PenalFr/s02/298` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 298.- Est puni de six mois d'emprisonnement et de soixante douze dinars d'amende, quiconque, s'étant fait remettre des avances en vue de l'exécution d'un contrat, refuse sans motif légitime d' (5.1)
-      `PenalFr/s02/61-ter` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 61 ter. (Ajouté par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l'article 62 du présent code, tout Tunisien ou Etrange (5.1)
-      `PenalFr/s02/22` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 22.- L'interdiction de séjour consiste dans la défense faite au condamné de résider et de paraître dans les lieux ou régions déterminés par le jugement. Elle est prononcée dans les cas prévus  (5.1)
-      `PenalFr/s02/60-bis` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 60 bis (Ajouté par le décret du 10 janvier 1957).- Est coupable de trahison et puni de mort : 1°- tout Tunisien qui aura livré à une puissance étrangère ou à ses agents, de quelque manière et  (5.0)
-      `PenalFr/s02/101` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 101.- Est puni de cinq ans d'emprisonnement et de cent vingt dinars d'amende, tout fonctionnaire public ou assimilé qui, dans l'exercice ou à l'occasion de l'exercice de ses fonctions aura, sa (4.9)
-      `PenalFr/s02/270` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 270.- Sont considérés comme armes, au sens de l'article 260, tous instruments fabriqués pour l'attaque ou la défense des personnes. Sont également considérés comme armes, les bâtons, rasoirs,  (4.3)
-      `PenalFr/s02/61-quater` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 61 quater. (Ajouté par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l'article 62 du présent code, sans préjudice, le ca (4.1)

**Retrieved:** _hidden (test concept)_

**Suggested change:** Replace 39 by 40. Art 40 covers 'se défendant contre les auteurs de vols ou de pillages' and repelling a nocturnal break-in = légitime défense. Art 39 is contrainte/état de nécessité ('danger imminent'). JUDGMENT CALL: you may prefer to keep 39 as a related article.

- add chunks: PenalFr/s02/40
- drop chunks: PenalFr/s02/39
- proposed gold:
    - NEW article 40 `Article 40` → `PenalFr/s02/40`
        > Article 40.- Il n'y a pas d'infraction : 1) si l'homicide a été commis, si les blessures ont été faites ou les coups portés en repoussant, la nuit, l'

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_arson  (dev)

- `q010` [fr, penal, concept] Comment est puni l'incendie volontaire ?

**Current gold** → chunks

- `PenalFr/s02/307` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 307 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, quiconque aura mis volontairement le feu, directement ou indirectement, à des édifices, navires, bateaux, magasins, chantiers habités ou servant à l'habitation, et généralement aux lieux habités ou ser
- `PenalFr/s02/308` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 308 (Modifié par la loi n° 89-23 du 27 février 1989).- La peine encourue est celle de vingt ans d'emprisonnement, si les bâtiments incendiés n'étaient pas habités ou ne servaient pas d'habitation, elle est réduite à dix ans si l'auteur du crime est propriétaire du bâtiment incendié.
- `PenalFr/s02/309` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 309 (Modifié par la loi n° 69-44 du 26 juillet 1969).- Est puni d'un emprisonnement de trois ans et d'une amende de deux mille dinars, celui qui, par maladresse, imprudence, inattention, négligence ou inobservation des règlements, détermine un incendie sur les propriétés mobilières ou immobi

**Corpus candidates** (BM25 over PenalFr.pdf; query terms: puni incendie volontaire)

-      `PenalFr/s02/210` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 210 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni d'emprisonnement à vie, le père qui commet un homicide volontaire sur la personne de son enfant. (9.0)
-      `PenalFr/s02/204` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 204 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de mort, l’auteur de l'homicide volontaire lorsque l’homicide a été précédé, accompagné ou suivi d’une autre infraction passible (6.7)
- gold `PenalFr/s02/307` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 307 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, quiconque aura mis volontairement le feu, directement ou indirectement, à des édifices, navires, bate (5.9)
- gold `PenalFr/s02/309` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 309 (Modifié par la loi n° 69-44 du 26 juillet 1969).- Est puni d'un emprisonnement de trois ans et d'une amende de deux mille dinars, celui qui, par maladresse, imprudence, inattention, négli (5.6)
-      `PenalFr/s02/304` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 304 (Modifié par la loi n° 69-44 du 26 juillet 1969).- Quiconque, volontairement et autrement que par une explosion ou un incendie, cause un dommage à la propriété immobilière ou mobilière d'a (5.0)
-      `PenalFr/s02/143` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 143.- Est puni d’un mois d'emprisonnement et de quarante huit dinars d’amende, quiconque, le pouvant, refuse ou néglige de faire les travaux, les services ou de prêter le secours dont il a été (4.6)
-      `PenalFr/s02/306-ter` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 306 ter (Ajouté par la loi n° 77-56 du 3 août 1977).- Est puni d’un à cinq ans d'emprisonnement et de deux cents dinars à quatre mille dinars d'amende, quiconque, ayant propagé, sciemment, de  (4.3)
-      `PenalFr/s02/263` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 263.- Est puni de dix ans d’emprisonnement l’auteur du vol commis : 1°- au cours d'un incendie ou après une explosion, inondation, naufrage, accident de chemin de fer, révolte, émeute ou tout  (4.3)

**Retrieved** (top-6, dev only)

- `q010` [fr]
    -   `PenalFr/s02/295` Article 295.- Est puni des peines prévues à l'article 291du présent code, quiconque, amène, frauduleusement, autrui à quitter le territoire tunisien e
    -   `PenalFr/s02/264` Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   `PenalFr/s02/61-quater` Article 61 quater. (Ajouté par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l
    -   `PenalFr/s02/129` Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   `PenalFr/s02/247` Article 247.- Est puni de six mois d’emprisonnement et de deux cent quarante dinars d’amende, quiconque, se sera rendu coupable de diffamation. Est pu
    -   `PenalFr/s02/60-bis` Article 60 bis (Ajouté par le décret du 10 janvier 1957).- Est coupable de trahison et puni de mort : 1°- tout Tunisien qui aura livré à une puissance

**Suggested change:** Remove 309: it punishes fires caused by 'maladresse, imprudence, négligence' (involuntary), while the question asks about incendie volontaire. 307 and 308 unchanged.

- add chunks: none
- drop chunks: PenalFr/s02/309
- proposed gold:
    - article 307 `Article 307` → `PenalFr/s02/307`
        > Article 307 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, quiconque aura mis volontairement le feu, directeme
    - article 308 `Article 308` → `PenalFr/s02/308`
        > Article 308 (Modifié par la loi n° 89-23 du 27 février 1989).- La peine encourue est celle de vingt ans d'emprisonnement, si les bâtiments incendiés n

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_attempt  (dev)

- `q011` [fr, penal, concept] Que dit la loi sur la tentative de crime ?

**Current gold** → chunks

- `PenalFr/s02/59` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 59.- Toute tentative d'infraction est punissable comme l'infraction elle-même si elle n'a été suspendue ou si elle n'a manqué son effet que par des circonstances indépendantes de la volonté de son auteur. Toutefois, la tentative n'est pas punissable, sauf disposition contraire de la loi, dan

**Corpus candidates** (BM25 over PenalFr.pdf; query terms: tentative crime)

-      `PenalFr/s02/227` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 227 (Modifié par la loi n° 85-9 du 7 mars 1985 et par la loi n° 89-23 du 27 février 1989).- Est puni de mort : 1) le crime de viol commis avec violence, usage ou menace d'usage d'arme. 2) le c (6.4)
-      `PenalFr/s02/308` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 308 (Modifié par la loi n° 89-23 du 27 février 1989).- La peine encourue est celle de vingt ans d'emprisonnement, si les bâtiments incendiés n'étaient pas habités ou ne servaient pas d'habitat (4.9)
-      `PenalFr/s02/14` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 14 (Modifié par le décret du 15 septembre 1923).- La condamnation à l'emprisonnement est prononcée pour cinq années au moins quand l'infraction est considérée comme crime, aux termes de l’arti (4.0)
-      `PenalFr/s02/30` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 30 (Modifié par la loi n° 89-23 du 27 février 1989).- Est de plein droit en état d'interdiction légale, à partir du jugement et pour la durée de sa peine, tout condamné, pour un seul crime, à  (3.7)
-      `PenalFr/s02/92` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 92 (Modifié par la loi n° 98-33 du 23 mai 1998).- La peine est d'un an d'emprisonnement et de mille dinars d'amende, si la tentative de corruption n'a eu aucun effet. Elle est de deux ans d'em (3.4)
-      `PenalFr/s02/251` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 251 (Modifié par la loi n° 2005-45 du 6 juin 2005).- La peine est de vingt ans d'emprisonnement et de vingt mille dinars d'amende : a) si la capture, arrestation, détention ou séquestration a  (3.3)
-      `PenalFr/s02/58` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 58.- Les peines de l'interdiction de séjour et de la surveillance administrative ne se confondent pas. CHAPITRE VI DE LA TENTATIVE (3.3)
-      `PenalFr/s02/257` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 257.- Si les infractions prévues aux deux articles précédents ont été commises pendant la nuit la peine est de 6 mois de prison. Si elles ont été commises à l'aide d'escalade ou d'effraction o (3.0)

**Retrieved** (top-6, dev only)

- `q011` [fr]
    -   `PenalFr/s02/61-quater` Article 61 quater. (Ajouté par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l
    -   `PenalFr/s00/1` Article premier.- Les textes promulgués ci-après, sous le titre de « code pénal tunisien », seront en vigueur, devant les tribunaux tunisiens, le 1er 
    -   `PenalFr/s02/295` Article 295.- Est puni des peines prévues à l'article 291du présent code, quiconque, amène, frauduleusement, autrui à quitter le territoire tunisien e
    -   `PenalFr/s02/129` Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   `PenalFr/s02/72` Article 72.- Est puni de mort, l’auteur de l'attentat ayant pour but de changer la forme du gouvernement, d'inciter les gens à s'armer les uns contre 
    -   `PenalFr/s02/61` Article 61 (Modifié par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l'articl

**Suggested change:** No change (Art 59 = tentative punissable).

- add chunks: none
- drop chunks: none
- proposed gold:
    - article 59 `Article 59` → `PenalFr/s02/59`
        > Article 59.- Toute tentative d'infraction est punissable comme l'infraction elle-même si elle n'a été suspendue ou si elle n'a manqué son effet que pa

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_assault  (dev)

- `q012` [fr, penal, concept] Quelle est la peine pour les coups et blessures volontaires ?
- `q046` [fr, penal, colloquial] Que risque-t-on si on frappe quelqu'un ?

**Current gold** → chunks

- `PenalFr/s02/217` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 217 (Modifié par le décret du 17 février 1936).- Est puni de deux ans d'emprisonnement et de sept cent vingt dinars d’amende, l’auteur de l'homicide involontaire, commis ou causé par maladresse, imprudence, négligence, inattention ou inobservation des règlements. Section II - Violences - Men
- `PenalFr/s02/218` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 218 (Modifié par la loi n° 93-72 du 12 juillet 1993).- Tout individu qui, volontairement, fait des blessures, porte des coups, ou commet toute autre violence ou voie de fait ne rentrant pas dans les prévisions de l'article 319, est puni d'un emprisonnement d'un an et d'une amende de mille di
- `PenalFr/s02/219` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 219 (Modifié par la loi n° 64-34 du 2 juillet 1964 et par la loi n° 1989-23 du 27 février 1989).- Quand les violences ci-dessus exprimées ont été suivies de mutilation, perte de l'usage d'un membre, défiguration, infirmité ou incapacité permanente dont le taux ne dépasse pas 20%, le coupable

**Corpus candidates** (BM25 over PenalFr.pdf; query terms: peine coups blessures volontaires)

-      `PenalFr/s02/208` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 208 (Modifié par la loi n° 89-23 du 27 février 1989).- Le coupable est puni de vingt ans d'emprisonnement, si les coups portés ou les blessures faites volontairement, mais sans intention de do (9.9)
-      `PenalFr/s02/220` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 220 ( Modifié par la loi n° 64-34 du 2 juillet 1964).- Les individus, ayant participé à une rixe au cours de laquelle ont été portés des coups et blessures de la nature de ceux prévus aux arti (9.8)
-      `PenalFr/s02/215` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 215 (Le paragraphe 2 a été modifié par la loi n° 89-23 du 27 février 1989).- Quiconque, sans intention de donner la mort, administre volontairement à une personne des substances ou se livre su (8.7)
-      `PenalFr/s02/40` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 40.- Il n'y a pas d'infraction : 1) si l'homicide a été commis, si les blessures ont été faites ou les coups portés en repoussant, la nuit, l'escalade ou l'effraction des clôtures, murs ou ent (8.3)
-      `PenalFr/s02/119` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 119.- Tout individu, ayant participé à une rébellion armée ou non armée, au cours de laquelle des voies de fait ont été exercées sur un fonctionnaire dans l'exercice des ses fonctions, est, du (8.3)
- gold `PenalFr/s02/218` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 218 (Modifié par la loi n° 93-72 du 12 juillet 1993).- Tout individu qui, volontairement, fait des blessures, porte des coups, ou commet toute autre violence ou voie de fait ne rentrant pas da (7.2)
-      `PenalFr/s02/306-bis` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 306 bis (Ajouté par la loi n° 77-56 du 3 août 1977 et modifié par la loi n° 89-23 du 27 février 1989).- Sera punie d'un emprisonnement de dix ans, toute personne qui, par violence ou menace, s (4.5)
-      `PenalFr/s02/157` [CODE PENAL LIVRE PREMIER DISPOSITIONS GENERALES CH] Article 157 (Modifié par la loi n° 89-23 du 27 février 1989).- Le coupable est puni de quinze ans d'emprisonnement, si les bris de scellés, les soustractions, l'enlèvement, destruction ou altération d (4.2)

**Retrieved** (top-6, dev only)

- `q012` [fr]
    -   `PenalFr/s02/295` Article 295.- Est puni des peines prévues à l'article 291du présent code, quiconque, amène, frauduleusement, autrui à quitter le territoire tunisien e
    -   `PenalFr/s02/61-quater` Article 61 quater. (Ajouté par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l
    -   `PenalFr/s00/1` Article premier.- Les textes promulgués ci-après, sous le titre de « code pénal tunisien », seront en vigueur, devant les tribunaux tunisiens, le 1er 
    -   `PenalFr/s02/61` Article 61 (Modifié par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l'articl
    -   `PenalFr/s02/129` Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   `PenalFr/s02/233` Article 233 (Abrogé par le décret du 26 mai 1949 et ajouté par la loi 64-34 du 2 juillet 1964).- La peine sera d'un emprisonnement de trois à cinq ans
- `q046` [fr]
    -   `PenalFr/s02/116` Article 116.- Est puni de six mois d'emprisonnement et de quarante huit dinars d’amende, quiconque exerce ou menace d'exercer des violences pour résis
    -   `PenalFr/s02/264` Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   `PenalFr/s02/295` Article 295.- Est puni des peines prévues à l'article 291du présent code, quiconque, amène, frauduleusement, autrui à quitter le territoire tunisien e
    -   `PenalFr/s02/127` Article 127.- Est puni d'un an d’emprisonnement et de soixante douze dinars d’amende, quiconque exerce sur un fonctionnaire public ou assimilé des voi
    -   `PenalFr/s02/129` Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   `PenalFr/s02/61-bis` Article 61 bis (Ajouté par le décret du 10 janvier 1957).- Est coupable d'atteinte à la sûreté extérieure de l'État et puni des peines prévues à l'art

**Suggested change:** Remove 217: it is homicide involontaire (maladresse, imprudence). Add 208 (coups portés ou blessures faites volontairement sans intention de donner la mort: 20 years). 218-219 unchanged; 218 anchored to the main article (a fragment chunk also carries 218).

- add chunks: PenalFr/s02/208
- drop chunks: PenalFr/s02/217
- proposed gold:
    - NEW article 208 `Article 208` → `PenalFr/s02/208`
        > Article 208 (Modifié par la loi n° 89-23 du 27 février 1989).- Le coupable est puni de vingt ans d'emprisonnement, si les coups portés ou les blessure
    - article 218 `Article 218 (Modifié par la loi n° 93-72` → `PenalFr/s02/218`
        > Article 218 (Modifié par la loi n° 93-72 du 12 juillet 1993).- Tout individu qui, volontairement, fait des blessures, porte des coups, ou commet toute
    - article 219 `Article 219` → `PenalFr/s02/219`
        > Article 219 (Modifié par la loi n° 64-34 du 2 juillet 1964 et par la loi n° 1989-23 du 27 février 1989).- Quand les violences ci-dessus exprimées ont 

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## const_right_to_life  (test)

- `q015` [fr, constitution, article_lookup] Que dit l'article 24 sur le droit à la vie ?
- `q053` [ar, constitution, article_lookup] ماذا ينص الفصل 24 من الدستور؟

**Current gold** → chunks

- `tun_RecAcFreeLi/s00/24` Art. 24 – Le droit à la vie est sacré. Il ne peut y être porté atteinte, que dans des cas extrêmes prévus par la loi.

**Corpus candidates** (BM25 over tun_RecAcFreeLi.pdf; query terms: droit vie)

- gold `tun_RecAcFreeLi/s00/24` Art. 24 – Le droit à la vie est sacré. Il ne peut y être porté atteinte, que dans des cas extrêmes prévus par la loi. (7.3)
-      `tun_RecAcFreeLi/s00/30` Art. 30 – L’Etat protège la vie privée, l’inviolabilité du domicile et le secret des correspondances, des communications et des données personnelles. Tout citoyen dispose de la liberté de choisir son  (5.2)
-      `tun_RecAcFreeLi/s00/22` Art. 22 – L’Etat garantit aux citoyens et aux citoyennes les libertés et les droits individuels et collectifs. Il leur assure les conditions d’une vie digne. (4.5)
-      `tun_RecAcFreeLi/s00/5` Art. 5 – La Tunisie constitue une partie de la nation islamique. Seul l’Etat doit œuvrer, dans un régime démocratique, à la réalisation des vocations de l’Islam authentique qui consistent à préserver  (3.8)
-      `tun_RecAcFreeLi/s00/41` Art. 41 – Le droit syndical, y compris le droit de grève, est garanti. Ce droit ne s’applique pas à l’Armée nationale. Les magistrats, les forces de sécurité intérieure et la douane ne disposent pas d (3.1)
-      `tun_RecAcFreeLi/s00/38` Art. 38 – L’Etat garantit le droit à l’information et le droit d’accès à l’information. L’Etat œuvre en vue de garantir le droit d’accès aux réseaux de communication. (3.1)
-      `tun_RecAcFreeLi/s00/99` Art. 99 – Le Président de la République dispose du droit de grâce. (2.5)
-      `tun_RecAcFreeLi/s00/100` Art. 100 – Le Président de la République dispose du droit de grâce. (2.5)

**Retrieved:** _hidden (test concept)_

**Suggested change:** No change; anchored.

- add chunks: none
- drop chunks: none
- proposed gold:
    - article 24 `Art. 24` → `tun_RecAcFreeLi/s00/24`
        > Art. 24 – Le droit à la vie est sacré. Il ne peut y être porté atteinte, que dans des cas extrêmes prévus par la loi.

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## const_fundamental_rights  (dev)

- `q016` [fr, constitution, concept] Quels sont les droits fondamentaux ?
- `q076` [en, constitution, concept] What are the fundamental rights?

**Current gold** → chunks

- `tun_RecAcFreeLi/s00/24` Art. 24 – Le droit à la vie est sacré. Il ne peut y être porté atteinte, que dans des cas extrêmes prévus par la loi.
- `tun_RecAcFreeLi/s00/25` Art. 25 – L’Etat protège la dignité de l’être humain et son intégrité physique et interdit la torture morale et physique. L’infraction de torture est imprescriptible.
- `tun_RecAcFreeLi/s00/26` Art. 26 – La liberté de l’individu est garantie.

**Corpus candidates** (BM25 over tun_RecAcFreeLi.pdf; query terms: droits fondamentaux)

-      `tun_RecAcFreeLi/s00/55` Art. 55 – Aucune restriction ne peut être apportée aux droits et libertés garantis par la présente Constitution qu'en vertu d'une loi et pour répondre aux exigences d’un régime démocratique et en vue  (3.8)
-      `tun_RecAcFreeLi/s00/39` Art. 39 – Les droits d’élire, de voter et de se porter candidat sont garantis dans les conditions fixées par la loi. (3.5)
-      `tun_RecAcFreeLi/s00/23` Art. 23 – Les citoyens et les citoyennes sont égaux en droits et en devoirs. Ils sont égaux devant la loi sans aucune discrimination. (3.5)
-      `tun_RecAcFreeLi/s00/21` Art. 21 – L’Etat garantit la neutralité des institutions éducatives de toute exploitation partisane. Chapitre II – Des droits et libertés (3.3)
-      `tun_RecAcFreeLi/s00/22` Art. 22 – L’Etat garantit aux citoyens et aux citoyennes les libertés et les droits individuels et collectifs. Il leur assure les conditions d’une vie digne. (3.2)
-      `tun_RecAcFreeLi/s00/35` Art. 35 – Aucune personne ne peut être arrêtée ou détenue, sauf en cas de flagrant délit ou en vertu d’une décision judiciaire. Elle est immédiatement informée de ses droits et de l’accusation qui lui (2.5)
-      `tun_RecAcFreeLi/s00/75` Art. 75 – Sont pris sous forme de loi organique, les textes relatifs aux matières suivantes : − les modalités générales de l’application de la Constitution, − l’approbation des traités, − l’organisati (2.5)
-      `tun_RecAcFreeLi/s00/115` Art. 115 – L’Assemblée des représentants du peuple et le Conseil national des régions et des districts peuvent conjointement s’opposer à la poursuite de l’activité du Gouvernement en déposant une moti (2.4)

**Retrieved** (top-6, dev only)

- `q016` [fr]
    -   `tun_RecAcFreeLi/s00/37` Art. 37 – Les libertés d’opinion, de pensée, d’expression, d’information et de publication sont garanties. Aucun contrôle préalable ne peut être exerc
    -   `tun_RecAcFreeLi/s00/9` Art. 9 – La devise de la République tunisienne est Liberté, Ordre, Justice.
    -   `tun_RecAcFreeLi/s00/39` Art. 39 – Les droits d’élire, de voter et de se porter candidat sont garantis dans les conditions fixées par la loi.
    -   `tun_RecAcFreeLi/s00/31` Art. 31 – Aucun citoyen ne peut être déchu de la nationalité tunisienne, ni être banni, extradé, ni empêché de revenir à son pays.
    -   `tun_RecAcFreeLi/s00/30` Art. 30 – L’Etat protège la vie privée, l’inviolabilité du domicile et le secret des correspondances, des communications et des données personnelles. 
    - ✓ `tun_RecAcFreeLi/s00/26` Art. 26 – La liberté de l’individu est garantie.
- `q076` [en]
    -   `tun_RecAcFreeLi/s00/37` Art. 37 – Les libertés d’opinion, de pensée, d’expression, d’information et de publication sont garanties. Aucun contrôle préalable ne peut être exerc
    -   `tun_RecAcFreeLi/s00/9` Art. 9 – La devise de la République tunisienne est Liberté, Ordre, Justice.
    -   `tun_RecAcFreeLi/s00/52` Art. 52 – Les droits de l’enfant sont garantis. Il incombe à ses père et mère et à l’Etat de lui garantir la dignité, la santé, les soins, l’éducation
    -   `tun_RecAcFreeLi/s00/1` Article premier – La Tunisie est un Etat libre, indépendant et souverain.
    - ✓ `tun_RecAcFreeLi/s00/26` Art. 26 – La liberté de l’individu est garantie.
    -   `tun_RecAcFreeLi/s00/5` Art. 5 – La Tunisie constitue une partie de la nation islamique. Seul l’Etat doit œuvrer, dans un régime démocratique, à la réalisation des vocations 

**Suggested change:** Add 22 ('L'Etat garantit aux citoyens ... les libertés et les droits individuels et collectifs'). The question is inherently broad; consider whether it should stay in the scored set. NOTE: the chunk labelled 26 also contains Art. 27 ('Art . 27' with a space escapes the splitter).

- add chunks: tun_RecAcFreeLi/s00/22
- drop chunks: none
- proposed gold:
    - NEW article 22 `Art. 22` → `tun_RecAcFreeLi/s00/22`
        > Art. 22 – L’Etat garantit aux citoyens et aux citoyennes les libertés et les droits individuels et collectifs. Il leur assure les conditions d’une vie
    - article 24 `Art. 24` → `tun_RecAcFreeLi/s00/24`
        > Art. 24 – Le droit à la vie est sacré. Il ne peut y être porté atteinte, que dans des cas extrêmes prévus par la loi.
    - article 25 `Art. 25` → `tun_RecAcFreeLi/s00/25`
        > Art. 25 – L’Etat protège la dignité de l’être humain et son intégrité physique et interdit la torture morale et physique. L’infraction de torture est 
    - article 26 `Art. 26` → `tun_RecAcFreeLi/s00/26`
        > Art. 26 – La liberté de l’individu est garantie.

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## cpp_custody_duration  (dev)

- `q017` [fr, procedure_penale, article_lookup] Que dit l'article 13 sur la garde à vue ?
- `q018` [fr, procedure_penale, concept] Quelle est la durée maximale de la garde à vue ?
- `q055` [ar, procedure_penale, concept] ما هي مدة الاحتفاظ؟
- `q078` [en, procedure_penale, concept] How long can police custody last?

**Current gold** → chunks

- `ProcedurepenaleFr/s01/13` [Code pénal, le décret du 3 août 1908, instituant u] Article 13.- Les officiers de police judiciaire visés aux 3° et 4° de l'article 10 doivent : 1) donner avis au Procureur de la République de toute infraction dont ils acquièrent la connaissance dans l'exercice de leurs fonctions et lui transmettre tous renseignements et procès-verbaux qui s'y rappor
- `ProcedurepenaleFr/s01/13-bis` [Code pénal, le décret du 3 août 1908, instituant u] Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'enquête l'exigent, les officiers de police judiciaire visés aux numéros 3° et 4° de l'article 10, même en cas de crimes ou délits flagrants, et les offi
- `ProcedurepenaleFr/s03/13` [Loi n° 2002-94 du 29 octobre 2002, relative à l'in] Article 13.- Une indemnisation globale du préjudice causé au demandeur lui sera allouée s'il prouve que le préjudice est réel, grave, actuel, et résultant directement de la détention provisoire ou de l'exécution de la peine de prison. Pour l'évaluation du montant de la réparation, doivent être pris 
- `ProcedurepenaleFr/s04/13` [Loi n° 2003-75 du 10 décembre 2003, relative au so] Article 13.- Est puni de cinq à douze ans d’emprisonnement et d'une amende de cinq mille à cinquante mille dinars : - Quiconque adhère sur le territoire de la République, à quelque titre que ce soit, à une organisation ou entente, quelque soit la forme ou le nombre de ses membres, qui a fait, même f

**Corpus candidates** (BM25 over ProcedurepenaleFr.pdf; query terms: garde vue)

- gold `ProcedurepenaleFr/s01/13-bis` [Code pénal, le décret du 3 août 1908, instituant u] Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'enquête l'exigent, les officiers de police judiciair (9.9)
-      `ProcedurepenaleFr/s04/35` [Loi n° 2003-75 du 10 décembre 2003, relative au so] Article 35.- Les procureurs de la République près les tribunaux de première instance autres que Tunis sont habilités à procéder aux actes urgents de l’enquête préliminaire en vue de constater l'infrac (7.7)
-      `ProcedurepenaleFr/s02/361` Article 361.- Les greffiers des tribunaux sont tenus de consigner, sur un registre particulier, les nom, prénom, profession, âge et résidence de tous les individus condamnés pour crimes ou délits, ave (4.9)
-      `ProcedurepenaleFr/s02/71` Article 71.- L'inculpé est soumis à l'examen du service de l'identité judiciaire en vue de faire vérifier son identité et rechercher ses antécédents. (4.5)
-      `ProcedurepenaleFr/s04/11` [Loi n° 2003-75 du 10 décembre 2003, relative au so] Article 11.- Est coupable d'infraction terroriste celui : - qui a incité ou s’est concerté pour la commettre. - qui s’est résolu à la commettre, si cette résolution est accompagnée d'un acte préparato (4.3)
-      `ProcedurepenaleFr/s02/139` Article 139.- La citation doit être remise à la personne de l'intéressé, à son mandataire, à son domestique ou à toute personne habitant avec lui, à la condition que celle-ci soit douée de discernemen (4.1)
-      `ProcedurepenaleFr/s01/10` [Code pénal, le décret du 3 août 1908, instituant u] Article 10.- La police judiciaire est exercée sous l'autorité du Procureur Général de la République et, dans chaque ressort de Cour d'Appel, des avocats généraux par : 1) les Procureurs de la Républiq (3.8)
-      `ProcedurepenaleFr/s04/14` [Loi n° 2003-75 du 10 décembre 2003, relative au so] Article 14.- Est puni de cinq à douze ans d'emprisonnement et d'une amende de cinq mille à cinquante mille dinars quiconque utilise le territoire de la République pour recruter ou entraîner une person (3.7)

**Retrieved** (top-6, dev only)

- `q017` [fr]
    - ✓ `ProcedurepenaleFr/s04/13` Article 13.- Est puni de cinq à douze ans d’emprisonnement et d'une amende de cinq mille à cinquante mille dinars : - Quiconque adhère sur le territoi
    - ✓ `ProcedurepenaleFr/s03/13` Article 13.- Une indemnisation globale du préjudice causé au demandeur lui sera allouée s'il prouve que le préjudice est réel, grave, actuel, et résul
    - ✓ `ProcedurepenaleFr/s01/13` Article 13.- Les officiers de police judiciaire visés aux 3° et 4° de l'article 10 doivent : 1) donner avis au Procureur de la République de toute inf
    - ✓ `ProcedurepenaleFr/s01/13-bis` Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'en
- `q018` [fr]
    -   `ProcedurepenaleFr/s02/321` Article 321.- L'examen des demandes d'extradition est de la compétence de la chambre d'accusation de la cour d'appel de Tunis. L'étranger comparaît de
    -   `ProcedurepenaleFr/s02/85` Article 85 (Modifié par la loi n° 93-114 du 22 novembre 1993).- L'inculpé peut être soumis à la détention préventive dans les cas de crimes ou délits 
    -   `ProcedurepenaleFr/s04/35` Article 35.- Les procureurs de la République près les tribunaux de première instance autres que Tunis sont habilités à procéder aux actes urgents de l
    -   `ProcedurepenaleFr/s04/103` Article 103.- Sont abrogées, les dispositions de l'article 52 bis du code pénal, le troisième alinéa de l'article 305, le deuxième alinéa de premièrem
    -   `ProcedurepenaleFr/s02/311` Article 311.- L'extradition est accordée : 1) lorsque l'infraction motivant la demande est punie par la loi tunisienne d'une peine criminelle ou corre
    - ✓ `ProcedurepenaleFr/s01/13-bis` Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'en
- `q055` [ar]
    -   `ProcedurepenaleFr/s04/75` Article 75 (Modifié par la loi n°2009-65 du 12 août 2009).- Les personnes visées à l’article 74 de la présente loi doivent conserver pendant une pério
    -   `ProcedurepenaleFr/s04/70` Article 70.- Les personnes morales doivent : - tenir des comptes sur un livre-journal faisant état de toutes recettes et dépenses . - tenir un inventa
    -   `ProcedurepenaleFr/s04/83` Article 83 (Modifié par la loi n°2009-65 du 12 août 2009).- La commission tunisienne des analyses financières est tenue de mettre en place une base de
    -   `ProcedurepenaleFr/s02/85` Article 85 (Modifié par la loi n° 93-114 du 22 novembre 1993).- L'inculpé peut être soumis à la détention préventive dans les cas de crimes ou délits 
    - ✓ `ProcedurepenaleFr/s01/13-bis` Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'en
    -   `ProcedurepenaleFr/s02/202` Article 202.- Le juge peut retenir à sa disposition sous mandat de dépôt, le prévenu en état d'ivresse, ou ne pouvant justifier de son identité, ou n'
- `q078` [en]
    -   `ProcedurepenaleFr/s02/85` Article 85 (Modifié par la loi n° 93-114 du 22 novembre 1993).- L'inculpé peut être soumis à la détention préventive dans les cas de crimes ou délits 
    -   `ProcedurepenaleFr/s02/321` Article 321.- L'examen des demandes d'extradition est de la compétence de la chambre d'accusation de la cour d'appel de Tunis. L'étranger comparaît de
    -   `ProcedurepenaleFr/s04/7` Article 7.- Le minimum de la peine d'emprisonnement encourue pour infraction terroriste est fixé comme suit : - Si la peine encourue est l'emprisonnem
    - ✓ `ProcedurepenaleFr/s01/13-bis` Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'en
    -   `ProcedurepenaleFr/s04/103` Article 103.- Sont abrogées, les dispositions de l'article 52 bis du code pénal, le troisième alinéa de l'article 305, le deuxième alinéa de premièrem
    -   `ProcedurepenaleFr/s02/136` Article 136.- Le délai entre le jour où la citation est délivrée et le jour fixé pour la comparution à l'audience est d'au moins trois jours. Si la pa

**Suggested change:** Disambiguate: ProcedurepenaleFr.pdf bundles several laws and has 4 chunks numbered 13 (OPJ powers, garde à vue = Art 13 bis, an indemnisation law, a terrorism law). Only Art 13 (OPJ) and Art 13 bis count.

- add chunks: none
- drop chunks: ProcedurepenaleFr/s03/13, ProcedurepenaleFr/s04/13
- proposed gold:
    - article 13 `Article 13.- Les officiers de police judiciaire visés aux 3°` → `ProcedurepenaleFr/s01/13`
        > Article 13.- Les officiers de police judiciaire visés aux 3° et 4° de l'article 10 doivent : 1) donner avis au Procureur de la République de toute inf
    - article 13 `Article 13 bis` → `ProcedurepenaleFr/s01/13-bis`
        > Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'en

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## cpp_detainee_rights  (test)

- `q019` [fr, procedure_penale, concept] Quels sont les droits de la personne gardée à vue ?
- `q054` [ar, procedure_penale, concept] ما هي حقوق الموقوف؟
- `q077` [en, procedure_penale, concept] What are the rights of a detainee?

**Current gold** → chunks

- `ProcedurepenaleFr/s01/13` [Code pénal, le décret du 3 août 1908, instituant u] Article 13.- Les officiers de police judiciaire visés aux 3° et 4° de l'article 10 doivent : 1) donner avis au Procureur de la République de toute infraction dont ils acquièrent la connaissance dans l'exercice de leurs fonctions et lui transmettre tous renseignements et procès-verbaux qui s'y rappor
- `ProcedurepenaleFr/s01/13-bis` [Code pénal, le décret du 3 août 1908, instituant u] Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'enquête l'exigent, les officiers de police judiciaire visés aux numéros 3° et 4° de l'article 10, même en cas de crimes ou délits flagrants, et les offi
- `ProcedurepenaleFr/s03/13` [Loi n° 2002-94 du 29 octobre 2002, relative à l'in] Article 13.- Une indemnisation globale du préjudice causé au demandeur lui sera allouée s'il prouve que le préjudice est réel, grave, actuel, et résultant directement de la détention provisoire ou de l'exécution de la peine de prison. Pour l'évaluation du montant de la réparation, doivent être pris 
- `ProcedurepenaleFr/s04/13` [Loi n° 2003-75 du 10 décembre 2003, relative au so] Article 13.- Est puni de cinq à douze ans d’emprisonnement et d'une amende de cinq mille à cinquante mille dinars : - Quiconque adhère sur le territoire de la République, à quelque titre que ce soit, à une organisation ou entente, quelque soit la forme ou le nombre de ses membres, qui a fait, même f
- `ProcedurepenaleFr/s02/70` Article 70.- L'inculpé détenu est autorisé à communiquer à tout moment avec son conseil, aussitôt après la première comparution. Le juge d'instruction peut, par ordonnance motivée et non susceptible d'appel, prescrire l'interdiction de communiquer pour une période de dix jours. Cette interdiction pe
- `ProcedurepenaleFr/s04/70` [Loi n° 2003-75 du 10 décembre 2003, relative au so] Article 70.- Les personnes morales doivent : - tenir des comptes sur un livre-journal faisant état de toutes recettes et dépenses . - tenir un inventaire des recettes et virements en rapport avec l'étranger faisant état des montants y afférents, leur justification , la date de leur réalisation et l’

**Corpus candidates** (BM25 over ProcedurepenaleFr.pdf; query terms: droits personne gardée vue)

- gold `ProcedurepenaleFr/s01/13-bis` [Code pénal, le décret du 3 août 1908, instituant u] Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'enquête l'exigent, les officiers de police judiciair (7.6)
-      `ProcedurepenaleFr/s04/14` [Loi n° 2003-75 du 10 décembre 2003, relative au so] Article 14.- Est puni de cinq à douze ans d'emprisonnement et d'une amende de cinq mille à cinquante mille dinars quiconque utilise le territoire de la République pour recruter ou entraîner une person (6.3)
-      `ProcedurepenaleFr/s04/102` [Loi n° 2003-75 du 10 décembre 2003, relative au so] Article 102.- Les jugements prononçant la liquidation ou la confiscation des avoirs en application de la présente loi ne peuvent, en aucun cas, porter atteinte aux droits des tiers acquis de bonne foi (6.3)
-      `ProcedurepenaleFr/s04/72-bis` [Loi n° 2003-75 du 10 décembre 2003, relative au so] Article 72 bis (Ajouté par la loi n°2009-65 du 12 août 2009) Dans le cadre du respect des engagements internationaux de la Tunisie, le ministre chargé des finances peut, après avis du gouverneur de la (5.5)
-      `ProcedurepenaleFr/s04/49` [Loi n° 2003-75 du 10 décembre 2003, relative au so] Article 49 (Modifié par la loi n°2009-65 du 12 août 2009) En cas de péril en la demeure, le juge d'instruction ou le président du tribunal peuvent, selon les cas, et si les circonstances l’exigent, or (4.6)
-      `ProcedurepenaleFr/s02/276` Article 276.- Le procureur général près la cour de cassation peut nonobstant l'expiration du délai de cassation se pourvoir dans l'intérêt de la loi si la décision attaquée a été rendue en violation d (4.5)
-      `ProcedurepenaleFr/s02/71` Article 71.- L'inculpé est soumis à l'examen du service de l'identité judiciaire en vue de faire vérifier son identité et rechercher ses antécédents. (4.5)
-      `ProcedurepenaleFr/s02/263` Article 263.- Le greffier ne doit accepter la requête que si elle est accompagnée de la quittance de consignation à la recette de l'enregistrement de l'amende à laquelle le demandeur serait condamné s (4.4)

**Retrieved:** _hidden (test concept)_

**Suggested change:** Same disambiguation for 13/13 bis; 70 anchored to 'L'inculpé détenu est autorisé à communiquer ... avec son conseil' (another chunk numbered 70 is about personnes morales).

- add chunks: none
- drop chunks: ProcedurepenaleFr/s03/13, ProcedurepenaleFr/s04/13, ProcedurepenaleFr/s04/70
- proposed gold:
    - article 13 `Article 13.- Les officiers de police judiciaire visés aux 3°` → `ProcedurepenaleFr/s01/13`
        > Article 13.- Les officiers de police judiciaire visés aux 3° et 4° de l'article 10 doivent : 1) donner avis au Procureur de la République de toute inf
    - article 13 `Article 13 bis` → `ProcedurepenaleFr/s01/13-bis`
        > Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'en
    - article 70 `Article 70.- L'inculpé détenu` → `ProcedurepenaleFr/s02/70`
        > Article 70.- L'inculpé détenu est autorisé à communiquer à tout moment avec son conseil, aussitôt après la première comparution. Le juge d'instruction

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## cpp_public_action_limitation  (dev)

- `q020` [fr, procedure_penale, concept] Comment se prescrit l'action publique ?

**Current gold** → chunks

- `ProcedurepenaleFr/s01/5` [Code pénal, le décret du 3 août 1908, instituant u] Article 5.- Sauf dispositions spéciales de la loi, l'action publique qui résulte d'un crime se prescrit par dix années révolues, celle qui résulte d'un délit par trois années révolues et celle qui résulte d'une contravention par une année révolue, et ce, à compter du jour où l'infraction a été commi
- `ProcedurepenaleFr/s03/5` [Loi n° 2002-94 du 29 octobre 2002, relative à l'in] Article 5.- La cour d'appel de Tunis est seule compétente pour connaître des demandes en indemnisation. Ces demandes sont de la compétence d'une chambre spécialisée, composée du premier président de la cour d'appel ou de son adjoint et de deux membres ayant fonction de président de chambre au sein d
- `ProcedurepenaleFr/s04/5` [Loi n° 2003-75 du 10 décembre 2003, relative au so] Article 5 (abrogé par la loi n°2009-65 du 12 août 2009)

**Corpus candidates** (BM25 over ProcedurepenaleFr.pdf; query terms: prescrit action publique)

-      `ProcedurepenaleFr/s01/8` [Code pénal, le décret du 3 août 1908, instituant u] Article 8.- L'action civile se prescrit dans les mêmes conditions et délais que l'action publique résultant de l'infraction qui lui donne ouverture. Elle est soumise à tous autres égards aux règles du (13.2)
-      `ProcedurepenaleFr/s04/37` [Loi n° 2003-75 du 10 décembre 2003, relative au so] Article 37.- L'action publique relative à une infraction terroriste se prescrit par vingt ans révolus si elle résulte d’un crime, celle qui résulte d'un délit se prescrit par dix ans révolus, et ce, à (12.1)
-      `ProcedurepenaleFr/s01/6` [Code pénal, le décret du 3 août 1908, instituant u] Article 6.- S'il a été fait, au cours des délais de prescription énumérés à l'article précédent, des actes d'instruction ou de poursuite non suivis de jugement, l'action publique interrompue ne se pre (10.8)
- gold `ProcedurepenaleFr/s01/5` [Code pénal, le décret du 3 août 1908, instituant u] Article 5.- Sauf dispositions spéciales de la loi, l'action publique qui résulte d'un crime se prescrit par dix années révolues, celle qui résulte d'un délit par trois années révolues et celle qui rés (9.6)
-      `ProcedurepenaleFr/s01/3` [Code pénal, le décret du 3 août 1908, instituant u] Article 3.- Hors les cas prévus par la loi, l'action publique n'est pas subordonnée à l'existence d'une plainte et ne peut être arrêtée ni suspendue par le retrait de la plainte ou la renonciation à l (7.7)
-      `ProcedurepenaleFr/s01/1` [Code pénal, le décret du 3 août 1908, instituant u] Article premier.- Toute infraction donne ouverture à une action publique ayant pour but l'application des peines et, si un dommage a été causé, à une action civile en réparation de ce dommage. (7.6)
-      `ProcedurepenaleFr/s02/37` Article 37.- L'action civile poursuivie en même temps que l'action publique conformément à l'article 7 du présent code, peut être exercée, soit devant le juge d'instruction en cours d'information, soi (7.3)
-      `ProcedurepenaleFr/s01/20` [Code pénal, le décret du 3 août 1908, instituant u] Article 20.- Le ministère public met en mouvement et exerce l'action publique. Il requiert l'application de la loi et assure l'exécution des décisions de justice. (7.1)

**Retrieved** (top-6, dev only)

- `q020` [fr]
    -   `ProcedurepenaleFr/s01/6` Article 6.- S'il a été fait, au cours des délais de prescription énumérés à l'article précédent, des actes d'instruction ou de poursuite non suivis de
    - ✓ `ProcedurepenaleFr/s01/5` Article 5.- Sauf dispositions spéciales de la loi, l'action publique qui résulte d'un crime se prescrit par dix années révolues, celle qui résulte d'u
    -   `ProcedurepenaleFr/s02/350` Article 350.- La prescription est suspendue par tout obstacle de droit ou de fait empêchant l'exécution de la peine hors celui qui résulte de la volon
    -   `ProcedurepenaleFr/s04/103` Article 103.- Sont abrogées, les dispositions de l'article 52 bis du code pénal, le troisième alinéa de l'article 305, le deuxième alinéa de premièrem
    -   `ProcedurepenaleFr/s02/335-septies` Article 335 Septies.- S'il a été impossible de conclure une transaction ou si celle ci n'a pas été intégralement exécutée dans les délais impartis, le
    -   `ProcedurepenaleFr/s04/37` Article 37.- L'action publique relative à une infraction terroriste se prescrit par vingt ans révolus si elle résulte d’un crime, celle qui résulte d'

**Suggested change:** Anchor 5 to the prescription article (another 'Article 5' concerns the cour d'appel de Tunis and one is abrogated). Add 6 (interruption of the prescription).

- add chunks: ProcedurepenaleFr/s01/6
- drop chunks: ProcedurepenaleFr/s03/5, ProcedurepenaleFr/s04/5
- proposed gold:
    - article 5 `Article 5.- Sauf dispositions spéciales de la loi, l'action publique` → `ProcedurepenaleFr/s01/5`
        > Article 5.- Sauf dispositions spéciales de la loi, l'action publique qui résulte d'un crime se prescrit par dix années révolues, celle qui résulte d'u
    - NEW article 6 `Article 6.- S'il a été fait, au cours des délais` → `ProcedurepenaleFr/s01/6`
        > Article 6.- S'il a été fait, au cours des délais de prescription énumérés à l'article précédent, des actes d'instruction ou de poursuite non suivis de

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## travail_hours  (test)

- `q021` [fr, travail, concept] Quelle est la durée légale du travail ?
- `q043` [fr, unfiltered, cross_domain] Combien d'heures par semaine peut-on travailler ?
- `q056` [ar, travail, concept] ما هي مدة العمل القانونية؟
- `q079` [en, travail, concept] What is the legal working hours limit?

**Current gold** → chunks

- `travailFr/s01/79` [Le Président de la République Tunisienne HABIB BOU] Article 79 (Modifié par la loi n° 96-62 du 15 juillet 1996).- La durée du travail effectif ne peut excéder 48 heures par semaine ou une limitation équivalente établie sur une période de temps autre que la semaine sans que la durée de cette période ne puisse être supérieure à une année. Cette durée p
- `travailFr/s01/85` [Le Président de la République Tunisienne HABIB BOU] Article 85 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Les salariés ne peuvent être employés que conformément aux indications d’un horaire précisant, pour chaque journée et éventuellement pour chaque semaine ou chaque mois, la répartition des heures de travail. Cet horaire fixe les heures aux

**Corpus candidates** (BM25 over travailFr.pdf; query terms: durée légale travail)

-      `travailFr/s01/88` [Le Président de la République Tunisienne HABIB BOU] Article 88.- Dans les entreprises agricoles, la durée légale du travail est fixée à deux mille sept cents heures par an au maximum pour trois cents jours de travail effectif. Des arrêtés conjoints du  (9.2)
-      `travailFr/s01/286` [Le Président de la République Tunisienne HABIB BOU] Article 286 (Modifié par la loi n° 96-62 du 15 juillet 1996).- L'employeur est tenu de justifier, à tout moment aux agents chargés de l'application des dispositions du présent chapitre, avoir fait les (5.7)
-      `travailFr/s01/6-2` [Le Président de la République Tunisienne HABIB BOU] Article 6-2 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Le contrat de travail est conclu pour une durée indéterminée ou pour une durée déterminée. Le contrat de travail à durée déterminée peut c (3.9)
-      `travailFr/s01/94-2` [Le Président de la République Tunisienne HABIB BOU] Article 94-2 (Ajouté par la loi n°96-62 du 15 juillet 1996).- Le contrat de travail à durée déterminée ou indéterminée peut être conclu pour un travail à temps partiel. Est considéré comme travail à t (3.7)
-      `travailFr/s01/32` [Le Président de la République Tunisienne HABIB BOU] Article 32.- La convention collective de travail peut être conclue, soit pour une durée indéterminée, soit pour une durée déterminée ne pouvant excéder cinq ans. A défaut de stipulation contraire, la  (3.6)
-      `travailFr/s01/94-6` [Le Président de la République Tunisienne HABIB BOU] Article 94-6 (Ajouté par la loi n°96-62 du 15 juillet 1996).- Sont considérées heures supplémentaires les heures effectuées par le travailleur à temps partiel au delà de la durée normale de travail fi (3.5)
-      `travailFr/s01/83` [Le Président de la République Tunisienne HABIB BOU] Article 83 (Modifié par la loi n° 96-62 du 15 juillet 1996).- A titre exceptionnel, l’inspection du travail territorialement compétente peut : 1- autoriser l’employeur à prolonger la durée du travail  (3.5)
-      `travailFr/s01/14` [Le Président de la République Tunisienne HABIB BOU] Article 14.- (Modifié par la loi n° 94-29 du 21 février 1994). .- Le contrat de travail à durée déterminée prend fin par l’expiration de la durée convenue ou par l’accomplissement du travail objet du  (3.4)

**Retrieved:** _hidden (test concept)_

**Suggested change:** Add 88 (legal duration in agricultural enterprises: 2700 h/year) and 83 (exceptional extensions of the working day). 79 and 85 kept (85 = work schedule, borderline).

- add chunks: travailFr/s01/83, travailFr/s01/88
- drop chunks: none
- proposed gold:
    - article 79 `Article 79` → `travailFr/s01/79`
        > Article 79 (Modifié par la loi n° 96-62 du 15 juillet 1996).- La durée du travail effectif ne peut excéder 48 heures par semaine ou une limitation équ
    - NEW article 83 `Article 83` → `travailFr/s01/83`
        > Article 83 (Modifié par la loi n° 96-62 du 15 juillet 1996).- A titre exceptionnel, l’inspection du travail territorialement compétente peut : 1- auto
    - article 85 `Article 85` → `travailFr/s01/85`
        > Article 85 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Les salariés ne peuvent être employés que conformément aux indications d’un horaire préc
    - NEW article 88 `Article 88` → `travailFr/s01/88`
        > Article 88.- Dans les entreprises agricoles, la durée légale du travail est fixée à deux mille sept cents heures par an au maximum pour trois cents jo

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## travail_dismissal  (test)

- `q022` [fr, travail, concept] Quelles sont les conditions de licenciement ?
- `q044` [fr, travail, colloquial] Mon patron peut-il me virer sans préavis ?
- `q058` [ar, travail, colloquial] متى يمكن للمؤجر طرد العامل؟
- `q081` [en, travail, concept] When can an employer lawfully dismiss an employee?

**Current gold** → chunks

- `travailFr/s01/14` [Le Président de la République Tunisienne HABIB BOU] Article 14.- (Modifié par la loi n° 94-29 du 21 février 1994). .- Le contrat de travail à durée déterminée prend fin par l’expiration de la durée convenue ou par l’accomplissement du travail objet du contrat. Le contrat à durée indéterminée prend fin par l’expiration du délai de préavis. Le contrat 
- `travailFr/s01/14-bis` [Le Président de la République Tunisienne HABIB BOU] Article 14 bis. (Ajouté par la loi n° 94-29 du 21 février 1994).- Le préavis de rupture du contrat de travail à durée indéterminée est notifié par lettre recommandée adressée à l’autre partie un mois avant la rupture du contrat. Les travailleurs sont autorisés à s’absenter durant toute la deuxième m
- `travailFr/s01/14-ter` [Le Président de la République Tunisienne HABIB BOU] Article 14 ter. (Ajouté par la loi n° 94-29 du 21 février 1994).- L’employeur qui a l’intention de licencier un travailleur est tenu d’indiquer les causes du licenciement dans la lettre de préavis. Est considéré abusif le licenciement intervenu sans l’existence d’une cause réelle et sérieuse le just
- `travailFr/s01/14-quater` [Le Président de la République Tunisienne HABIB BOU] Article 14 quater. (Ajouté par la loi n° 94-29 du 21 février 1994).- La faute grave est considérée comme l’une des causes réelles et sérieuses justifiant le licenciement. Peuvent être considérés comme fautes graves selon les circonstances dans lesquelles ont été commises notamment les cas suivants :
- `travailFr/s01/14-quinter` [Le Président de la République Tunisienne HABIB BOU] Article 14 quinter (Ajouté par la loi n° 94-29 du 21 février 1994).- Il appartient au juge d’apprécier l’existence du caractère réel et sérieux des causes du licenciement et le respect des procédures légales ou conventionnelles y afférentes, et ce, sur la base des éléments de preuve qui lui sont pré
- `travailFr/s01/16` [Le Président de la République Tunisienne HABIB BOU] Article 16.- La faillite de l’employeur n’est pas une cause de résiliation du contrat et la masse des créanciers est subrogée aux droits et obligations qui en résultent.
- `travailFr/s01/23` [Le Président de la République Tunisienne HABIB BOU] Article 23 (Modifié par la loi n° 94-29 du 21 février 1994).- La rupture abusive du contrat du travail par l’une des parties ouvre droit à des dommages-intérêts qui ne se confondent pas avec l’indemnité due pour inobservation du délai de préavis ou avec la gratification de fin de service visée à l’a
- `travailFr/s01/23-bis` [Le Président de la République Tunisienne HABIB BOU] Article 23 bis (Ajouté par la loi n° 94-29 du 21 février 1994).- En cas de licenciement abusif, le préjudice donne lieu à des dommages-intérêts dont le montant varie entre le salaire d’un mois et celui de deux mois pour chaque année d’ancienneté dans l’entreprise sans que ces dommages-intérêts ne dé

**Corpus candidates** (BM25 over travailFr.pdf; query terms: conditions licenciement)

-      `travailFr/s01/21-9` [Le Président de la République Tunisienne HABIB BOU] Article 21-9 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- La commission régionale ou la commission centrale de contrôle du licenciement examine le dossier du licenciement ou de la mise en chômage (6.5)
-      `travailFr/s01/21-13` [Le Président de la République Tunisienne HABIB BOU] Article 21-13 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Les travailleurs dont les contrats de travail auront été résiliés du fait de la suppression de leurs emplois pour des raisons économique (5.4)
-      `travailFr/s01/21-12` [Le Président de la République Tunisienne HABIB BOU] Article 21-12 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Sont abusifs, le licenciement ou la mise en chômage intervenus sans l’avis préalable de la commission régionale ou la commission central (5.0)
-      `travailFr/s01/42` [Le Président de la République Tunisienne HABIB BOU] Article 42.- Les conventions collectives visées à l’article précédent doivent au moins contenir des dispositions concernant : a) la liberté syndicale et la liberté d’opinion; b) les salaires applicabl (5.0)
- gold `travailFr/s01/14-ter` [Le Président de la République Tunisienne HABIB BOU] Article 14 ter. (Ajouté par la loi n° 94-29 du 21 février 1994).- L’employeur qui a l’intention de licencier un travailleur est tenu d’indiquer les causes du licenciement dans la lettre de préavis. Es (4.9)
-      `travailFr/s01/21-3` [Le Président de la République Tunisienne HABIB BOU] Article 21-3 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- L’inspection du travail territorialement compétente ou la Direction Générale de l’Inspection du Travail, selon le cas, doit procéder à un (4.8)
-      `travailFr/s01/21-7` [Le Président de la République Tunisienne HABIB BOU] Article 21-7 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- La commission régionale ou la commission centrale de contrôle du licenciement peut demander à l’employeur de lui fournir les informations (4.7)
-      `travailFr/s01/371` [Le Président de la République Tunisienne HABIB BOU] Article 371 .- Au cas de licenciement d'un ouvrier permanent, intervenu une fois la période d'essai expirée, pour quelque motif que ce soit, sauf celui de faute grave, insuffisance professionnelle ou  (4.6)

**Retrieved:** _hidden (test concept)_

**Suggested change:** Remove 16 (employer bankruptcy 'n'est pas une cause de résiliation': not a dismissal condition). Add 21 (the 21-x series on economic dismissal and the control commission). 14 (14 bis..quinquies: notice, grounds, serious fault, judge control) and 23 kept.

- add chunks: travailFr/s01/21, travailFr/s01/21-10, travailFr/s01/21-11, travailFr/s01/21-12, travailFr/s01/21-13, travailFr/s01/21-2, travailFr/s01/21-3, travailFr/s01/21-4, travailFr/s01/21-5, travailFr/s01/21-6, travailFr/s01/21-7, travailFr/s01/21-8, travailFr/s01/21-9
- drop chunks: travailFr/s01/16
- proposed gold:
    - article 14 `Article 14` → `travailFr/s01/14`, `travailFr/s01/14-bis`, `travailFr/s01/14-ter`, `travailFr/s01/14-quater`, `travailFr/s01/14-quinter`
        > Article 14.- (Modifié par la loi n° 94-29 du 21 février 1994). .- Le contrat de travail à durée déterminée prend fin par l’expiration de la durée conv
    - NEW article 21 `Article 21` → `travailFr/s01/21`, `travailFr/s01/21-2`, `travailFr/s01/21-3`, `travailFr/s01/21-4`, `travailFr/s01/21-5`, `travailFr/s01/21-6`, `travailFr/s01/21-7`, `travailFr/s01/21-8`, `travailFr/s01/21-9`, `travailFr/s01/21-10`, `travailFr/s01/21-11`, `travailFr/s01/21-12`, `travailFr/s01/21-13`
        > Article 21. (Modifié par la loi n° 96-62 du 15 juillet 1996).- Tout employeur qui a l’intention de licencier ou de mettre en chômage pour des raisons 
    - article 23 `Article 23` → `travailFr/s01/23`, `travailFr/s01/23-bis`
        > Article 23 (Modifié par la loi n° 94-29 du 21 février 1994).- La rupture abusive du contrat du travail par l’une des parties ouvre droit à des dommage

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## travail_paid_leave  (dev)

- `q023` [fr, travail, concept] Quelle est la durée du congé annuel payé ?
- `q057` [ar, travail, concept] ما هي مدة الإجازة السنوية المدفوعة؟
- `q080` [en, travail, concept] How many days of paid annual leave is a worker entitled to?

**Current gold** → chunks

- `travailFr/s01/112` [Le Président de la République Tunisienne HABIB BOU] Article 112.- Tout salarié a droit, chaque année, à un congé payé à la charge de l'employeur dans les conditions fixées ci-après.

**Corpus candidates** (BM25 over travailFr.pdf; query terms: durée congé annuel payé)

-      `travailFr/s01/125` [Le Président de la République Tunisienne HABIB BOU] Article 125.- Le congé annuel payé peut être fractionné en périodes d’un ou plusieurs jours jusqu’à concurrence de la moitié de sa durée totale. Sont réputés jours ouvrables pour la jouissance d’un co (17.1)
-      `travailFr/s01/94-5` [Le Président de la République Tunisienne HABIB BOU] Article 94-5 (Ajouté par la loi n°96-62 du 15 juillet 1996).- Le salaire du travailleur à temps partiel et les indemnités auxquelles a droit au titre du congé annuel payé, des jours fériés chômés et p (15.9)
-      `travailFr/s01/118` [Le Président de la République Tunisienne HABIB BOU] Article 118.- Le congé payé ne dépassant pas six jours ouvrables doit être continu. Le congé d'une durée supérieure à six jours ouvrables peut être fractionné par l'employeur, avec l'agrément du salar (14.0)
-      `travailFr/s01/133` [Le Président de la République Tunisienne HABIB BOU] Article 133.- Est considéré comme ne donnant pas le congé légal, l'employeur qui fait travailler un salarié, même en dehors de l'établissement où il travaille habituellement, pendant la période fixée  (13.5)
-      `travailFr/s01/128` [Le Président de la République Tunisienne HABIB BOU] Article 128.- Lorsque le contrat de travail d’un salarié, ayant au moins six mois de services continus dans la même entreprise, est résilié par le fait de l'employeur, avant que ledit salarié ait pu b (12.5)
-      `travailFr/s01/119` [Le Président de la République Tunisienne HABIB BOU] Article 119 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Le travailleur perçoit pendant son congé une indemnité calculée sur la base de la durée du congé à laquelle il a droit d'une part, et le  (12.1)
-      `travailFr/s01/130` [Le Président de la République Tunisienne HABIB BOU] Article 130.- Les employeurs doivent, en vue du contrôle de l'application du présent chapitre, tenir un registre portant leur nom et leur adresse où sont indiqués : 1) la période ordinaire des vacance (10.7)
-      `travailFr/s01/127` [Le Président de la République Tunisienne HABIB BOU] Article 127.- L’indemnité journalière versée au salarié au titre de congé payé est égale au salaire moyen journalier qu’il a ou aurait perçu pendant l’année, dans l’établissement, pour une période équ (9.7)

**Retrieved** (top-6, dev only)

- `q023` [fr]
    -   `travailFr/s01/125` Article 125.- Le congé annuel payé peut être fractionné en périodes d’un ou plusieurs jours jusqu’à concurrence de la moitié de sa durée totale. Sont 
    -   `travailFr/s01/114` Article 114 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Sont considérées comme un mois de travail effectif, pour la détermination de la durée d
    -   `travailFr/s01/113` Article 113 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Tout travailleur qui, au cours de l'année de référence, justifie avoir été occupé chez 
    -   `travailFr/s01/118` Article 118.- Le congé payé ne dépassant pas six jours ouvrables doit être continu. Le congé d'une durée supérieure à six jours ouvrables peut être fr
    -   `travailFr/s01/117` Article 117 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Le congé annuel est octroyé au cours de la période du 1er juin au 31 octobre de chaque 
    -   `travailFr/s01/123` Article 123 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Les travailleurs ont droit, à condition de compter au moins six mois de services contin
- `q057` [ar]
    -   `travailFr/s01/125` Article 125.- Le congé annuel payé peut être fractionné en périodes d’un ou plusieurs jours jusqu’à concurrence de la moitié de sa durée totale. Sont 
    -   `travailFr/s01/114` Article 114 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Sont considérées comme un mois de travail effectif, pour la détermination de la durée d
    -   `travailFr/s01/410` Article 410.- Les contrats ci-dessus définis doivent être écrits. Ils sont au choix des parties, soit d’une durée déterminée, soit d’une durée indéter
    -   `travailFr/s01/118` Article 118.- Le congé payé ne dépassant pas six jours ouvrables doit être continu. Le congé d'une durée supérieure à six jours ouvrables peut être fr
    -   `travailFr/s01/113` Article 113 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Tout travailleur qui, au cours de l'année de référence, justifie avoir été occupé chez 
    -   `travailFr/s01/117` Article 117 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Le congé annuel est octroyé au cours de la période du 1er juin au 31 octobre de chaque 
- `q080` [en]
    -   `travailFr/s01/123` Article 123 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Les travailleurs ont droit, à condition de compter au moins six mois de services contin
    -   `travailFr/s01/113` Article 113 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Tout travailleur qui, au cours de l'année de référence, justifie avoir été occupé chez 
    -   `travailFr/s01/118` Article 118.- Le congé payé ne dépassant pas six jours ouvrables doit être continu. Le congé d'une durée supérieure à six jours ouvrables peut être fr
    -   `travailFr/s01/114` Article 114 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Sont considérées comme un mois de travail effectif, pour la détermination de la durée d
    -   `travailFr/s01/125` Article 125.- Le congé annuel payé peut être fractionné en périodes d’un ou plusieurs jours jusqu’à concurrence de la moitié de sa durée totale. Sont 
    -   `travailFr/s01/128` Article 128.- Lorsque le contrat de travail d’un salarié, ayant au moins six mois de services continus dans la même entreprise, est résilié par le fai

**Suggested change:** Add 113 (right acquired per month of work, i.e. the duration) and 115 (extra day per 5 years of service). 112 only states the right.

- add chunks: travailFr/s01/113, travailFr/s01/115
- drop chunks: none
- proposed gold:
    - article 112 `Article 112` → `travailFr/s01/112`
        > Article 112.- Tout salarié a droit, chaque année, à un congé payé à la charge de l'employeur dans les conditions fixées ci-après.
    - NEW article 113 `Article 113` → `travailFr/s01/113`
        > Article 113 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Tout travailleur qui, au cours de l'année de référence, justifie avoir été occupé chez 
    - NEW article 115 `Article 115` → `travailFr/s01/115`
        > Article 115(1).- La durée du congé ainsi fixée est augmentée à raison d'un jour ouvrable par période entière, continue ou non, de cinq ans de services

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## travail_fixed_term  (test)

- `q024` [fr, travail, concept] Qu'est-ce que le contrat de travail à durée déterminée ?

**Current gold** → chunks

- `travailFr/s01/6` [Le Président de la République Tunisienne HABIB BOU] Article 6 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Le contrat de travail est une convention par laquelle l’une des parties appelée travailleur ou salarié s’engage à fournir à l’autre partie appelée employeur ses services personnels sous la direction et le contrôle de celle-ci moyennant une
- `travailFr/s01/6-2` [Le Président de la République Tunisienne HABIB BOU] Article 6-2 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Le contrat de travail est conclu pour une durée indéterminée ou pour une durée déterminée. Le contrat de travail à durée déterminée peut comporter une limitation de la durée de son exécution ou l’indication du travail dont l’accomplisseme
- `travailFr/s01/6-3` [Le Président de la République Tunisienne HABIB BOU] Article 6-3 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Les travailleurs recrutés par contrats de travail à durée indéterminée sont soumis en ce qui concerne la période d’essai et la confirmation aux dispositions légales ou contractuelles qui leur sont applicables.
- `travailFr/s01/6-4` [Le Président de la République Tunisienne HABIB BOU] Article 6-4 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- 1- Le contrat de travail à durée déterminée peut être conclu dans les cas suivants : - l’accomplissement de travaux de premier établissement ou de travaux neufs; - l’accomplissement de travaux nécessités par un surcroît extraordinaire de 

**Corpus candidates** (BM25 over travailFr.pdf; query terms: contrat travail durée déterminée)

- gold `travailFr/s01/6-2` [Le Président de la République Tunisienne HABIB BOU] Article 6-2 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Le contrat de travail est conclu pour une durée indéterminée ou pour une durée déterminée. Le contrat de travail à durée déterminée peut c (12.8)
-      `travailFr/s01/14` [Le Président de la République Tunisienne HABIB BOU] Article 14.- (Modifié par la loi n° 94-29 du 21 février 1994). .- Le contrat de travail à durée déterminée prend fin par l’expiration de la durée convenue ou par l’accomplissement du travail objet du  (10.9)
-      `travailFr/s01/24` [Le Président de la République Tunisienne HABIB BOU] Article 24 (Modifié par la loi n° 94-29 du 21 février 1994).- Les dommages-intérêts dus pour rupture abusive du contrat de travail à durée déterminée du fait de l’employeur sont fixés à un montant éga (10.6)
-      `travailFr/s01/94-2` [Le Président de la République Tunisienne HABIB BOU] Article 94-2 (Ajouté par la loi n°96-62 du 15 juillet 1996).- Le contrat de travail à durée déterminée ou indéterminée peut être conclu pour un travail à temps partiel. Est considéré comme travail à t (9.9)
- gold `travailFr/s01/6-4` [Le Président de la République Tunisienne HABIB BOU] Article 6-4 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- 1- Le contrat de travail à durée déterminée peut être conclu dans les cas suivants : - l’accomplissement de travaux de premier établisseme (9.6)
-      `travailFr/s01/132` [Le Président de la République Tunisienne HABIB BOU] Article 132.- Lorsqu'un contrat de travail est conclu pour une durée déterminée, l'employeur doit, sou peine de dommages-intérêts, faire bénéficier le salarié de son congé dans des conditions telles q (9.4)
-      `travailFr/s01/413` [Le Président de la République Tunisienne HABIB BOU] Article 413.- En cas de résiliation d'un contrat fait sans détermination de durée par le fait de l'employeur et lorsque cette résiliation n'est pas provoquée par une faute du voyageur, représentant ou (9.0)
-      `travailFr/s01/32` [Le Président de la République Tunisienne HABIB BOU] Article 32.- La convention collective de travail peut être conclue, soit pour une durée indéterminée, soit pour une durée déterminée ne pouvant excéder cinq ans. A défaut de stipulation contraire, la  (8.7)

**Retrieved:** _hidden (test concept)_

**Suggested change:** Narrow to the CDD articles 6-2 (CDI or CDD, limitation of duration) and 6-4 (cases where a CDD may be concluded); plain 'Article 6' is the general contract definition.

- add chunks: none
- drop chunks: travailFr/s01/6, travailFr/s01/6-3
- proposed gold:
    - article 6 `Article 6-2` → `travailFr/s01/6-2`
        > Article 6-2 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Le contrat de travail est conclu pour une durée indéterminée ou pour une durée déterminé
    - article 6 `Article 6-4` → `travailFr/s01/6-4`
        > Article 6-4 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- 1- Le contrat de travail à durée déterminée peut être conclu dans les cas suivants : - l

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## travail_maternity  (dev)

- `q025` [fr, travail, concept] Quels sont les droits de la femme enceinte au travail ?

**Current gold** → chunks

- `travailFr/s01/64` [Le Président de la République Tunisienne HABIB BOU] Article 64.- Dans les entreprises de toute nature, à l’exception des établissements où sont exclusivement employés les membres d’une même famille, la femme : a) aura droit à l’occasion de son accouchement, sur production d’un certificat médical, à un congé de repos de 30 jours. Ce congé peut être pr

**Corpus candidates** (BM25 over travailFr.pdf; query terms: droits femme enceinte travail)

-      `travailFr/s01/20` [Le Président de la République Tunisienne HABIB BOU] Article 20.- La maladie suspend le contrat de travail. Elle ne constitue un motif de rupture que si elle est suffisamment grave ou prolongée et si les nécessités de l’entreprise obligent l’employeur à (6.9)
-      `travailFr/s01/5-bis` [Le Président de la République Tunisienne HABIB BOU] Article 5 bis ( Ajouté par la loi n° 93-66 du 5 juillet 1993).- Il ne peut être fait de discrimination entre l’homme et la femme dans l’application des dispositions du présent code et des textes pris  (5.8)
-      `travailFr/s01/68-3` [Le Président de la République Tunisienne HABIB BOU] Article 68-3 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Il est interdit d’appliquer les dispositions de l’article 68-2 à la femme travailleuse pendant une période de seize semaines au minimum a (5.3)
-      `travailFr/s01/263` [Le Président de la République Tunisienne HABIB BOU] Article 263 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Le travailleur étranger bénéficie des mêmes droits et est soumis aux mêmes obligations résultant des relations du travail et applicables  (4.9)
-      `travailFr/s01/16` [Le Président de la République Tunisienne HABIB BOU] Article 16.- La faillite de l’employeur n’est pas une cause de résiliation du contrat et la masse des créanciers est subrogée aux droits et obligations qui en résultent. (4.9)
-      `travailFr/s01/249` [Le Président de la République Tunisienne HABIB BOU] Article 249.- Il n'est dérogé en aucune façon aux dispositions spéciales qui auraient accordé aux syndicats des droits non visés dans le présent chapitre. (4.8)
-      `travailFr/s01/386-ter` [Le Président de la République Tunisienne HABIB BOU] Article 386 - ter (Ajouté par la loi n°94-29 du 21 février 1994).- Sont exonérées des droits de timbre et d'enregistrement toutes les formalités accomplies et exigées par la procédure d'arbitrage ains (4.6)
-      `travailFr/s01/195` [Le Président de la République Tunisienne HABIB BOU] Article 195.- Le montant des indemnités et droits alloués aux conseillers et témoins des conseils de prud'hommes ainsi que l'imputation et le mode de règlement des dépenses de fonctionnement de ces ju (4.5)

**Retrieved** (top-6, dev only)

- `q025` [fr]
    - ✓ `travailFr/s01/64` Article 64.- Dans les entreprises de toute nature, à l’exception des établissements où sont exclusivement employés les membres d’une même famille, la 
    -   `travailFr/s01/68-2` Article 68-2 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- L’intervalle de nuit pendant lequel les femmes ne peuvent être employées prévu par l’ar
    -   `travailFr/s01/68-3` Article 68-3 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Il est interdit d’appliquer les dispositions de l’article 68-2 à la femme travailleuse 
    -   `travailFr/s01/18` Article 18.- Dans tout contrat de travail, la durée de la période d’essai résulte des conventions collectives ou particulières, de l’usage ou de la lo
    -   `travailFr/s01/20` Article 20.- La maladie suspend le contrat de travail. Elle ne constitue un motif de rupture que si elle est suffisamment grave ou prolongée et si les
    -   `travailFr/s01/166` Article 166 (Modifié par la loi n° 94-29 du 21 février 1994 et par la loi n° 2007-19 du 2 avril 2007).- Tout licenciement d’un membre titulaire ou sup

**Suggested change:** No change; anchored (two fragment chunks also carry number 64).

- add chunks: none
- drop chunks: none
- proposed gold:
    - article 64 `Article 64.- Dans les entreprises` → `travailFr/s01/64`
        > Article 64.- Dans les entreprises de toute nature, à l’exception des établissements où sont exclusivement employés les membres d’une même famille, la 

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## csp_marriage_conditions  (dev)

- `q026` [fr, statut_personnel, concept] Quelles sont les conditions du mariage ?
- `q059` [ar, statut_personnel, concept] ما هي شروط الزواج؟
- `q067` [ar, unfiltered, cross_domain] ما هي شروط الزواج؟
- `q073` [en, statut_personnel, concept] What are the conditions for marriage?

**Current gold** → chunks

- `Statutpersonnel/s01/5` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 5 (Modifié par le décret-loi n°64-1 du 20 février 1964, ratifié par la loi n°64-1 du 21 avril 1964 et par la loi n°2007-32 du 14 mai 2007).- Les deux futurs époux ne doivent pas se trouver dans l'un des cas d'empêchements prévus par la loi. En outre, chacun des deux futurs époux n’ayant pas 
- `Statutpersonnel/s02/5` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article 5 .- L'officier de l'état civil donnera lecture des actes aux parties comparantes et aux témoins. Il y sera fait mention de l'accomplissement de cette formalité.
- `Statutpersonnel/s05/5` [ANNEXE : (NDLR) L’annexe du présent arrêté compren] Article 5 .- Le Premier ministre, ministre de l'intérieur, les gouverneurs, les délégués et les présidents des communes sont chargés, chacun en ce qui le concerne, de l'exécution du présent décret qui sera publié au Journal Officiel de la République Tunisienne. Fait à Tunis, le 22 janvier 1986. P/le
- `Statutpersonnel/s07/5` [Loi n°98-94 du 9 novembre 1998, relative au régime] Article 5 .- La procuration en vue du mariage n'est valable que pour autant qu'elle exprime l’option expresse du mandant relative à l'adhésion ou la non adhésion au régime de la communauté des biens.
- `Statutpersonnel/s08/5` [Loi n°64-46 du 3 novembre 1964 (29 joumada II 1384] Article 5 .- Dans les cas exceptionnels, le juge peut dispenser les futurs époux, ou l'un d'eux seulement, de la remise du certificat médical. Le certificat n'est exigible d'aucun des futurs époux au cas du péril imminent de mort de l'un d'eux.
- `Statutpersonnel/s11/5` [Loi n°58-27 du 4 mars 1958 (12 Chaabane 1377) rela] Article 5 .- Le tuteur officieux a, vis-à-vis du pupille, les droits et obligations prévus par les articles 54 et suivant du code du statut personnel. Il est, en outre, civilement responsable des actes du pupille, dans les mêmes conditions que les père et mère.
- `Statutpersonnel/s12/5` [Décret du 18 juillet 1957 (20 dhoul hidja 1376), s] Article 5 .- Aussitôt cette transcription effectuée, le tuteur testamentaire administre les biens du mineur. A défaut du tuteur testamentaire, le juge des tutelles, visé à l'article 11, saisi par le commissaire du gouvernement(*), désigne, comme tuteur du mineur, le tuteur provisoire ou une autre pe
- `Statutpersonnel/s13/5` [Loi n°98-75 du 28 octobre 1998, relative à l'attri] Article 5 .- Les règles relatives aux empêchements au mariage prévues par les articles 14, 15, 16 et 17 du code du statut personnel, lorsque la paternité est prouvée, sont applicables aux enfants abandonnés ou dont la filiation est inconnue auxquels on a attribué un nom patronymique en vertu de la p
- `Statutpersonnel/s14/5` [Loi n°93-65 du 5 juillet 1993, portant création d'] Article 5 .- Le montant de la pension alimentaire ou de la rente de divorce, due en vertu d'un jugement, qui n'a pas été payé par la partie débitrice au fonds de garantie de la pension alimentaire et de la rente de divorce, est majoré d'une indemnité de retard qui sera versée par le débiteur à ce fo
- `Statutpersonnel/s15/5` [Décret n°93-1655 du 9 août 1993, relatif à la proc] Article 5 .- A l’expiration du délai fixé par l’article 4 ci-dessus, la caisse nationale de sécurité sociale établit à l’encontre du débiteur une contrainte rendue exécutoire par le ministre des affaires sociales.
- `Statutpersonnel/s01/8` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 8 .- Consent au mariage du mineur le plus proche parent agnat. Il doit être saint d'esprit, de sexe masculin, majeur. Le père ou son mandataire consent au mariage de son enfant mineur, qu'il soit de sexe masculin ou féminin. S'il n’y a point de tuteur, le consentement est donné par le juge.
- `Statutpersonnel/s02/8` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article 8 .- Les actes de l'état civil seront inscrits sur des registres tenus en double.
- `Statutpersonnel/s07/8` [Loi n°98-94 du 9 novembre 1998, relative au régime] Article 8 .- L'accord sur la communauté des biens, postérieur à la conclusion du contrat de mariage, doit être constaté par acte authentique. L'officier public ayant rédigé l'acte doit se conformer aux dispositions du paragraphe 2 de l'article 7 de cette loi.
- `Statutpersonnel/s11/8` [Loi n°58-27 du 4 mars 1958 (12 Chaabane 1377) rela] Article 8 .- L'adoption est permise dans les conditions prévues aux articles suivants.
- `Statutpersonnel/s12/8` [Décret du 18 juillet 1957 (20 dhoul hidja 1376), s] Article 8 .- Lorsqu'à la suite de reddition de comptes de gestion d'un tuteur testamentaire ou autre, le commissaire du gouvernement(*) constate que des deniers appartenant aux mineurs sont disponibles, il en ordonne le versement immédiat à la caisse des dépôts et consignations, au compte courant de
- `Statutpersonnel/s14/8` [Loi n°93-65 du 5 juillet 1993, portant création d'] Article 8 .- La caisse Nationale de Sécurité Sociale est en droit de prendre toutes les mesures et d'introduire toute action en justice susceptibles de protéger les droits du fonds de garantie de la pension alimentaire et de la rente de divorce. Elle est convoquée obligatoirement dans tous les cas o
- `Statutpersonnel/s15/8` [Décret n°93-1655 du 9 août 1993, relatif à la proc] Article 8 .- Quiconque a indûment bénéficié des sommes d’argent du fonds de garantie de la pension alimentaire et de la rente de divorce doit les restituer sans délai. La caisse nationale de sécurité sociale peut se faire rembourser lesdites sommes par voie de contraintes selon la procédure de rembo
- `Statutpersonnel/s01/14` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 14 .- Les empêchements au mariage sont de deux sortes : permanents et provisoires. Les empêchements permanents résultent de la parenté, de l'alliance, de l'allaitement ou du triple divorce. Les empêchements provisoires résultent de l'existence d'un mariage non dissous et de la non-expiration
- `Statutpersonnel/s07/14` [Loi n°98-94 du 9 novembre 1998, relative au régime] Article 14 .- Lorsque les deux époux choisissent le régime de la communauté des biens, l'officier de l'état civil doit le mentionner dans ses registres et dans tous extrait et copie. Si l'accord des époux stipule une condition contraire aux dispositions de cette loi, l'officier de l'état civil doit 
- `Statutpersonnel/s11/14` [Loi n°58-27 du 4 mars 1958 (12 Chaabane 1377) rela] Article 14 .- L'adopté prend le nom de l’adoptant. Il peut changer de prénom, mention en sera faite dans le jugement d'adoption à la demande de l'adoptant.
- `Statutpersonnel/s12/14` [Décret du 18 juillet 1957 (20 dhoul hidja 1376), s] Article 14 .- Le tuteur doit administrer les biens de ses pupilles susvisés, conformément à la loi, et en bon père de famille. Il doit tenir un registre sur lequel il fait inscrire, par les soins de deux notaires, toutes les recettes et dépenses effectuées par lui.

**Corpus candidates** (BM25 over Statutpersonnel.pdf; query terms: conditions mariage)

-      `Statutpersonnel/s01/4` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 4 .- La preuve du mariage ne peut être rapportée que par un acte authentique dans des conditions fixées par une loi ultérieure. En ce qui concerne les mariages célébrés à l'étranger, la preuve (6.5)
-      `Statutpersonnel/s02/1` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article premier.- La présente loi règle : 1°) les conditions dans lesquelles seront déclarés les naissances et décès, 2°) l'établissement et la transcription des actes de mariage ainsi que le transcri (5.6)
-      `Statutpersonnel/s08/1` [Loi n°64-46 du 3 novembre 1964 (29 joumada II 1384] Article premier.- L'officier de l'état civil ou les notaires, choisis pour l'établissement de l'acte de mariage, ne peuvent procéder à la célébration du mariage, qu'après la remise par chacun des futu (4.9)
- gold `Statutpersonnel/s11/8` [Loi n°58-27 du 4 mars 1958 (12 Chaabane 1377) rela] Article 8 .- L'adoption est permise dans les conditions prévues aux articles suivants. (4.7)
-      `Statutpersonnel/s11/9` [Loi n°58-27 du 4 mars 1958 (12 Chaabane 1377) rela] Article 9. (Modifié par la loi n°59-69 du 19 juin 1959).- L'adoptant doit être une personne majeure de l'un ou l'autre sexe, mariée, jouissant de la pleine capacité civile. Il doit être de bonne moral (4.1)
-      `Statutpersonnel/s07/13` [Loi n°98-94 du 9 novembre 1998, relative au régime] Article 13 .- Sont communes, les dettes et les charges découlant de l'acquisition de la propriété du bien commun, de son exploitation, administration, usage ou de la disposition de ce bien. Sont égale (4.0)
- gold `Statutpersonnel/s11/5` [Loi n°58-27 du 4 mars 1958 (12 Chaabane 1377) rela] Article 5 .- Le tuteur officieux a, vis-à-vis du pupille, les droits et obligations prévus par les articles 54 et suivant du code du statut personnel. Il est, en outre, civilement responsable des acte (3.7)
-      `Statutpersonnel/s01/27` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 27 .- Lorsqu'un des époux prédécède et qu'une contestation s'élève entre le conjoint survivant et les héritiers du prédécédé au sujet de la propriété des biens se trouvant au domicile conjugal (3.6)

**Retrieved** (top-6, dev only)

- `q026` [fr]
    -   `Statutpersonnel/s02/31` Article 31 .- L'acte de mariage est conclu en Tunisie devant deux notaires ou devant l'Officier de l'état civil en présence de deux témoins honorables
    -   `Statutpersonnel/s02/37` Article 37 .- Tout acte de mariage des Tunisiens, conclu à l'étranger selon les formes locales, devra être transcrit, dans les trois mois de sa rédact
    -   `Statutpersonnel/s02/38` Article 38 .- L'acte de mariage des Etrangers en Tunisie sera rédigé conformément aux lois tunisiennes, sur le vu d'un certificat de leur consul attes
    -   `Statutpersonnel/s11/10` Article 10 .- La différence d'âge entre l'adoptant et l'adopté doit être au minimum de 15 ans, sauf dans les cas ou l'adopté est l'enfant du conjoint 
    -   `Statutpersonnel/s08/7` Article 7 .- L'officier de l'état civil et les notaires qui ne se conformeront pas aux prescriptions de l'article premier de la présente loi seront po
    -   `Statutpersonnel/s03/3` Article 3 .- La demande d'acquisition de l'attestation de conformité est déposée auprès du greffe du tribunal cantonal compétent sur papier libre acco
- `q059` [ar]
    -   `Statutpersonnel/s02/31` Article 31 .- L'acte de mariage est conclu en Tunisie devant deux notaires ou devant l'Officier de l'état civil en présence de deux témoins honorables
    -   `Statutpersonnel/s02/37` Article 37 .- Tout acte de mariage des Tunisiens, conclu à l'étranger selon les formes locales, devra être transcrit, dans les trois mois de sa rédact
    -   `Statutpersonnel/s02/38` Article 38 .- L'acte de mariage des Etrangers en Tunisie sera rédigé conformément aux lois tunisiennes, sur le vu d'un certificat de leur consul attes
    -   `Statutpersonnel/s11/10` Article 10 .- La différence d'âge entre l'adoptant et l'adopté doit être au minimum de 15 ans, sauf dans les cas ou l'adopté est l'enfant du conjoint 
    -   `Statutpersonnel/s06/2` Article 2 .- Le ministre de l'intérieur est chargé de l'exécution du présent arrêté qui sera publié au Journal Officiel de la République Tunisienne. T
    -   `Statutpersonnel/s08/7` Article 7 .- L'officier de l'état civil et les notaires qui ne se conformeront pas aux prescriptions de l'article premier de la présente loi seront po
- `q067` [ar]
    -   `Statutpersonnel/s02/31` Article 31 .- L'acte de mariage est conclu en Tunisie devant deux notaires ou devant l'Officier de l'état civil en présence de deux témoins honorables
    -   `tun_RecAcFreeLi/s00/4` Art. 4 – La Tunisie est un Etat unitaire. Il n’est pas permis d’édicter toute législation portant atteinte à son unité.
    -   `Statutpersonnel/s02/37` Article 37 .- Tout acte de mariage des Tunisiens, conclu à l'étranger selon les formes locales, devra être transcrit, dans les trois mois de sa rédact
    -   `Statutpersonnel/s02/38` Article 38 .- L'acte de mariage des Etrangers en Tunisie sera rédigé conformément aux lois tunisiennes, sur le vu d'un certificat de leur consul attes
    -   `NationaliteFr/s01/13` Article 13.- La femme étrangère qui épouse un tunisien acquiert la nationalité tunisienne au moment de la célébration du mariage, lorsque, en vertu de
    -   `tun_RecAcFreeLi/s00/59` Art. 59 – Est électeur tout citoyen ou citoyenne de nationalité tunisienne, âgé de dix-huit ans révolus et remplissant les conditions fixées par la lo
- `q073` [en]
    -   `Statutpersonnel/s11/9` Article 9. (Modifié par la loi n°59-69 du 19 juin 1959).- L'adoptant doit être une personne majeure de l'un ou l'autre sexe, mariée, jouissant de la p
    -   `Statutpersonnel/s01/58` Article 58 (Modifié par la loi n°81-7 du 18 février 1981).- Le titulaire du droit de garde doit être majeur, sain d'esprit, honnête, capable de pourvo
    -   `Statutpersonnel/s15/9` Article 9 .- Les ministres de la justice et des affaires sociales sont chargés, chacun en ce qui le concerne, de l’exécution du présent décret qui ser
    - ✓ `Statutpersonnel/s01/8` Article 8 .- Consent au mariage du mineur le plus proche parent agnat. Il doit être saint d'esprit, de sexe masculin, majeur. Le père ou son mandatair
    -   `Statutpersonnel/s01/118` Article 118.- En cas d’égalité dans la classe et le degré et lorsque la parenté est plus ou moins proche, le lien de parenté le plus fort l’emporte su
    -   `Statutpersonnel/s11/10` Article 10 .- La différence d'âge entre l'adoptant et l'adopté doit être au minimum de 15 ans, sauf dans les cas ou l'adopté est l'enfant du conjoint 

**Suggested change:** Statutpersonnel.pdf bundles the CSP with état-civil, adoption, tutelle... laws, so 'Article 5/8/14' have 13/9/6 chunks. Anchors select the CSP articles. Add 3 (consentement des deux époux) and 6 (consentement du tuteur pour le mineur). Optional candidates not added: 7 (prodigue), 15-17 (empêchements).

- add chunks: Statutpersonnel/s01/3, Statutpersonnel/s01/6
- drop chunks: Statutpersonnel/s02/5, Statutpersonnel/s02/8, Statutpersonnel/s05/5, Statutpersonnel/s07/14, Statutpersonnel/s07/5, Statutpersonnel/s07/8, Statutpersonnel/s08/5, Statutpersonnel/s11/14, Statutpersonnel/s11/5, Statutpersonnel/s11/8, Statutpersonnel/s12/14, Statutpersonnel/s12/5, Statutpersonnel/s12/8, Statutpersonnel/s13/5, Statutpersonnel/s14/5, Statutpersonnel/s14/8, Statutpersonnel/s15/5, Statutpersonnel/s15/8
- proposed gold:
    - NEW article 3 `Article 3 .- Le mariage n'est formé` → `Statutpersonnel/s01/3`
        > Article 3 .- Le mariage n'est formé que par le consentement des deux époux. La présence de deux témoins honorables et la fixation d'une dot au profit 
    - article 5 `Article 5 (Modifié par le décret-loi n°64-1` → `Statutpersonnel/s01/5`
        > Article 5 (Modifié par le décret-loi n°64-1 du 20 février 1964, ratifié par la loi n°64-1 du 21 avril 1964 et par la loi n°2007-32 du 14 mai 2007).- L
    - NEW article 6 `Article 6 (Modifié par la loi n°93-74 du 12 juillet 1993).- Le mariage du mineur` → `Statutpersonnel/s01/6`
        > Article 6 (Modifié par la loi n°93-74 du 12 juillet 1993).- Le mariage du mineur est subordonné au consentement de son tuteur et de sa mère. En cas de
    - article 8 `Article 8 .- Consent au mariage du mineur` → `Statutpersonnel/s01/8`
        > Article 8 .- Consent au mariage du mineur le plus proche parent agnat. Il doit être saint d'esprit, de sexe masculin, majeur. Le père ou son mandatair
    - article 14 `Article 14 .- Les empêchements au mariage` → `Statutpersonnel/s01/14`
        > Article 14 .- Les empêchements au mariage sont de deux sortes : permanents et provisoires. Les empêchements permanents résultent de la parenté, de l'a

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## csp_divorce  (test)

- `q027` [fr, statut_personnel, concept] Comment se déroule le divorce ?
- `q042` [fr, unfiltered, cross_domain] Quelles sont les causes de divorce ?
- `q061` [ar, statut_personnel, concept] كيف يتم الطلاق؟
- `q087` [en, unfiltered, cross_domain] What are the grounds for divorce?

**Current gold** → chunks

- `Statutpersonnel/s01/29` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 29 .- Le divorce est la dissolution du mariage.
- `Statutpersonnel/s02/29` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article 29 .- Au premier port où le bâtiment abordera, pour toute autre cause que celle que son désarmement, l'officier instrumentaire sera tenu de déposer deux expéditions de chacun des actes de naissance dressés à bord, dans un port tunisien, au Bureau de l'Autorité Maritime, et, dans un port étra
- `Statutpersonnel/s01/30` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 30 .- Le divorce ne peut avoir lieu que par-devant le Tribunal.
- `Statutpersonnel/s02/30` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article 30 .- A l'arrivée du bâtiment dans le port de désarmement, l'officier instrumentaire sera tenu de déposer, en même temps que le rôle d'équipage, une expédition de chacun des actes de naissance dressés à bord dont copie n'aurait point été déjà déposée conformément aux prescriptions de l'artic
- `Statutpersonnel/s01/31` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 31. (Modifié par la loi n°81-7 du 18 février 1981).- Le Tribunal prononce le divorce : 1) en cas de consentement mutuel des époux, 2) à la demande de l'un des époux en raison du préjudice qu'il a subi, 3) à la demande du mari ou de la femme. Il est statué sur la réparation du préjudice matér
- `Statutpersonnel/s02/31` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article 31 .- L'acte de mariage est conclu en Tunisie devant deux notaires ou devant l'Officier de l'état civil en présence de deux témoins honorables. Le mariage des Tunisiens à l'étranger est célébré devant les agents diplomatiques ou consulaires de Tunisie, ou selon la loi locale.

**Corpus candidates** (BM25 over Statutpersonnel.pdf; query terms: déroule divorce)

-      `Statutpersonnel/s12/11` [Décret du 18 juillet 1957 (20 dhoul hidja 1376), s] Article 11 .- Les fonctions de juge des tutelles sont assurées au tribunal de première instance de Tunis par un magistrat ayant le grade de vice-président de cette juridiction. Dans les autres tribuna (3.8)
-      `Statutpersonnel/s15/2` [Décret n°93-1655 du 9 août 1993, relatif à la proc] Article 2(Modifié par le décret n°2006-826 du 23 mars 2006).- Les demandes d’obtention de la pension alimentaire ou de la rente de divorce doivent être accompagnées des pièces suivantes : - une copie  (3.8)
-      `Statutpersonnel/s14/6` [Loi n°93-65 du 5 juillet 1993, portant création d'] Article 6 .- Les montants de la pension alimentaire ou de la rente de divorce payés par le fonds de garantie de la pension alimentaire et de la rente de divorce sont majorés de 5% à titre de frais de  (3.7)
- gold `Statutpersonnel/s01/29` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 29 .- Le divorce est la dissolution du mariage. (3.6)
- gold `Statutpersonnel/s01/30` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 30 .- Le divorce ne peut avoir lieu que par-devant le Tribunal. (3.5)
-      `Statutpersonnel/s01/39` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 39 .- Le mari indigent ne doit pas d'aliments. Cependant, si, à l'expiration d'un délai de deux mois accordé par le juge, il ne peut exécuter cette obligation, le juge prononcera le divorce. T (3.3)
-      `Statutpersonnel/s14/3` [Loi n°93-65 du 5 juillet 1993, portant création d'] Article 3 .- Le fonds de garantie de la pension alimentaire et de la rente de divorce est subrogé aux ayants-droit de la pension alimentaire ou de la rente de divorce dans leurs droits vis-à-vis de la (3.3)
-      `Statutpersonnel/s15/6` [Décret n°93-1655 du 9 août 1993, relatif à la proc] Article 6 .- Les bénéficiaires de la pension alimentaire ou de la rente de divorce du fonds de garantie de la pension alimentaire et de la rente de divorce sont tenus de présenter au bureau régional d (3.2)

**Retrieved:** _hidden (test concept)_

**Suggested change:** Anchor 29/30/31 to the CSP divorce articles (other chunks numbered 29/30/31 are ship registers and civil-status acts). Add 32 (procedure before the tribunal).

- add chunks: Statutpersonnel/s01/32
- drop chunks: Statutpersonnel/s02/29, Statutpersonnel/s02/30, Statutpersonnel/s02/31
- proposed gold:
    - article 29 `Article 29 .- Le divorce est la dissolution` → `Statutpersonnel/s01/29`
        > Article 29 .- Le divorce est la dissolution du mariage.
    - article 30 `Article 30 .- Le divorce ne peut avoir lieu` → `Statutpersonnel/s01/30`
        > Article 30 .- Le divorce ne peut avoir lieu que par-devant le Tribunal.
    - article 31 `Article 31. (Modifié par la loi n°81-7` → `Statutpersonnel/s01/31`
        > Article 31. (Modifié par la loi n°81-7 du 18 février 1981).- Le Tribunal prononce le divorce : 1) en cas de consentement mutuel des époux, 2) à la dem
    - NEW article 32 `Article 32 (Modifié par la loi n°2010-50` → `Statutpersonnel/s01/32`
        > Article 32 (Modifié par la loi n°2010-50 du 1er novembre 2010).- Le président du tribunal choisit le juge de la famille parmi ses vice-présidents. Le 

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## csp_polygamy  (test)

- `q028` [fr, statut_personnel, concept] La polygamie est-elle autorisée ?
- `q045` [fr, statut_personnel, colloquial] Mon mari peut-il se remarier ?
- `q060` [ar, statut_personnel, concept] هل يجوز تعدد الزوجات؟
- `q074` [en, statut_personnel, concept] Is polygamy allowed?

**Current gold** → chunks

- `Statutpersonnel/s01/18` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 18 (Modifié par la loi n°58-70 du 4 juillet 1958 et les alinéas 3, 4 et 5 ajoutés par le décret-loi n°64-1 du 20 février 1964, ratifié par la loi n°64-1 du 21 avril 1964).- La polygamie est interdite. Quiconque, étant engagé dans les liens du mariage, en aura contracté un autre avant la diss
- `Statutpersonnel/s02/18` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article 18 .- Toute contravention aux articles précédents de la part des fonctionnaires y dénommés sera poursuivie devant le Tribunal de Première Instance de la circonscription et punie d'une amende qui ne pourra excéder dix mille francs.
- `Statutpersonnel/s07/18` [Loi n°98-94 du 9 novembre 1998, relative au régime] Article 18 .- La communauté des biens est dissoute par : - Le décès de l'un des deux époux - Le divorce - La disparition de l'un d'eux - La séparation judiciaire de leurs biens - L'accord des deux parties.
- `Statutpersonnel/s12/18` [Décret du 18 juillet 1957 (20 dhoul hidja 1376), s] Article 18 .- Les dispositions du présent décret s'appliquent aux tuteurs quels que soient la cause et le mode de leur désignation.

**Corpus candidates** (BM25 over Statutpersonnel.pdf; query terms: polygamie autorisée)

- gold `Statutpersonnel/s01/18` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 18 (Modifié par la loi n°58-70 du 4 juillet 1958 et les alinéas 3, 4 et 5 ajoutés par le décret-loi n°64-1 du 20 février 1964, ratifié par la loi n°64-1 du 21 avril 1964).- La polygamie est in (3.8)

**Retrieved:** _hidden (test concept)_

**Suggested change:** No change; anchored to the CSP Art 18 (4 other chunks are numbered 18).

- add chunks: none
- drop chunks: Statutpersonnel/s02/18, Statutpersonnel/s07/18, Statutpersonnel/s12/18
- proposed gold:
    - article 18 `Article 18 (Modifié par la loi n°58-70` → `Statutpersonnel/s01/18`
        > Article 18 (Modifié par la loi n°58-70 du 4 juillet 1958 et les alinéas 3, 4 et 5 ajoutés par le décret-loi n°64-1 du 20 février 1964, ratifié par la 

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## csp_child_custody  (dev)

- `q029` [fr, statut_personnel, concept] Comment est attribuée la garde des enfants ?
- `q062` [ar, statut_personnel, concept] من يحق له حضانة الأطفال؟
- `q075` [en, statut_personnel, concept] Who gets custody of the children after divorce?

**Current gold** → chunks

- `Statutpersonnel/s01/54` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 54 .- La garde consiste à élever l'enfant et à assurer sa protection dans sa demeure.
- `Statutpersonnel/s02/54` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article 54 .- Lorsqu'un Tunisien aura disparu en Tunisie ou hors de Tunisie, dans des circonstances de nature à mettre sa vie en danger, et que sa mort n'aura pu être constatée, un procès-verbal de disparition sera établi par : 1°) le Secrétaire d'Etat à la Défense Nationale à l'égard des militaires
- `Statutpersonnel/s01/55` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 55 .- La femme qui refuse d'assurer la garde de l'enfant n'y sera obligée que lorsque aucune autre personne ne pourra lui être substituée.
- `Statutpersonnel/s02/55` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article 55 .- Les procès-verbaux, visés à l'article précédent, seront transmis, soit au Chef du parquet Général(*) près de la Cour d'Appel dans le ressort de laquelle a eu lieu la disparition, au cas où celle-ci a eu lieu en territoire tunisien, soit au Chef du Parquet Général (*) près de la Cour d'
- `Statutpersonnel/s01/56` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 56 (Paragraphes 2, 3, 4, 5, 6 et 7 ajoutés par la loi n°2008-20 du 4 mars 2008).- Les frais nécessaires à l'entretien de l'enfant sont prélevés sur ses biens ou sur ceux du père si l'enfant n'a pas de biens propres. Le père doit pourvoir au logement de l'enfant et de la titulaire de la garde
- `Statutpersonnel/s01/56-bis` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 56 bis (Ajouté par la loi n°2008-20 du 4 mars 2008).- Est puni d’un emprisonnement de trois mois à un an et d’une amende de cent à mille dinars, quiconque cède sciemment, à titre onéreux ou gratuit, un local d’habitation dont le père est astreint à consacrer à l’hébergement de la titulaire d
- `Statutpersonnel/s02/56` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article 56 .- En transmettant le procès-verbal, le Secrétaire d'Etat compétent requerra le Chef du Parquet Général(*) de poursuivre d'office la déclaration judiciaire du décès. Les parties intéressées pourront, également, se pourvoir en déclaration de décès. La requête sera communiquée, pour avis, a
- `Statutpersonnel/s01/57` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 57 (Modifié par la loi n°66-49 du 3 juin 1966).- La garde appartient durant le mariage aux père et mère.
- `Statutpersonnel/s02/57` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article 57 .- Tout jugement déclaratif de décès sera transcrit à sa date sur les registres de l'état civil du dernier domicile, ou sur les registres de la municipalité de Tunis, si ce domicile est inconnu. __________ * Lire : Procureur de la République. Il sera fait mention du jugement et de sa tran

**Corpus candidates** (BM25 over Statutpersonnel.pdf; query terms: attribuée garde enfants)

-      `Statutpersonnel/s01/103` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 103 .- Trois cas se présentent pour les filles : 1°) la moitié est attribuée à la fille quand elle est fille unique, 2°) les deux tiers sont attribués aux filles quand elles sont plusieurs (so (5.7)
-      `Statutpersonnel/s15/7` [Décret n°93-1655 du 9 août 1993, relatif à la proc] Article 7. (Modifié par le décret n° 98-671 du 16 mars 1998)..- La caisse nationale de sécurité sociale cesse de payer les montants de la pension alimentaire ou de la rente de divorce lorsque le non l (4.9)
-      `Statutpersonnel/s01/64` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 64. (Modifié par la loi n°66-49 du 3 juin 1966).- La personne à qui la garde est confiée peut y renoncer. Dans ce cas, le juge désigne un nouveau titulaire de la garde. (4.9)
-      `Statutpersonnel/s01/105` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 105.- Les sœurs germaines présentent cinq cas : 1°) la moitié est attribuée quand il s'agit d'une sœur unique, 2°) les deux tiers sont attribués quand il s'agit de deux sœurs germaines ou plus (4.6)
-      `Statutpersonnel/s15/8` [Décret n°93-1655 du 9 août 1993, relatif à la proc] Article 8 .- Quiconque a indûment bénéficié des sommes d’argent du fonds de garantie de la pension alimentaire et de la rente de divorce doit les restituer sans délai. La caisse nationale de sécurité  (4.4)
-      `Statutpersonnel/s01/58` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 58 (Modifié par la loi n°81-7 du 18 février 1981).- Le titulaire du droit de garde doit être majeur, sain d'esprit, honnête, capable de pourvoir aux besoins de l'enfant, indemne de toute malad (4.3)
- gold `Statutpersonnel/s01/54` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 54 .- La garde consiste à élever l'enfant et à assurer sa protection dans sa demeure. (4.2)
- gold `Statutpersonnel/s01/57` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 57 (Modifié par la loi n°66-49 du 3 juin 1966).- La garde appartient durant le mariage aux père et mère. (4.2)

**Retrieved** (top-6, dev only)

- `q029` [fr]
    -   `Statutpersonnel/s01/67` Article 67. (Modifié par la loi n°93-74 du 12 juillet 1993).- En cas de dissolution du mariage par décès, la garde est confiée au survivant des père e
    -   `Statutpersonnel/s13/1` Article premier (Modifié par la loi n°2003-51 du 7 juillet 2003).- La mère qui a la garde de son enfant mineur et dont la filiation est inconnue doit 
    -   `Statutpersonnel/s01/61` Article 61 .- Si celui qui a la garde de l'enfant change de résidence et s'installe à une distance qui empêche le tuteur d'accomplir ses devoirs enver
    - ✓ `Statutpersonnel/s01/57` Article 57 (Modifié par la loi n°66-49 du 3 juin 1966).- La garde appartient durant le mariage aux père et mère.
    -   `Statutpersonnel/s01/59` Article 59 .- La titulaire du droit de garde d'une confession autre que celle du père de l'enfant ne pourra exercer ce droit qu'autant que l'enfant n'
    -   `Statutpersonnel/s01/58` Article 58 (Modifié par la loi n°81-7 du 18 février 1981).- Le titulaire du droit de garde doit être majeur, sain d'esprit, honnête, capable de pourvo
- `q062` [ar]
    -   `Statutpersonnel/s11/5` Article 5 .- Le tuteur officieux a, vis-à-vis du pupille, les droits et obligations prévus par les articles 54 et suivant du code du statut personnel.
    -   `Statutpersonnel/s01/59` Article 59 .- La titulaire du droit de garde d'une confession autre que celle du père de l'enfant ne pourra exercer ce droit qu'autant que l'enfant n'
    -   `Statutpersonnel/s01/60` Article 60. (Modifié par la loi n°93-74 du 12 juillet 1993).- Le père, le tuteur et la mère de l'enfant peuvent avoir un droit de regard sur ses affai
    -   `Statutpersonnel/s01/58` Article 58 (Modifié par la loi n°81-7 du 18 février 1981).- Le titulaire du droit de garde doit être majeur, sain d'esprit, honnête, capable de pourvo
    -   `Statutpersonnel/s11/3` Article 3 .- La tutelle officieuse est l'acte par lequel une personne majeure jouissant de la pleine capacité civile, ou un organisme d'assistance, pr
    - ✓ `Statutpersonnel/s01/55` Article 55 .- La femme qui refuse d'assurer la garde de l'enfant n'y sera obligée que lorsque aucune autre personne ne pourra lui être substituée.
- `q075` [en]
    -   `Statutpersonnel/s11/11` Article 11 .- (Modifié par la loi n°59-69 du 19 juin 1959).- Dans tous les cas, et compte tenu des dispositions des deuxième et troisième alinéa de l'
    -   `Statutpersonnel/s01/69` Article 69 .- La filiation n’est pas établie en cas de désaveu d’un enfant d’une femme mariée dont la non-cohabitation avec le mari a été prouvée, ou 
    -   `Statutpersonnel/s01/59` Article 59 .- La titulaire du droit de garde d'une confession autre que celle du père de l'enfant ne pourra exercer ce droit qu'autant que l'enfant n'
    -   `Statutpersonnel/s01/60` Article 60. (Modifié par la loi n°93-74 du 12 juillet 1993).- Le père, le tuteur et la mère de l'enfant peuvent avoir un droit de regard sur ses affai
    -   `Statutpersonnel/s01/63` Article 63 .- La femme à laquelle le droit de garde est transféré, pour une cause autre que l'incapacité physique de la gardienne précédente ne peut c
    -   `Statutpersonnel/s13/5` Article 5 .- Les règles relatives aux empêchements au mariage prévues par les articles 14, 15, 16 et 17 du code du statut personnel, lorsque la patern

**Suggested change:** Anchor 54-57 to the CSP garde articles (54/55/56/57 each also exist as 'disparu / procès-verbal' civil-status articles). Add 58 (conditions to hold the garde) and 67 (garde when the marriage is dissolved by divorce).

- add chunks: Statutpersonnel/s01/58, Statutpersonnel/s01/67
- drop chunks: Statutpersonnel/s01/56-bis, Statutpersonnel/s02/54, Statutpersonnel/s02/55, Statutpersonnel/s02/56, Statutpersonnel/s02/57
- proposed gold:
    - article 54 `Article 54 .- La garde consiste` → `Statutpersonnel/s01/54`
        > Article 54 .- La garde consiste à élever l'enfant et à assurer sa protection dans sa demeure.
    - article 55 `Article 55 .- La femme qui refuse` → `Statutpersonnel/s01/55`
        > Article 55 .- La femme qui refuse d'assurer la garde de l'enfant n'y sera obligée que lorsque aucune autre personne ne pourra lui être substituée.
    - article 56 `Article 56 (Paragraphes 2, 3, 4` → `Statutpersonnel/s01/56`
        > Article 56 (Paragraphes 2, 3, 4, 5, 6 et 7 ajoutés par la loi n°2008-20 du 4 mars 2008).- Les frais nécessaires à l'entretien de l'enfant sont prélevé
    - article 57 `Article 57 (Modifié par la loi n°66-49` → `Statutpersonnel/s01/57`
        > Article 57 (Modifié par la loi n°66-49 du 3 juin 1966).- La garde appartient durant le mariage aux père et mère.
    - NEW article 58 `Article 58 (Modifié par la loi n°81-7` → `Statutpersonnel/s01/58`
        > Article 58 (Modifié par la loi n°81-7 du 18 février 1981).- Le titulaire du droit de garde doit être majeur, sain d'esprit, honnête, capable de pourvo
    - NEW article 67 `Article 67. (Modifié par la loi n°93-74` → `Statutpersonnel/s01/67`
        > Article 67. (Modifié par la loi n°93-74 du 12 juillet 1993).- En cas de dissolution du mariage par décès, la garde est confiée au survivant des père e

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## csp_alimony  (test)

- `q030` [fr, statut_personnel, concept] Quelles sont les règles de la pension alimentaire ?

**Current gold** → chunks

- `Statutpersonnel/s01/37` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 37 .- L'obligation alimentaire prend sa source dans le mariage, la parenté ou l'engagement volontaire. Obligation suite au mariage (*)
- `Statutpersonnel/s02/37` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article 37 .- Tout acte de mariage des Tunisiens, conclu à l'étranger selon les formes locales, devra être transcrit, dans les trois mois de sa rédaction et à la diligence des époux, dans le registre des mariages du Consulat de Tunisie le plus proche. Toute infraction à cette obligation sera punie d
- `Statutpersonnel/s01/38` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 38 .- Le mari doit des aliments à la femme après la consommation du mariage et durant le délai de viduité en cas de divorce.
- `Statutpersonnel/s02/38` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article 38 .- L'acte de mariage des Etrangers en Tunisie sera rédigé conformément aux lois tunisiennes, sur le vu d'un certificat de leur consul attestant qu'ils peuvent contracter mariage. Le mariage contracté en Tunisie entre deux Etrangers de même nationalité pourra être célébré par les agents di
- `Statutpersonnel/s01/46` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 46 (Modifié par la loi n°93-74 du 12 juillet 1993).- Les aliments continuent à être servis aux enfants jusqu'à ce qu'ils atteignent l'âge de la majorité ou, au-delà de cette majorité, jusqu'à la fin de leurs études, à condition qu'ils ne dépassent pas l'âge de 25 ans. La fille continue à avo
- `Statutpersonnel/s02/46` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article 46 .- Lorsqu'un décès se sera produit ailleurs que dans la commune où le défunt était domicilié, l'officier de l'état civil qui aura dressé l'acte de décès, enverra, dans le plus bref délai possible, à l'officier de l'état civil du dernier domicile du défunt une expédition de cet acte, laque
- `Statutpersonnel/s01/47` [CODE DU STATUT PERSONNEL LIVRE PREMIER DU MARIAGE ] Article 47 .- En cas d'indigence du père, la mère est appelée avant le grand-père pour servir des aliments à ses enfants.
- `Statutpersonnel/s02/47` [Loi n°57-3 du 1er août 1957 (4 Moharem 1377), régl] Article 47 .- L'acte de décès énoncera : le jour, l'heure et le lieu du décès, les prénom, nom, date et lieu de naissance, profession, domicile et nationalité de la personne décédée; les prénoms, noms, professions, domiciles et nationalités de ses père et mère; les prénoms et noms de l'autre époux, 

**Corpus candidates** (BM25 over Statutpersonnel.pdf; query terms: règles pension alimentaire)

-      `Statutpersonnel/s14/6` [Loi n°93-65 du 5 juillet 1993, portant création d'] Article 6 .- Les montants de la pension alimentaire ou de la rente de divorce payés par le fonds de garantie de la pension alimentaire et de la rente de divorce sont majorés de 5% à titre de frais de  (8.8)
-      `Statutpersonnel/s15/2` [Décret n°93-1655 du 9 août 1993, relatif à la proc] Article 2(Modifié par le décret n°2006-826 du 23 mars 2006).- Les demandes d’obtention de la pension alimentaire ou de la rente de divorce doivent être accompagnées des pièces suivantes : - une copie  (8.0)
-      `Statutpersonnel/s14/3` [Loi n°93-65 du 5 juillet 1993, portant création d'] Article 3 .- Le fonds de garantie de la pension alimentaire et de la rente de divorce est subrogé aux ayants-droit de la pension alimentaire ou de la rente de divorce dans leurs droits vis-à-vis de la (7.9)
-      `Statutpersonnel/s15/6` [Décret n°93-1655 du 9 août 1993, relatif à la proc] Article 6 .- Les bénéficiaires de la pension alimentaire ou de la rente de divorce du fonds de garantie de la pension alimentaire et de la rente de divorce sont tenus de présenter au bureau régional d (7.6)
-      `Statutpersonnel/s14/1` [Loi n°93-65 du 5 juillet 1993, portant création d'] Article premier.- Il est crée un fonds pour garantir le paiement de la pension alimentaire ou de la rente de divorce, due en vertu d'un jugement au profit des femmes divorcées et leurs enfants et ce,  (7.6)
-      `Statutpersonnel/s14/10` [Loi n°93-65 du 5 juillet 1993, portant création d'] Article 10 .- La procédure d'intervention du fonds de garantie de la pension alimentaire et de la rente de divorce est fixée par décret. La présente loi sera publiée au Journal officiel de la Républiq (7.6)
-      `Statutpersonnel/s15/8` [Décret n°93-1655 du 9 août 1993, relatif à la proc] Article 8 .- Quiconque a indûment bénéficié des sommes d’argent du fonds de garantie de la pension alimentaire et de la rente de divorce doit les restituer sans délai. La caisse nationale de sécurité  (7.6)
-      `Statutpersonnel/s14/7` [Loi n°93-65 du 5 juillet 1993, portant création d'] Article 7 .- Le fonds de garantie de la pension alimentaire et de la rente de divorce est financé par les ressources suivantes : - Une contribution du budget de l'Etat; - Les montants de la pension al (7.5)

**Retrieved:** _hidden (test concept)_

**Suggested change:** Anchor 37/38/46/47 to the CSP alimony articles (other chunks with these numbers concern marriage abroad and death certificates). Add 43 (who is entitled), 50 (what the pension comprises), 51 (extinction), 52 (proportionality).

- add chunks: Statutpersonnel/s01/43, Statutpersonnel/s01/50, Statutpersonnel/s01/51, Statutpersonnel/s01/52
- drop chunks: Statutpersonnel/s02/37, Statutpersonnel/s02/38, Statutpersonnel/s02/46, Statutpersonnel/s02/47
- proposed gold:
    - article 37 `Article 37 .- L'obligation alimentaire` → `Statutpersonnel/s01/37`
        > Article 37 .- L'obligation alimentaire prend sa source dans le mariage, la parenté ou l'engagement volontaire. Obligation suite au mariage (*)
    - article 38 `Article 38 .- Le mari doit des aliments` → `Statutpersonnel/s01/38`
        > Article 38 .- Le mari doit des aliments à la femme après la consommation du mariage et durant le délai de viduité en cas de divorce.
    - NEW article 43 `Article 43 (Modifié par la loi n°93-74` → `Statutpersonnel/s01/43`
        > Article 43 (Modifié par la loi n°93-74 du 12 juillet 1993).- Ont droit aux aliments : a) les père et mère, les grands-parents paternels à quelque degr
    - article 46 `Article 46 (Modifié par la loi n°93-74` → `Statutpersonnel/s01/46`
        > Article 46 (Modifié par la loi n°93-74 du 12 juillet 1993).- Les aliments continuent à être servis aux enfants jusqu'à ce qu'ils atteignent l'âge de l
    - article 47 `Article 47 .- En cas d'indigence` → `Statutpersonnel/s01/47`
        > Article 47 .- En cas d'indigence du père, la mère est appelée avant le grand-père pour servir des aliments à ses enfants.
    - NEW article 50 `Article 50 .- La pension alimentaire comprend` → `Statutpersonnel/s01/50`
        > Article 50 .- La pension alimentaire comprend la nourriture, l'habillement, le logement, l'instruction et tout ce qui est considéré comme nécessaire à
    - NEW article 51 `Article 51 .- La pension alimentaire s'éteint` → `Statutpersonnel/s01/51`
        > Article 51 .- La pension alimentaire s'éteint avec l'extinction de sa cause. Le débiteur d'aliments aura droit à la restitution de ce qu'il aura payé 
    - NEW article 52 `Article 52.- Les aliments ne sont accordés` → `Statutpersonnel/s01/52`
        > Article 52.- Les aliments ne sont accordés que dans la proportion de la fortune de celui qui les doit et du besoin de celui qui les réclame, compte te

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## coc_contract_validity  (dev)

- `q031` [fr, obligations_contrats, concept] Quelles sont les conditions de validité d'un contrat ?
- `q063` [ar, obligations_contrats, concept] ما هي شروط صحة العقد؟
- `q082` [en, obligations_contrats, concept] What makes a contract valid?

**Current gold** → chunks

- `COC/s00/2` Article 2.- Ce code est divisé en deux livres : le premier, formé des articles de 1 à 717, concerne les obligations; le second, formé des articles de 718 à 1632, concerne les contrats et quasi-contrats.
- `COC/s01/2` [Loi n° 2005-87 du 15 août 2005, portant approbatio] Article 2.- Il ne découle de la réorganisation du code des obligations et des contrats tunisien aucune modification de son contenu, ou abrogation ou modification des dispositions spéciales qui lui sont contraires. La présente loi sera publiée au Journal Officiel de la République Tunisienne et exécut
- `COC/s02/2` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 2.- Les éléments nécessaires pour la validité des obligations qui dérivent d'une déclaration de volonté sont : 1) la capacité de s'obliger ; 2) une déclaration valable de volonté portant sur les éléments essentiels de l'obligation ; 3) un objet certain pouvant former objet d'obligation ; 4) 
- `COC/s00/3` Article 3.- Les dispositions du présent code seront mises en vigueur et appliquées par nos juridictions tunisiennes à dater du 1er juin 1907. Elles n’ont pas d’effet rétroactif.
- `COC/s02/3` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 3.- Toute personne est capable d'obliger et de s'obliger sauf si elle est déclarée incapable par la loi.

**Corpus candidates** (BM25 over COC.pdf; query terms: conditions validité contrat)

-      `COC/s02/328` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 328.- L’obligation qui est nulle comme telle, mais qui a les conditions de validité d’une autre obligation légitime, doit être régie par les règles établies pour cette obligation. (10.4)
-      `COC/s02/737` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 737.- Les baux des biens habous sont, notamment quant aux conditions de validité et de forme, soumis à des règlements particuliers. Les dispositions de la présente loi non contraires à ces règ (9.6)
-      `COC/s02/233` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 233.- Il n'est pas nécessaire pour la validité de la délégation que les deux dettes soient égales quant à la quotité, ni qu'elles aient une cause analogue. (6.1)
-      `COC/s02/1000` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 1000.- Il n’est pas nécessaire, pour la validité du dépôt entre les parties, que le déposant soit propriétaire de la chose déposée ni qu’il la possède à titre légitime. (6.1)
-      `COC/s02/1487` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 1487.- Il n'est pas obligatoire pour la validité du cautionnement que le créancier déclare l'avoir accepté; cependant, le cautionnement devient nul si le créancier le récuse. (6.1)
-      `COC/s02/470` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 470 (Modifié par la loi n°2000-57 du 13 juin 2000).- Les copies faites sur les originaux des actes authentiques ou des écritures privées ont la même valeur que les originaux lorsqu’elles sont  (6.1)
-      `COC/s02/1477` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 1477.- Lorsque, malgré les termes employés, la convention dénommée transaction constitue, en réalité, une donation, une vente ou autre rapport de droit, la validité et les effets du contrat do (5.8)
-      `COC/s02/1420` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 1420.- Le colon peut céder son contrat, à moins qu'il n'ait été stipulé expressément qu'il doit l'exécuter personnellement. Il peut constituer un nantissement sur sa part indivise, dans les co (5.8)

**Retrieved** (top-6, dev only)

- `q031` [fr]
    - ✓ `COC/s02/2` Article 2.- Les éléments nécessaires pour la validité des obligations qui dérivent d'une déclaration de volonté sont : 1) la capacité de s'obliger ; 2
    -   `COC/s02/119` Article 119.- La condition incompatible avec la nature de l'acte auquel elle est ajoutée est nulle et rend nulle l'obligation qui en dépend. Cette obl
    -   `COC/s02/29` Article 29.- Lorsqu'une réponse d'acceptation n'est pas exigée par le proposant ou par l'usage du commerce, le contrat est parfait dès que l'autre par
    -   `COC/s02/1477` Article 1477.- Lorsque, malgré les termes employés, la convention dénommée transaction constitue, en réalité, une donation, une vente ou autre rapport
    -   `COC/s02/133` Article 133.- La condition accomplie a un effet rétroactif au jour auquel l'obligation a été contractée, lorsqu'il résulte de la volonté des parties o
    -   `COC/s02/242` Article 242.- Les obligations contractuelles valablement formées tiennent lieu de loi à ceux qui les ont faites, et ne peuvent être révoquées que de l
- `q063` [ar]
    -   `COC/s02/1531` Article 1531.- La caution qui a été condamnée à payer, faute de présenter le débiteur, a le droit de faire révoquer la condamnation, si elle prouve qu
    -   `COC/s02/119` Article 119.- La condition incompatible avec la nature de l'acte auquel elle est ajoutée est nulle et rend nulle l'obligation qui en dépend. Cette obl
    -   `COC/s00/1` Article premier.- Les textes publiés ci-après et relatifs aux obligations et aux contrats sont réunis en un seul corps sous le titre du code tunisien 
    - ✓ `COC/s02/2` Article 2.- Les éléments nécessaires pour la validité des obligations qui dérivent d'une déclaration de volonté sont : 1) la capacité de s'obliger ; 2
    - ✓ `COC/s01/2` Article 2.- Il ne découle de la réorganisation du code des obligations et des contrats tunisien aucune modification de son contenu, ou abrogation ou m
    -   `COC/s02/830` Article 830.- Le louage d'ouvrages et celui de services ne sont valables que si les parties contractantes ont la capacité de s'obliger ; l'interdit et
- `q082` [en]
    - ✓ `COC/s02/2` Article 2.- Les éléments nécessaires pour la validité des obligations qui dérivent d'une déclaration de volonté sont : 1) la capacité de s'obliger ; 2
    -   `COC/s02/1531` Article 1531.- La caution qui a été condamnée à payer, faute de présenter le débiteur, a le droit de faire révoquer la condamnation, si elle prouve qu
    -   `COC/s02/119` Article 119.- La condition incompatible avec la nature de l'acte auquel elle est ajoutée est nulle et rend nulle l'obligation qui en dépend. Cette obl
    - ✓ `COC/s01/2` Article 2.- Il ne découle de la réorganisation du code des obligations et des contrats tunisien aucune modification de son contenu, ou abrogation ou m
    -   `COC/s02/24` Article 24.- Le contrat n'est point parfait lorsque les parties ont expressément réservé certaines clauses comme devant former objet d'un accord ultér
    -   `COC/s00/1` Article premier.- Les textes publiés ci-après et relatifs aux obligations et aux contrats sont réunis en un seul corps sous le titre du code tunisien 

**Suggested change:** Anchor: COC.pdf has three chunks numbered 2 and two numbered 3; the right ones are Art 2 'Les éléments nécessaires pour la validité des obligations ...' and Art 3 'Toute personne est capable'. Not added (lexical search did not surface them): the articles on consent, object and cause, so the label may be incomplete.

- add chunks: none
- drop chunks: COC/s00/2, COC/s00/3, COC/s01/2
- proposed gold:
    - article 2 `Article 2.- Les éléments nécessaires pour la validité` → `COC/s02/2`
        > Article 2.- Les éléments nécessaires pour la validité des obligations qui dérivent d'une déclaration de volonté sont : 1) la capacité de s'obliger ; 2
    - article 3 `Article 3.- Toute personne est capable` → `COC/s02/3`
        > Article 3.- Toute personne est capable d'obliger et de s'obliger sauf si elle est déclarée incapable par la loi.

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## coc_civil_liability  (test)

- `q032` [fr, obligations_contrats, concept] Qu'est-ce que la responsabilité civile ?

**Current gold** → chunks

- `COC/s02/82` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 82.- Tout fait quelconque de l'homme qui, sans l’autorité de la loi, cause sciemment et volontairement à autrui un dommage matériel ou moral, oblige son auteur à réparer le dommage résultant de son fait, lorsqu'il est établi que ce fait en est la cause directe. Toute stipulation contraire es
- `COC/s02/83` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 83.- Chacun est responsable du dommage moral ou matériel qu'il a causé, non seulement par son fait, mais par sa faute, lorsqu’il est établi que cette faute en est la cause directe. Toute stipulation contraire est sans effet. La faute consiste, soit à omettre ce qu'on était tenu de faire, soi
- `COC/s02/84` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 84.- La responsabilité établie aux deux articles ci-dessus s'applique également à l'Etat, même lorsqu'il agit comme puissance publique, aux communes et aux administrations publiques, pour les faits ou les fautes imputables à leurs représentants, agents et fonctionnaires dans l'exercice de le

**Corpus candidates** (BM25 over COC.pdf; query terms: responsabilité civile)

-      `COC/s02/102` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 102.- L'état d'ivresse, lorsqu'elle est volontaire, n'empêche point la responsabilité civile dans les obligations dérivant des délits et quasi-délits. Il n'y a point de responsabilité civile l (14.2)
-      `COC/s02/103` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 103.- Il n'y a pas lieu à responsabilité civile lorsqu'une personne, sans intention de nuire, a fait ce qu'elle avait le droit de faire. Cependant, lorsque l'exercice de ce droit est de nature (12.2)
-      `COC/s02/173` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 173.- Le créancier solidaire qui, après avoir reçu sa part, ne peut la représenter pour une cause imputable à sa faute, est tenu envers les autres créanciers jusqu'à concurrence de leur part e (8.6)
-      `COC/s02/104` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 104.- Il n'y a pas lieu à responsabilité civile dans le cas de légitime défense, ou lorsque le dommage a été produit par une cause purement fortuite ou de force majeure qui n'a été ni précédée (7.8)
- gold `COC/s02/84` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 84.- La responsabilité établie aux deux articles ci-dessus s'applique également à l'Etat, même lorsqu'il agit comme puissance publique, aux communes et aux administrations publiques, pour les  (5.6)
-      `COC/s02/858` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 858.- Sont sans effet, toutes clauses et conventions ayant pour objet de restreindre ou d'écarter la responsabilité établie par les articles 856 et 857 à la charge des maîtres ou employeurs. (5.4)
-      `COC/s02/1100` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 1100 (Modifié par la loi n°83-14 du 15 février 1983).- Lorsque les parties n’ont pas déterminé le taux des intérêts, le taux de l’intérêt légal qui s’applique est le suivant : 1) en matière ci (5.0)
-      `COC/s02/1447` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 1447.- Les associés sont solidairement responsables de la perte de la chose qui leur a été confiée par le commettant, lors même que cette perte proviendrait du fait d'un seul des associés, sau (4.5)

**Retrieved:** _hidden (test concept)_

**Suggested change:** No change; anchored.

- add chunks: none
- drop chunks: none
- proposed gold:
    - article 82 `Article 82` → `COC/s02/82`
        > Article 82.- Tout fait quelconque de l'homme qui, sans l’autorité de la loi, cause sciemment et volontairement à autrui un dommage matériel ou moral, 
    - article 83 `Article 83` → `COC/s02/83`
        > Article 83.- Chacun est responsable du dommage moral ou matériel qu'il a causé, non seulement par son fait, mais par sa faute, lorsqu’il est établi qu
    - article 84 `Article 84` → `COC/s02/84`
        > Article 84.- La responsabilité établie aux deux articles ci-dessus s'applique également à l'Etat, même lorsqu'il agit comme puissance publique, aux co

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## coc_force_majeure  (test)

- `q033` [fr, obligations_contrats, concept] Qu'est-ce que la force majeure ?
- `q064` [ar, obligations_contrats, concept] ما هي القوة القاهرة؟
- `q083` [en, obligations_contrats, concept] What is force majeure?

**Current gold** → chunks

- `COC/s02/283` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 283.- La force majeure est tout fait que l'homme ne peut prévenir, tel que les phénomènes naturels (inondations, sécheresses, orages, incendies, sauterelles), l'invasion ennemie, le fait du prince, et qui rend impossible l'exécution de l'obligation. N'est point considérée comme force majeure

**Corpus candidates** (BM25 over COC.pdf; query terms: force majeure)

-      `COC/s02/280` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 280.- Le débiteur en demeure répond du cas fortuit et de la force majeure. (10.2)
-      `COC/s02/1050` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 1050.- Il répond de la force majeure et du cas fortuit, s'il est en demeure de restituer la chose, si, étant partie au procès, il a accepté d'être constitué gardien provisoire, ou si la force  (9.7)
-      `COC/s02/1022` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 1022.- Le dépositaire ne répond pas : 1) de la perte ou de la détérioration causées par la nature ou le vice des choses déposées ou par la négligence du déposant ; 2) des cas de force majeure  (9.4)
-      `COC/s02/1207` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 1207.- Le gérant ne peut être chargé des cas fortuits ou de force majeure. Toute stipulation contraire est non avenue. (9.3)
- gold `COC/s02/283` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 283.- La force majeure est tout fait que l'homme ne peut prévenir, tel que les phénomènes naturels (inondations, sécheresses, orages, incendies, sauterelles), l'invasion ennemie, le fait du pr (9.3)
-      `COC/s02/1024` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 1024.- Le dépositaire auquel la chose a été enlevée par une force majeure, et qui a reçu une somme ou quelque chose à la place, doit restituer ce qu’il a reçu. (8.6)
-      `COC/s02/744` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 744.- Aucune des réparations réputées locatives n’est à la charge du preneur quand elles sont occasionnées par vétusté ou force majeure, par le vice de construction ou par le fait du bailleur. (8.4)
-      `COC/s02/847` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 847.- Ils ne répondent pas de la détérioration et de la perte provenant d'un cas fortuit ou de force majeure, qui n'a pas été occasionné par leur fait on par leur faute et sauf le cas où ils s (8.3)

**Retrieved:** _hidden (test concept)_

**Suggested change:** Add 280 ('Le débiteur en demeure répond du cas fortuit et de la force majeure').

- add chunks: COC/s02/280
- drop chunks: none
- proposed gold:
    - NEW article 280 `Article 280` → `COC/s02/280`
        > Article 280.- Le débiteur en demeure répond du cas fortuit et de la force majeure.
    - article 283 `Article 283` → `COC/s02/283`
        > Article 283.- La force majeure est tout fait que l'homme ne peut prévenir, tel que les phénomènes naturels (inondations, sécheresses, orages, incendie

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## coc_binding_force  (test)

- `q034` [fr, obligations_contrats, concept] Quelle est la force obligatoire du contrat ?

**Current gold** → chunks

- `COC/s02/242` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 242.- Les obligations contractuelles valablement formées tiennent lieu de loi à ceux qui les ont faites, et ne peuvent être révoquées que de leur consentement mutuel ou dans les cas prévus par la loi.

**Corpus candidates** (BM25 over COC.pdf; query terms: force obligatoire contrat)

-      `COC/s02/1487` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 1487.- Il n'est pas obligatoire pour la validité du cautionnement que le créancier déclare l'avoir accepté; cependant, le cautionnement devient nul si le créancier le récuse. (8.2)
-      `COC/s02/864` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 864.- Le maître a le droit de résoudre le contrat pour cause de maladie ou autre accident de force majeure survenus à son serviteur ou employé, en payant ce qui est dû à ce dernier proportionn (5.6)
-      `COC/s02/623` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 623.- Les choses qui se vendent au poids et au nombre et ne présentent pas de variations sensibles dans leur prix, celles qu’on peut diviser sans préjudice, peuvent être vendues pour un prix u (5.3)
-      `COC/s02/280` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 280.- Le débiteur en demeure répond du cas fortuit et de la force majeure. (5.0)
-      `COC/s02/1422` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 1422.- Si les plantations périssent, en totalité, par cas fortuit ou force majeure, après avoir atteint l'âge convenu, le colon aura droit de partager le sol dans les proportions établies au c (4.9)
-      `COC/s02/1050` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 1050.- Il répond de la force majeure et du cas fortuit, s'il est en demeure de restituer la chose, si, étant partie au procès, il a accepté d'être constitué gardien provisoire, ou si la force  (4.8)
-      `COC/s02/1022` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 1022.- Le dépositaire ne répond pas : 1) de la perte ou de la détérioration causées par la nature ou le vice des choses déposées ou par la négligence du déposant ; 2) des cas de force majeure  (4.6)
-      `COC/s02/394` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 394.- La prescription n’a pas lieu à l’égard des droits résultant d’un jugement passé en force de chose jugée. (4.6)

**Retrieved:** _hidden (test concept)_

**Suggested change:** No change; anchored.

- add chunks: none
- drop chunks: none
- proposed gold:
    - article 242 `Article 242` → `COC/s02/242`
        > Article 242.- Les obligations contractuelles valablement formées tiennent lieu de loi à ceux qui les ont faites, et ne peuvent être révoquées que de l

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## coc_seller_duties  (dev)

- `q035` [fr, obligations_contrats, concept] Quelles sont les obligations du vendeur ?

**Current gold** → chunks

- `COC/s02/564` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 564.- La vente est un contrat par lequel l’une des parties transmet la propriété d’une chose ou d’un droit à l’autre contractant, contre un prix que ce dernier s’oblige à lui payer.
- `COC/s02/611` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 611.- La vente d’un héritage comprend celle des constructions et des plantations qui s’y trouvent, celle des récoltes qui n’ont pas encore levé, des fruits non noués. Elle ne comprend pas les fruits noués, les récoltes pendantes, les plantes en pots et les pépinières, les arbres secs qui ne 
- `COC/s02/612` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 612.- La vente d’un édifice comprend celle du sol qui le soutient, et des accessoires fixes et immobilisés, tels que les portes, fenêtres, clefs faisant partie des serrures, moulins, escaliers ou armoires fixes, tuyaux servant à la conduite des eaux, poutres et fourneaux fixés au mur. Elle n

**Corpus candidates** (BM25 over COC.pdf; query terms: obligations vendeur)

-      `COC/s02/590` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 590.- En cas de vente de fruits sur l’arbre, des produits d’un potager ou d’une récolte pendante, les fruits ou les légumes sont aux risques du vendeur jusqu’au moment de leur complète maturat (7.5)
-      `COC/s02/591` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 591.- Le vendeur a deux obligations principales : 1) celle de délivrer la chose vendue ; 2) celle de la garantir. Parag. I. - De la délivrance (7.2)
-      `COC/s02/800` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 800.- Si le nouvel acquéreur n'exécute pas les obligations imposées par le bail au bailleur, le preneur aura action contre lui et contre son vendeur, solidairement entre eux, pour toutes indem (5.9)
-      `COC/s02/601` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 601.- Le vendeur n’est pas tenu de délivrer la chose vendue, quand même il aurait accordé un délai pour le paiement : 1) si, depuis la vente, l’acheteur est tombé en déconfiture ; 2) s’il étai (4.7)
-      `COC/s02/642` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 642.- Les parties peuvent convenir que le vendeur ne sera soumis à aucune garantie. Cette clause n'a cependant pour effet que d’affranchir le vendeur des dommages-intérêts, mais ne peut le lib (4.5)
-      `COC/s02/576` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 576.- La vente de la chose d’autrui est valable : 1) si le maître la ratifie ; 2) si le vendeur acquiert ensuite la propriété de la chose ; Dans le cas où le maître refuse de ratifier, l’acqué (4.4)
-      `COC/s02/588` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 588.- La chose vendue voyage aux risques du vendeur jusqu’à sa réception par l’acheteur. (4.4)
-      `COC/s02/651` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 651.- En cas de doute, le dire du vendeur fait foi à charge de serment. (4.4)

**Retrieved** (top-6, dev only)

- `q035` [fr]
    -   `COC/s02/631` Article 631.- L’obligation de garantir emporte pour le vendeur celle de s’abstenir de tout acte ou réclamation qui tendrait à inquiéter l’acheteur ou 
    -   `COC/s02/591` Article 591.- Le vendeur a deux obligations principales : 1) celle de délivrer la chose vendue ; 2) celle de la garantir. Parag. I. - De la délivrance
    -   `COC/s00/1` Article premier.- Les textes publiés ci-après et relatifs aux obligations et aux contrats sont réunis en un seul corps sous le titre du code tunisien 
    -   `COC/s02/242` Article 242.- Les obligations contractuelles valablement formées tiennent lieu de loi à ceux qui les ont faites, et ne peuvent être révoquées que de l
    -   `COC/s02/630` Article 630.- La garantie que le vendeur doit à l’acquéreur à deux objets : a) le premier est la jouissance et la possession paisible de la chose vend
    -   `COC/s02/748` Article 748.- L’obligation de garantie emporte pour le bailleur celle de s’abstenir de tout ce qui tendrait à troubler la possession du preneur ou à l

**Suggested change:** Replace: 564 is the definition of sale, 611/612 say what the sale of land/building includes. Art 591: 'Le vendeur a deux obligations principales : 1) délivrer la chose 2) la garantir' is the duties article. Its sub-articles (délivrance, garantie) were not reviewed, so recall is likely understated.

- add chunks: COC/s02/591
- drop chunks: COC/s02/564, COC/s02/611, COC/s02/612
- proposed gold:
    - NEW article 591 `Article 591` → `COC/s02/591`
        > Article 591.- Le vendeur a deux obligations principales : 1) celle de délivrer la chose vendue ; 2) celle de la garantir. Parag. I. - De la délivrance

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## coc_lease  (test)

- `q036` [fr, obligations_contrats, concept] Quelles sont les règles du contrat de louage ?

**Current gold** → chunks

- `COC/s02/728` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 728.- Le louage de choses est parfait par le consentement des parties sur la chose, sur le prix et sur les autres clauses dont elles pourraient convenir dans le contrat.

**Corpus candidates** (BM25 over COC.pdf; query terms: règles contrat louage)

-      `COC/s02/738` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 738.- La location des mines, minières, carrières et gisements, enfouis dans le sol ou affleurant à la surface, est soumise également aux règlements spéciaux et aux règles de la vente. Section  (7.4)
-      `COC/s02/724` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 724.- Les règles de la vente s'appliquent à l'échange dans la mesure où le permet la nature de ce contrat. (7.2)
-      `COC/s02/993` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 993.- La naçba est régie par les dispositions relatives au louage de choses dans la mesure où elles sont applicables à ce contrat. (7.0)
- gold `COC/s02/728` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 728.- Le louage de choses est parfait par le consentement des parties sur la chose, sur le prix et sur les autres clauses dont elles pourraient convenir dans le contrat. (6.5)
-      `COC/s02/757` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 757.- Les actions du preneur contre le bailleur à raison des articles 748 à 756 inclus se prescrivent par l’expiration du contrat de louage. b) – De la garantie des défauts de la chose louée (6.3)
-      `COC/s02/777` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 777.- La cession est régie par les dispositions établies au chapitre de la cession des créances (articles 199 et suivants) et emporte la substitution du cessionnaire dans les droits et dans le (6.1)
-      `COC/s02/766` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 766.- Les actions du preneur contre le bailleur, à raison des articles 758, 764 et 765 ne peuvent plus être utilement intentées à partir du moment où le contrat de louage a pris fin. Parag. II (6.0)
-      `COC/s02/828` [CODE DES OBLIGATIONS ET DES CONTRATS LIVRE PREMIER] Article 828.- Le louage de services ou de travail est un contrat par lequel l'une des parties s'engage, moyennant un prix que l'autre partie s'oblige à lui payer, à fournir à cette dernière ses servic (6.0)

**Retrieved:** _hidden (test concept)_

**Suggested change:** No change; anchored.

- add chunks: none
- drop chunks: none
- proposed gold:
    - article 728 `Article 728` → `COC/s02/728`
        > Article 728.- Le louage de choses est parfait par le consentement des parties sur la chose, sur le prix et sur les autres clauses dont elles pourraien

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## nat_acquisition  (test)

- `q037` [fr, nationalite, concept] Comment acquérir la nationalité tunisienne ?
- `q065` [ar, nationalite, concept] كيف تكتسب الجنسية التونسية؟
- `q084` [en, nationalite, concept] How can someone acquire Tunisian nationality?

**Current gold** → chunks

- `NationaliteFr/s01/6` [Loi n° 63-7 du 22 avril 1963, (28 doul kaada 1382)] Article 6 (Modifié par la loi n° 2010-55 du 1er décembre 2010)(*). - Est tunisien l’enfant né d’un père tunisien ou d’une mère tunisienne. Section II - Attribution en raison de la natalité en Tunisie
- `NationaliteFr/s01/7` [Loi n° 63-7 du 22 avril 1963, (28 doul kaada 1382)] Article 7.- Est Tunisien, l’enfant né en Tunisie et dont le père et le grand-père y sont eux-mêmes nés. L’intéressé peut, sauf s’il est né après l’entrée en vigueur du présent Code, répudier la nationalité tunisienne dans l’année précédant sa majorité; il est libéré de son allégeance à l’égard de la
- `NationaliteFr/s01/8` [Loi n° 63-7 du 22 avril 1963, (28 doul kaada 1382)] Article 8.- Est tunisien, l’enfant né en Tunisie de parents apatrides résidant en Tunisie depuis cinq ans au moins.
- `NationaliteFr/s01/9` [Loi n° 63-7 du 22 avril 1963, (28 doul kaada 1382)] Article 9.- Est Tunisien, l’enfant né en Tunisie de parents inconnus. Toutefois, il sera réputé n’avoir jamais été Tunisien si, au cours de la minorité, sa filiation est établie à l’égard d’un étranger et s’il a, conformément à la loi nationale de cet étranger, la nationalité de celui-ci.

**Corpus candidates** (BM25 over NationaliteFr.pdf; query terms: acquérir nationalité tunisienne)

-      `NationaliteFr/s01/17` [Loi n° 63-7 du 22 avril 1963, (28 doul kaada 1382)] Article 17.- Lorsque la validité des actes, passés antérieurement à la décision constatant la nullité du mariage ou au décret d’opposition, était subordonnée à l’acquisition par l’intéressé de la nati (6.3)
-      `NationaliteFr/s01/29` [Loi n° 63-7 du 22 avril 1963, (28 doul kaada 1382)] Article 29.- Le mariage ne produit effet, quant à la nationalité, que s’il est célébré en l’une des formes admises, soit par la loi tunisienne, soit par la loi du pays où il a été célébré. Chapitre II (3.0)
-      `NationaliteFr/s01/1` [Loi n° 63-7 du 22 avril 1963, (28 doul kaada 1382)] Article premier.- Le présent Code détermine quels individus ont, à leur naissance, la nationalité tunisienne, à titre de nationalité d’origine. La nationalité tunisienne s’acquiert ou se perd après la (2.8)
-      `NationaliteFr/s01/65` [Loi n° 63-7 du 22 avril 1963, (28 doul kaada 1382)] Article 65 (Modifié par la loi n° 71-12 du 9 mars 1971). -Lorsque le ministre de la justice, les agents diplomatiques et consulaires représentant la Tunisie à l’étranger ou les juges cantonaux refusen (2.7)
-      `NationaliteFr/s01/30` [Loi n° 63-7 du 22 avril 1963, (28 doul kaada 1382)] Article 30 (Modifié par la loi n° 75-79 du 14 novembre 1975). - La perte de la nationalité tunisienne ne peut être prononcée que par décret. (*) Lire : Ministre ou Ministère selon le cas. En cas d’acq (2.6)
-      `NationaliteFr/s01/59` [Loi n° 63-7 du 22 avril 1963, (28 doul kaada 1382)] Article 59.- La charge de la preuve, en matière de nationalité, incombe à celui qui, par voie d’action ou par voie d’exception, prétend avoir ou non la nationalité tunisienne. Toutefois, cette charge  (2.6)
-      `NationaliteFr/s01/62` [Loi n° 63-7 du 22 avril 1963, (28 doul kaada 1382)] Article 62.- La preuve d’un décret de naturalisation ou d’un décret portant perte, déchéance, retrait de la nationalité tunisienne ou opposition du Président de la République ) ( à l’acquisition de ce (2.5)
-      `NationaliteFr/s01/13` [Loi n° 63-7 du 22 avril 1963, (28 doul kaada 1382)] Article 13.- La femme étrangère qui épouse un tunisien acquiert la nationalité tunisienne au moment de la célébration du mariage, lorsque, en vertu de sa loi nationale, elle perd sa nationalité d’orig (2.4)

**Retrieved:** _hidden (test concept)_

**Suggested change:** No change; anchored. The question says 'acquérir': the corpus also has acquisition by marriage (13-14) and naturalisation, which lexical search did not surface, so the label may be incomplete.

- add chunks: none
- drop chunks: none
- proposed gold:
    - article 6 `Article 6` → `NationaliteFr/s01/6`
        > Article 6 (Modifié par la loi n° 2010-55 du 1er décembre 2010)(*). - Est tunisien l’enfant né d’un père tunisien ou d’une mère tunisienne. Section II 
    - article 7 `Article 7` → `NationaliteFr/s01/7`
        > Article 7.- Est Tunisien, l’enfant né en Tunisie et dont le père et le grand-père y sont eux-mêmes nés. L’intéressé peut, sauf s’il est né après l’ent
    - article 8 `Article 8` → `NationaliteFr/s01/8`
        > Article 8.- Est tunisien, l’enfant né en Tunisie de parents apatrides résidant en Tunisie depuis cinq ans au moins.
    - article 9 `Article 9` → `NationaliteFr/s01/9`
        > Article 9.- Est Tunisien, l’enfant né en Tunisie de parents inconnus. Toutefois, il sera réputé n’avoir jamais été Tunisien si, au cours de la minorit

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## enfant_at_risk  (test)

- `q038` [fr, protection_enfant, concept] Quels sont les droits de l'enfant en danger ?

**Current gold** → chunks

- `EnfantFr/s01/20` [CODE DE LA PROTECTION] Article 20.- Sont considérés, en particulier, comme des situations difficiles menaçant la santé de l'enfant ou son intégrité physique ou morale : a/ la perte des parents de l'enfant qui demeure sans soutien familial. b/ l'exposition de l'enfant à la négligence et au vagabondage. c/ le manquement not
- `EnfantFr/s03/20` Article 20.- 1. - Tout enfant qui est temporairement ou définitivement privé de son milieu familial, ou qui dans son propre intérêt ne peut être laissé dans ce milieu, a droit à une protection et une aide spéciales de l'Etat. 2. - Les Etats parties prévoient pour cet enfant une protection de remplac
- `EnfantFr/s05/20` [Décret n° 95-2423 du 11 décembre 1995, portant] Article 20.- Les mineurs nouvellement admis sont soumis à un examen médical général, les mineurs malades sont soumis à l'examen médical aussi souvent qu'il est jugé nécessaire, le malade est confié à l'infirmerie du centre, et les médicaments prescrits lui sont fournis gratuitement.
- `EnfantFr/s08/20` [Vu la convention des nations unies sur les droits ] Article 20.- Les ministres des finances et de la jeunesse, de l'enfance et des sports sont chargés, chacun en ce qui le concerne, de l'exécution du présent décret qui sera publié au Journal Officiel de la République Tunisienne. Tunis, le 14 février 2002. Zine El Abidine Ben Ali
- `EnfantFr/s01/21` [CODE DE LA PROTECTION] Article 21.- La négligence signifie la mise en danger de l'intégrité mentale ou psychologique ou physique de l'enfant soit par son abandon par ses parents, sans motif valable dans un endroit ou dans une institution publique ou privée, soit par l'abandon du foyer familial par les parents pendant une 
- `EnfantFr/s03/21` Article 21.- Les Etats parties qui admettent et/ou autorisent l'adoption s'assurent que l'intérêt supérieur de l'enfant est la considération primordiale en la matière, et : a) veillant à ce que l'adoption d'un enfant ne soit autorisée que par les autorités compétentes, qui vérifient, conformément à 
- `EnfantFr/s05/21` [Décret n° 95-2423 du 11 décembre 1995, portant] Article 21.- Le mineur malade bénéficie de la gratuité des soins aux hôpitaux relevant du ministère de la santé publique conformément à la législation en vigueur.
- `EnfantFr/s01/22` [CODE DE LA PROTECTION] Article 22.- Est considéré comme étant une des situations nécessitant l'intervention, le vagabondage de l'enfant qui reste sans suivi ni formation, en raison du refus de celui qui est chargé de son éducation ou de sa garde de le confier à une école, en application des dispositions de la loi relative
- `EnfantFr/s03/22` Article 22.- 1. - Les Etats parties prennent les mesures appropriées pour qu'un enfant qui cherche à obtenir le statut de réfugié ou qui est considéré comme réfugié en vertu des règles et procédures du droit international ou national applicable, qu'il soit seul ou accompagné de ses père et mère ou d
- `EnfantFr/s05/22` [Décret n° 95-2423 du 11 décembre 1995, portant] Article 22.- Le mineur peut être autorisé par la direction générale des prisons et de la rééducation à être soigné à ses frais dans les cliniques privées selon la volonté de ses parents.

**Corpus candidates** (BM25 over EnfantFr.pdf; query terms: droits enfant danger)

-      `EnfantFr/s01/46` [CODE DE LA PROTECTION] Article 46.- Dans les cas de danger imminent, le délégué à la protection de l'enfance peut prendre l'initiative d'éloigner l'enfant de l'endroit du danger en ayant recours même à la force publique, et (7.9)
-      `EnfantFr/s01/19` [CODE DE LA PROTECTION] Article 19.- Il est interdit d'exploiter l'enfant dans les différentes formes de criminalité organisée, y compris le fait de lui inculquer le fanatisme et la haine et de l'inciter à commettre des acte (6.6)
- gold `EnfantFr/s01/21` [CODE DE LA PROTECTION] Article 21.- La négligence signifie la mise en danger de l'intégrité mentale ou psychologique ou physique de l'enfant soit par son abandon par ses parents, sans motif valable dans un endroit ou dans u (5.7)
-      `EnfantFr/s08/2` [Vu la convention des nations unies sur les droits ] Article 2.- L'observatoire d'information, de formation, de documentation et d'études pour la protection des droits de l'enfant est chargé des missions suivantes : - observer l'état de la protection de (5.5)
-      `EnfantFr/s01/30` [CODE DE LA PROTECTION] Article 30.- Le délégué à la protection de l'enfance est chargé d'une mission d'intervention préventive dans tous les cas où il s'avère que la santé de l'enfant ou son intégrité physique ou morale est (4.8)
-      `EnfantFr/s01/43` [CODE DE LA PROTECTION] Article 43.- Le délégué à la protection de l'enfance peut proposer l'une des mesures conventionnelles suivantes : a) le maintien de l'enfant dans sa famille et l'engagement des parents à prendre les m (4.8)
-      `EnfantFr/s03/15` Article 15.- 1. – Les Etats parties reconnaissent les droits de l'enfant à la liberté d'association et à la liberté de réunion pacifique. 2. – L'exercice de ces droits ne peut faire l'objet que des se (4.8)
-      `EnfantFr/s08/4` [Vu la convention des nations unies sur les droits ] Article 4.- L'observatoire d'information, de formation, de documentation et d'études pour la protection des droits de l'enfant est dirigé par un directeur général. Le directeur général de l'observatoi (4.7)

**Retrieved:** _hidden (test concept)_

**Suggested change:** Anchor 20/21/22 to the child-protection code (other chunks numbered 20-22 are CRC treaty articles and prison rules). Add 30 (délégué à la protection de l'enfance, preventive intervention) and 46 (danger imminent: removal of the child).

- add chunks: EnfantFr/s01/30, EnfantFr/s01/46
- drop chunks: EnfantFr/s03/20, EnfantFr/s03/21, EnfantFr/s03/22, EnfantFr/s05/20, EnfantFr/s05/21, EnfantFr/s05/22, EnfantFr/s08/20
- proposed gold:
    - article 20 `Article 20.- Sont considérés, en particulier, comme des situations difficiles` → `EnfantFr/s01/20`
        > Article 20.- Sont considérés, en particulier, comme des situations difficiles menaçant la santé de l'enfant ou son intégrité physique ou morale : a/ l
    - article 21 `Article 21.- La négligence signifie` → `EnfantFr/s01/21`
        > Article 21.- La négligence signifie la mise en danger de l'intégrité mentale ou psychologique ou physique de l'enfant soit par son abandon par ses par
    - article 22 `Article 22.- Est considéré comme étant une des situations` → `EnfantFr/s01/22`
        > Article 22.- Est considéré comme étant une des situations nécessitant l'intervention, le vagabondage de l'enfant qui reste sans suivi ni formation, en
    - NEW article 30 `Article 30.- Le délégué à la protection de l'enfance est chargé` → `EnfantFr/s01/30`
        > Article 30.- Le délégué à la protection de l'enfance est chargé d'une mission d'intervention préventive dans tous les cas où il s'avère que la santé d
    - NEW article 46 `Article 46.- Dans les cas de danger imminent` → `EnfantFr/s01/46`
        > Article 46.- Dans les cas de danger imminent, le délégué à la protection de l'enfance peut prendre l'initiative d'éloigner l'enfant de l'endroit du da

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## arb_agreement  (dev)

- `q039` [fr, arbitrage, concept] Qu'est-ce qu'une convention d'arbitrage ?

**Current gold** → chunks

- `ArbitrageFr/s00/2` Article 2 Les dispositions du présent code ne dérogent pas aux lois spéciales interdisant le règlement de certains différends par voie d'arbitrage ou prescrivant des procédures spéciales pour le recours à l'arbitrage.
- `ArbitrageFr/s01/2` [CODE DE L'ARBITRAGE] Article 2 La convention d'arbitrage est l'engagement des parties de régler par l'arbitrage toutes ou certaines contestations nées ou pouvant naître entre elles concernant un rapport de droit déterminé, contractuel ou non contractuel. La convention d'arbitrage revêt la forme d'une clause compromissoi
- `ArbitrageFr/s02/2` [Loi n° 94-56 du 16 mai 1994, portant dispense des ] Article 2 Les dispositions du numéro 18 de l'article 20 du code des droits d'enregistrement et de timbre sont abrogées. La présente loi sera publiée au Journal Officiel de la République Tunisienne et exécutée comme loi de l’Etat. Tunis, le 16 mai 1994. Zine El Abidine Ben Ali
- `ArbitrageFr/s03/2` [Décret n° 95-2084 du 23 octobre 1995, portant] Art. 2. – Le Premier ministre est chargé de l’exécution du présent décret qui sera publié au Journal Officiel de la République Tunisienne. Tunis, le 23 octobre 1995 Zine El Abidine Ben Ali
- `ArbitrageFr/s04/2` [CONVENTION ENTRE LA RÉPUBLIQUE TUNISIENNE] Article 2. – Entraide judiciaire 1.- Les autorités judiciaires des deux parties contractantes se prêteront réciproquement entraide judiciaire en matière civile et commerciale.
- `ArbitrageFr/s05/2` [Décret n° 2005-1908 du 5 juillet 2005 portant publ] Art. 2. - Le Premier ministre et les ministres concernés sont chargés, chacun selon ses attributions, de l’exécution du présent décret qui sera publié au Journal Officiel de la République Tunisienne. Tunis, le 5 juillet 2005 Zine El Abidine Ben Ali 1) Le texte de l'accord est publié uniquement en la
- `ArbitrageFr/s00/3` Article 3 Sont abrogées les dispositions des articles 258 à 284 du Code de Procédure Civile et Commerciale promulgué par la loi n° 59-130 datée du 5 octobre 1959. Toutefois les instances arbitrales en cours devant les arbitres ou devant les juridictions, restent soumises aux procédures en (1) Travau
- `ArbitrageFr/s01/3` [CODE DE L'ARBITRAGE] Article 3 La clause compromissoire est l'engagement des parties à un contrat, de soumettre à l'arbitrage, les contestations qui pourraient naître de ce contrat.
- `ArbitrageFr/s04/3` [CONVENTION ENTRE LA RÉPUBLIQUE TUNISIENNE] Article 3. – Mode de transmission 1.- Les autorités judiciaires des parties contractantes communiqueront entre elles, aux fins de l’entraide judiciaire, par l’intermédiaire de leurs organes centraux, à savoir le ministère de la justice des deux pays.

**Corpus candidates** (BM25 over ArbitrageFr.pdf; query terms: convention arbitrage)

-      `ArbitrageFr/s01/51` [CODE DE L'ARBITRAGE] Article 51 Pour les questions objet d'une convention d'arbitrage international, les tribunaux ne peuvent intervenir qu'en vertu des dispositions du présent code. Section II. - Convention d'arbitrage (1.6)
-      `ArbitrageFr/s01/48` [CODE DE L'ARBITRAGE] Article 48 1- L'arbitrage est international dans l'un des cas suivants : a) Si les parties à une convention d'arbitrage ont, au moment de la conclusion de ladite convention, leur établissement dans de (1.5)
- gold `ArbitrageFr/s01/2` [CODE DE L'ARBITRAGE] Article 2 La convention d'arbitrage est l'engagement des parties de régler par l'arbitrage toutes ou certaines contestations nées ou pouvant naître entre elles concernant un rapport de droit déterminé (1.4)
-      `ArbitrageFr/s01/6` [CODE DE L'ARBITRAGE] Article 6 La convention d'arbitrage ne peut être établie que par écrit, soit par acte authentique ou sous seing privé, soit par procès- verbal d'audience ou procès-verbal dressé auprès du tribunal arb (1.3)
-      `ArbitrageFr/s01/52` [CODE DE L'ARBITRAGE] Article 52 Le tribunal saisi d'un différend sur une question faisant l'objet d'une convention d'arbitrage, renverra les parties à l'arbitrage si l'une d'entre elles le demande au plus tard lorsqu'elle (1.3)
-      `ArbitrageFr/s01/8` [CODE DE L'ARBITRAGE] Article 8 Les parties à une convention d'arbitrage doivent avoir la capacité de disposer de leurs droits. (1.3)
-      `ArbitrageFr/s01/1` [CODE DE L'ARBITRAGE] Article premier L'arbitrage est un procédé privé de règlement de certaines catégories de contestations par un tribunal arbitral auquel les parties confient la mission de les juger en vertu d'une conve (1.3)
-      `ArbitrageFr/s01/42` [CODE DE L'ARBITRAGE] Article 42 Même si les parties en conviennent autrement, le recours en annulation d'une sentence arbitrale définitive, peut être formé dans les cas suivants : 1- si la sentence est rendue en l'absence (1.3)

**Retrieved** (top-6, dev only)

- `q039` [fr]
    - ✓ `ArbitrageFr/s00/3` Article 3 Sont abrogées les dispositions des articles 258 à 284 du Code de Procédure Civile et Commerciale promulgué par la loi n° 59-130 datée du 5 o
    -   `ArbitrageFr/s01/6` Article 6 La convention d'arbitrage ne peut être établie que par écrit, soit par acte authentique ou sous seing privé, soit par procès- verbal d'audie
    - ✓ `ArbitrageFr/s01/2` Article 2 La convention d'arbitrage est l'engagement des parties de régler par l'arbitrage toutes ou certaines contestations nées ou pouvant naître en
    -   `ArbitrageFr/s01/56` Article 56 1- Nul ne peut, en raison de sa nationalité être empêché d'exercer des fonctions d'arbitre, sauf convention contraire des parties. 2- Les p
    -   `ArbitrageFr/s01/61` Article 61 1- Le tribunal arbitral statue sur sa propre compétence et sur toute opposition relative à l'existence ou à la validité de la convention d'
    -   `ArbitrageFr/s01/8` Article 8 Les parties à une convention d'arbitrage doivent avoir la capacité de disposer de leurs droits.

**Suggested change:** Anchor 2 and 3 to the arbitration-agreement/clause articles (6 chunks each carry numbers 2 and 3). Add 6 (form: la convention d'arbitrage ne peut être établie que par écrit).

- add chunks: ArbitrageFr/s01/6
- drop chunks: ArbitrageFr/s00/2, ArbitrageFr/s00/3, ArbitrageFr/s02/2, ArbitrageFr/s03/2, ArbitrageFr/s04/2, ArbitrageFr/s04/3, ArbitrageFr/s05/2
- proposed gold:
    - article 2 `Article 2 La convention d'arbitrage est l'engagement` → `ArbitrageFr/s01/2`
        > Article 2 La convention d'arbitrage est l'engagement des parties de régler par l'arbitrage toutes ou certaines contestations nées ou pouvant naître en
    - article 3 `Article 3 La clause compromissoire` → `ArbitrageFr/s01/3`
        > Article 3 La clause compromissoire est l'engagement des parties à un contrat, de soumettre à l'arbitrage, les contestations qui pourraient naître de c
    - NEW article 6 `Article 6 La convention d'arbitrage ne peut` → `ArbitrageFr/s01/6`
        > Article 6 La convention d'arbitrage ne peut être établie que par écrit, soit par acte authentique ou sous seing privé, soit par procès- verbal d'audie

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## any_art13  (test)

- `q040` [fr, unfiltered, cross_domain] Que dit l'article 13 ?
- `q086` [en, unfiltered, cross_domain] What does article 13 say?

**Current gold** → chunks

- article 13 in any code (35 chunks)

**Retrieved:** _hidden (test concept)_

**Suggested change:** No change. Source wildcard kept: the question names no code, so an article 13 from any code is an acceptable answer.

- add chunks: none
- drop chunks: none
- proposed gold:
    - any code, article 13

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______
