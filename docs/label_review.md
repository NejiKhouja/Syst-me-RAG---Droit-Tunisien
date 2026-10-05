# Gold-label review sheet

One section per concept. For each: mark **Decision** (approve / reject / edit) for the suggested change.
`H` = chunk starts with a real article heading, `F` = fragment created by an in-text reference ("…de l'article 62 du présent code…"). Candidates are lexical hits for the French question over heading chunks of the gold source; they are evidence, not truth.

---
## penal_theft

- `q001` [fr, penal, concept] Quelle est la peine pour le vol ?
- `q013` [fr, penal, article_lookup] Que dit l'article 258 du code pénal ?
- `q041` [fr, unfiltered, cross_domain] Quelle est la peine pour le vol ?
- `q047` [ar, penal, concept] ما هي عقوبة السرقة؟
- `q066` [ar, unfiltered, cross_domain] ما هي عقوبة السرقة؟
- `q068` [en, penal, concept] What is the penalty for theft?
- `q085` [en, unfiltered, cross_domain] What is the penalty for theft?

**Current gold** (PenalFr.pdf)

- **258** `H` Article 258.- Quiconque soustrait frauduleusement une chose qui ne lui appartient pas est coupable de vol. Est assimilée au vol, l'utilisation frauduleuse d'eau, de gaz, d'électricité au détriment des concessionnaires.
- **260** `H` Article 260 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, le vol commis avec la réunion des cinq circonstances suivantes : 1) à l'aide de violences graves ou de menaces de violences graves envers la victime ou ses proches, 2) à l'aide d'escalade ou d'ouvertur
- **260** `F` article 260 , même s'il n'est pas occupé au moment de l'infraction.
- **260** `F` article 260 , tous instruments fabriqués pour l'attaque ou la défense des personnes. Sont également considérés comme armes, les bâtons, rasoirs, couteaux de poche et tous autres instruments susceptibles de faire des blessures dont le coupable aura fait usage pour commettre le vol.
- **261** `H` Article 261 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de vingt ans de prison, le vol commis à l'aide de l'une des deux premières circonstances édictées par l'article précédent.
- **262** `H` Article 262 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de douze ans de prison, le vol commis avec la réunion des trois dernières circonstances prévues à l'

**Corpus candidates** (BM25 over PenalFr.pdf headings; query terms: peine vol)

- gold **258** (6.0) Article 258.- Quiconque soustrait frauduleusement une chose qui ne lui appartient pas est coupable de vol. Est assimilée au vol, l'utilisation frauduleuse d'eau, de gaz, d'électricité au détriment des
-      **265** (5.5) Article 265.- Tout individu coupable de vol peut être condamné aux peines accessoires prévues par l'
- gold **262** (5.0) Article 262 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de douze ans de prison, le vol commis avec la réunion des trois dernières circonstances prévues à l'
- gold **261** (4.9) Article 261 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de vingt ans de prison, le vol commis à l'aide de l'une des deux premières circonstances édictées par l'article précédent.
-      **274** (4.2) Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confectionné, sciemment, un instrument destiné à commettre u
-      **266** (3.8) Article 266.- Ne constitue pas un vol, la soustraction commise par les ascendants de quelque degré qu’ils soient au préjudice de leurs enfants, à moins que l'objet soustrait n'appartienne pour partie 
- gold **260** (2.9) Article 260 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, le vol commis avec la réunion des cinq circonstances suivantes : 1) à l'aide de violences graves ou d
-      **263** (2.9) Article 263.- Est puni de dix ans d’emprisonnement l’auteur du vol commis : 1°- au cours d'un incendie ou après une explosion, inondation, naufrage, accident de chemin de fer, révolte, émeute ou tout 

**Retrieved by official v1** (top-6, one block per language variant)

- `q001` [fr] hit=False
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 274: Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confection
    -   PenalFr.pd art 263: Article 263.- Est puni de dix ans d’emprisonnement l’auteur du vol commis : 1°- au cours d'un incendie ou après une explosion, inondation, naufrage, a
    -   PenalFr.pd art 186: Article 186 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de quinze ans d'emprisonnement, celui qui contrefait ou altère des monnaies en
    -   PenalFr.pd art 190: Article 190.- Est puni de trois ans d'emprisonnement, quiconque aura coloré les monnaies ayant cours légal en Tunisie ou les monnaies étrangères, dans
- `q013` [fr] hit=True
    - ✓ PenalFr.pd art 258: Article 258.- Quiconque soustrait frauduleusement une chose qui ne lui appartient pas est coupable de vol. Est assimilée au vol, l'utilisation fraudul
- `q041` [fr] hit=False
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 274: Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confection
    -   PenalFr.pd art 186: Article 186 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de quinze ans d'emprisonnement, celui qui contrefait ou altère des monnaies en
    -   PenalFr.pd art 190: Article 190.- Est puni de trois ans d'emprisonnement, quiconque aura coloré les monnaies ayant cours légal en Tunisie ou les monnaies étrangères, dans
    -   PenalFr.pd art 188: Article 188 (Modifié par la loi n° 89-23 du 27 février 1989).- Sont punis d'emprisonnement à vie ceux qui ont contrefait ou falsifié les billets de ba
- `q047` [ar] hit=False
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 62: article 62 du présent code, sans préjudice, le cas échéant, des peines encourues pour la tentative des crimes prévus aux articles 60 et 60 bis du prés
    -   PenalFr.pd art 274: Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confection
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 263: Article 263.- Est puni de dix ans d’emprisonnement l’auteur du vol commis : 1°- au cours d'un incendie ou après une explosion, inondation, naufrage, a
    -   PenalFr.pd art 60: Article 60 bis (Ajouté par le décret du 10 janvier 1957).- Est coupable de trahison et puni de mort : 1°- tout Tunisien qui aura livré à une puissance
- `q066` [ar] hit=False
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 62: article 62 du présent code, sans préjudice, le cas échéant, des peines encourues pour la tentative des crimes prévus aux articles 60 et 60 bis du prés
    -   CommerceFr art 53: article 53 du code pénal ne s’appliquent pas à l’amende prévue à l’alinéa premier du présent article. Est puni d’une amende égale à quarante pour cent
    -   PenalFr.pd art 274: Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confection
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 263: Article 263.- Est puni de dix ans d’emprisonnement l’auteur du vol commis : 1°- au cours d'un incendie ou après une explosion, inondation, naufrage, a
- `q068` [en] hit=True
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 62: article 62 du présent code, sans préjudice, le cas échéant, des peines encourues pour la tentative des crimes prévus aux articles 60 et 60 bis du prés
    -   PenalFr.pd art 274: Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confection
    -   PenalFr.pd art 247: Article 247.- Est puni de six mois d’emprisonnement et de deux cent quarante dinars d’amende, quiconque, se sera rendu coupable de diffamation. Est pu
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    - ✓ PenalFr.pd art 262: Article 262 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de douze ans de prison, le vol commis avec la réunion des trois dernières circ
- `q085` [en] hit=True
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 62: article 62 du présent code, sans préjudice, le cas échéant, des peines encourues pour la tentative des crimes prévus aux articles 60 et 60 bis du prés
    -   PenalFr.pd art 274: Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confection
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    - ✓ PenalFr.pd art 262: Article 262 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de douze ans de prison, le vol commis avec la réunion des trois dernières circ
    -   PenalFr.pd art 263: Article 263.- Est puni de dix ans d’emprisonnement l’auteur du vol commis : 1°- au cours d'un incendie ou après une explosion, inondation, naufrage, a

**Suggested change:** Add 263 (theft committed during fire/explosion etc., 10 years) and 264 ("tous autres vols", 5 years): both are theft penalties in the corpus, and 264 is the single most frequent 'wrong' result in the v1 baseline.

- add: 263, 264   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **258** `Article 258`
        > Article 258.- Quiconque soustrait frauduleusement une chose qui ne lui appartient pas est coupable de vol. Est assimilée au vol, l'utilisation fraudul
    - **260** `Article 260 (Modifié par la loi n° 89-23`
        > Article 260 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, le vol commis avec la réunion des cinq circonstance
    - **261** `Article 261`
        > Article 261 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de vingt ans de prison, le vol commis à l'aide de l'une des deux premières cir
    - **262** `Article 262`
        > Article 262 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de douze ans de prison, le vol commis avec la réunion des trois dernières circ
    - NEW **263** `Article 263`
        > Article 263.- Est puni de dix ans d’emprisonnement l’auteur du vol commis : 1°- au cours d'un incendie ou après une explosion, inondation, naufrage, a
    - NEW **264** `Article 264`
        > Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_homicide

- `q002` [fr, penal, concept] Qu'est-ce que le meurtre ?
- `q014` [fr, penal, article_lookup] Que dit l'article 201 ?
- `q049` [ar, penal, concept] ما هي عقوبة القتل العمد؟
- `q069` [en, penal, concept] What is the penalty for murder?

**Current gold** (PenalFr.pdf)

- **201** `H` Article 201.- Est puni de mort, quiconque aura, par quelque moyen que ce soit, commis volontairement et avec préméditation un homicide.
- **202** `H` Article 202.- La préméditation consiste dans le dessein, formé avant l'action, d'attentat à la personne d'autrui.
- **203** `H` Article 203.- Est puni de mort, l’auteur de parricide. Est qualifié parricide, le meurtre des ascendants quel qu’en soit le degré.

**Corpus candidates** (BM25 over PenalFr.pdf headings; query terms: meurtre)

- gold **203** (6.4) Article 203.- Est puni de mort, l’auteur de parricide. Est qualifié parricide, le meurtre des ascendants quel qu’en soit le degré.
-      **205** (6.0) Article 205 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni d'emprisonnement à vie le coupable de meurtre dans tous les cas non prévus par les articles ci-dessus. 63
-      **211** (5.9) Article 211 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de deux ans de prison, le meurtre commis par la mère sur son enfant à sa naissance ou immédiatement après.
-      **72** (5.3) Article 72.- Est puni de mort, l’auteur de l'attentat ayant pour but de changer la forme du gouvernement, d'inciter les gens à s'armer les uns contre les autres ou à provoquer le désordre, le meurtre 

**Retrieved by official v1** (top-6, one block per language variant)

- `q002` [fr] hit=True
    -   PenalFr.pd art 72: Article 72.- Est puni de mort, l’auteur de l'attentat ayant pour but de changer la forme du gouvernement, d'inciter les gens à s'armer les uns contre 
    -   PenalFr.pd art 60: Article 60 (Modifié par le décret du 10 janvier 1957).- Est coupable de trahison et puni de mort : 1° - tout Tunisien qui aura porté les armes contre 
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 185: Article 185 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, celui qui contrefait ou altère la monnaie fiduciair
    - ✓ PenalFr.pd art 201: Article 201.- Est puni de mort, quiconque aura, par quelque moyen que ce soit, commis volontairement et avec préméditation un homicide.
    -   PenalFr.pd art 188: Article 188 (Modifié par la loi n° 89-23 du 27 février 1989).- Sont punis d'emprisonnement à vie ceux qui ont contrefait ou falsifié les billets de ba
- `q014` [fr] hit=True
    - ✓ PenalFr.pd art 201: Article 201.- Est puni de mort, quiconque aura, par quelque moyen que ce soit, commis volontairement et avec préméditation un homicide.
- `q049` [ar] hit=True
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 62: article 62 du présent code, sans préjudice, le cas échéant, des peines encourues pour la tentative des crimes prévus aux articles 60 et 60 bis du prés
    -   PenalFr.pd art 208: Article 208 (Modifié par la loi n° 89-23 du 27 février 1989).- Le coupable est puni de vingt ans d'emprisonnement, si les coups portés ou les blessure
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 170: Article 170.- Est puni de six mois d’emprisonnement et de soixante douze dinars d’amende, quiconque aura déplacé, enterré clandestinement ou fait disp
    - ✓ PenalFr.pd art 201: Article 201.- Est puni de mort, quiconque aura, par quelque moyen que ce soit, commis volontairement et avec préméditation un homicide.
- `q069` [en] hit=True
    -   PenalFr.pd art 62: article 62 du présent code, sans préjudice, le cas échéant, des peines encourues pour la tentative des crimes prévus aux articles 60 et 60 bis du prés
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 208: Article 208 (Modifié par la loi n° 89-23 du 27 février 1989).- Le coupable est puni de vingt ans d'emprisonnement, si les coups portés ou les blessure
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    - ✓ PenalFr.pd art 201: Article 201.- Est puni de mort, quiconque aura, par quelque moyen que ce soit, commis volontairement et avec préméditation un homicide.
    -   PenalFr.pd art 170: Article 170.- Est puni de six mois d’emprisonnement et de soixante douze dinars d’amende, quiconque aura déplacé, enterré clandestinement ou fait disp

**Suggested change:** Add 204 (homicide preceded/accompanied by another offence: death) and 205 (meurtre in all cases not provided above: life imprisonment): they define/penalise murder directly. 201-203 unchanged.

- add: 204, 205   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **201** `Article 201`
        > Article 201.- Est puni de mort, quiconque aura, par quelque moyen que ce soit, commis volontairement et avec préméditation un homicide.
    - **202** `Article 202`
        > Article 202.- La préméditation consiste dans le dessein, formé avant l'action, d'attentat à la personne d'autrui.
    - **203** `Article 203`
        > Article 203.- Est puni de mort, l’auteur de parricide. Est qualifié parricide, le meurtre des ascendants quel qu’en soit le degré.
    - NEW **204** `Article 204`
        > Article 204 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de mort, l’auteur de l'homicide volontaire lorsque l’homicide a été précédé, a
    - NEW **205** `Article 205`
        > Article 205 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni d'emprisonnement à vie le coupable de meurtre dans tous les cas non prévus par

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_corruption

- `q003` [fr, penal, concept] Quelle est la peine pour la corruption ?
- `q048` [ar, penal, concept] ما هي عقوبة الرشوة؟
- `q071` [en, penal, concept] What is the penalty for bribery?

**Current gold** (PenalFr.pdf)

- **84** `H` Article 84 (Modifié par la loi n° 98-33 du 23 mai 1998).- Si le fonctionnaire public ou assimilé a provoqué la corruption, la peine prévue à l'
- **85** `H` Article 85 (Modifié par la loi n° 98-33 du 23 mai 1998).- Si le fonctionnaire public ou assimilé a accepté des dons, promesses, présents ou avantages de quelque nature que ce soit en récompense d'actes qu'il a accomplis et qui sont liés à sa fonction, mais non sujet à contre partie, ou d'un acte qu'
- **86** `H` Article 86 (Abrogé par la loi n° 1998-33 du 23 mai 1998) .

**Corpus candidates** (BM25 over PenalFr.pdf headings; query terms: peine corruption)

- gold **84** (6.7) Article 84 (Modifié par la loi n° 98-33 du 23 mai 1998).- Si le fonctionnaire public ou assimilé a provoqué la corruption, la peine prévue à l'
-      **147** (6.5) Article 147 (Modifié par la loi n° 89-23 du 27 février 1989).- Est augmentée d'un an, la peine du condamné à l'emprisonnement à temps qui s'est évadé ou tenté de s'évader. S'il y a eu violence, bris d
-      **89** (5.7) Article 89 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni, le juge corrompu, de la même peine prononcée contre le prévenu par l'effet de la corruption, à condition que la peine prononcée 
-      **146** (5.1) Article 146.- Tout prévenu qui s'évade du lieu de sa détention ou se délivre des mains de ses gardiens à l'aide de violences, de menaces ou de bris de prison est puni d'un emprisonnement d'un an. La t
-      **92** (5.1) Article 92 (Modifié par la loi n° 98-33 du 23 mai 1998).- La peine est d'un an d'emprisonnement et de mille dinars d'amende, si la tentative de corruption n'a eu aucun effet. Elle est de deux ans d'em
-      **94** (4.9) Article 94.- Dans tous les cas de corruption, les choses données ou reçues sont confisquées au profit de l'Etat. Section III - La concussion
-      **93** (4.7) Article 93.- Est absous le corrupteur ou l'intermédiaire qui, avant toute poursuite, révèle volontairement le fait de corruption et, en même temps, en rapporte la preuve.
-      **234** (3.5) ABROGATED Article 234 (Abrogé par le décret du 26 mai 1949 et ajouté par la loi n° 64-34 du 2 juillet 1964).- Sous réserve des peines plus fortes prévues par l'article précédent, sera puni d'un à trois ans d'em

**Retrieved by official v1** (top-6, one block per language variant)

- `q003` [fr] hit=False
    -   PenalFr.pd art 92: Article 92 (Modifié par la loi n° 98-33 du 23 mai 1998).- La peine est d'un an d'emprisonnement et de mille dinars d'amende, si la tentative de corrup
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 234: Article 234 (Abrogé par le décret du 26 mai 1949 et ajouté par la loi n° 64-34 du 2 juillet 1964).- Sous réserve des peines plus fortes prévues par l'
    -   PenalFr.pd art 186: Article 186 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de quinze ans d'emprisonnement, celui qui contrefait ou altère des monnaies en
    -   PenalFr.pd art 218: article 218 du présent code. La peine est de dix ans d'emprisonnement est et de quatre cent quatre vingt dinars d'amende si, dans ce dernier cas, les 
    -   PenalFr.pd art 128: Article 128.- Est puni de deux ans d’emprisonnement et de cent vingt dinars d’amende, quiconque par discours publics, presse ou tous autres moyens de 
- `q048` [ar] hit=False
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 234: Article 234 (Abrogé par le décret du 26 mai 1949 et ajouté par la loi n° 64-34 du 2 juillet 1964).- Sous réserve des peines plus fortes prévues par l'
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 92: Article 92 (Modifié par la loi n° 98-33 du 23 mai 1998).- La peine est d'un an d'emprisonnement et de mille dinars d'amende, si la tentative de corrup
    -   PenalFr.pd art 188: Article 188 (Modifié par la loi n° 89-23 du 27 février 1989).- Sont punis d'emprisonnement à vie ceux qui ont contrefait ou falsifié les billets de ba
    -   PenalFr.pd art 155: article 155 du présent code. La peine est de douze ans d'emprisonnement si l’auteur de l’infraction est le dépositaire lui-même.
- `q071` [en] hit=False
    -   PenalFr.pd art 234: Article 234 (Abrogé par le décret du 26 mai 1949 et ajouté par la loi n° 64-34 du 2 juillet 1964).- Sous réserve des peines plus fortes prévues par l'
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 92: Article 92 (Modifié par la loi n° 98-33 du 23 mai 1998).- La peine est d'un an d'emprisonnement et de mille dinars d'amende, si la tentative de corrup
    -   PenalFr.pd art 188: Article 188 (Modifié par la loi n° 89-23 du 27 février 1989).- Sont punis d'emprisonnement à vie ceux qui ont contrefait ou falsifié les billets de ba
    -   PenalFr.pd art 247: Article 247.- Est puni de six mois d’emprisonnement et de deux cent quarante dinars d’amende, quiconque, se sera rendu coupable de diffamation. Est pu
    -   PenalFr.pd art 233: Article 233 (Abrogé par le décret du 26 mai 1949 et ajouté par la loi 64-34 du 2 juillet 1964).- La peine sera d'un emprisonnement de trois à cinq ans

**Suggested change:** Remove 86: its heading says 'Abrogé par la loi n° 1998-33' (empty article). Add 83 (fonctionnaire who agrees to offers/promises, i.e. passive corruption) and 91 (person who corrupted or attempted to corrupt, 5 years). 84-85 unchanged.

- add: 83, 91   |   remove: 86
- proposed gold (anchor = the text the intended chunk must start with):
    - NEW **83** `Article 83`
        > Article 83 (Modifié par la loi n° 98-33 du 23 mai 1998).- Toute personne ayant la qualité de fonctionnaire public ou assimilé conformément aux disposi
    - **84** `Article 84`
        > Article 84 (Modifié par la loi n° 98-33 du 23 mai 1998).- Si le fonctionnaire public ou assimilé a provoqué la corruption, la peine prévue à l'
    - **85** `Article 85`
        > Article 85 (Modifié par la loi n° 98-33 du 23 mai 1998).- Si le fonctionnaire public ou assimilé a accepté des dons, promesses, présents ou avantages 
    - NEW **91** `Article 91`
        > Article 91 (Modifié par la loi n° 98-33 du 23 mai 1998).- Est punie de cinq ans d'emprisonnement et de cinq mille dinars d'amende, toute personne qui 

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_fraud

- `q004` [fr, penal, concept] Quelle est la peine pour l'escroquerie ?
- `q050` [ar, penal, concept] ما هي عقوبة الاحتيال؟
- `q070` [en, penal, concept] How is fraud punished?

**Current gold** (PenalFr.pdf)

- **291** `H` Article 291 (Modifié par le décret du 8 octobre 1935).- Est puni de cinq ans d’emprisonnement et de deux mille quatre cents dinars d’amende, quiconque, soit en faisant usage de faux noms ou de fausses qualités, soit en employant des ruses ou artifices propres à persuader de l'existence de fausses en
- **291** `F` article 291 du présent code, quiconque, amène, frauduleusement, autrui à quitter le territoire tunisien en alléguant de faits inexistants ou en usant de fausses nouvelles.
- **291** `F` article 291 , celui qui, prétendant connaître le lieu où se trouvent des objets ou des animaux égarés ou volés, se fait remettre une somme d'argent sous promesse de les faire retrouver ou de les ramener. Section V - Abus de confiance - appropriations illégitimes

**Corpus candidates** (BM25 over PenalFr.pdf headings; query terms: peine escroquerie)

-      **290** (5.7) Article 290.- Est puni de deux ans d’emprisonnement, le commerçant qui s'est réduit à l'insolvabilité par sa prodigalité ou par des spéculations hasardeuses ne rentrant pas dans le cercle ordinaire de
-      **292** (4.7) Article 292.- Est assimilé à l'escroquerie et puni des peines prévues à l'article précédent, le fait : 85 1) de vendre, hypothéquer, mettre en gage ou louer des biens dont on n'a pas le droit de dispo
-      **6** (1.7) Article 6.- Le présent code détermine pour chaque infraction le maximum de la peine encourue. Le minimum de chaque peine est déterminé par ses articles 14 et 16.
-      **54** (1.7) Article 54.- Lorsque le même fait constitue plusieurs infractions, la peine encourue pour l'infraction entraînant la peine la plus forte est seule prononcée.
-      **43** (1.6) Article 43 (Modifié par la loi n° 89-23 du 27 février 1989 et la loi n° 95-93 du 9 novembre 1995).- La loi pénale est applicable aux délinquants âgés de plus de treize ans révolus et moins de dix huit
-      **15** (1.6) Article 15 quater (ajouté par la loi n°2009-68 du 12 août 2009).- La peine de réparation pénale tend à remplacer la peine d'emprisonnement prononcée par le tribunal par une réparation pécuniaire que d
-      **34** (1.6) Article 34 (Modifié par la loi n° 89-23 du 27 février 1989).- La peine de mort, lorsqu'elle est applicable aux auteurs principaux d'une infraction, est remplacée à l'égard des complices qui se sont re
-      **123** (1.6) Article 123.- La peine prononcée contre l’auteur de rébellion parmi les prisonniers s'ajoute à celle qu’il est entrain de purger. Si l’auteur de la rébellion est en état de détention préventive, la pe

**Retrieved by official v1** (top-6, one block per language variant)

- `q004` [fr] hit=False
    -   PenalFr.pd art 62: article 62 du présent code, sans préjudice, le cas échéant, des peines encourues pour la tentative des crimes prévus aux articles 60 et 60 bis du prés
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 292: Article 292.- Est assimilé à l'escroquerie et puni des peines prévues à l'article précédent, le fait : 85 1) de vendre, hypothéquer, mettre en gage ou
    -   PenalFr.pd art 233: Article 233 (Abrogé par le décret du 26 mai 1949 et ajouté par la loi 64-34 du 2 juillet 1964).- La peine sera d'un emprisonnement de trois à cinq ans
    -   PenalFr.pd art 155: article 155 du présent code. La peine est de douze ans d'emprisonnement si l’auteur de l’infraction est le dépositaire lui-même.
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
- `q050` [ar] hit=False
    -   PenalFr.pd art 62: article 62 du présent code, sans préjudice, le cas échéant, des peines encourues pour la tentative des crimes prévus aux articles 60 et 60 bis du prés
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 275: Article 275.- Est puni de deux mois d’emprisonnement, l’artisan serrurier ou tout autre artisan qui vend ou remet à une personne, sans s’assurer de sa
    -   PenalFr.pd art 274: Article 274.- Est puni de deux ans d’emprisonnement et de trente six dinars d’amende quiconque, aura contrefait ou altéré des clefs ou aura confection
    -   PenalFr.pd art 164: Article 164.- Est puni de dix ans d'emprisonnement et de deux cent quarante dinars d’amende, quiconque aura, en dehors du cas prévu à l’
    -   PenalFr.pd art 247: Article 247.- Est puni de six mois d’emprisonnement et de deux cent quarante dinars d’amende, quiconque, se sera rendu coupable de diffamation. Est pu
- `q070` [en] hit=False
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 188: Article 188 (Modifié par la loi n° 89-23 du 27 février 1989).- Sont punis d'emprisonnement à vie ceux qui ont contrefait ou falsifié les billets de ba
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 116: Article 116.- Est puni de six mois d'emprisonnement et de quarante huit dinars d’amende, quiconque exerce ou menace d'exercer des violences pour résis
    -   PenalFr.pd art 62: article 62 du présent code, sans préjudice, le cas échéant, des peines encourues pour la tentative des crimes prévus aux articles 60 et 60 bis du prés
    -   PenalFr.pd art 186: Article 186 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de quinze ans d'emprisonnement, celui qui contrefait ou altère des monnaies en

**Suggested change:** Add 292: 'assimilé à l'escroquerie et puni des peines prévues à l'article précédent'. 291 is anchored to the main article (two fragment chunks also carry number 291).

- add: 292   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **291** `Article 291 (Modifié par le décret du 8 octobre 1935)`
        > Article 291 (Modifié par le décret du 8 octobre 1935).- Est puni de cinq ans d’emprisonnement et de deux mille quatre cents dinars d’amende, quiconque
    - NEW **292** `Article 292`
        > Article 292.- Est assimilé à l'escroquerie et puni des peines prévues à l'article précédent, le fait : 85 1) de vendre, hypothéquer, mettre en gage ou

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_breach_of_trust

- `q005` [fr, penal, concept] Qu'est-ce que l'abus de confiance ?

**Current gold** (PenalFr.pdf)

- **297** `H` Article 297.- Est puni de trois ans d’emprisonnement et de deux cent quarante dinars d’amende, quiconque détourne ou dissipe, tente de détourner ou dissiper au préjudice des propriétaires, possesseurs ou détenteurs, des effets, deniers, marchandises, billets, quittances ou tous autres écrits contena

**Corpus candidates** (BM25 over PenalFr.pdf headings; query terms: abus confiance)

-      **233** (3.7) ABROGATED Article 233 (Abrogé par le décret du 26 mai 1949 et ajouté par la loi 64-34 du 2 juillet 1964).- La peine sera d'un emprisonnement de trois à cinq ans et d'une amende de cinq cents à mille dinars dans
-      **321** (2.6) Article 321 bis (Ajouté par la loi organique n° 2001-43 du 3 mai 2001, portant modification du code de la presse).- Quiconque voudra exercer, sur la voie publique ou en tout autre lieu public ou privé
-      **32** (2.3) Article 32.- Est considéré complice et puni comme tel : 1°- celui qui, par dons, promesses, menaces, abus d'autorité ou de pouvoir, machinations, artifices coupables, a provoqué à l'action ou donné de

**Retrieved by official v1** (top-6, one block per language variant)

- `q005` [fr] hit=False
    -   PenalFr.pd art 185: Article 185 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, celui qui contrefait ou altère la monnaie fiduciair
    -   PenalFr.pd art 301: Article 301 (Modifié et complété par les décrets datés du 8 octobre 1935 et du 1er février 1945).- Est puni de trois ans d’emprisonnement et de cent d
    -   PenalFr.pd art 60: Article 60 (Modifié par le décret du 10 janvier 1957).- Est coupable de trahison et puni de mort : 1° - tout Tunisien qui aura porté les armes contre 
    -   PenalFr.pd art 223: Article 223.- Est puni d'un an d’emprisonnement et de deux cent vingt dinars d’amende, quiconque aura menacé autrui à l’aide d’une arme, même sans int
    -   PenalFr.pd art 241: Article 241 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de la peine prévue pour l'infraction poursuivie, celui qui, dans une affaire p
    -   PenalFr.pd art 103: Article 103 (Ajouté art. premier D.L n° 2011-106 du 22 octobre 2011).- Est puni d'un emprisonnement de cinq ans et d'une amende de cinq milles dinars 

**Suggested change:** No change; only anchored to the real heading (297 is the abus de confiance article).

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **297** `Article 297`
        > Article 297.- Est puni de trois ans d’emprisonnement et de deux cent quarante dinars d’amende, quiconque détourne ou dissipe, tente de détourner ou di

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_defamation

- `q006` [fr, penal, concept] Que dit la loi sur la diffamation ?

**Current gold** (PenalFr.pdf)

- **245** `H` Article 245.- Il y a diffamation dans toute allégation ou imputation publique d'un fait qui porte atteinte à l'honneur ou à la considération d'une personne ou d'un corps constitué. La preuve du fait diffamatoire peut être établie dans les cas prévus à l'
- **246** `H` Article 246.- Il y a calomnie : 1) lorsque le fait diffamatoire a été judiciairement déclaré non établi, 2) lorsque le prévenu ne peut rapporter la preuve dudit fait dans le cas où la loi l'y autorise. La calomnie est punissable même si les imputations ont été faites par écrits non rendus publics, m

**Corpus candidates** (BM25 over PenalFr.pdf headings; query terms: diffamation)

- gold **245** (5.8) Article 245.- Il y a diffamation dans toute allégation ou imputation publique d'un fait qui porte atteinte à l'honneur ou à la considération d'une personne ou d'un corps constitué. La preuve du fait d
-      **247** (5.2) Article 247.- Est puni de six mois d’emprisonnement et de deux cent quarante dinars d’amende, quiconque, se sera rendu coupable de diffamation. Est puni d'un an d’emprisonnement et de deux cent quaran
-      **15** (1.1) Article 15 bis (Ajouté par la loi n° 99-89 du 2 août 1999).- Dans le cas où le tribunal prononce une peine de prison ferme d’une durée ne dépassant pas un an, il peut la remplacer dans le même jugemen

**Retrieved by official v1** (top-6, one block per language variant)

- `q006` [fr] hit=False
    -   PenalFr.pd art 4: Art. 4.- Il ne découle de la réorganisation du code pénal et de sa nouvelle rédaction aucune modification quant au fond. La présente loi sera publiée 
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 188: Article 188 (Modifié par la loi n° 89-23 du 27 février 1989).- Sont punis d'emprisonnement à vie ceux qui ont contrefait ou falsifié les billets de ba
    -   PenalFr.pd art 291: article 291 du présent code, quiconque, amène, frauduleusement, autrui à quitter le territoire tunisien en alléguant de faits inexistants ou en usant 
    -   PenalFr.pd art 185: Article 185 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, celui qui contrefait ou altère la monnaie fiduciair
    -   PenalFr.pd art 72: Article 72.- Est puni de mort, l’auteur de l'attentat ayant pour but de changer la forme du gouvernement, d'inciter les gens à s'armer les uns contre 

**Suggested change:** Add 247: it is the penalty article ('Est puni de six mois d'emprisonnement ... diffamation'); 245 defines diffamation, 246 defines calomnie. 247 is a frequent 'wrong' result in v1 because it is in fact relevant.

- add: 247   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **245** `Article 245`
        > Article 245.- Il y a diffamation dans toute allégation ou imputation publique d'un fait qui porte atteinte à l'honneur ou à la considération d'une per
    - **246** `Article 246`
        > Article 246.- Il y a calomnie : 1) lorsque le fait diffamatoire a été judiciairement déclaré non établi, 2) lorsque le prévenu ne peut rapporter la pr
    - NEW **247** `Article 247`
        > Article 247.- Est puni de six mois d’emprisonnement et de deux cent quarante dinars d’amende, quiconque, se sera rendu coupable de diffamation. Est pu

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_rape

- `q007` [fr, penal, concept] Comment est puni le viol ?
- `q051` [ar, penal, concept] ما هي عقوبة الاغتصاب؟

**Current gold** (PenalFr.pdf)

- **227** `H` Article 227 (Modifié par la loi n° 85-9 du 7 mars 1985 et par la loi n° 89-23 du 27 février 1989).- Est puni de mort : 69 1) le crime de viol commis avec violence, usage ou menace d'usage d'arme. 2) le crime de viol commis même sans usage des moyens précités sur une personne âgée de moins de dix ans
- **227** `H` Article 227 bis (Ajouté par la loi n° 1958 du 4 mars 1958 et modifié par la loi n° 69-21 du 27 mars 1969 et modifié par la loi n° 89-23 du 27 février 1989).- Est puni d'emprisonnement pendant six ans, celui qui fait subir sans violence, l'acte sexuel à un enfant de sexe féminin âgé de moins de quinz

**Corpus candidates** (BM25 over PenalFr.pdf headings; query terms: puni viol)

- gold **227** (10.0) Article 227 (Modifié par la loi n° 85-9 du 7 mars 1985 et par la loi n° 89-23 du 27 février 1989).- Est puni de mort : 69 1) le crime de viol commis avec violence, usage ou menace d'usage d'arme. 2) l
-      **293** (2.1) Article 293.- Est puni des peines prévues à l'
-      **295** (2.1) Article 295.- Est puni des peines prévues à l'
-      **279** (2.0) Article 279.- Est puni des peines prévues au deuxième paragraphe de l’
-      **296** (1.9) Article 296 (Modifié par le décret du 18 avril 1946).- Est puni des peines prévues à l'
-      **63** (1.9) Article 63.- L'attentat contre la vie du chef de l'État est puni de mort.
-      **247** (1.9) Article 247.- Est puni de six mois d’emprisonnement et de deux cent quarante dinars d’amende, quiconque, se sera rendu coupable de diffamation. Est puni d'un an d’emprisonnement et de deux cent quaran
-      **206** (1.9) Article 206.- Est puni de cinq ans d'emprisonnement, celui qui, sciemment, aide à un suicide.

**Retrieved by official v1** (top-6, one block per language variant)

- `q007` [fr] hit=True
    - ✓ PenalFr.pd art 227: Article 227 (Modifié par la loi n° 85-9 du 7 mars 1985 et par la loi n° 89-23 du 27 février 1989).- Est puni de mort : 69 1) le crime de viol commis a
    -   PenalFr.pd art 218: article 218 du présent code. La peine est de dix ans d'emprisonnement est et de quatre cent quatre vingt dinars d'amende si, dans ce dernier cas, les 
    -   PenalFr.pd art 319: article 319 du présent code, dans l'exercice ou à l'occasion de l'exercice de ses fonctions. La peine est de cinq ans d'emprisonnement et de deux cent
    -   PenalFr.pd art 231: Article 231 (Abrogé par le décret du 26 mai 1949 et ajouté par la loi n° 64-34 du 2 juillet 1964 puis modifié par la loi n° 68-1 du 8 mars 1968).- Hor
    -   PenalFr.pd art 223: Article 223.- Est puni d'un an d’emprisonnement et de deux cent vingt dinars d’amende, quiconque aura menacé autrui à l’aide d’une arme, même sans int
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
- `q051` [ar] hit=False
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 223: Article 223.- Est puni d'un an d’emprisonnement et de deux cent vingt dinars d’amende, quiconque aura menacé autrui à l’aide d’une arme, même sans int
    -   PenalFr.pd art 164: Article 164.- Est puni de dix ans d'emprisonnement et de deux cent quarante dinars d’amende, quiconque aura, en dehors du cas prévu à l’
    -   PenalFr.pd art 319: article 319 du présent code, dans l'exercice ou à l'occasion de l'exercice de ses fonctions. La peine est de cinq ans d'emprisonnement et de deux cent
    -   PenalFr.pd art 226: Article 226 ter (Ajouté par la loi n° 2004-73 du 2 août 2004).- Est puni d’un an d’emprisonnement et d’une amende de trois mille dinars celui qui comm

**Suggested change:** No change in articles; anchors separate 227 and 227 bis (same law, both about rape / sexual acts without violence).

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **227** `Article 227 (Modifié par la loi n° 85-9`
        > Article 227 (Modifié par la loi n° 85-9 du 7 mars 1985 et par la loi n° 89-23 du 27 février 1989).- Est puni de mort : 69 1) le crime de viol commis a
    - **227** `Article 227 bis`
        > Article 227 bis (Ajouté par la loi n° 1958 du 4 mars 1958 et modifié par la loi n° 69-21 du 27 mars 1969 et modifié par la loi n° 89-23 du 27 février 

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_harassment

- `q008` [fr, penal, concept] Quelle est la sanction du harcèlement sexuel ?

**Current gold** (PenalFr.pdf)

- **226** `H` Article 226.- Est puni de six mois d'emprisonnement et de quarante huit dinars d’amende, quiconque se sera, sciemment, rendu coupable d'outrage public à la pudeur. 68
- **226** `H` Article 226 bis (Ajouté par la loi n° 2004-73 du 2 août 2004).- Est puni de six mois d’emprisonnement et d’une amende de mille dinars quiconque porte publiquement atteinte aux bonnes mœurs ou à la morale publique par le geste ou la parole ou gène intentionnellement autrui d’une façon qui porte attei
- **226** `H` Article 226 ter (Ajouté par la loi n° 2004-73 du 2 août 2004).- Est puni d’un an d’emprisonnement et d’une amende de trois mille dinars celui qui commet le harcèlement sexuel. Est considéré comme harcèlement sexuel toute persistance dans la gène d’autrui par la répétition d’actes ou de paroles ou de
- **226** `H` Article 226 quater (Ajouté par la loi n° 2004-73 du 2 août 2004).- Les peines prévues aux deux articles précédents ne préjudicient pas à l’application des peines plus sévères prévues pour d’autres infractions. Les poursuites ne peuvent être exercées qu’à la demande du ministère public sur la base d’

**Corpus candidates** (BM25 over PenalFr.pdf headings; query terms: sanction harcèlement sexuel)

- gold **226** (12.5) Article 226 ter (Ajouté par la loi n° 2004-73 du 2 août 2004).- Est puni d’un an d’emprisonnement et d’une amende de trois mille dinars celui qui commet le harcèlement sexuel. Est considéré comme harc
-      **319** (4.3) Article 319.- Sont passibles des mêmes peines, les auteurs de rixes et ceux qui se livrent à des voies de fait ou à des violences n'entraînant pour la santé d'autrui aucune conséquence sérieuse ou dur
-      **227** (3.3) Article 227 bis (Ajouté par la loi n° 1958 du 4 mars 1958 et modifié par la loi n° 69-21 du 27 mars 1969 et modifié par la loi n° 89-23 du 27 février 1989).- Est puni d'emprisonnement pendant six ans,
-      **15** (2.8) Article 15 ter (Ajouté par la loi n° 99-89 du 2 août 1999).- Pour remplacer la peine d'emprisonnement par la peine de travail d’intérêt général, il est exigé que l’inculpé soit présent à l’audience, q
-      **248** (2.4) Article 248 (Modifié par la loi n° 58-73 du 4 juillet 1958).- Est puni de deux à cinq ans d'emprisonnement et de sept cent vingt dinars d’amende, quiconque aura, par quelque moyen que ce soit, fait un

**Retrieved by official v1** (top-6, one block per language variant)

- `q008` [fr] hit=True
    - ✓ PenalFr.pd art 226: Article 226 ter (Ajouté par la loi n° 2004-73 du 2 août 2004).- Est puni d’un an d’emprisonnement et d’une amende de trois mille dinars celui qui comm
    -   PenalFr.pd art 231: Article 231 (Abrogé par le décret du 26 mai 1949 et ajouté par la loi n° 64-34 du 2 juillet 1964 puis modifié par la loi n° 68-1 du 8 mars 1968).- Hor
    -   PenalFr.pd art 234: Article 234 (Abrogé par le décret du 26 mai 1949 et ajouté par la loi n° 64-34 du 2 juillet 1964).- Sous réserve des peines plus fortes prévues par l'
    -   PenalFr.pd art 223: Article 223.- Est puni d'un an d’emprisonnement et de deux cent vingt dinars d’amende, quiconque aura menacé autrui à l’aide d’une arme, même sans int
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 228: Article 228 (Modifié par la loi n° 95-93 du 9 novembre 1995).- Est puni d'un emprisonnement pendant six ans, l'attentat à la pudeur, commis sur une pe

**Suggested change:** Narrow: the harassment article is 226 ter ('commet le harcèlement sexuel', 1 year + 3000 dinars). 226 (outrage public à la pudeur) and 226 bis (atteinte aux bonnes moeurs) are different offences. Keep 226 quater (rules attached to the two preceding articles).

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **226** `Article 226 ter`
        > Article 226 ter (Ajouté par la loi n° 2004-73 du 2 août 2004).- Est puni d’un an d’emprisonnement et d’une amende de trois mille dinars celui qui comm
    - **226** `Article 226 quater`
        > Article 226 quater (Ajouté par la loi n° 2004-73 du 2 août 2004).- Les peines prévues aux deux articles précédents ne préjudicient pas à l’application

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_self_defence

- `q009` [fr, penal, concept] Qu'est-ce que la légitime défense ?
- `q052` [ar, penal, concept] ما هو الدفاع الشرعي؟
- `q072` [en, penal, concept] What counts as self-defence?

**Current gold** (PenalFr.pdf)

- **39** `H` Article 39.- Il n'y a pas d'infraction lorsque l'auteur y a été contraint par une circonstance qui exposait sa vie ou celle de l’un de ses proches à un danger imminent, et lorsque ce danger ne pouvait être autrement détourné. Sont considérés comme proches : 18 1°- les ascendants et descendants, 2°- 

**Corpus candidates** (BM25 over PenalFr.pdf headings; query terms: légitime défense)

-      **22** (5.5) Article 22.- L'interdiction de séjour consiste dans la défense faite au condamné de résider et de paraître dans les lieux ou régions déterminés par le jugement. Elle est prononcée dans les cas prévus 
-      **60** (5.4) Article 60 bis (Ajouté par le décret du 10 janvier 1957).- Est coupable de trahison et puni de mort : 1°- tout Tunisien qui aura livré à une puissance étrangère ou à ses agents, de quelque manière et 
-      **276** (5.3) Article 276.- Est puni de six mois de prison celui qui, ayant été précédemment condamné à une peine corporelle pour un attentat contre la propriété, est trouvé en possession de numéraire, valeurs ou o
-      **298** (4.9) Article 298.- Est puni de six mois d'emprisonnement et de soixante douze dinars d'amende, quiconque, s'étant fait remettre des avances en vue de l'exécution d'un contrat, refuse sans motif légitime d'
-      **101** (4.7) Article 101.- Est puni de cinq ans d'emprisonnement et de cent vingt dinars d'amende, tout fonctionnaire public ou assimilé qui, dans l'exercice ou à l'occasion de l'exercice de ses fonctions aura, sa
-      **107** (4.0) Article 107.- Le concert, arrêté entre deux ou plusieurs fonctionnaires ou assimilés en vue de faire obstacle par voie de démission collective ou autrement, à l'exécution des lois ou d'un service publ
-      **60** (3.6) Article 60 quater (Ajouté par le décret du 10 janvier 1957).- Est considéré secret défense nationale : 1°- Les renseignements d'ordre militaire, diplomatique, économique ou industriel qui, par leur na
-      **103** (3.5) Article 103 (Ajouté art. premier D.L n° 2011-106 du 22 octobre 2011).- Est puni d'un emprisonnement de cinq ans et d'une amende de cinq milles dinars tout fonctionnaire public ou assimilé qui, sans mo

**Retrieved by official v1** (top-6, one block per language variant)

- `q009` [fr] hit=False
    -   PenalFr.pd art 62: article 62 du présent code, sans préjudice, le cas échéant, des peines encourues pour la tentative des crimes prévus aux articles 60 et 60 bis du prés
    -   PenalFr.pd art 60: Article 60 (Modifié par le décret du 10 janvier 1957).- Est coupable de trahison et puni de mort : 1° - tout Tunisien qui aura porté les armes contre 
    -   PenalFr.pd art 185: Article 185 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, celui qui contrefait ou altère la monnaie fiduciair
    -   PenalFr.pd art 22: Article 22.- L'interdiction de séjour consiste dans la défense faite au condamné de résider et de paraître dans les lieux ou régions déterminés par le
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 72: Article 72.- Est puni de mort, l’auteur de l'attentat ayant pour but de changer la forme du gouvernement, d'inciter les gens à s'armer les uns contre 
- `q052` [ar] hit=False
    -   PenalFr.pd art 60: Article 60 (Modifié par le décret du 10 janvier 1957).- Est coupable de trahison et puni de mort : 1° - tout Tunisien qui aura porté les armes contre 
    -   PenalFr.pd art 22: Article 22.- L'interdiction de séjour consiste dans la défense faite au condamné de résider et de paraître dans les lieux ou régions déterminés par le
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 53: Article 53. 1- Lorsque les circonstances du fait poursuivi paraissent de nature à justifier l’atténuation de la peine et que la loi ne s'y oppose pas,
    -   PenalFr.pd art 4: Art. 4.- Il ne découle de la réorganisation du code pénal et de sa nouvelle rédaction aucune modification quant au fond. La présente loi sera publiée 
    -   PenalFr.pd art 223: Article 223.- Est puni d'un an d’emprisonnement et de deux cent vingt dinars d’amende, quiconque aura menacé autrui à l’aide d’une arme, même sans int
- `q072` [en] hit=False
    -   PenalFr.pd art 251: Article 251 (Modifié par la loi n° 2005-45 du 6 juin 2005).- La peine est de vingt ans d'emprisonnement et de vingt mille dinars d'amende : a) si la c
    -   PenalFr.pd art 60: Article 60 (Modifié par le décret du 10 janvier 1957).- Est coupable de trahison et puni de mort : 1° - tout Tunisien qui aura porté les armes contre 
    -   PenalFr.pd art 223: Article 223.- Est puni d'un an d’emprisonnement et de deux cent vingt dinars d’amende, quiconque aura menacé autrui à l’aide d’une arme, même sans int
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 72: Article 72.- Est puni de mort, l’auteur de l'attentat ayant pour but de changer la forme du gouvernement, d'inciter les gens à s'armer les uns contre 
    -   PenalFr.pd art 218: Article 218 (Modifié par la loi n° 93-72 du 12 juillet 1993).- Tout individu qui, volontairement, fait des blessures, porte des coups, ou commet toute

**Suggested change:** Replace 39 by 40. Art 40 covers 'se défendant contre les auteurs de vols ou de pillages' and repelling a nocturnal break-in = légitime défense. Art 39 is contrainte/état de nécessité ('danger imminent'). JUDGMENT CALL: you may prefer to keep 39 as a related article.

- add: 40   |   remove: 39
- proposed gold (anchor = the text the intended chunk must start with):
    - NEW **40** `Article 40`
        > Article 40.- Il n'y a pas d'infraction : 1) si l'homicide a été commis, si les blessures ont été faites ou les coups portés en repoussant, la nuit, l'

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_arson

- `q010` [fr, penal, concept] Comment est puni l'incendie volontaire ?

**Current gold** (PenalFr.pdf)

- **307** `H` Article 307 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, quiconque aura mis volontairement le feu, directement ou indirectement, à des édifices, navires, bateaux, magasins, chantiers habités ou servant à l'habitation, et généralement aux lieux habités ou ser
- **308** `H` Article 308 (Modifié par la loi n° 89-23 du 27 février 1989).- La peine encourue est celle de vingt ans d'emprisonnement, si les bâtiments incendiés n'étaient pas habités ou ne servaient pas d'habitation, elle est réduite à dix ans si l'auteur du crime est propriétaire du bâtiment incendié. 90
- **309** `H` Article 309 (Modifié par la loi n° 69-44 du 26 juillet 1969).- Est puni d'un emprisonnement de trois ans et d'une amende de deux mille dinars, celui qui, par maladresse, imprudence, inattention, négligence ou inobservation des règlements, détermine un incendie sur les propriétés mobilières ou immobi

**Corpus candidates** (BM25 over PenalFr.pdf headings; query terms: puni incendie volontaire)

-      **210** (8.7) Article 210 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni d'emprisonnement à vie, le père qui commet un homicide volontaire sur la personne de son enfant.
-      **204** (6.3) Article 204 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de mort, l’auteur de l'homicide volontaire lorsque l’homicide a été précédé, accompagné ou suivi d’une autre infraction passible
- gold **307** (5.5) Article 307 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, quiconque aura mis volontairement le feu, directement ou indirectement, à des édifices, navires, bate
- gold **309** (5.3) Article 309 (Modifié par la loi n° 69-44 du 26 juillet 1969).- Est puni d'un emprisonnement de trois ans et d'une amende de deux mille dinars, celui qui, par maladresse, imprudence, inattention, négli
-      **304** (4.7) Article 304 (Modifié par la loi n° 69-44 du 26 juillet 1969).- Quiconque, volontairement et autrement que par une explosion ou un incendie, cause un dommage à la propriété immobilière ou mobilière d'a
-      **143** (4.3) Article 143.- Est puni d’un mois d'emprisonnement et de quarante huit dinars d’amende, quiconque, le pouvant, refuse ou néglige de faire les travaux, les services ou de prêter le secours dont il a été
-      **263** (4.0) Article 263.- Est puni de dix ans d’emprisonnement l’auteur du vol commis : 1°- au cours d'un incendie ou après une explosion, inondation, naufrage, accident de chemin de fer, révolte, émeute ou tout 
-      **306** (4.0) Article 306 ter (Ajouté par la loi n° 77-56 du 3 août 1977).- Est puni d’un à cinq ans d'emprisonnement et de deux cents dinars à quatre mille dinars d'amende, quiconque, ayant propagé, sciemment, de 

**Retrieved by official v1** (top-6, one block per language variant)

- `q010` [fr] hit=False
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 60: Article 60 bis (Ajouté par le décret du 10 janvier 1957).- Est coupable de trahison et puni de mort : 1°- tout Tunisien qui aura livré à une puissance
    -   PenalFr.pd art 62: article 62 du présent code, sans préjudice, le cas échéant, des peines encourues pour la tentative des crimes prévus aux articles 60 et 60 bis du prés
    -   PenalFr.pd art 164: Article 164.- Est puni de dix ans d'emprisonnement et de deux cent quarante dinars d’amende, quiconque aura, en dehors du cas prévu à l’
    -   PenalFr.pd art 223: Article 223.- Est puni d'un an d’emprisonnement et de deux cent vingt dinars d’amende, quiconque aura menacé autrui à l’aide d’une arme, même sans int

**Suggested change:** Remove 309: it punishes fires caused by 'maladresse, imprudence, négligence' (involuntary), while the question asks about incendie volontaire. 307 and 308 unchanged.

- add: none   |   remove: 309
- proposed gold (anchor = the text the intended chunk must start with):
    - **307** `Article 307`
        > Article 307 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, quiconque aura mis volontairement le feu, directeme
    - **308** `Article 308`
        > Article 308 (Modifié par la loi n° 89-23 du 27 février 1989).- La peine encourue est celle de vingt ans d'emprisonnement, si les bâtiments incendiés n

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_attempt

- `q011` [fr, penal, concept] Que dit la loi sur la tentative de crime ?

**Current gold** (PenalFr.pdf)

- **59** `H` Article 59.- Toute tentative d'infraction est punissable comme l'infraction elle-même si elle n'a été suspendue ou si elle n'a manqué son effet que par des circonstances indépendantes de la volonté de son auteur. Toutefois, la tentative n'est pas punissable, sauf disposition contraire de la loi, dan

**Corpus candidates** (BM25 over PenalFr.pdf headings; query terms: tentative crime)

-      **227** (6.4) Article 227 (Modifié par la loi n° 85-9 du 7 mars 1985 et par la loi n° 89-23 du 27 février 1989).- Est puni de mort : 69 1) le crime de viol commis avec violence, usage ou menace d'usage d'arme. 2) l
-      **14** (5.6) Article 14 (Modifié par le décret du 15 septembre 1923).- La condamnation à l'emprisonnement est prononcée pour cinq années au moins quand l'infraction est considérée comme crime, aux termes de l’
-      **308** (4.8) Article 308 (Modifié par la loi n° 89-23 du 27 février 1989).- La peine encourue est celle de vingt ans d'emprisonnement, si les bâtiments incendiés n'étaient pas habités ou ne servaient pas d'habitat
-      **30** (3.6) Article 30 (Modifié par la loi n° 89-23 du 27 février 1989).- Est de plein droit en état d'interdiction légale, à partir du jugement et pour la durée de sa peine, tout condamné, pour un seul crime, à 
-      **92** (3.5) Article 92 (Modifié par la loi n° 98-33 du 23 mai 1998).- La peine est d'un an d'emprisonnement et de mille dinars d'amende, si la tentative de corruption n'a eu aucun effet. Elle est de deux ans d'em
-      **58** (3.3) Article 58.- Les peines de l'interdiction de séjour et de la surveillance administrative ne se confondent pas. CHAPITRE VI DE LA TENTATIVE
-      **251** (3.1) Article 251 (Modifié par la loi n° 2005-45 du 6 juin 2005).- La peine est de vingt ans d'emprisonnement et de vingt mille dinars d'amende : a) si la capture, arrestation, détention ou séquestration a 
-      **256** (3.0) Article 256.- Celui qui, contre le gré du propriétaire, pénètre ou demeure dans un lieu servant à l'habitation, est puni d'un emprisonnement de 3 mois. La tentative est punissable.

**Retrieved by official v1** (top-6, one block per language variant)

- `q011` [fr] hit=False
    -   PenalFr.pd art 291: article 291 du présent code, quiconque, amène, frauduleusement, autrui à quitter le territoire tunisien en alléguant de faits inexistants ou en usant 
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 72: Article 72.- Est puni de mort, l’auteur de l'attentat ayant pour but de changer la forme du gouvernement, d'inciter les gens à s'armer les uns contre 
    -   PenalFr.pd art 4: Art. 4.- Il ne découle de la réorganisation du code pénal et de sa nouvelle rédaction aucune modification quant au fond. La présente loi sera publiée 
    -   PenalFr.pd art 185: Article 185 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, celui qui contrefait ou altère la monnaie fiduciair
    -   PenalFr.pd art 188: Article 188 (Modifié par la loi n° 89-23 du 27 février 1989).- Sont punis d'emprisonnement à vie ceux qui ont contrefait ou falsifié les billets de ba

**Suggested change:** No change (Art 59 = tentative punissable).

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **59** `Article 59`
        > Article 59.- Toute tentative d'infraction est punissable comme l'infraction elle-même si elle n'a été suspendue ou si elle n'a manqué son effet que pa

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## penal_assault

- `q012` [fr, penal, concept] Quelle est la peine pour les coups et blessures volontaires ?
- `q046` [fr, penal, colloquial] Que risque-t-on si on frappe quelqu'un ?

**Current gold** (PenalFr.pdf)

- **217** `H` Article 217 (Modifié par le décret du 17 février 1936).- Est puni de deux ans d'emprisonnement et de sept cent vingt dinars d’amende, l’auteur de l'homicide involontaire, commis ou causé par maladresse, imprudence, négligence, inattention ou inobservation des règlements. Section II - Violences - Men
- **218** `F` article 218 du présent code. La peine est de dix ans d'emprisonnement est et de quatre cent quatre vingt dinars d'amende si, dans ce dernier cas, les violences ont été préméditées ou ont engendré des blessures ou maladie ou si elles ont été commises à l'audience sur un fonctionnaire de l'ordre judic
- **218** `H` Article 218 (Modifié par la loi n° 93-72 du 12 juillet 1993).- Tout individu qui, volontairement, fait des blessures, porte des coups, ou commet toute autre violence ou voie de fait ne rentrant pas dans les prévisions de l'
- **219** `H` Article 219 (Modifié par la loi n° 64-34 du 2 juillet 1964 et par la loi n° 1989-23 du 27 février 1989).- Quand les violences ci-dessus exprimées ont été suivies de mutilation, perte de l'usage d'un membre, défiguration, infirmité ou incapacité permanente dont le taux ne dépasse pas 20%, le coupable

**Corpus candidates** (BM25 over PenalFr.pdf headings; query terms: peine coups blessures volontaires)

-      **208** (10.0) Article 208 (Modifié par la loi n° 89-23 du 27 février 1989).- Le coupable est puni de vingt ans d'emprisonnement, si les coups portés ou les blessures faites volontairement, mais sans intention de do
-      **220** (9.8) Article 220 ( Modifié par la loi n° 64-34 du 2 juillet 1964).- Les individus, ayant participé à une rixe au cours de laquelle ont été portés des coups et blessures de la nature de ceux prévus aux arti
- gold **218** (9.7) Article 218 (Modifié par la loi n° 93-72 du 12 juillet 1993).- Tout individu qui, volontairement, fait des blessures, porte des coups, ou commet toute autre violence ou voie de fait ne rentrant pas da
-      **215** (8.7) Article 215 (Le paragraphe 2 a été modifié par la loi n° 89-23 du 27 février 1989).- Quiconque, sans intention de donner la mort, administre volontairement à une personne des substances ou se livre su
-      **40** (8.2) Article 40.- Il n'y a pas d'infraction : 1) si l'homicide a été commis, si les blessures ont été faites ou les coups portés en repoussant, la nuit, l'escalade ou l'effraction des clôtures, murs ou ent
-      **119** (8.2) Article 119.- Tout individu, ayant participé à une rébellion armée ou non armée, au cours de laquelle des voies de fait ont été exercées sur un fonctionnaire dans l'exercice des ses fonctions, est, du
-      **306** (4.6) Article 306 bis (Ajouté par la loi n° 77-56 du 3 août 1977 et modifié par la loi n° 89-23 du 27 février 1989).- Sera punie d'un emprisonnement de dix ans, toute personne qui, par violence ou menace, s
-      **157** (4.1) Article 157 (Modifié par la loi n° 89-23 du 27 février 1989).- Le coupable est puni de quinze ans d'emprisonnement, si les bris de scellés, les soustractions, l'enlèvement, destruction ou altération d

**Retrieved by official v1** (top-6, one block per language variant)

- `q012` [fr] hit=False
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    -   PenalFr.pd art 233: Article 233 (Abrogé par le décret du 26 mai 1949 et ajouté par la loi 64-34 du 2 juillet 1964).- La peine sera d'un emprisonnement de trois à cinq ans
    -   PenalFr.pd art 208: Article 208 (Modifié par la loi n° 89-23 du 27 février 1989).- Le coupable est puni de vingt ans d'emprisonnement, si les coups portés ou les blessure
    -   PenalFr.pd art 185: Article 185 (Modifié par la loi n° 89-23 du 27 février 1989).- Est puni de l'emprisonnement à vie, celui qui contrefait ou altère la monnaie fiduciair
    -   PenalFr.pd art 188: Article 188 (Modifié par la loi n° 89-23 du 27 février 1989).- Sont punis d'emprisonnement à vie ceux qui ont contrefait ou falsifié les billets de ba
    -   PenalFr.pd art 215: Article 215 (Le paragraphe 2 a été modifié par la loi n° 89-23 du 27 février 1989).- Quiconque, sans intention de donner la mort, administre volontair
- `q046` [fr] hit=True
    -   PenalFr.pd art 116: Article 116.- Est puni de six mois d'emprisonnement et de quarante huit dinars d’amende, quiconque exerce ou menace d'exercer des violences pour résis
    -   PenalFr.pd art 264: Article 264.- La peine est de cinq ans d’emprisonnement et de cent vingt dinars d’amende, pour tous autres vols et soustractions commis hors les cas p
    -   PenalFr.pd art 129: Article 129.- Est puni d’un an d'emprisonnement, quiconque par paroles, écrits, gestes ou tous autres moyens, porte atteinte publiquement, au drapeau 
    - ✓ PenalFr.pd art 218: article 218 du présent code. La peine est de dix ans d'emprisonnement est et de quatre cent quatre vingt dinars d'amende si, dans ce dernier cas, les 
    -   PenalFr.pd art 101: Article 101.- Est puni de cinq ans d'emprisonnement et de cent vingt dinars d'amende, tout fonctionnaire public ou assimilé qui, dans l'exercice ou à 
    -   PenalFr.pd art 286: Article 286.- Est puni d’un an d'emprisonnement et de cent vingt dinars d'amende, quiconque, dans le but de s’approprier tout ou partie de la propriét

**Suggested change:** Remove 217: it is homicide involontaire (maladresse, imprudence). Add 208 (coups portés ou blessures faites volontairement sans intention de donner la mort: 20 years). 218-219 unchanged; 218 anchored to the main article (a fragment chunk also carries 218).

- add: 208   |   remove: 217
- proposed gold (anchor = the text the intended chunk must start with):
    - NEW **208** `Article 208`
        > Article 208 (Modifié par la loi n° 89-23 du 27 février 1989).- Le coupable est puni de vingt ans d'emprisonnement, si les coups portés ou les blessure
    - **218** `Article 218 (Modifié par la loi n° 93-72`
        > Article 218 (Modifié par la loi n° 93-72 du 12 juillet 1993).- Tout individu qui, volontairement, fait des blessures, porte des coups, ou commet toute
    - **219** `Article 219`
        > Article 219 (Modifié par la loi n° 64-34 du 2 juillet 1964 et par la loi n° 1989-23 du 27 février 1989).- Quand les violences ci-dessus exprimées ont 

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## const_right_to_life

- `q015` [fr, constitution, article_lookup] Que dit l'article 24 sur le droit à la vie ?
- `q053` [ar, constitution, article_lookup] ماذا ينص الفصل 24 من الدستور؟

**Current gold** (tun_RecAcFreeLi.pdf)

- **24** `H` Art. 24 – Le droit à la vie est sacré. Il ne peut y être porté atteinte, que dans des cas extrêmes prévus par la loi.

**Corpus candidates** (BM25 over tun_RecAcFreeLi.pdf headings; query terms: droit vie)

- gold **24** (7.3) Art. 24 – Le droit à la vie est sacré. Il ne peut y être porté atteinte, que dans des cas extrêmes prévus par la loi.
-      **30** (5.2) Art. 30 – L’Etat protège la vie privée, l’inviolabilité du domicile et le secret des correspondances, des communications et des données personnelles. Tout citoyen dispose de la liberté de choisir son 
-      **22** (4.4) Art. 22 – L’Etat garantit aux citoyens et aux citoyennes les libertés et les droits individuels et collectifs. Il leur assure les conditions d’une vie digne.
-      **5** (3.8) Art. 5 – La Tunisie constitue une partie de la nation islamique. Seul l’Etat doit œuvrer, dans un régime démocratique, à la réalisation des vocations de l’Islam authentique qui consistent à préserver 
-      **41** (3.2) Art. 41 – Le droit syndical, y compris le droit de grève, est garanti. Ce droit ne s’applique pas à l’Armée nationale. Les magistrats, les forces de sécurité intérieure et la douane ne disposent pas d
-      **38** (3.1) Art. 38 – L’Etat garantit le droit à l’information et le droit d’accès à l’information. L’Etat œuvre en vue de garantir le droit d’accès aux réseaux de communication.
-      **99** (2.6) Art. 99 – Le Président de la République dispose du droit de grâce.
-      **100** (2.6) Art. 100 – Le Président de la République dispose du droit de grâce.

**Retrieved by official v1** (top-6, one block per language variant)

- `q015` [fr] hit=True
    - ✓ tun_RecAcF art 24: Art. 24 – Le droit à la vie est sacré. Il ne peut y être porté atteinte, que dans des cas extrêmes prévus par la loi.
- `q053` [ar] hit=True
    - ✓ tun_RecAcF art 24: Art. 24 – Le droit à la vie est sacré. Il ne peut y être porté atteinte, que dans des cas extrêmes prévus par la loi.

**Suggested change:** No change; anchored.

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **24** `Art. 24`
        > Art. 24 – Le droit à la vie est sacré. Il ne peut y être porté atteinte, que dans des cas extrêmes prévus par la loi.

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## const_fundamental_rights

- `q016` [fr, constitution, concept] Quels sont les droits fondamentaux ?
- `q076` [en, constitution, concept] What are the fundamental rights?

**Current gold** (tun_RecAcFreeLi.pdf)

- **24** `H` Art. 24 – Le droit à la vie est sacré. Il ne peut y être porté atteinte, que dans des cas extrêmes prévus par la loi.
- **25** `H` Art. 25 – L’Etat protège la dignité de l’être humain et son intégrité physique et interdit la torture morale et physique. L’infraction de torture est imprescriptible.
- **26** `H` Art. 26 – La liberté de l’individu est garantie. Art . 27 – L’Etat garantit la liberté de croyance et de conscience.

**Corpus candidates** (BM25 over tun_RecAcFreeLi.pdf headings; query terms: droits fondamentaux)

-      **55** (3.9) Art. 55 – Aucune restriction ne peut être apportée aux droits et libertés garantis par la présente Constitution qu'en vertu d'une loi et pour répondre aux exigences d’un régime démocratique et en vue 
-      **39** (3.6) Art. 39 – Les droits d’élire, de voter et de se porter candidat sont garantis dans les conditions fixées par la loi.
-      **23** (3.6) Art. 23 – Les citoyens et les citoyennes sont égaux en droits et en devoirs. Ils sont égaux devant la loi sans aucune discrimination.
-      **21** (3.4) Art. 21 – L’Etat garantit la neutralité des institutions éducatives de toute exploitation partisane. Chapitre II – Des droits et libertés
-      **22** (3.3) Art. 22 – L’Etat garantit aux citoyens et aux citoyennes les libertés et les droits individuels et collectifs. Il leur assure les conditions d’une vie digne.
-      **115** (2.7) Art. 115 – L’Assemblée des représentants du peuple et le Conseil national des régions et des districts peuvent conjointement s’opposer à la poursuite de l’activité du Gouvernement en déposant une moti
-      **35** (2.6) Art. 35 – Aucune personne ne peut être arrêtée ou détenue, sauf en cas de flagrant délit ou en vertu d’une décision judiciaire. Elle est immédiatement informée de ses droits et de l’accusation qui lui
-      **52** (2.2) Art. 52 – Les droits de l’enfant sont garantis. Il incombe à ses père et mère et à l’Etat de lui garantir la dignité, la santé, les soins, l’éducation et l’enseignement. L’Etat doit également fournir 

**Retrieved by official v1** (top-6, one block per language variant)

- `q016` [fr] hit=True
    -   tun_RecAcF art 37: Art. 37 – Les libertés d’opinion, de pensée, d’expression, d’information et de publication sont garanties. Aucun contrôle préalable ne peut être exerc
    -   tun_RecAcF art 9: Art. 9 – La devise de la République tunisienne est Liberté, Ordre, Justice.
    -   tun_RecAcF art 39: Art. 39 – Les droits d’élire, de voter et de se porter candidat sont garantis dans les conditions fixées par la loi.
    -   tun_RecAcF art 31: Art. 31 – Aucun citoyen ne peut être déchu de la nationalité tunisienne, ni être banni, extradé, ni empêché de revenir à son pays.
    -   tun_RecAcF art 30: Art. 30 – L’Etat protège la vie privée, l’inviolabilité du domicile et le secret des correspondances, des communications et des données personnelles. 
    - ✓ tun_RecAcF art 26: Art. 26 – La liberté de l’individu est garantie. Art . 27 – L’Etat garantit la liberté de croyance et de conscience.
- `q076` [en] hit=True
    -   tun_RecAcF art 37: Art. 37 – Les libertés d’opinion, de pensée, d’expression, d’information et de publication sont garanties. Aucun contrôle préalable ne peut être exerc
    -   tun_RecAcF art 9: Art. 9 – La devise de la République tunisienne est Liberté, Ordre, Justice.
    -   tun_RecAcF art 52: Art. 52 – Les droits de l’enfant sont garantis. Il incombe à ses père et mère et à l’Etat de lui garantir la dignité, la santé, les soins, l’éducation
    - ✓ tun_RecAcF art 26: Art. 26 – La liberté de l’individu est garantie. Art . 27 – L’Etat garantit la liberté de croyance et de conscience.
    -   tun_RecAcF art 5: Art. 5 – La Tunisie constitue une partie de la nation islamique. Seul l’Etat doit œuvrer, dans un régime démocratique, à la réalisation des vocations 
    -   tun_RecAcF art 3: Art. 3 – Le peuple tunisien est le détenteur de la souveraineté, il l’exerce dans les conditions fixées par la présente Constitution.

**Suggested change:** Add 22 ('L'Etat garantit aux citoyens ... les libertés et les droits individuels et collectifs'). The question is inherently broad; consider whether it should stay in the scored set. NOTE: the chunk labelled 26 also contains Art. 27 ('Art . 27' with a space escapes the splitter).

- add: 22   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - NEW **22** `Art. 22`
        > Art. 22 – L’Etat garantit aux citoyens et aux citoyennes les libertés et les droits individuels et collectifs. Il leur assure les conditions d’une vie
    - **24** `Art. 24`
        > Art. 24 – Le droit à la vie est sacré. Il ne peut y être porté atteinte, que dans des cas extrêmes prévus par la loi.
    - **25** `Art. 25`
        > Art. 25 – L’Etat protège la dignité de l’être humain et son intégrité physique et interdit la torture morale et physique. L’infraction de torture est 
    - **26** `Art. 26`
        > Art. 26 – La liberté de l’individu est garantie. Art . 27 – L’Etat garantit la liberté de croyance et de conscience.

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## cpp_custody_duration

- `q017` [fr, procedure_penale, article_lookup] Que dit l'article 13 sur la garde à vue ?
- `q018` [fr, procedure_penale, concept] Quelle est la durée maximale de la garde à vue ?
- `q055` [ar, procedure_penale, concept] ما هي مدة الاحتفاظ؟
- `q078` [en, procedure_penale, concept] How long can police custody last?

**Current gold** (ProcedurepenaleFr.pdf)

- **13** `H` Article 13.- Les officiers de police judiciaire visés aux 3° et 4° de l'
- **13** `H` Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'enquête l'exigent, les officiers de police judiciaire visés aux numéros 3° et 4° de l'
- **13** `F` article 13 bis quant à l'insertion des identités dans le registre, à l'établissement des procès-verbaux et à l'examen médical. Le juge cantonal, commis rogatoirement, ne peut, sans l'autorisation expresse du juge d'instruction, subdéléguer les autres officiers de police judiciaire.
- **13** `H` Article 13.- Une indemnisation globale du préjudice causé au demandeur lui sera allouée s'il prouve que le préjudice est réel, grave, actuel, et résultant directement de la détention provisoire ou de l'exécution de la peine de prison. Pour l'évaluation du montant de la réparation, doivent être pris 
- **13** `H` Article 13.- Est puni de cinq à douze ans d’emprisonnement et d'une amende de cinq mille à cinquante mille dinars : - Quiconque adhère sur le territoire de la République, à quelque titre que ce soit, à une organisation ou entente, quelque soit la forme ou le nombre de ses membres, qui a fait, même f

**Corpus candidates** (BM25 over ProcedurepenaleFr.pdf headings; query terms: garde vue)

-      **35** (7.9) Article 35.- Les procureurs de la République près les tribunaux de première instance autres que Tunis sont habilités à procéder aux actes urgents de l’enquête préliminaire en vue de constater l'infrac
-      **361** (5.1) Article 361.- Les greffiers des tribunaux sont tenus de consigner, sur un registre particulier, les nom, prénom, profession, âge et résidence de tous les individus condamnés pour crimes ou délits, ave
-      **71** (4.7) Article 71.- L'inculpé est soumis à l'examen du service de l'identité judiciaire en vue de faire vérifier son identité et rechercher ses antécédents.
-      **11** (4.5) Article 11.- Est coupable d'infraction terroriste celui : - qui a incité ou s’est concerté pour la commettre. - qui s’est résolu à la commettre, si cette résolution est accompagnée d'un acte préparato
-      **139** (4.3) Article 139.- La citation doit être remise à la personne de l'intéressé, à son mandataire, à son domestique ou à toute personne habitant avec lui, à la condition que celle-ci soit douée de discernemen
-      **10** (4.0) Article 10.- La police judiciaire est exercée sous l'autorité du Procureur Général de la République et, dans chaque ressort de Cour d'Appel, des avocats généraux par : 1) les Procureurs de la Républiq
-      **14** (3.8) Article 14.- Est puni de cinq à douze ans d'emprisonnement et d'une amende de cinq mille à cinquante mille dinars quiconque utilise le territoire de la République pour recruter ou entraîner une person
-      **335** (3.8) Article 335.- L'envoi des individus détenus, en vue d'une confrontation, doit être demandé par la voie diplomatique. Il est donné suite à la demande, à moins que des considérations particulières ne s'

**Retrieved by official v1** (top-6, one block per language variant)

- `q017` [fr] hit=True
    - ✓ Procedurep art 13: Article 13.- Les officiers de police judiciaire visés aux 3° et 4° de l'
    - ✓ Procedurep art 13: Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'en
    - ✓ Procedurep art 13: article 13 bis quant à l'insertion des identités dans le registre, à l'établissement des procès-verbaux et à l'examen médical. Le juge cantonal, commi
    - ✓ Procedurep art 13: Article 13.- Est puni de cinq à douze ans d’emprisonnement et d'une amende de cinq mille à cinquante mille dinars : - Quiconque adhère sur le territoi
    - ✓ Procedurep art 13: Article 13.- Une indemnisation globale du préjudice causé au demandeur lui sera allouée s'il prouve que le préjudice est réel, grave, actuel, et résul
- `q018` [fr] hit=False
    -   Procedurep art 321: Article 321.- L'examen des demandes d'extradition est de la compétence de la chambre d'accusation de la cour d'appel de Tunis. L'étranger comparaît de
    -   Procedurep art 85: Article 85 (Modifié par la loi n° 93-114 du 22 novembre 1993).- L'inculpé peut être soumis à la détention préventive dans les cas de crimes ou délits 
    -   Procedurep art 35: Article 35.- Les procureurs de la République près les tribunaux de première instance autres que Tunis sont habilités à procéder aux actes urgents de l
    -   Procedurep art 311: Article 311.- L'extradition est accordée : 1) lorsque l'infraction motivant la demande est punie par la loi tunisienne d'une peine criminelle ou corre
    -   Procedurep art 10: article 10 , même en cas de crimes ou délits flagrants, et les officiers de police judiciaire des douanes, dans le cadre des compétences qui leur sont
    -   Procedurep art 326: Article 326.- L'individu arrêté provisoirement dans les conditions prévues par l'article précédent, peut, s'il séjourne en Tunisie, être mis en libert
- `q055` [ar] hit=False
    -   Procedurep art 74: article 74 de la présente loi doivent conserver pendant une période qui ne peut être inférieure à dix ans à compter de la date de la réalisation de l’
    -   Procedurep art 70: Article 70.- Les personnes morales doivent : - tenir des comptes sur un livre-journal faisant état de toutes recettes et dépenses . - tenir un inventa
    -   Procedurep art 83: Article 83 (Modifié par la loi n°2009-65 du 12 août 2009).- La commission tunisienne des analyses financières est tenue de mettre en place une base de
    -   Procedurep art 346: Article 346 (Modifié par la loi n° 99-90 du 2 août 1999).- La durée de la contrainte est réduite de moitié et peut être, à la demande du 
    -   Procedurep art 202: Article 202.- Le juge peut retenir à sa disposition sous mandat de dépôt, le prévenu en état d'ivresse, ou ne pouvant justifier de son identité, ou n'
    -   Procedurep art 10: article 10 , même en cas de crimes ou délits flagrants, et les officiers de police judiciaire des douanes, dans le cadre des compétences qui leur sont
- `q078` [en] hit=False
    -   Procedurep art 85: Article 85 (Modifié par la loi n° 93-114 du 22 novembre 1993).- L'inculpé peut être soumis à la détention préventive dans les cas de crimes ou délits 
    -   Procedurep art 321: Article 321.- L'examen des demandes d'extradition est de la compétence de la chambre d'accusation de la cour d'appel de Tunis. L'étranger comparaît de
    -   Procedurep art 7: Article 7.- Le minimum de la peine d'emprisonnement encourue pour infraction terroriste est fixé comme suit : - Si la peine encourue est l'emprisonnem
    -   Procedurep art 10: article 10 , même en cas de crimes ou délits flagrants, et les officiers de police judiciaire des douanes, dans le cadre des compétences qui leur sont
    -   Procedurep art 136: Article 136.- Le délai entre le jour où la citation est délivrée et le jour fixé pour la comparution à l'audience est d'au moins trois jours. Si la pa
    -   Procedurep art 311: Article 311.- L'extradition est accordée : 1) lorsque l'infraction motivant la demande est punie par la loi tunisienne d'une peine criminelle ou corre

**Suggested change:** Disambiguate: ProcedurepenaleFr.pdf bundles several laws and has 4 chunks numbered 13 (OPJ powers, garde à vue = Art 13 bis, an indemnisation law, a terrorism law). Only Art 13 (OPJ) and Art 13 bis count.

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **13** `Article 13.- Les officiers de police judiciaire visés aux 3°`
        > Article 13.- Les officiers de police judiciaire visés aux 3° et 4° de l'
    - **13** `Article 13 bis`
        > Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'en

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## cpp_detainee_rights

- `q019` [fr, procedure_penale, concept] Quels sont les droits de la personne gardée à vue ?
- `q054` [ar, procedure_penale, concept] ما هي حقوق الموقوف؟
- `q077` [en, procedure_penale, concept] What are the rights of a detainee?

**Current gold** (ProcedurepenaleFr.pdf)

- **13** `H` Article 13.- Les officiers de police judiciaire visés aux 3° et 4° de l'
- **13** `H` Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'enquête l'exigent, les officiers de police judiciaire visés aux numéros 3° et 4° de l'
- **13** `F` article 13 bis quant à l'insertion des identités dans le registre, à l'établissement des procès-verbaux et à l'examen médical. Le juge cantonal, commis rogatoirement, ne peut, sans l'autorisation expresse du juge d'instruction, subdéléguer les autres officiers de police judiciaire.
- **13** `H` Article 13.- Une indemnisation globale du préjudice causé au demandeur lui sera allouée s'il prouve que le préjudice est réel, grave, actuel, et résultant directement de la détention provisoire ou de l'exécution de la peine de prison. Pour l'évaluation du montant de la réparation, doivent être pris 
- **13** `H` Article 13.- Est puni de cinq à douze ans d’emprisonnement et d'une amende de cinq mille à cinquante mille dinars : - Quiconque adhère sur le territoire de la République, à quelque titre que ce soit, à une organisation ou entente, quelque soit la forme ou le nombre de ses membres, qui a fait, même f
- **70** `H` Article 70.- L'inculpé détenu est autorisé à communiquer à tout moment avec son conseil, aussitôt après la première comparution. Le juge d'instruction peut, par ordonnance motivée et non susceptible d'appel, prescrire l'interdiction de communiquer pour une période de dix jours. Cette interdiction pe
- **70** `H` Article 70.- Les personnes morales doivent : - tenir des comptes sur un livre-journal faisant état de toutes recettes et dépenses . - tenir un inventaire des recettes et virements en rapport avec l'étranger faisant état des montants y afférents, leur justification , la date de leur réalisation et l’

**Corpus candidates** (BM25 over ProcedurepenaleFr.pdf headings; query terms: droits personne gardée vue)

-      **14** (6.4) Article 14.- Est puni de cinq à douze ans d'emprisonnement et d'une amende de cinq mille à cinquante mille dinars quiconque utilise le territoire de la République pour recruter ou entraîner une person
-      **102** (6.0) Article 102.- Les jugements prononçant la liquidation ou la confiscation des avoirs en application de la présente loi ne peuvent, en aucun cas, porter atteinte aux droits des tiers acquis de bonne foi
-      **72** (5.0) Article 72 bis (Ajouté par la loi n°2009-65 du 12 août 2009) Dans le cadre du respect des engagements internationaux de la Tunisie, le ministre chargé des finances peut, après avis du gouverneur de la
-      **71** (4.7) Article 71.- L'inculpé est soumis à l'examen du service de l'identité judiciaire en vue de faire vérifier son identité et rechercher ses antécédents.
-      **11** (4.5) Article 11.- Est coupable d'infraction terroriste celui : - qui a incité ou s’est concerté pour la commettre. - qui s’est résolu à la commettre, si cette résolution est accompagnée d'un acte préparato
-      **49** (4.5) Article 49 (Modifié par la loi n°2009-65 du 12 août 2009) En cas de péril en la demeure, le juge d'instruction ou le président du tribunal peuvent, selon les cas, et si les circonstances l’exigent, or
-      **276** (4.2) Article 276.- Le procureur général près la cour de cassation peut nonobstant l'expiration du délai de cassation se pourvoir dans l'intérêt de la loi si la décision attaquée a été rendue en violation d
-      **35** (4.2) Article 35.- Les procureurs de la République près les tribunaux de première instance autres que Tunis sont habilités à procéder aux actes urgents de l’enquête préliminaire en vue de constater l'infrac

**Retrieved by official v1** (top-6, one block per language variant)

- `q019` [fr] hit=False
    -   Procedurep art 10: article 10 , même en cas de crimes ou délits flagrants, et les officiers de police judiciaire des douanes, dans le cadre des compétences qui leur sont
    -   Procedurep art 51: Article 51 (Modifié par la loi n°2009-65 du 12 août 2009).- En cas de péril en la demeure, et si les circonstances l’exigent, toutes les données susce
    -   Procedurep art 50: Article 50.- Les personnes visées au troisième alinéa de l'article précédent peuvent , si elles sont appelées à faire des dépositions auprès des offic
    -   Procedurep art 61: Article 61.- Toute personne citée comme témoin est tenue de comparaître, de prêter serment et de déposer sous réserve des dispositions du code pénal r
    -   Procedurep art 2: Article 2.- Sont abrogées, à compter de l'entrée en vigueur dudit code, à l'exception de la loi n° 68-17 du 2 juillet 1968, toutes dispositions contra
    -   Procedurep art 95: Article 95.- La décision de gel prévue à l'article précédent est prise par le président du tribunal de première instance de Tunis conformément à la pr
- `q054` [ar] hit=False
    -   Procedurep art 141: Article 141.- Le prévenu poursuivi pour un crime ou pour un délit puni d'emprisonnement est tenu de comparaître personnellement. Pour les délits n'ent
    -   Procedurep art 49: Article 49 (Modifié par la loi n°2009-65 du 12 août 2009) En cas de péril en la demeure, le juge d'instruction ou le président du tribunal peuvent, se
    -   Procedurep art 35: Article 35.- Les procureurs de la République près les tribunaux de première instance autres que Tunis sont habilités à procéder aux actes urgents de l
    -   Procedurep art 10: article 10 , même en cas de crimes ou délits flagrants, et les officiers de police judiciaire des douanes, dans le cadre des compétences qui leur sont
    -   Procedurep art 53: Article 53.- Les mesures de protection ne peuvent en tout état de cause porter atteinte au droit du prévenu ou de son conseil d’accéder aux procès-ver
    -   Procedurep art 173: Article 173.- Dans le cas où le prévenu est libre, s'il est condamné à l'emprisonnement, ou à l'emprisonnement et à l'amende, le tribunal peut ordonne
- `q077` [en] hit=False
    -   Procedurep art 2: Article 2.- Sont abrogées, à compter de l'entrée en vigueur dudit code, à l'exception de la loi n° 68-17 du 2 juillet 1968, toutes dispositions contra
    -   Procedurep art 308: article 308 et suivants du code de procédure pénale, si elles sont commises hors du territoire de la République par un sujet non tunisien contre un ét
    -   Procedurep art 334: Article 334.- Si dans une cause pénale, la comparution personnelle d'un témoin résidant en Tunisie est jugée nécessaire par un Gouvernement étranger, 
    -   Procedurep art 320: Article 320.- L'étranger est transféré dans le plus bref délai à Tunis et écroué à la prison civile.
    -   Procedurep art 321: Article 321.- L'examen des demandes d'extradition est de la compétence de la chambre d'accusation de la cour d'appel de Tunis. L'étranger comparaît de
    -   Procedurep art 315: Article 315.- Dans le cas où un étranger est poursuivi ou a été condamné en Tunisie, et où son extradition est demandée au gouvernement Tunisien à rai

**Suggested change:** Same disambiguation for 13/13 bis; 70 anchored to 'L'inculpé détenu est autorisé à communiquer ... avec son conseil' (another chunk numbered 70 is about personnes morales).

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **13** `Article 13.- Les officiers de police judiciaire visés aux 3°`
        > Article 13.- Les officiers de police judiciaire visés aux 3° et 4° de l'
    - **13** `Article 13 bis`
        > Article 13 bis (Ajouté par la loi n° 87-70 du 26 novembre 1987 et modifié par la loi n° 99-90 du 2 août 1999).- Dans les cas où les nécessités de l'en
    - **70** `Article 70.- L'inculpé détenu`
        > Article 70.- L'inculpé détenu est autorisé à communiquer à tout moment avec son conseil, aussitôt après la première comparution. Le juge d'instruction

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## cpp_public_action_limitation

- `q020` [fr, procedure_penale, concept] Comment se prescrit l'action publique ?

**Current gold** (ProcedurepenaleFr.pdf)

- **5** `H` Article 5.- Sauf dispositions spéciales de la loi, l'action publique qui résulte d'un crime se prescrit par dix années révolues, celle qui résulte d'un délit par trois années révolues et celle qui résulte d'une contravention par une année révolue, et ce, à compter du jour où l'infraction a été commi
- **5** `H` Article 5.- La cour d'appel de Tunis est seule compétente pour connaître des demandes en indemnisation. Ces demandes sont de la compétence d'une chambre spécialisée, composée du premier président de la cour d'appel ou de son adjoint et de deux membres ayant fonction de président de chambre au sein d
- **5** `H` Article 5 (abrogé par la loi n°2009-65 du 12 août 2009)

**Corpus candidates** (BM25 over ProcedurepenaleFr.pdf headings; query terms: prescrit action publique)

-      **8** (12.8) Article 8.- L'action civile se prescrit dans les mêmes conditions et délais que l'action publique résultant de l'infraction qui lui donne ouverture. Elle est soumise à tous autres égards aux règles du
-      **37** (11.6) Article 37.- L'action publique relative à une infraction terroriste se prescrit par vingt ans révolus si elle résulte d’un crime, celle qui résulte d'un délit se prescrit par dix ans révolus, et ce, à
-      **6** (10.3) Article 6.- S'il a été fait, au cours des délais de prescription énumérés à l'article précédent, des actes d'instruction ou de poursuite non suivis de jugement, l'action publique interrompue ne se pre
- gold **5** (10.0) Article 5.- Sauf dispositions spéciales de la loi, l'action publique qui résulte d'un crime se prescrit par dix années révolues, celle qui résulte d'un délit par trois années révolues et celle qui rés
-      **37** (8.6) Article 37.- L'action civile poursuivie en même temps que l'action publique conformément à l'
-      **3** (7.7) Article 3.- Hors les cas prévus par la loi, l'action publique n'est pas subordonnée à l'existence d'une plainte et ne peut être arrêtée ni suspendue par le retrait de la plainte ou la renonciation à l
-      **20** (7.0) Article 20.- Le ministère public met en mouvement et exerce l'action publique. Il requiert l'application de la loi et assure l'exécution des décisions de justice. 14
-      **57** (7.0) Article 57.- Le Ministère Public est seul habilité à déclencher et exercer l'action publique résultant des infractions terroristes commises à l'étranger.

**Retrieved by official v1** (top-6, one block per language variant)

- `q020` [fr] hit=True
    -   Procedurep art 6: Article 6.- S'il a été fait, au cours des délais de prescription énumérés à l'article précédent, des actes d'instruction ou de poursuite non suivis de
    - ✓ Procedurep art 5: Article 5.- Sauf dispositions spéciales de la loi, l'action publique qui résulte d'un crime se prescrit par dix années révolues, celle qui résulte d'u
    -   Procedurep art 350: Article 350.- La prescription est suspendue par tout obstacle de droit ou de fait empêchant l'exécution de la peine hors celui qui résulte de la volon
    -   Procedurep art 335: Article 335 Septies.- S'il a été impossible de conclure une transaction ou si celle ci n'a pas été intégralement exécutée dans les délais impartis, le
    -   Procedurep art 37: Article 37.- L'action publique relative à une infraction terroriste se prescrit par vingt ans révolus si elle résulte d’un crime, celle qui résulte d'
    -   Procedurep art 326: Article 326.- L'individu arrêté provisoirement dans les conditions prévues par l'article précédent, peut, s'il séjourne en Tunisie, être mis en libert

**Suggested change:** Anchor 5 to the prescription article (another 'Article 5' concerns the cour d'appel de Tunis and one is abrogated). Add 6 (interruption of the prescription).

- add: 6   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **5** `Article 5.- Sauf dispositions spéciales de la loi, l'action publique`
        > Article 5.- Sauf dispositions spéciales de la loi, l'action publique qui résulte d'un crime se prescrit par dix années révolues, celle qui résulte d'u
    - NEW **6** `Article 6.- S'il a été fait, au cours des délais`
        > Article 6.- S'il a été fait, au cours des délais de prescription énumérés à l'article précédent, des actes d'instruction ou de poursuite non suivis de

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## travail_hours

- `q021` [fr, travail, concept] Quelle est la durée légale du travail ?
- `q043` [fr, unfiltered, cross_domain] Combien d'heures par semaine peut-on travailler ?
- `q056` [ar, travail, concept] ما هي مدة العمل القانونية؟
- `q079` [en, travail, concept] What is the legal working hours limit?

**Current gold** (travailFr.pdf)

- **79** `H` Article 79 (Modifié par la loi n° 96-62 du 15 juillet 1996).- La durée du travail effectif ne peut excéder 48 heures par semaine ou une limitation équivalente établie sur une période de temps autre que la semaine sans que la durée de cette période ne puisse être supérieure à une année. 41 Cette duré
- **79** `F` article 79 du présent code peut être portée, pour certaines entreprises ou certaines catégories du personnel, à 64 heures au maximum afin de tenir compte de la perte de temps résultant de l’interruption du travail ou de la nature du travail et ce, par Arrêté du Ministre chargé des Affaires Sociales.
- **79** `F` article 79 du décret- loi n°2011-115 du 2 novembre 2011).-
- **79** `F` article 79 du décret- loi n°2011-115 du 2 novembre 2011).-
- **79** `F` article 79 du décret- loi n°2011-115 du 2 novembre 2011).-
- **85** `H` Article 85 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Les salariés ne peuvent être employés que conformément aux indications d’un horaire précisant, pour chaque journée et éventuellement pour chaque semaine ou chaque mois, la répartition des heures de travail. Cet horaire fixe les heures aux
- **85** `F` article 85 et il y reste apposé pendant l’année courante et jusqu’au 15 janvier de l’année suivante.

**Corpus candidates** (BM25 over travailFr.pdf headings; query terms: durée légale travail)

-      **88** (9.1) Article 88.- Dans les entreprises agricoles, la durée légale du travail est fixée à deux mille sept cents heures par an au maximum pour trois cents jours de travail effectif. Des arrêtés conjoints du 
-      **286** (5.5) Article 286 (Modifié par la loi n° 96-62 du 15 juillet 1996).- L'employeur est tenu de justifier, à tout moment aux agents chargés de l'application des dispositions du présent chapitre, avoir fait les
-      **6** (4.2) Article 6- 2 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Le contrat de travail est conclu pour une durée indéterminée ou pour une durée déterminée. Le contrat de travail à durée déterminée peut 
-      **94** (4.1) Article 94- 2 (Ajouté par la loi n°96-62 du 15 juillet 1996).- Le contrat de travail à durée déterminée ou indéterminée peut être conclu pour un travail à temps partiel. Est considéré comme travail à 
-      **32** (3.9) Article 32.- La convention collective de travail peut être conclue, soit pour une durée indéterminée, soit pour une durée déterminée ne pouvant excéder cinq ans. A défaut de stipulation contraire, la 
-      **94** (3.9) Article 94- 6 (Ajouté par la loi n°96-62 du 15 juillet 1996).- Sont considérées heures supplémentaires les heures effectuées par le travailleur à temps partiel au delà de la durée normale de travail f
-      **83** (3.8) Article 83 (Modifié par la loi n° 96-62 du 15 juillet 1996).- A titre exceptionnel, l’inspection du travail territorialement compétente peut : 1- autoriser l’employeur à prolonger la durée du travail 
-      **14** (3.7) Article 14.- (Modifié par la loi n° 94-29 du 21 février 1994). .- Le contrat de travail à durée déterminée prend fin par l’expiration de la durée convenue ou par l’accomplissement du travail objet du 

**Retrieved by official v1** (top-6, one block per language variant)

- `q021` [fr] hit=True
    - ✓ travailFr. art 79: Article 79 (Modifié par la loi n° 96-62 du 15 juillet 1996).- La durée du travail effectif ne peut excéder 48 heures par semaine ou une limitation équ
    -   travailFr. art 95: Article 95 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Les entreprises non agricoles ou leurs dépendances, de quelque nature 48 qu'elles soient
    -   travailFr. art 88: Article 88.- Dans les entreprises agricoles, la durée légale du travail est fixée à deux mille sept cents heures par an au maximum pour trois cents jo
    -   travailFr. art 93: Article 93.- L’exécution d’heures supplémentaires ou la récupération d’heures perdues ne peuvent avoir pour effet de porter à plus de soixante heures,
    -   travailFr. art 90: Article 90 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Sont considérées comme heures supplémentaires les heures de travail effectuées au-delà d
    -   travailFr. art 82: Article 82 (Modifié par la loi n° 96-62 du 15 juillet 1996).- La durée hebdomadaire de présence fixée conformément aux dispositions de l’
- `q043` [fr] hit=True
    - ✓ travailFr. art 79: Article 79 (Modifié par la loi n° 96-62 du 15 juillet 1996).- La durée du travail effectif ne peut excéder 48 heures par semaine ou une limitation équ
    -   travailFr. art 4: Article 4.- Sont abrogées, toutes les dispositions antérieures contraires au présent Code et notamment les textes suivants : - décret du 15 juin 1910 
    -   travailFr. art 90: Article 90 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Sont considérées comme heures supplémentaires les heures de travail effectuées au-delà d
    -   travailFr. art 93: Article 93.- L’exécution d’heures supplémentaires ou la récupération d’heures perdues ne peuvent avoir pour effet de porter à plus de soixante heures,
    -   EnfantFr.p art 5: Article 5.- Les autorisations accordées pour l'accomplis- sement des travaux visées à l'article premier fixent la période de l'autorisation, le nombre
    -   travailFr. art 88: Article 88.- Dans les entreprises agricoles, la durée légale du travail est fixée à deux mille sept cents heures par an au maximum pour trois cents jo
- `q056` [ar] hit=True
    - ✓ travailFr. art 79: Article 79 (Modifié par la loi n° 96-62 du 15 juillet 1996).- La durée du travail effectif ne peut excéder 48 heures par semaine ou une limitation équ
    -   travailFr. art 106: Article 106 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Les employeurs sont tenus de donner à leur personnel permanent ou occasionnel, un repos
    -   travailFr. art 89: Article 89.- Dans les entreprises de toutes natures, la journée de travail doit être coupée par un ou plusieurs repos pendant lesquels le travail est 
    -   travailFr. art 95: Article 95 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Les entreprises non agricoles ou leurs dépendances, de quelque nature 48 qu'elles soient
    -   travailFr. art 90: Article 90 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Sont considérées comme heures supplémentaires les heures de travail effectuées au-delà d
    -   travailFr. art 4: Article 4.- Sont abrogées, toutes les dispositions antérieures contraires au présent Code et notamment les textes suivants : - décret du 15 juin 1910 
- `q079` [en] hit=True
    -   travailFr. art 4: Article 4.- Sont abrogées, toutes les dispositions antérieures contraires au présent Code et notamment les textes suivants : - décret du 15 juin 1910 
    - ✓ travailFr. art 79: Article 79 (Modifié par la loi n° 96-62 du 15 juillet 1996).- La durée du travail effectif ne peut excéder 48 heures par semaine ou une limitation équ
    -   travailFr. art 95: Article 95 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Les entreprises non agricoles ou leurs dépendances, de quelque nature 48 qu'elles soient
    -   travailFr. art 410: Article 410.- Les contrats ci-dessus définis doivent être écrits. Ils sont au choix des parties, soit d’une durée déterminée, soit d’une durée indéter
    -   travailFr. art 88: Article 88.- Dans les entreprises agricoles, la durée légale du travail est fixée à deux mille sept cents heures par an au maximum pour trois cents jo
    -   travailFr. art 90: Article 90 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Sont considérées comme heures supplémentaires les heures de travail effectuées au-delà d

**Suggested change:** Add 88 (legal duration in agricultural enterprises: 2700 h/year) and 83 (exceptional extensions of the working day). 79 and 85 kept (85 = work schedule, borderline).

- add: 83, 88   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **79** `Article 79`
        > Article 79 (Modifié par la loi n° 96-62 du 15 juillet 1996).- La durée du travail effectif ne peut excéder 48 heures par semaine ou une limitation équ
    - NEW **83** `Article 83`
        > Article 83 (Modifié par la loi n° 96-62 du 15 juillet 1996).- A titre exceptionnel, l’inspection du travail territorialement compétente peut : 1- auto
    - **85** `Article 85`
        > Article 85 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Les salariés ne peuvent être employés que conformément aux indications d’un horaire préc
    - NEW **88** `Article 88`
        > Article 88.- Dans les entreprises agricoles, la durée légale du travail est fixée à deux mille sept cents heures par an au maximum pour trois cents jo

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## travail_dismissal

- `q022` [fr, travail, concept] Quelles sont les conditions de licenciement ?
- `q044` [fr, travail, colloquial] Mon patron peut-il me virer sans préavis ?
- `q058` [ar, travail, colloquial] متى يمكن للمؤجر طرد العامل؟
- `q081` [en, travail, concept] When can an employer lawfully dismiss an employee?

**Current gold** (travailFr.pdf)

- **14** `H` Article 14.- (Modifié par la loi n° 94-29 du 21 février 1994). .- Le contrat de travail à durée déterminée prend fin par l’expiration de la durée convenue ou par l’accomplissement du travail objet du contrat. Le contrat à durée indéterminée prend fin par l’expiration du délai de préavis. Le contrat 
- **14** `H` Article 14 bis. (Ajouté par la loi n° 94-29 du 21 février 1994).- Le préavis de rupture du contrat de travail à durée indéterminée est notifié par lettre recommandée adressée à l’autre partie un mois avant la rupture du contrat. 14 Les travailleurs sont autorisés à s’absenter durant toute la deuxièm
- **14** `H` Article 14 ter. (Ajouté par la loi n° 94-29 du 21 février 1994).- L’employeur qui a l’intention de licencier un travailleur est tenu d’indiquer les causes du licenciement dans la lettre de préavis. Est considéré abusif le licenciement intervenu sans l’existence d’une cause réelle et sérieuse le just
- **14** `H` Article 14 quater. (Ajouté par la loi n° 94-29 du 21 février 1994).- La faute grave est considérée comme l’une des causes réelles et sérieuses justifiant le licenciement. Peuvent être considérés comme fautes graves selon les circonstances dans lesquelles ont été commises notamment les cas suivants :
- **14** `H` Article 14 quinter (Ajouté par la loi n° 94-29 du 21 février 1994).- Il appartient au juge d’apprécier l’existence du caractère réel et sérieux des causes du licenciement et le respect des procédures légales ou conventionnelles y afférentes, et ce, sur la base des éléments de preuve qui lui sont pré
- **16** `H` Article 16.- La faillite de l’employeur n’est pas une cause de résiliation du contrat et la masse des créanciers est subrogée aux droits et obligations qui en résultent.
- **23** `H` Article 23 (Modifié par la loi n° 94-29 du 21 février 1994).- La rupture abusive du contrat du travail par l’une des parties ouvre droit à des dommages-intérêts qui ne se confondent pas avec l’indemnité due pour inobservation du délai de préavis ou avec la gratification de fin de service visée à l’
- **23** `H` Article 23 bis (Ajouté par la loi n° 94-29 du 21 février 1994).- En cas de licenciement abusif, le préjudice donne lieu à des dommages-intérêts dont le montant varie entre le salaire d’un mois et celui de deux mois pour chaque année d’ancienneté dans l’entreprise sans que ces dommages-intérêts ne dé

**Corpus candidates** (BM25 over travailFr.pdf headings; query terms: conditions licenciement)

-      **21** (6.3) Article 21- 13 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Les travailleurs dont les contrats de travail auront été résiliés du fait de la suppression de leurs emplois pour des raisons économiqu
-      **21** (6.3) Article 21- 9 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- La commission régionale ou la commission centrale de contrôle du licenciement examine le dossier du licenciement ou de la mise en chômag
-      **21** (4.9) Article 21- 12 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Sont abusifs, le licenciement ou la mise en chômage intervenus sans l’avis préalable de la commission régionale ou la commission centra
-      **42** (4.9) Article 42.- Les conventions collectives visées à l’article précédent doivent au moins contenir des dispositions concernant : a) la liberté syndicale et la liberté d’opinion; b) les salaires applicabl
- gold **14** (4.8) Article 14 ter. (Ajouté par la loi n° 94-29 du 21 février 1994).- L’employeur qui a l’intention de licencier un travailleur est tenu d’indiquer les causes du licenciement dans la lettre de préavis. Es
-      **21** (4.6) Article 21- 3 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- L’inspection du travail territorialement compétente ou la Direction Générale de l’Inspection du Travail, selon le cas, doit procéder à u
-      **21** (4.5) Article 21- 7 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- La commission régionale ou la commission centrale de contrôle du licenciement peut demander à l’employeur de lui fournir les information
-      **371** (4.4) Article 371 .- Au cas de licenciement d'un ouvrier permanent, intervenu une fois la période d'essai expirée, pour quelque motif que ce soit, sauf celui de faute grave, insuffisance professionnelle ou 

**Retrieved by official v1** (top-6, one block per language variant)

- `q022` [fr] hit=False
    -   travailFr. art 258: Article 258- 2 (Ajouté par la loi n°96-62 du 15 juillet 1996).- Tout étranger, qui veut exercer en Tunisie un travail salarié de quelque nature qu'il 
    -   travailFr. art 4: Article 4.- Sont abrogées, toutes les dispositions antérieures contraires au présent Code et notamment les textes suivants : - décret du 15 juin 1910 
    -   travailFr. art 7: Article 7.- L’emploi de travailleurs étrangers est régi par les dispositions réglementant l’entrée, le séjour et le travail des étrangers en Tunisie.
    -   travailFr. art 263: Article 263 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Le travailleur étranger bénéficie des mêmes droits et est soumis aux mêmes obligations 
    -   travailFr. art 2: article 2 de la loi n° 60-18 du 27 juillet 1960 relative aux relations du travail et modifiant la loi n° 58-117 du 4 novembre 1958, instituant des con
    -   travailFr. art 166: Article 166 (Modifié par la loi n° 94-29 du 21 février 1994 et par la loi n° 2007-19 du 2 avril 2007).- Tout licenciement d’un membre titulaire ou sup
- `q044` [fr] hit=False
    -   travailFr. art 166: Article 166 (Modifié par la loi n° 94-29 du 21 février 1994 et par la loi n° 2007-19 du 2 avril 2007).- Tout licenciement d’un membre titulaire ou sup
    -   travailFr. art 378: Article 378 (Modifié par la loi n°76-84 du 11 août 1976 puis la loi n° 94-29 du 21 février 1994).- Au cas où la grève ou le lock-out s'étend sur deux 
    -   travailFr. art 370: Article 370.- Tout salarié, lors de son embauchage, doit être avisé s'il est engagé à titre permanent ou saisonnier ou occasionnel. Le salarié permane
    -   travailFr. art 376: Article 376 - ter (Ajouté par la loi n°94-29 du 21 février 1994).- Le préavis est adressé en même temps aux parties concernées par lettre recommandée 
    -   travailFr. art 21: Article 21- 3 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- L’inspection du travail territorialement compétente ou la Direction Générale de l’Insp
    -   travailFr. art 398: Article 398.- En cas de résiliation d'un contrat de louage de services fait sans détermination de durée, le préavis est, pour l'une et l'autre partie 
- `q058` [ar] hit=True
    -   travailFr. art 166: Article 166 (Modifié par la loi n° 94-29 du 21 février 1994 et par la loi n° 2007-19 du 2 avril 2007).- Tout licenciement d’un membre titulaire ou sup
    - ✓ travailFr. art 14: Article 14 ter. (Ajouté par la loi n° 94-29 du 21 février 1994).- L’employeur qui a l’intention de licencier un travailleur est tenu d’indiquer les ca
    -   travailFr. art 132: Article 132.- Lorsqu'un contrat de travail est conclu pour une durée déterminée, l'employeur doit, sou peine de dommages-intérêts, faire bénéficier le
    -   travailFr. art 371: Article 371 .- Au cas de licenciement d'un ouvrier permanent, intervenu une fois la période d'essai expirée, pour quelque motif que ce soit, sauf celu
    -   travailFr. art 128: Article 128.- Lorsque le contrat de travail d’un salarié, ayant au moins six mois de services continus dans la même entreprise, est résilié par le fai
    -   travailFr. art 258: Article 258- 2 (Ajouté par la loi n°96-62 du 15 juillet 1996).- Tout étranger, qui veut exercer en Tunisie un travail salarié de quelque nature qu'il 
- `q081` [en] hit=True
    - ✓ travailFr. art 14: Article 14 ter. (Ajouté par la loi n° 94-29 du 21 février 1994).- L’employeur qui a l’intention de licencier un travailleur est tenu d’indiquer les ca
    -   travailFr. art 166: Article 166 (Modifié par la loi n° 94-29 du 21 février 1994 et par la loi n° 2007-19 du 2 avril 2007).- Tout licenciement d’un membre titulaire ou sup
    -   travailFr. art 371: Article 371 .- Au cas de licenciement d'un ouvrier permanent, intervenu une fois la période d'essai expirée, pour quelque motif que ce soit, sauf celu
    -   travailFr. art 370: Article 370.- Tout salarié, lors de son embauchage, doit être avisé s'il est engagé à titre permanent ou saisonnier ou occasionnel. Le salarié permane
    -   travailFr. art 21: Article 21. (Modifié par la loi n° 96-62 du 15 juillet 1996).- Tout employeur qui a l’intention de licencier ou de mettre en chômage pour des raisons 
    -   travailFr. art 128: Article 128.- Lorsque le contrat de travail d’un salarié, ayant au moins six mois de services continus dans la même entreprise, est résilié par le fai

**Suggested change:** Remove 16 (employer bankruptcy 'n'est pas une cause de résiliation': not a dismissal condition). Add 21 (the 21-x series on economic dismissal and the control commission). 14 (14 bis..quinquies: notice, grounds, serious fault, judge control) and 23 kept.

- add: 21   |   remove: 16
- proposed gold (anchor = the text the intended chunk must start with):
    - **14** `Article 14` (5 chunks: sub-numbered series, all intended)
        > Article 14.- (Modifié par la loi n° 94-29 du 21 février 1994). .- Le contrat de travail à durée déterminée prend fin par l’expiration de la durée conv
    - NEW **21** `Article 21` (13 chunks: sub-numbered series, all intended)
        > Article 21. (Modifié par la loi n° 96-62 du 15 juillet 1996).- Tout employeur qui a l’intention de licencier ou de mettre en chômage pour des raisons 
    - **23** `Article 23` (2 chunks: sub-numbered series, all intended)
        > Article 23 (Modifié par la loi n° 94-29 du 21 février 1994).- La rupture abusive du contrat du travail par l’une des parties ouvre droit à des dommage

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## travail_paid_leave

- `q023` [fr, travail, concept] Quelle est la durée du congé annuel payé ?
- `q057` [ar, travail, concept] ما هي مدة الإجازة السنوية المدفوعة؟
- `q080` [en, travail, concept] How many days of paid annual leave is a worker entitled to?

**Current gold** (travailFr.pdf)

- **112** `H` Article 112.- Tout salarié a droit, chaque année, à un congé payé à la charge de l'employeur dans les conditions fixées ci-après.

**Corpus candidates** (BM25 over travailFr.pdf headings; query terms: durée congé annuel payé)

-      **125** (16.6) Article 125.- Le congé annuel payé peut être fractionné en périodes d’un ou plusieurs jours jusqu’à concurrence de la moitié de sa durée totale. Sont réputés jours ouvrables pour la jouissance d’un co
-      **94** (15.6) Article 94- 5 (Ajouté par la loi n°96-62 du 15 juillet 1996).- Le salaire du travailleur à temps partiel et les indemnités auxquelles a droit au titre du congé annuel payé, des jours fériés chômés et 
-      **118** (13.5) Article 118.- Le congé payé ne dépassant pas six jours ouvrables doit être continu. Le congé d'une durée supérieure à six jours ouvrables peut être fractionné par l'employeur, avec l'agrément du salar
-      **133** (13.1) Article 133.- Est considéré comme ne donnant pas le congé légal, l'employeur qui fait travailler un salarié, même en dehors de l'établissement où il travaille habituellement, pendant la période fixée 
-      **128** (12.0) Article 128.- Lorsque le contrat de travail d’un salarié, ayant au moins six mois de services continus dans la même entreprise, est résilié par le fait de l'employeur, avant que ledit salarié ait pu b
-      **119** (11.7) Article 119 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Le travailleur perçoit pendant son congé une indemnité calculée sur la base de la durée du congé à laquelle il a droit d'une part, et le 
-      **114** (11.0) Article 114 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Sont considérées comme un mois de travail effectif, pour la détermination de la durée du congé annuel, les périodes équivalentes à vingt-
-      **130** (10.4) Article 130.- Les employeurs doivent, en vue du contrôle de l'application du présent chapitre, tenir un registre portant leur nom et leur adresse où sont indiqués : 1) la période ordinaire des vacance

**Retrieved by official v1** (top-6, one block per language variant)

- `q023` [fr] hit=False
    -   travailFr. art 125: Article 125.- Le congé annuel payé peut être fractionné en périodes d’un ou plusieurs jours jusqu’à concurrence de la moitié de sa durée totale. Sont 
    -   travailFr. art 114: Article 114 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Sont considérées comme un mois de travail effectif, pour la détermination de la durée d
    -   travailFr. art 113: Article 113 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Tout travailleur qui, au cours de l'année de référence, justifie avoir été 53 occupé ch
    -   travailFr. art 118: Article 118.- Le congé payé ne dépassant pas six jours ouvrables doit être continu. Le congé d'une durée supérieure à six jours ouvrables peut être fr
    -   travailFr. art 117: Article 117 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Le congé annuel est octroyé au cours de la période du 1er juin au 31 octobre de chaque 
    -   travailFr. art 119: Article 119 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Le travailleur perçoit pendant son congé une indemnité calculée sur la base de la durée
- `q057` [ar] hit=False
    -   travailFr. art 125: Article 125.- Le congé annuel payé peut être fractionné en périodes d’un ou plusieurs jours jusqu’à concurrence de la moitié de sa durée totale. Sont 
    -   travailFr. art 410: Article 410.- Les contrats ci-dessus définis doivent être écrits. Ils sont au choix des parties, soit d’une durée déterminée, soit d’une durée indéter
    -   travailFr. art 118: Article 118.- Le congé payé ne dépassant pas six jours ouvrables doit être continu. Le congé d'une durée supérieure à six jours ouvrables peut être fr
    -   travailFr. art 114: Article 114 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Sont considérées comme un mois de travail effectif, pour la détermination de la durée d
    -   travailFr. art 113: Article 113 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Tout travailleur qui, au cours de l'année de référence, justifie avoir été 53 occupé ch
    -   travailFr. art 117: Article 117 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Le congé annuel est octroyé au cours de la période du 1er juin au 31 octobre de chaque 
- `q080` [en] hit=False
    -   travailFr. art 113: Article 113 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Tout travailleur qui, au cours de l'année de référence, justifie avoir été 53 occupé ch
    -   travailFr. art 123: Article 123 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Les travailleurs ont droit, à condition de compter au moins six mois de services contin
    -   travailFr. art 118: Article 118.- Le congé payé ne dépassant pas six jours ouvrables doit être continu. Le congé d'une durée supérieure à six jours ouvrables peut être fr
    -   travailFr. art 125: Article 125.- Le congé annuel payé peut être fractionné en périodes d’un ou plusieurs jours jusqu’à concurrence de la moitié de sa durée totale. Sont 
    -   travailFr. art 114: Article 114 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Sont considérées comme un mois de travail effectif, pour la détermination de la durée d
    -   travailFr. art 128: Article 128.- Lorsque le contrat de travail d’un salarié, ayant au moins six mois de services continus dans la même entreprise, est résilié par le fai

**Suggested change:** Add 113 (right acquired per month of work, i.e. the duration) and 115 (extra day per 5 years of service). 112 only states the right.

- add: 113, 115   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **112** `Article 112`
        > Article 112.- Tout salarié a droit, chaque année, à un congé payé à la charge de l'employeur dans les conditions fixées ci-après.
    - NEW **113** `Article 113`
        > Article 113 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Tout travailleur qui, au cours de l'année de référence, justifie avoir été 53 occupé ch
    - NEW **115** `Article 115`
        > Article 115 (1).- La durée du congé ainsi fixée est augmentée à raison d'un jour ouvrable par période entière, continue ou non, de cinq ans de service

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## travail_fixed_term

- `q024` [fr, travail, concept] Qu'est-ce que le contrat de travail à durée déterminée ?

**Current gold** (travailFr.pdf)

- **6** `H` Article 6 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Le contrat de travail est une convention par laquelle l’une des parties appelée travailleur ou salarié s’engage à fournir à l’autre partie appelée employeur ses services personnels sous la direction et le contrôle de celle-ci moyennant une
- **6** `H` Article 6- 2 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Le contrat de travail est conclu pour une durée indéterminée ou pour une durée déterminée. Le contrat de travail à durée déterminée peut comporter une limitation de la durée de son exécution ou l’indication du travail dont l’accomplissem
- **6** `H` Article 6- 3 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Les travailleurs recrutés par contrats de travail à durée indéterminée sont soumis en ce qui concerne la période d’essai et la confirmation aux dispositions légales ou contractuelles qui leur sont applicables.
- **6** `H` Article 6- 4 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- 1- Le contrat de travail à durée déterminée peut être conclu dans les cas suivants : 11 - l’accomplissement de travaux de premier établissement ou de travaux neufs; - l’accomplissement de travaux nécessités par un surcroît extraordinaire

**Corpus candidates** (BM25 over travailFr.pdf headings; query terms: contrat travail durée déterminée)

- gold **6** (13.5) Article 6- 2 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Le contrat de travail est conclu pour une durée indéterminée ou pour une durée déterminée. Le contrat de travail à durée déterminée peut 
-      **14** (11.2) Article 14.- (Modifié par la loi n° 94-29 du 21 février 1994). .- Le contrat de travail à durée déterminée prend fin par l’expiration de la durée convenue ou par l’accomplissement du travail objet du 
-      **24** (11.1) Article 24 (Modifié par la loi n° 94-29 du 21 février 1994).- Les dommages-intérêts dus pour rupture abusive du contrat de travail à durée déterminée du fait de l’employeur sont fixés à un montant éga
-      **94** (10.5) Article 94- 2 (Ajouté par la loi n°96-62 du 15 juillet 1996).- Le contrat de travail à durée déterminée ou indéterminée peut être conclu pour un travail à temps partiel. Est considéré comme travail à 
- gold **6** (9.9) Article 6- 4 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- 1- Le contrat de travail à durée déterminée peut être conclu dans les cas suivants : 11 - l’accomplissement de travaux de premier établis
-      **132** (9.7) Article 132.- Lorsqu'un contrat de travail est conclu pour une durée déterminée, l'employeur doit, sou peine de dommages-intérêts, faire bénéficier le salarié de son congé dans des conditions telles q
-      **32** (9.1) Article 32.- La convention collective de travail peut être conclue, soit pour une durée indéterminée, soit pour une durée déterminée ne pouvant excéder cinq ans. A défaut de stipulation contraire, la 
-      **412** (8.2) Article 412.- Quelles que soient la cause et la date de la cessation des services de l'employé, même lorsqu'elle se produit à l'expiration du contrat à durée déterminée, l'employé a toujours droit, à 

**Retrieved by official v1** (top-6, one block per language variant)

- `q024` [fr] hit=True
    - ✓ travailFr. art 6: Article 6- 2 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Le contrat de travail est conclu pour une durée indéterminée ou pour une durée détermin
    -   travailFr. art 94: Article 94- 2 (Ajouté par la loi n°96-62 du 15 juillet 1996).- Le contrat de travail à durée déterminée ou indéterminée peut être conclu pour un trava
    -   travailFr. art 410: Article 410.- Les contrats ci-dessus définis doivent être écrits. Ils sont au choix des parties, soit d’une durée déterminée, soit d’une durée indéter
    -   travailFr. art 132: Article 132.- Lorsqu'un contrat de travail est conclu pour une durée déterminée, l'employeur doit, sou peine de dommages-intérêts, faire bénéficier le
    -   travailFr. art 14: Article 14.- (Modifié par la loi n° 94-29 du 21 février 1994). .- Le contrat de travail à durée déterminée prend fin par l’expiration de la durée conv
    -   travailFr. art 17: Article 17.- Lorsqu’à l’expiration du terme établi, le salarié continue à rendre ses services sans opposition de l’autre partie, le contrat se transfo

**Suggested change:** Narrow to the CDD articles 6-2 (CDI or CDD, limitation of duration) and 6-4 (cases where a CDD may be concluded); plain 'Article 6' is the general contract definition.

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **6** `Article 6- 2`
        > Article 6- 2 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- Le contrat de travail est conclu pour une durée indéterminée ou pour une durée détermin
    - **6** `Article 6- 4`
        > Article 6- 4 (Ajouté par la loi n° 96-62 du 15 juillet 1996).- 1- Le contrat de travail à durée déterminée peut être conclu dans les cas suivants : 11

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## travail_maternity

- `q025` [fr, travail, concept] Quels sont les droits de la femme enceinte au travail ?

**Current gold** (travailFr.pdf)

- **64** `F` article 64 de ce code sans excéder douze semaines, l’employeur ne pourrait lui donner congé pendant cette absence.
- **64** `H` Article 64.- Dans les entreprises de toute nature, à l’exception des établissements où sont exclusivement employés les membres d’une même famille, la femme : a) aura droit à l’occasion de son accouchement, sur production d’un certificat médical, à un congé de repos de 30 jours. Ce congé peut être pr
- **64** `F` article 64 du présent code et les périodes pendant lesquelles l'exécution du contrat de travail est suspendue pour cause d'accident de travail au cours d'une période ininterrompue ne dépassant pas une année.

**Corpus candidates** (BM25 over travailFr.pdf headings; query terms: droits femme enceinte travail)

-      **20** (7.8) Article 20.- La maladie suspend le contrat de travail. Elle ne constitue un motif de rupture que si elle est suffisamment grave ou prolongée et si les nécessités de l’entreprise obligent l’employeur à
-      **5** (6.4) Article 5 bis ( Ajouté par la loi n° 93-66 du 5 juillet 1993).- Il ne peut être fait de discrimination entre l’homme et la femme dans l’application des dispositions du présent code et des textes pris 
-      **263** (5.3) Article 263 (Modifié par la loi n° 96-62 du 15 juillet 1996).- Le travailleur étranger bénéficie des mêmes droits et est soumis aux mêmes obligations résultant des relations du travail et applicables 
-      **16** (5.1) Article 16.- La faillite de l’employeur n’est pas une cause de résiliation du contrat et la masse des créanciers est subrogée aux droits et obligations qui en résultent.
-      **249** (5.1) Article 249.- Il n'est dérogé en aucune façon aux dispositions spéciales qui auraient accordé aux syndicats des droits non visés dans le présent chapitre. 94
-      **386** (4.8) Article 386 - ter (Ajouté par la loi n°94-29 du 21 février 1994).- Sont exonérées des droits de timbre et d'enregistrement toutes les formalités accomplies et exigées par la procédure d'arbitrage ains
-      **437** (4.8) Article 437 (1) (Modifié par la loi n° 70-20 du 30 avril 1970).- La médaille du travail ne sera conférée qu'aux personnes jouissant de leurs droits civils et politiques. En cas de services discontinus
-      **195** (4.7) Article 195.- Le montant des indemnités et droits alloués aux conseillers et témoins des conseils de prud'hommes ainsi que l'imputation et le mode de règlement des dépenses de fonctionnement de ces ju

**Retrieved by official v1** (top-6, one block per language variant)

- `q025` [fr] hit=True
    - ✓ travailFr. art 64: Article 64.- Dans les entreprises de toute nature, à l’exception des établissements où sont exclusivement employés les membres d’une même famille, la 
    -   travailFr. art 66: article 66 du présent code peut être modifié et l’interdiction du travail de nuit des femmes prévue par le même article peut être levée et ce, dans le
    -   travailFr. art 18: Article 18.- Dans tout contrat de travail, la durée de la période d’essai résulte des conventions collectives ou particulières, de l’usage ou de la lo
    -   travailFr. art 68: article 68- 2 à la femme travailleuse pendant une période de seize semaines au minimum avant et après l’accouchement, dont au moins huit avant la date
    -   travailFr. art 166: Article 166 (Modifié par la loi n° 94-29 du 21 février 1994 et par la loi n° 2007-19 du 2 avril 2007).- Tout licenciement d’un membre titulaire ou sup
    -   travailFr. art 29: Article 29.- Le chef d’entreprise est responsable avec le sous- entrepreneur de main-d’œuvre de l’observation de toutes les prescriptions de la législ

**Suggested change:** No change; anchored (two fragment chunks also carry number 64).

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **64** `Article 64.- Dans les entreprises`
        > Article 64.- Dans les entreprises de toute nature, à l’exception des établissements où sont exclusivement employés les membres d’une même famille, la 

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## csp_marriage_conditions

- `q026` [fr, statut_personnel, concept] Quelles sont les conditions du mariage ?
- `q059` [ar, statut_personnel, concept] ما هي شروط الزواج؟
- `q067` [ar, unfiltered, cross_domain] ما هي شروط الزواج؟
- `q073` [en, statut_personnel, concept] What are the conditions for marriage?

**Current gold** (Statutpersonnel.pdf)

- **5** `F` article 5 de la loi n°57-40 du 27 septembre 1957).
- **5** `H` Article 5 (Modifié par le décret-loi n°64-1 du 20 février 1964, ratifié par la loi n°64-1 du 21 avril 1964 et par la loi n°2007-32 du 14 mai 2007).- Les deux futurs époux ne doivent pas se trouver dans l'un des cas d'empêchements prévus par la loi. En outre, chacun des deux futurs époux n’ayant pas 
- **5** `F` article 5 et des articles 15, 16, 17, 18 ,19, et 20 du présent code. 9 Lorsque des poursuites pénales seront exercées par application de l'
- **5** `H` Article 5 .- L'officier de l'état civil donnera lecture des actes aux parties comparantes et aux témoins. Il y sera fait mention de l'accomplissement de cette formalité.
- **5** `H` Article 5 .- Le Premier ministre, ministre de l'intérieur, les gouverneurs, les délégués et les présidents des communes sont chargés, chacun en ce qui le concerne, de l'exécution du présent décret qui sera publié au Journal Officiel de la République Tunisienne. Fait à Tunis, le 22 janvier 1986. P/le
- **5** `H` Article 5 .- La procuration en vue du mariage n'est valable que pour autant qu'elle exprime l’option expresse du mandant relative à l'adhésion ou la non adhésion au régime de la communauté des biens.
- **5** `H` Article 5 .- Dans les cas exceptionnels, le juge peut dispenser les futurs époux, ou l'un d'eux seulement, de la remise du certificat médical. Le certificat n'est exigible d'aucun des futurs époux au cas du péril imminent de mort de l'un d'eux.
- **5** `H` Article 5 .- Le tuteur officieux a, vis-à-vis du pupille, les droits et obligations prévus par les articles 54 et suivant du code du statut personnel. Il est, en outre, civilement responsable des actes du pupille, dans les mêmes conditions que les père et mère.
- **5** `H` Article 5 .- Aussitôt cette transcription effectuée, le tuteur testamentaire administre les biens du mineur. A défaut du tuteur testamentaire, le juge des tutelles, visé à l'
- **5** `F` article 5 de la présente loi sont applicables lorsque la maternité est prouvée.
- **5** `H` Article 5 .- Les règles relatives aux empêchements au mariage prévues par les articles 14, 15, 16 et 17 du code du statut personnel, lorsque la paternité est prouvée, sont applicables aux enfants abandonnés ou dont la filiation est inconnue auxquels on a attribué un nom patronymique en vertu de la p
- **5** `H` Article 5 .- Le montant de la pension alimentaire ou de la rente de divorce, due en vertu d'un jugement, qui n'a pas été payé par la partie débitrice au fonds de garantie de la pension alimentaire et de la rente de divorce, est majoré d'une indemnité de retard qui sera versée par le débiteur à ce fo
- **5** `H` Article 5 .- A l’expiration du délai fixé par l’
- **8** `H` Article 8 .- Consent au mariage du mineur le plus proche parent agnat. Il doit être saint d'esprit, de sexe masculin, majeur. Le père ou son mandataire consent au mariage de son enfant mineur, qu'il soit de sexe masculin ou féminin. S'il n’y a point de tuteur, le consentement est donné par le juge.
- **8** `F` article 8 du présent code, relatif au mariage. Le testament du père ne produit ses effets qu'après la mort de la mère ou de son incapacité. En cas de décès des parents ou de leur incapacité, et à défaut de tuteur testamentaire, le juge doit nommer un tuteur.
- **8** `H` Article 8 .- Les actes de l'état civil seront inscrits sur des registres tenus en double.
- **8** `H` Article 8 .- L'accord sur la communauté des biens, postérieur à la conclusion du contrat de mariage, doit être constaté par acte authentique. L'officier public ayant rédigé l'acte doit se conformer aux dispositions du paragraphe 2 de l'
- **8** `F` article 8 de cette loi. 95 Titre II DU DOMAINE DE LA COMMUNAUTE DES BIENS Chapitre I Les biens communs
- **8** `H` Article 8 .- L'adoption est permise dans les conditions prévues aux articles suivants. 115
- **8** `H` Article 8 .- Lorsqu'à la suite de reddition de comptes de gestion d'un tuteur testamentaire ou autre, le commissaire du gouvernement(*) constate que des deniers appartenant aux mineurs sont disponibles, il en ordonne le versement immédiat à la caisse des dépôts et consignations, au compte courant de
- **8** `H` Article 8 .- La caisse Nationale de Sécurité Sociale est en droit de prendre toutes les mesures et d'introduire toute action en justice susceptibles de protéger les droits du fonds de garantie de la pension alimentaire et de la rente de divorce. Elle est convoquée obligatoirement dans tous les cas o
- **8** `H` Article 8 .- Quiconque a indûment bénéficié des sommes d’argent du fonds de garantie de la pension alimentaire et de la rente de divorce doit les restituer sans délai. La caisse nationale de sécurité sociale peut se faire rembourser lesdites sommes par voie de contraintes selon la procédure de rembo
- **14** `H` Article 14 .- Les empêchements au mariage sont de deux sortes : permanents et provisoires. Les empêchements permanents résultent de la parenté, de l'alliance, de l'allaitement ou du triple divorce. Les empêchements provisoires résultent de l'existence d'un mariage non dissous et de la non-expiration
- **14** `F` article 14 ci-dessous, se faire délivrer, par les dépositaires des registres de l'état civil, des copies des actes inscrits sur les registres. Les copies, délivrées conformes aux registres, portant en toutes lettres la date de leur délivrance et revêtues de la signature et du sceau de l'autorité qui
- **14** `H` Article 14 .- Nul, à l'exception du commissaire du gouvernement(*), de l'enfant, de ses ascendants et descendants en ligne directe, de son conjoint ni séparé ni divorcé, de son tuteur ou de son représentant légal, s'il est mineur ou en état d'incapacité, ne pourra obtenir une copie conforme d'un act
- **14** `H` Article 14 .- Lorsque les deux époux choisissent le régime de la communauté des biens, l'officier de l'état civil doit le mentionner dans ses registres et dans tous extrait et copie. Si l'accord des époux stipule une condition contraire aux dispositions de cette loi, l'officier de l'état civil doit 
- **14** `H` Article 14 .- L'adopté prend le nom de l’adoptant. Il peut changer de prénom, mention en sera faite dans le jugement d'adoption à la demande de l'adoptant.
- **14** `H` Article 14 .- Le tuteur doit administrer les biens de ses pupilles susvisés, conformément à la loi, et en bon père de famille. Il doit tenir un registre sur lequel il fait inscrire, par les soins de deux notaires, toutes les recettes et dépenses effectuées par lui.

**Corpus candidates** (BM25 over Statutpersonnel.pdf headings; query terms: conditions mariage)

-      **4** (6.5) Article 4 .- La preuve du mariage ne peut être rapportée que par un acte authentique dans des conditions fixées par une loi ultérieure. En ce qui concerne les mariages célébrés à l'étranger, la preuve
- gold **8** (4.8) Article 8 .- L'adoption est permise dans les conditions prévues aux articles suivants. 115
-      **9** (4.1) Article 9. (Modifié par la loi n°59-69 du 19 juin 1959).- L'adoptant doit être une personne majeure de l'un ou l'autre sexe, mariée, jouissant de la pleine capacité civile. Il doit être de bonne moral
-      **13** (4.0) Article 13 .- Sont communes, les dettes et les charges découlant de l'acquisition de la propriété du bien commun, de son exploitation, administration, usage ou de la disposition de ce bien. Sont égale
- gold **5** (3.7) Article 5 .- Le tuteur officieux a, vis-à-vis du pupille, les droits et obligations prévus par les articles 54 et suivant du code du statut personnel. Il est, en outre, civilement responsable des acte
-      **27** (3.6) Article 27 .- Lorsqu'un des époux prédécède et qu'une contestation s'élève entre le conjoint survivant et les héritiers du prédécédé au sujet de la propriété des biens se trouvant au domicile conjugal
-      **16** (3.2) Article 16 .- Est prohibé, le mariage de l'homme avec les ascendantes de sa femme dès la célébration du mariage, avec les descendantes de sa femme à condition que le mariage ait été consommé, avec les
-      **16** (3.1) Article 16 .- Tout acte de l'état civil des Tunisiens et des Etrangers, fait en pays étranger, fera foi, s'il a été rédigé dans les formes utilisées dans ledit pays. Ceux de ces actes, qui concernent 

**Retrieved by official v1** (top-6, one block per language variant)

- `q026` [fr] hit=False
    -   Statutpers art 31: Article 31 .- L'acte de mariage est conclu en Tunisie devant deux notaires ou devant l'Officier de l'état civil en présence de deux témoins honorables
    -   Statutpers art 37: Article 37 .- Tout acte de mariage des Tunisiens, conclu à l'étranger selon les formes locales, devra être transcrit, dans les trois mois de sa rédact
    -   Statutpers art 38: Article 38 .- L'acte de mariage des Etrangers en Tunisie sera rédigé conformément aux lois tunisiennes, sur le vu d'un certificat de leur consul attes
    -   Statutpers art 10: Article 10 .- La différence d'âge entre l'adoptant et l'adopté doit être au minimum de 15 ans, sauf dans les cas ou l'adopté est l'enfant du conjoint 
    -   Statutpers art 9: Article 9 .- Les ministres de la justice et des affaires sociales sont chargés, chacun en ce qui le concerne, de l’exécution du présent décret qui ser
    -   Statutpers art 4: Article 4 .- L'attestation de conformité a la même force probante que les extraits des actes de l'état civil. La présente loi sera publiée au Journal 
- `q059` [ar] hit=False
    -   Statutpers art 31: Article 31 .- L'acte de mariage est conclu en Tunisie devant deux notaires ou devant l'Officier de l'état civil en présence de deux témoins honorables
    -   Statutpers art 37: Article 37 .- Tout acte de mariage des Tunisiens, conclu à l'étranger selon les formes locales, devra être transcrit, dans les trois mois de sa rédact
    -   Statutpers art 38: Article 38 .- L'acte de mariage des Etrangers en Tunisie sera rédigé conformément aux lois tunisiennes, sur le vu d'un certificat de leur consul attes
    -   Statutpers art 10: Article 10 .- La différence d'âge entre l'adoptant et l'adopté doit être au minimum de 15 ans, sauf dans les cas ou l'adopté est l'enfant du conjoint 
    -   Statutpers art 9: Article 9 .- Les ministres de la justice et des affaires sociales sont chargés, chacun en ce qui le concerne, de l’exécution du présent décret qui ser
    -   Statutpers art 7: Article 7 .- L'officier de l'état civil et les notaires qui ne se conformeront pas aux prescriptions de l'article premier de la présente loi seront po
- `q067` [ar] hit=False
    -   Statutpers art 31: Article 31 .- L'acte de mariage est conclu en Tunisie devant deux notaires ou devant l'Officier de l'état civil en présence de deux témoins honorables
    -   tun_RecAcF art 4: Art. 4 – La Tunisie est un Etat unitaire. Il n’est pas permis d’édicter toute législation portant atteinte à son unité.
    -   Statutpers art 37: Article 37 .- Tout acte de mariage des Tunisiens, conclu à l'étranger selon les formes locales, devra être transcrit, dans les trois mois de sa rédact
    -   Statutpers art 38: Article 38 .- L'acte de mariage des Etrangers en Tunisie sera rédigé conformément aux lois tunisiennes, sur le vu d'un certificat de leur consul attes
    -   EnfantFr.p art 2: article 2 de la convention qui ne peuvent constituer un obstacle à l'application des dispositions de sa législation nationale relative au statut perso
    -   Nationalit art 14: Article 14.- La femme étrangère, qui épouse un tunisien et qui, en vertu de sa loi nationale, conserve sa nationalité d’origine par le mariage avec un
- `q073` [en] hit=True
    -   Statutpers art 58: Article 58 (Modifié par la loi n°81-7 du 18 février 1981).- Le titulaire du droit de garde doit être majeur, sain d'esprit, honnête, capable de pourvo
    -   Statutpers art 9: Article 9 .- Les ministres de la justice et des affaires sociales sont chargés, chacun en ce qui le concerne, de l’exécution du présent décret qui ser
    - ✓ Statutpers art 8: Article 8 .- Consent au mariage du mineur le plus proche parent agnat. Il doit être saint d'esprit, de sexe masculin, majeur. Le père ou son mandatair
    -   Statutpers art 118: Article 118.- En cas d’égalité dans la classe et le degré et lorsque la parenté est plus ou moins proche, le lien de parenté le plus fort l’emporte su
    -   Statutpers art 10: Article 10 .- La différence d'âge entre l'adoptant et l'adopté doit être au minimum de 15 ans, sauf dans les cas ou l'adopté est l'enfant du conjoint 
    - ✓ Statutpers art 5: Article 5 (Modifié par le décret-loi n°64-1 du 20 février 1964, ratifié par la loi n°64-1 du 21 avril 1964 et par la loi n°2007-32 du 14 mai 2007).- L

**Suggested change:** Statutpersonnel.pdf bundles the CSP with état-civil, adoption, tutelle... laws, so 'Article 5/8/14' have 13/9/6 chunks. Anchors select the CSP articles. Add 3 (consentement des deux époux) and 6 (consentement du tuteur pour le mineur). Optional candidates not added: 7 (prodigue), 15-17 (empêchements).

- add: 3, 6   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - NEW **3** `Article 3 .- Le mariage n'est formé`
        > Article 3 .- Le mariage n'est formé que par le consentement des deux époux. La présence de deux témoins honorables et la fixation d'une dot au profit 
    - **5** `Article 5 (Modifié par le décret-loi n°64-1`
        > Article 5 (Modifié par le décret-loi n°64-1 du 20 février 1964, ratifié par la loi n°64-1 du 21 avril 1964 et par la loi n°2007-32 du 14 mai 2007).- L
    - NEW **6** `Article 6 (Modifié par la loi n°93-74 du 12 juillet 1993).- Le mariage du mineur`
        > Article 6 (Modifié par la loi n°93-74 du 12 juillet 1993).- Le mariage du mineur est subordonné au consentement de son tuteur et de sa mère. En cas de
    - **8** `Article 8 .- Consent au mariage du mineur`
        > Article 8 .- Consent au mariage du mineur le plus proche parent agnat. Il doit être saint d'esprit, de sexe masculin, majeur. Le père ou son mandatair
    - **14** `Article 14 .- Les empêchements au mariage`
        > Article 14 .- Les empêchements au mariage sont de deux sortes : permanents et provisoires. Les empêchements permanents résultent de la parenté, de l'a

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## csp_divorce

- `q027` [fr, statut_personnel, concept] Comment se déroule le divorce ?
- `q042` [fr, unfiltered, cross_domain] Quelles sont les causes de divorce ?
- `q061` [ar, statut_personnel, concept] كيف يتم الطلاق؟
- `q087` [en, unfiltered, cross_domain] What are the grounds for divorce?

**Current gold** (Statutpersonnel.pdf)

- **29** `H` Article 29 .- Le divorce est la dissolution du mariage.
- **29** `H` Article 29 .- Au premier port où le bâtiment abordera, pour toute autre cause que celle que son désarmement, l'officier instrumentaire sera tenu de déposer deux expéditions de chacun des actes de naissance dressés à bord, dans un port tunisien, au Bureau de l'Autorité Maritime, et, dans un port étra
- **30** `H` Article 30 .- Le divorce ne peut avoir lieu que par-devant le Tribunal.
- **30** `H` Article 30 .- A l'arrivée du bâtiment dans le port de désarmement, l'officier instrumentaire sera tenu de déposer, en même temps que le rôle d'équipage, une expédition de chacun des actes de naissance dressés à bord dont copie n'aurait point été déjà déposée conformément aux prescriptions de l'artic
- **30** `F` ARTICLE 30 DU CODE PENAL, D'UN ABSENT ET D'UN INTERDIT POUR CAUSE DE DEMENCE OU DE FAIBLESSE D'ESPRIT
- **30** `F` article 30 du code pénal, de l’absent et de l'interdit pour cause de démence ou de faiblesse d'esprit. L'inventaire énumère : 1) tous les biens meubles et immeubles, 2) toutes les charges, dettes ou obligations dont l'existence est déclarée ou relevée, Si, au cours de l'opération, des revendications
- **30** `F` article 30 du code pénal conserve la faculté d'exercer les droits exclusivement personnels qui ne sont pas contraires à l'intérêt de la peine. __________ (1) L'intitulé du titre II a été modifié par l'
- **30** `F` article 30 du code pénal, ni répondre en tant que défendeur, dans une action identique sans l'autorisation écrite du juge des tutelles.
- **31** `H` Article 31. (Modifié par la loi n°81-7 du 18 février 1981).- Le Tribunal prononce le divorce : 1) en cas de consentement mutuel des époux, 2) à la demande de l'un des époux en raison du préjudice qu'il a subi, 3) à la demande du mari ou de la femme. Il est statué sur la réparation du préjudice matér
- **31** `H` Article 31 .- L'acte de mariage est conclu en Tunisie devant deux notaires ou devant l'Officier de l'état civil en présence de deux témoins honorables. Le mariage des Tunisiens à l'étranger est célébré devant les agents diplomatiques ou consulaires de Tunisie, ou selon la loi locale.
- **31** `F` article 31 ci-dessus est nulle. En outre, les deux époux sont passibles d'une peine de trois mois d'emprisonnement. Lorsque des poursuites pénales seront exercées, en vertu des dispositions de l'alinéa précédent, il sera statué par un seul et même jugement sur l'infraction et la nullité du mariage. 

**Corpus candidates** (BM25 over Statutpersonnel.pdf headings; query terms: déroule divorce)

-      **11** (4.0) Article 11 .- Les fonctions de juge des tutelles sont assurées au tribunal de première instance de Tunis par un magistrat ayant le grade de vice-président de cette juridiction. Dans les autres tribuna
-      **2** (3.8) Article 2 (Modifié par le décret n°2006-826 du 23 mars 2006).- Les demandes d’obtention de la pension alimentaire ou de la rente de divorce doivent être accompagnées des pièces suivantes : 142 - une c
-      **6** (3.7) Article 6 .- Les montants de la pension alimentaire ou de la rente de divorce payés par le fonds de garantie de la pension alimentaire et de la rente de divorce sont majorés de 5% à titre de frais de 
- gold **29** (3.6) Article 29 .- Le divorce est la dissolution du mariage.
- gold **30** (3.5) Article 30 .- Le divorce ne peut avoir lieu que par-devant le Tribunal.
-      **39** (3.3) Article 39 .- Le mari indigent ne doit pas d'aliments. Cependant, si, à l'expiration d'un délai de deux mois accordé par le juge, il ne peut exécuter cette obligation, le juge prononcera le divorce. T
-      **3** (3.3) Article 3 .- Le fonds de garantie de la pension alimentaire et de la rente de divorce est subrogé aux ayants-droit de la pension alimentaire ou de la rente de divorce dans leurs droits vis-à-vis de la
-      **6** (3.2) Article 6 .- Les bénéficiaires de la pension alimentaire ou de la rente de divorce du fonds de garantie de la pension alimentaire et de la rente de divorce sont tenus de présenter au bureau régional d

**Retrieved by official v1** (top-6, one block per language variant)

- `q027` [fr] hit=True
    -   Statutpers art 10: Article 10 .- La procédure d'intervention du fonds de garantie de la pension alimentaire et de la rente de divorce est fixée par décret. La présente l
    -   Statutpers art 5: Article 5 .- Les règles relatives aux empêchements au mariage prévues par les articles 14, 15, 16 et 17 du code du statut personnel, lorsque la patern
    - ✓ Statutpers art 31: Article 31. (Modifié par la loi n°81-7 du 18 février 1981).- Le Tribunal prononce le divorce : 1) en cas de consentement mutuel des époux, 2) à la dem
    -   Statutpers art 26: Article 26 .- Lorsque les dettes sont supérieures à la valeur du bien commun, chacun des époux reste tenu de participer au paiement de la fraction non
    -   Statutpers art 2: Article 2 .- Le ministre de l'intérieur est chargé de l'exécution du présent arrêté qui sera publié au Journal Officiel de la République Tunisienne. T
    -   Statutpers art 9: Article 9 .- Les ministres de la justice et des affaires sociales sont chargés, chacun en ce qui le concerne, de l’exécution du présent décret qui ser
- `q042` [fr] hit=True
    -   Statutpers art 5: Article 5 .- Les règles relatives aux empêchements au mariage prévues par les articles 14, 15, 16 et 17 du code du statut personnel, lorsque la patern
    -   EnfantFr.p art 5: Article 5. – Les règles relatives aux empêchements au mariage prévues par les articles 14, 15, 16 et 17 du code du statut personnel, lorsque la patern
    - ✓ Statutpers art 29: Article 29 .- Le divorce est la dissolution du mariage.
    -   Statutpers art 11: Article 11 .- Peut être insérée dans l'acte de mariage, toute clause ou condition relative aux personnes ou aux biens. En cas de non- réalisation de l
    -   Statutpers art 28: Article 28 (Modifié par la loi n°93-74 du 12 juillet 1993).- En cas de dissolution du mariage avant la consommation, pour un motif imputable à l'un de
    -   Statutpers art 32: Article 32 .- L'acte de mariage énoncera : 1°) les prénoms, noms, professions, âges, dates et lieux de naissance, domiciles, résidence et nationalité 
- `q061` [ar] hit=True
    -   Statutpers art 9: Article 9 .- Les ministres de la justice et des affaires sociales sont chargés, chacun en ce qui le concerne, de l’exécution du présent décret qui ser
    -   Statutpers art 10: Article 10 .- La procédure d'intervention du fonds de garantie de la pension alimentaire et de la rente de divorce est fixée par décret. La présente l
    -   Statutpers art 37: Article 37 .- Tout acte de mariage des Tunisiens, conclu à l'étranger selon les formes locales, devra être transcrit, dans les trois mois de sa rédact
    - ✓ Statutpers art 31: Article 31 .- L'acte de mariage est conclu en Tunisie devant deux notaires ou devant l'Officier de l'état civil en présence de deux témoins honorables
    - ✓ Statutpers art 30: Article 30 .- Le divorce ne peut avoir lieu que par-devant le Tribunal.
    -   Statutpers art 26: Article 26 .- Lorsque les dettes sont supérieures à la valeur du bien commun, chacun des époux reste tenu de participer au paiement de la fraction non
- `q087` [en] hit=False
    -   EnfantFr.p art 2: article 2 de la convention qui ne peuvent constituer un obstacle à l'application des dispositions de sa législation nationale relative au statut perso
    -   DIPFR.pdf art 39: Article 39.- Le statut personnel est régi par le droit national de l'intéressé. Si l'intéressé bénéficie de plusieurs nationalités, le juge retiendra 
    -   DIPFR.pdf art 49: Article 49.- Le divorce et la séparation de corps sont régis par la loi nationale commune des époux en vigueur au moment où l'instance est introduite.
    -   Nationalit art 16: Article 16.- Dans les cas prévus aux articles 13 et 14 ci-dessus, l’intéressée est réputée n’avoir pas acquis la nationalité tunisienne si son mariage
    -   societeFr. art 16: article 16 du présent code. La nullité de la fusion ne peut être prononcée que pour les causes suivantes : - nullité de la délibération de l'assemblée
    -   tun_RecAcF art 4: Art. 4 – La Tunisie est un Etat unitaire. Il n’est pas permis d’édicter toute législation portant atteinte à son unité.

**Suggested change:** Anchor 29/30/31 to the CSP divorce articles (other chunks numbered 29/30/31 are ship registers and civil-status acts). Add 32 (procedure before the tribunal).

- add: 32   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **29** `Article 29 .- Le divorce est la dissolution`
        > Article 29 .- Le divorce est la dissolution du mariage.
    - **30** `Article 30 .- Le divorce ne peut avoir lieu`
        > Article 30 .- Le divorce ne peut avoir lieu que par-devant le Tribunal.
    - **31** `Article 31. (Modifié par la loi n°81-7`
        > Article 31. (Modifié par la loi n°81-7 du 18 février 1981).- Le Tribunal prononce le divorce : 1) en cas de consentement mutuel des époux, 2) à la dem
    - NEW **32** `Article 32 (Modifié par la loi n°2010-50`
        > Article 32 (Modifié par la loi n°2010-50 du 1er novembre 2010).- Le président du tribunal choisit le juge de la famille parmi ses vice-présidents. 12 

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## csp_polygamy

- `q028` [fr, statut_personnel, concept] La polygamie est-elle autorisée ?
- `q045` [fr, statut_personnel, colloquial] Mon mari peut-il se remarier ?
- `q060` [ar, statut_personnel, concept] هل يجوز تعدد الزوجات؟
- `q074` [en, statut_personnel, concept] Is polygamy allowed?

**Current gold** (Statutpersonnel.pdf)

- **18** `H` Article 18 (Modifié par la loi n°58-70 du 4 juillet 1958 et les alinéas 3, 4 et 5 ajoutés par le décret-loi n°64-1 du 20 février 1964, ratifié par la loi n°64-1 du 21 avril 1964).- La polygamie est interdite. Quiconque, étant engagé dans les liens du mariage, en aura contracté un autre avant la diss
- **18** `F` article 18 ci-dessus, il sera statué par un seul et même jugement sur l'infraction et la nullité du mariage. Sont passibles d'un emprisonnement de six mois, les époux dont le mariage a été déclaré nul et qui continuent ou reprennent la vie commune. L'
- **18** `H` Article 18 .- Toute contravention aux articles précédents de la part des fonctionnaires y dénommés sera poursuivie devant le Tribunal de Première Instance de la circonscription et punie d'une amende qui ne pourra excéder dix mille francs.
- **18** `H` Article 18 .- La communauté des biens est dissoute par : - Le décès de l'un des deux époux - Le divorce - La disparition de l'un d'eux - La séparation judiciaire de leurs biens - L'accord des deux parties.
- **18** `H` Article 18 .- Les dispositions du présent décret s'appliquent aux tuteurs quels que soient la cause et le mode de leur désignation.

**Corpus candidates** (BM25 over Statutpersonnel.pdf headings; query terms: polygamie autorisée)

- gold **18** (3.9) Article 18 (Modifié par la loi n°58-70 du 4 juillet 1958 et les alinéas 3, 4 et 5 ajoutés par le décret-loi n°64-1 du 20 février 1964, ratifié par la loi n°64-1 du 21 avril 1964).- La polygamie est in

**Retrieved by official v1** (top-6, one block per language variant)

- `q028` [fr] hit=True
    -   Statutpers art 9: Article 9 .- Les ministres de la justice et des affaires sociales sont chargés, chacun en ce qui le concerne, de l’exécution du présent décret qui ser
    - ✓ Statutpers art 18: Article 18 (Modifié par la loi n°58-70 du 4 juillet 1958 et les alinéas 3, 4 et 5 ajoutés par le décret-loi n°64-1 du 20 février 1964, ratifié par la 
    -   Statutpers art 37: Article 37 .- Tout acte de mariage des Tunisiens, conclu à l'étranger selon les formes locales, devra être transcrit, dans les trois mois de sa rédact
    -   Statutpers art 15: Article 15 .- Est prohibé, le mariage de l'homme avec ses ascendantes et descendantes, avec ses sœurs et les descendantes à l'infini de ses frères et 
    -   Statutpers art 19: Article 19 .- Est prohibé, le mariage de l'homme avec la femme dont il avait été divorcé trois fois.
    -   Statutpers art 68: Article 68 .- La filiation est établie par la cohabitation, l’aveu du père ou le témoignage de deux ou plusieurs personnes honorables.
- `q045` [fr] hit=False
    -   Statutpers art 34: Article 34 .- La femme, divorcée après la consommation du mariage ou devenue veuve avant ou après la consommation du mariage, doit observer le délai d
    -   Statutpers art 33: Article 33 .- Si le divorce est prononcé avant la consommation du mariage, la femme a droit à la moitié de la dot fixée. LIVRE TROIS DU DELAI DE VIDUI
    -   Statutpers art 31: Article 31. (Modifié par la loi n°81-7 du 18 février 1981).- Le Tribunal prononce le divorce : 1) en cas de consentement mutuel des époux, 2) à la dem
    -   Statutpers art 35: Article 35 .- La femme divorcée non enceinte observera un délai de viduité de trois mois accomplis. Pour la veuve, il est de quatre mois et dix jours 
    -   Statutpers art 32: Article 32 (Modifié par la loi n°2010-50 du 1er novembre 2010).- Le président du tribunal choisit le juge de la famille parmi ses vice-présidents. 12 
    -   Statutpers art 13: Article 13.- Le mari ne peut, s'il n'a pas acquitté la dot, contraindre la femme à la consommation du mariage. Après la consommation du mariage, la fe
- `q060` [ar] hit=True
    - ✓ Statutpers art 18: Article 18 (Modifié par la loi n°58-70 du 4 juillet 1958 et les alinéas 3, 4 et 5 ajoutés par le décret-loi n°64-1 du 20 février 1964, ratifié par la 
    -   Statutpers art 15: Article 15 .- Est prohibé, le mariage de l'homme avec ses ascendantes et descendantes, avec ses sœurs et les descendantes à l'infini de ses frères et 
    -   Statutpers art 102: Article 102 .- Deux cas se présentent quand il y a une ou plusieurs épouses : 1°) le quart est attribué à une ou plusieurs épouses en cas d'absence de
    -   Statutpers art 19: Article 19 .- Est prohibé, le mariage de l'homme avec la femme dont il avait été divorcé trois fois.
    -   Statutpers art 16: Article 16 .- Est prohibé, le mariage de l'homme avec les ascendantes de sa femme dès la célébration du mariage, avec les descendantes de sa femme à c
    -   Statutpers art 68: Article 68 .- La filiation est établie par la cohabitation, l’aveu du père ou le témoignage de deux ou plusieurs personnes honorables.
- `q074` [en] hit=True
    - ✓ Statutpers art 18: Article 18 (Modifié par la loi n°58-70 du 4 juillet 1958 et les alinéas 3, 4 et 5 ajoutés par le décret-loi n°64-1 du 20 février 1964, ratifié par la 
    -   Statutpers art 153: Article 153 (Modifié par la loi n°93-74 du 12 juillet 1993).- Est considéré comme interdit pour minorité, celui ou celle qui n'a pas atteint la majori
    -   Statutpers art 5: Article 5 .- Les règles relatives aux empêchements au mariage prévues par les articles 14, 15, 16 et 17 du code du statut personnel, lorsque la patern
    -   Statutpers art 10: Article 10 .- Aucune condition spéciale n'est exigée du mandataire visé à l'article précédent. Toutefois, il ne peut, à son tour, donner mandat à un t
    -   Statutpers art 15: Article 15 .- Est prohibé, le mariage de l'homme avec ses ascendantes et descendantes, avec ses sœurs et les descendantes à l'infini de ses frères et 
    -   Statutpers art 16: Article 16 .- Est prohibé, le mariage de l'homme avec les ascendantes de sa femme dès la célébration du mariage, avec les descendantes de sa femme à c

**Suggested change:** No change; anchored to the CSP Art 18 (4 other chunks are numbered 18).

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **18** `Article 18 (Modifié par la loi n°58-70`
        > Article 18 (Modifié par la loi n°58-70 du 4 juillet 1958 et les alinéas 3, 4 et 5 ajoutés par le décret-loi n°64-1 du 20 février 1964, ratifié par la 

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## csp_child_custody

- `q029` [fr, statut_personnel, concept] Comment est attribuée la garde des enfants ?
- `q062` [ar, statut_personnel, concept] من يحق له حضانة الأطفال؟
- `q075` [en, statut_personnel, concept] Who gets custody of the children after divorce?

**Current gold** (Statutpersonnel.pdf)

- **54** `H` Article 54 .- La garde consiste à élever l'enfant et à assurer sa protection dans sa demeure.
- **54** `H` Article 54 .- Lorsqu'un Tunisien aura disparu en Tunisie ou hors de Tunisie, dans des circonstances de nature à mettre sa vie en danger, et que sa mort n'aura pu être constatée, un procès-verbal de disparition sera établi par : 1°) le Secrétaire d'Etat à la Défense Nationale à l'égard des militaires
- **55** `H` Article 55 .- La femme qui refuse d'assurer la garde de l'enfant n'y sera obligée que lorsque aucune autre personne ne pourra lui être substituée. 17
- **55** `H` Article 55 .- Les procès-verbaux, visés à l'article précédent, seront transmis, soit au Chef du parquet Général(*) près de la Cour d'Appel dans le ressort de laquelle a eu lieu la disparition, au cas où celle-ci a eu lieu en territoire tunisien, soit au Chef du Parquet Général (*) près de la Cour d'
- **56** `H` Article 56 (Paragraphes 2, 3, 4, 5, 6 et 7 ajoutés par la loi n°2008-20 du 4 mars 2008).- Les frais nécessaires à l'entretien de l'enfant sont prélevés sur ses biens ou sur ceux du père si l'enfant n'a pas de biens propres. Le père doit pourvoir au logement de l'enfant et de la titulaire de la garde
- **56** `H` Article 56 bis (Ajouté par la loi n°2008-20 du 4 mars 2008).- Est puni d’un emprisonnement de trois mois à un an et d’une amende de cent à mille dinars, quiconque cède sciemment, à titre onéreux ou 18 gratuit, un local d’habitation dont le père est astreint à consacrer à l’hébergement de la titulair
- **56** `H` Article 56 .- En transmettant le procès-verbal, le Secrétaire d'Etat compétent requerra le Chef du Parquet Général(*) de poursuivre d'office la déclaration judiciaire du décès. Les parties intéressées pourront, également, se pourvoir en déclaration de décès. La requête sera communiquée, pour avis, a
- **56** `F` article 56 , seront transcrits sur les registres de l'état civil du lieu de la disparition, ou, à défaut, du lieu du départ. Des extraits individuels seront transmis à l'Officier de l'état civil désigné à l'
- **57** `H` Article 57 (Modifié par la loi n°66-49 du 3 juin 1966).- La garde appartient durant le mariage aux père et mère.
- **57** `H` Article 57 .- Tout jugement déclaratif de décès sera transcrit à sa date sur les registres de l'état civil du dernier domicile, ou sur les registres de la municipalité de Tunis, si ce domicile est inconnu. __________ * Lire : Procureur de la République. 74 Il sera fait mention du jugement et de sa t

**Corpus candidates** (BM25 over Statutpersonnel.pdf headings; query terms: attribuée garde enfants)

-      **103** (5.6) Article 103 .- Trois cas se présentent pour les filles : 1°) la moitié est attribuée à la fille quand elle est fille unique, 2°) les deux tiers sont attribués aux filles quand elles sont plusieurs (so
-      **7** (4.9) Article 7. (Modifié par le décret n° 98-671 du 16 mars 1998)..- La caisse nationale de sécurité sociale cesse de payer les montants de la pension alimentaire ou de la rente de divorce lorsque le non l
-      **64** (4.8) Article 64. (Modifié par la loi n°66-49 du 3 juin 1966).- La personne à qui la garde est confiée peut y renoncer. Dans ce cas, le juge désigne un nouveau titulaire de la garde.
-      **105** (4.6) Article 105.- Les sœurs germaines présentent cinq cas : 1°) la moitié est attribuée quand il s'agit d'une sœur unique, 2°) les deux tiers sont attribués quand il s'agit de deux sœurs germaines ou plus
-      **8** (4.4) Article 8 .- Quiconque a indûment bénéficié des sommes d’argent du fonds de garantie de la pension alimentaire et de la rente de divorce doit les restituer sans délai. La caisse nationale de sécurité 
-      **58** (4.2) Article 58 (Modifié par la loi n°81-7 du 18 février 1981).- Le titulaire du droit de garde doit être majeur, sain d'esprit, honnête, capable de pourvoir aux besoins de l'enfant, indemne de toute malad
- gold **54** (4.2) Article 54 .- La garde consiste à élever l'enfant et à assurer sa protection dans sa demeure.
- gold **57** (4.1) Article 57 (Modifié par la loi n°66-49 du 3 juin 1966).- La garde appartient durant le mariage aux père et mère.

**Retrieved by official v1** (top-6, one block per language variant)

- `q029` [fr] hit=True
    -   Statutpers art 67: Article 67. (Modifié par la loi n°93-74 du 12 juillet 1993).- En cas de dissolution du mariage par décès, la garde est confiée au survivant des père e
    -   Statutpers art 61: Article 61 .- Si celui qui a la garde de l'enfant change de résidence et s'installe à une distance qui empêche le tuteur d'accomplir ses devoirs enver
    - ✓ Statutpers art 57: Article 57 (Modifié par la loi n°66-49 du 3 juin 1966).- La garde appartient durant le mariage aux père et mère.
    -   Statutpers art 58: Article 58 (Modifié par la loi n°81-7 du 18 février 1981).- Le titulaire du droit de garde doit être majeur, sain d'esprit, honnête, capable de pourvo
    -   Statutpers art 60: Article 60. (Modifié par la loi n°93-74 du 12 juillet 1993).- Le père, le tuteur et la mère de l'enfant peuvent avoir un droit de regard sur ses affai
    -   Statutpers art 59: Article 59 .- La titulaire du droit de garde d'une confession autre que celle du père de l'enfant ne pourra exercer ce droit qu'autant que 19 l'enfant
- `q062` [ar] hit=False
    -   Statutpers art 5: Article 5 .- Le tuteur officieux a, vis-à-vis du pupille, les droits et obligations prévus par les articles 54 et suivant du code du statut personnel.
    -   Statutpers art 60: Article 60. (Modifié par la loi n°93-74 du 12 juillet 1993).- Le père, le tuteur et la mère de l'enfant peuvent avoir un droit de regard sur ses affai
    -   Statutpers art 59: Article 59 .- La titulaire du droit de garde d'une confession autre que celle du père de l'enfant ne pourra exercer ce droit qu'autant que 19 l'enfant
    -   Statutpers art 58: Article 58 (Modifié par la loi n°81-7 du 18 février 1981).- Le titulaire du droit de garde doit être majeur, sain d'esprit, honnête, capable de pourvo
    -   Statutpers art 3: Article 3 .- La tutelle officieuse est l'acte par lequel une personne majeure jouissant de la pleine capacité civile, ou un organisme d'assistance, pr
    -   Statutpers art 62: Article 62 .- Le père ne pourra sortir l'enfant du lieu de résidence de la mère qu'avec le consentement de celle-ci tant qu'elle conserve le droit de 
- `q075` [en] hit=False
    -   Statutpers art 69: Article 69 .- La filiation n’est pas établie en cas de désaveu d’un enfant d’une femme mariée dont la non-cohabitation avec le mari a été prouvée, ou 
    -   Statutpers art 60: Article 60. (Modifié par la loi n°93-74 du 12 juillet 1993).- Le père, le tuteur et la mère de l'enfant peuvent avoir un droit de regard sur ses affai
    -   Statutpers art 63: Article 63 .- La femme à laquelle le droit de garde est transféré, pour une cause autre que l'incapacité physique de la gardienne précédente ne peut c
    -   Statutpers art 5: Article 5 .- Les règles relatives aux empêchements au mariage prévues par les articles 14, 15, 16 et 17 du code du statut personnel, lorsque la patern
    -   Statutpers art 59: Article 59 .- La titulaire du droit de garde d'une confession autre que celle du père de l'enfant ne pourra exercer ce droit qu'autant que 19 l'enfant
    -   Statutpers art 61: Article 61 .- Si celui qui a la garde de l'enfant change de résidence et s'installe à une distance qui empêche le tuteur d'accomplir ses devoirs enver

**Suggested change:** Anchor 54-57 to the CSP garde articles (54/55/56/57 each also exist as 'disparu / procès-verbal' civil-status articles). Add 58 (conditions to hold the garde) and 67 (garde when the marriage is dissolved by divorce).

- add: 58, 67   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **54** `Article 54 .- La garde consiste`
        > Article 54 .- La garde consiste à élever l'enfant et à assurer sa protection dans sa demeure.
    - **55** `Article 55 .- La femme qui refuse`
        > Article 55 .- La femme qui refuse d'assurer la garde de l'enfant n'y sera obligée que lorsque aucune autre personne ne pourra lui être substituée. 17
    - **56** `Article 56 (Paragraphes 2, 3, 4`
        > Article 56 (Paragraphes 2, 3, 4, 5, 6 et 7 ajoutés par la loi n°2008-20 du 4 mars 2008).- Les frais nécessaires à l'entretien de l'enfant sont prélevé
    - **57** `Article 57 (Modifié par la loi n°66-49`
        > Article 57 (Modifié par la loi n°66-49 du 3 juin 1966).- La garde appartient durant le mariage aux père et mère.
    - NEW **58** `Article 58 (Modifié par la loi n°81-7`
        > Article 58 (Modifié par la loi n°81-7 du 18 février 1981).- Le titulaire du droit de garde doit être majeur, sain d'esprit, honnête, capable de pourvo
    - NEW **67** `Article 67. (Modifié par la loi n°93-74`
        > Article 67. (Modifié par la loi n°93-74 du 12 juillet 1993).- En cas de dissolution du mariage par décès, la garde est confiée au survivant des père e

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## csp_alimony

- `q030` [fr, statut_personnel, concept] Quelles sont les règles de la pension alimentaire ?

**Current gold** (Statutpersonnel.pdf)

- **37** `H` Article 37 .- L'obligation alimentaire prend sa source dans le mariage, la parenté ou l'engagement volontaire. Obligation suite au mariage (*)
- **37** `H` Article 37 .- Tout acte de mariage des Tunisiens, conclu à l'étranger selon les formes locales, devra être transcrit, dans les trois mois de sa rédaction et à la diligence des époux, dans le registre des mariages du Consulat de Tunisie le plus proche. Toute infraction à cette obligation sera punie d
- **38** `H` Article 38 .- Le mari doit des aliments à la femme après la consommation du mariage et durant le délai de viduité en cas de divorce.
- **38** `H` Article 38 .- L'acte de mariage des Etrangers en Tunisie sera rédigé conformément aux lois tunisiennes, sur le vu d'un certificat de leur consul attestant qu'ils peuvent contracter mariage. Le mariage contracté en Tunisie entre deux Etrangers de même nationalité pourra être célébré par les agents di
- **46** `H` Article 46 (Modifié par la loi n°93-74 du 12 juillet 1993).- Les aliments continuent à être servis aux enfants jusqu'à ce qu'ils atteignent l'âge de la majorité ou, au-delà de cette majorité, jusqu'à la fin de leurs études, à condition qu'ils ne dépassent pas l'âge de 25 ans. La fille continue à avo
- **46** `H` Article 46 .- Lorsqu'un décès se sera produit ailleurs que dans la commune où le défunt était domicilié, l'officier de l'état civil qui aura dressé l'acte de décès, enverra, dans le plus bref délai possible, à l'officier de l'état civil du dernier domicile du défunt une expédition de cet acte, laque
- **46** `F` article 46 et au secrétaire d'Etat compétent. Il pourra en être délivré copie aux intéressés. Les jugements déclaratifs de décès tiendront lieu d'actes de l'état civil et seront opposables aux tiers qui pourront seulement en obtenir la rectification.
- **46** `F` article 46 de la présente loi. La rectification des actes de l'état civil dressés ou transcrits par les agents diplomatiques et les consuls est ordonnée par le président du tribunal de première instance de Tunis ou par son suppléant. La rectification des jugements déclaratifs de naissance ou de décè
- **47** `H` Article 47 .- En cas d'indigence du père, la mère est appelée avant le grand-père pour servir des aliments à ses enfants.
- **47** `H` Article 47 .- L'acte de décès énoncera : le jour, l'heure et le lieu du décès, les prénom, nom, date et lieu de naissance, profession, domicile et nationalité de la personne décédée; les prénoms, noms, professions, domiciles et nationalités de ses père et mère; les prénoms et noms de l'autre époux, 
- **47** `F` article 47 , d'après lesquels l'acte de décès sera rédigé.

**Corpus candidates** (BM25 over Statutpersonnel.pdf headings; query terms: règles pension alimentaire)

-      **6** (8.9) Article 6 .- Les montants de la pension alimentaire ou de la rente de divorce payés par le fonds de garantie de la pension alimentaire et de la rente de divorce sont majorés de 5% à titre de frais de 
-      **2** (8.1) Article 2 (Modifié par le décret n°2006-826 du 23 mars 2006).- Les demandes d’obtention de la pension alimentaire ou de la rente de divorce doivent être accompagnées des pièces suivantes : 142 - une c
-      **3** (7.9) Article 3 .- Le fonds de garantie de la pension alimentaire et de la rente de divorce est subrogé aux ayants-droit de la pension alimentaire ou de la rente de divorce dans leurs droits vis-à-vis de la
-      **6** (7.7) Article 6 .- Les bénéficiaires de la pension alimentaire ou de la rente de divorce du fonds de garantie de la pension alimentaire et de la rente de divorce sont tenus de présenter au bureau régional d
-      **8** (7.6) Article 8 .- Quiconque a indûment bénéficié des sommes d’argent du fonds de garantie de la pension alimentaire et de la rente de divorce doit les restituer sans délai. La caisse nationale de sécurité 
-      **10** (7.6) Article 10 .- La procédure d'intervention du fonds de garantie de la pension alimentaire et de la rente de divorce est fixée par décret. La présente loi sera publiée au Journal officiel de la Républiq
-      **7** (7.5) Article 7 .- Le fonds de garantie de la pension alimentaire et de la rente de divorce est financé par les ressources suivantes : - Une contribution du budget de l'Etat; - Les montants de la pension al
-      **9** (7.3) Article 9 .- Le fonds de garantie de la pension alimentaire et de la rente de divorce cesse de payer les montants de pension alimentaire ou de rente de divorce dans tous les cas où il n'y a plus de ra

**Retrieved by official v1** (top-6, one block per language variant)

- `q030` [fr] hit=False
    -   Statutpers art 53: article 53 bis du code du statut personnel, la caisse nationale de sécurité sociale continue systématiquement le versement des montants de la pension 
    -   Statutpers art 49: Article 49 .- Quiconque s'oblige à servir pour une période déterminée une pension alimentaire à une personne, quel que soit l'âge de celle-ci, est ten
    -   Statutpers art 51: Article 51 .- La pension alimentaire s'éteint avec l'extinction de sa cause. Le débiteur d'aliments aura droit à la restitution de ce qu'il aura payé 
    -   Statutpers art 50: Article 50 .- La pension alimentaire comprend la nourriture, l'habillement, le logement, l'instruction et tout ce qui est considéré comme nécessaire à
    -   Statutpers art 5: Article 5 .- Le montant de la pension alimentaire ou de la rente de divorce, due en vertu d'un jugement, qui n'a pas été payé par la partie débitrice 
    -   Statutpers art 10: Article 10 .- La procédure d'intervention du fonds de garantie de la pension alimentaire et de la rente de divorce est fixée par décret. La présente l

**Suggested change:** Anchor 37/38/46/47 to the CSP alimony articles (other chunks with these numbers concern marriage abroad and death certificates). Add 43 (who is entitled), 50 (what the pension comprises), 51 (extinction), 52 (proportionality).

- add: 43, 50, 51, 52   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **37** `Article 37 .- L'obligation alimentaire`
        > Article 37 .- L'obligation alimentaire prend sa source dans le mariage, la parenté ou l'engagement volontaire. Obligation suite au mariage (*)
    - **38** `Article 38 .- Le mari doit des aliments`
        > Article 38 .- Le mari doit des aliments à la femme après la consommation du mariage et durant le délai de viduité en cas de divorce.
    - NEW **43** `Article 43 (Modifié par la loi n°93-74`
        > Article 43 (Modifié par la loi n°93-74 du 12 juillet 1993).- Ont droit aux aliments : a) les père et mère, les grands-parents paternels à quelque degr
    - **46** `Article 46 (Modifié par la loi n°93-74`
        > Article 46 (Modifié par la loi n°93-74 du 12 juillet 1993).- Les aliments continuent à être servis aux enfants jusqu'à ce qu'ils atteignent l'âge de l
    - **47** `Article 47 .- En cas d'indigence`
        > Article 47 .- En cas d'indigence du père, la mère est appelée avant le grand-père pour servir des aliments à ses enfants.
    - NEW **50** `Article 50 .- La pension alimentaire comprend`
        > Article 50 .- La pension alimentaire comprend la nourriture, l'habillement, le logement, l'instruction et tout ce qui est considéré comme nécessaire à
    - NEW **51** `Article 51 .- La pension alimentaire s'éteint`
        > Article 51 .- La pension alimentaire s'éteint avec l'extinction de sa cause. Le débiteur d'aliments aura droit à la restitution de ce qu'il aura payé 
    - NEW **52** `Article 52.- Les aliments ne sont accordés`
        > Article 52.- Les aliments ne sont accordés que dans la proportion de la fortune de celui qui les doit et du besoin de celui qui les réclame, compte te

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## coc_contract_validity

- `q031` [fr, obligations_contrats, concept] Quelles sont les conditions de validité d'un contrat ?
- `q063` [ar, obligations_contrats, concept] ما هي شروط صحة العقد؟
- `q082` [en, obligations_contrats, concept] What makes a contract valid?

**Current gold** (COC.pdf)

- **2** `H` Article 2.- Ce code est divisé en deux livres : le premier, formé des articles de 1 à 717, concerne les obligations; le second, formé des articles de 718 à 1632, concerne les contrats et quasi-contrats.
- **2** `H` Article 2.- Il ne découle de la réorganisation du code des obligations et des contrats tunisien aucune modification de son contenu, ou abrogation ou modification des dispositions spéciales qui lui sont contraires. La présente loi sera publiée au Journal Officiel de la République Tunisienne et exécut
- **2** `H` Article 2.- Les éléments nécessaires pour la validité des obligations qui dérivent d'une déclaration de volonté sont : 1) la capacité de s'obliger ; 2) une déclaration valable de volonté portant sur les éléments essentiels de l'obligation ; 3) un objet certain pouvant former objet d'obligation ; 4) 
- **3** `H` Article 3.- Les dispositions du présent code seront mises en vigueur et appliquées par nos juridictions tunisiennes à dater du 1er juin 1907. Elles n’ont pas d’effet rétroactif. Vu pour promulgation et mise en exécution Tunis, le 15 décembre 1906 Le délégué à la Résidence Générale de la République F
- **3** `H` Article 3.- Toute personne est capable d'obliger et de s'obliger sauf si elle est déclarée incapable par la loi.

**Corpus candidates** (BM25 over COC.pdf headings; query terms: conditions validité contrat)

-      **328** (10.3) Article 328.- L’obligation qui est nulle comme telle, mais qui a les conditions de validité d’une autre obligation légitime, doit être régie par les règles établies pour cette obligation.
-      **737** (9.5) Article 737.- Les baux des biens habous sont, notamment quant aux conditions de validité et de forme, soumis à des règlements particuliers. Les dispositions de la présente loi non contraires à ces règ
-      **233** (6.1) Article 233.- Il n'est pas nécessaire pour la validité de la délégation que les deux dettes soient égales quant à la quotité, ni qu'elles aient une cause analogue. 49
-      **1000** (6.1) Article 1000.- Il n’est pas nécessaire, pour la validité du dépôt entre les parties, que le déposant soit propriétaire de la chose déposée ni qu’il la possède à titre légitime.
-      **1487** (6.1) Article 1487.- Il n'est pas obligatoire pour la validité du cautionnement que le créancier déclare l'avoir accepté; cependant, le cautionnement devient nul si le créancier le récuse.
-      **470** (6.0) Article 470 (Modifié par la loi n°2000-57 du 13 juin 2000).- Les copies faites sur les originaux des actes authentiques ou des écritures privées ont la même valeur que les originaux lorsqu’elles sont 
-      **1477** (5.8) Article 1477.- Lorsque, malgré les termes employés, la convention dénommée transaction constitue, en réalité, une donation, une vente ou autre rapport de droit, la validité et les effets du contrat do
-      **1420** (5.7) Article 1420.- Le colon peut céder son contrat, à moins qu'il n'ait été stipulé expressément qu'il doit l'exécuter personnellement. Il peut constituer un nantissement sur sa part indivise, dans les co

**Retrieved by official v1** (top-6, one block per language variant)

- `q031` [fr] hit=False
    -   COC.pdf art 119: Article 119.- La condition incompatible avec la nature de l'acte auquel elle est ajoutée est nulle et rend nulle l'obligation qui en dépend. Cette obl
    -   COC.pdf art 24: Article 24.- Le contrat n'est point parfait lorsque les parties ont expressément réservé certaines clauses comme devant former objet d'un accord ultér
    -   COC.pdf art 29: Article 29.- Lorsqu'une réponse d'acceptation n'est pas exigée par le proposant ou par l'usage du commerce, le contrat est parfait dès que l'autre par
    -   COC.pdf art 1477: Article 1477.- Lorsque, malgré les termes employés, la convention dénommée transaction constitue, en réalité, une donation, une vente ou autre rapport
    -   COC.pdf art 1531: Article 1531.- La caution qui a été condamnée à payer, faute de présenter le débiteur, a le droit de faire révoquer la condamnation, si elle prouve qu
    -   COC.pdf art 133: Article 133.- La condition accomplie a un effet rétroactif au jour auquel l'obligation a été contractée, lorsqu'il résulte de la volonté des parties o
- `q063` [ar] hit=True
    -   COC.pdf art 1531: Article 1531.- La caution qui a été condamnée à payer, faute de présenter le débiteur, a le droit de faire révoquer la condamnation, si elle prouve qu
    - ✓ COC.pdf art 2: Article 2.- Il ne découle de la réorganisation du code des obligations et des contrats tunisien aucune modification de son contenu, ou abrogation ou m
    -   COC.pdf art 119: Article 119.- La condition incompatible avec la nature de l'acte auquel elle est ajoutée est nulle et rend nulle l'obligation qui en dépend. Cette obl
    - ✓ COC.pdf art 3: Article 3.- Les dispositions du présent code seront mises en vigueur et appliquées par nos juridictions tunisiennes à dater du 1er juin 1907. Elles n’
    -   COC.pdf art 830: Article 830.- Le louage d'ouvrages et celui de services ne sont valables que si les parties contractantes ont la capacité de s'obliger ; l'interdit et
    -   COC.pdf art 24: Article 24.- Le contrat n'est point parfait lorsque les parties ont expressément réservé certaines clauses comme devant former objet d'un accord ultér
- `q082` [en] hit=True
    -   COC.pdf art 1531: Article 1531.- La caution qui a été condamnée à payer, faute de présenter le débiteur, a le droit de faire révoquer la condamnation, si elle prouve qu
    -   COC.pdf art 119: Article 119.- La condition incompatible avec la nature de l'acte auquel elle est ajoutée est nulle et rend nulle l'obligation qui en dépend. Cette obl
    - ✓ COC.pdf art 2: Article 2.- Il ne découle de la réorganisation du code des obligations et des contrats tunisien aucune modification de son contenu, ou abrogation ou m
    - ✓ COC.pdf art 3: Article 3.- Les dispositions du présent code seront mises en vigueur et appliquées par nos juridictions tunisiennes à dater du 1er juin 1907. Elles n’
    -   COC.pdf art 24: Article 24.- Le contrat n'est point parfait lorsque les parties ont expressément réservé certaines clauses comme devant former objet d'un accord ultér
    -   COC.pdf art 133: Article 133.- La condition accomplie a un effet rétroactif au jour auquel l'obligation a été contractée, lorsqu'il résulte de la volonté des parties o

**Suggested change:** Anchor: COC.pdf has three chunks numbered 2 and two numbered 3; the right ones are Art 2 'Les éléments nécessaires pour la validité des obligations ...' and Art 3 'Toute personne est capable'. Not added (lexical search did not surface them): the articles on consent, object and cause, so the label may be incomplete.

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **2** `Article 2.- Les éléments nécessaires pour la validité`
        > Article 2.- Les éléments nécessaires pour la validité des obligations qui dérivent d'une déclaration de volonté sont : 1) la capacité de s'obliger ; 2
    - **3** `Article 3.- Toute personne est capable`
        > Article 3.- Toute personne est capable d'obliger et de s'obliger sauf si elle est déclarée incapable par la loi.

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## coc_civil_liability

- `q032` [fr, obligations_contrats, concept] Qu'est-ce que la responsabilité civile ?

**Current gold** (COC.pdf)

- **82** `H` Article 82.- Tout fait quelconque de l'homme qui, sans l’autorité de la loi, cause sciemment et volontairement à autrui un dommage matériel ou moral, oblige son auteur à réparer le dommage résultant de son fait, lorsqu'il est établi que ce fait en est la cause directe. Toute stipulation contraire es
- **83** `H` Article 83.- Chacun est responsable du dommage moral ou matériel qu'il a causé, non seulement par son fait, mais par sa faute, lorsqu’il est établi que cette faute en est la cause directe. Toute stipulation contraire est sans effet. 20 La faute consiste, soit à omettre ce qu'on était tenu de faire, 
- **84** `H` Article 84.- La responsabilité établie aux deux articles ci-dessus s'applique également à l'Etat, même lorsqu'il agit comme puissance publique, aux communes et aux administrations publiques, pour les faits ou les fautes imputables à leurs représentants, agents et fonctionnaires dans l'exercice de le

**Corpus candidates** (BM25 over COC.pdf headings; query terms: responsabilité civile)

-      **102** (14.1) Article 102.- L'état d'ivresse, lorsqu'elle est volontaire, n'empêche point la responsabilité civile dans les obligations dérivant des délits et quasi-délits. Il n'y a point de responsabilité civile l
-      **103** (12.1) Article 103.- Il n'y a pas lieu à responsabilité civile lorsqu'une personne, sans intention de nuire, a fait ce qu'elle avait le droit de faire. Cependant, lorsque l'exercice de ce droit est de nature
-      **173** (8.5) Article 173.- Le créancier solidaire qui, après avoir reçu sa part, ne peut la représenter pour une cause imputable à sa faute, est tenu envers les autres créanciers jusqu'à concurrence de leur part e
-      **104** (7.7) Article 104.- Il n'y a pas lieu à responsabilité civile dans le cas de légitime défense, ou lorsque le dommage a été produit par une cause purement fortuite ou de force majeure qui n'a été ni précédée
- gold **84** (5.6) Article 84.- La responsabilité établie aux deux articles ci-dessus s'applique également à l'Etat, même lorsqu'il agit comme puissance publique, aux communes et aux administrations publiques, pour les 
-      **858** (5.4) Article 858.- Sont sans effet, toutes clauses et conventions ayant pour objet de restreindre ou d'écarter la responsabilité établie par les articles 856 et 857 à la charge des maîtres ou employeurs.
-      **1100** (5.0) Article 1100 (Modifié par la loi n°83-14 du 15 février 1983).- Lorsque les parties n’ont pas déterminé le taux des intérêts, le taux de l’intérêt légal qui s’applique est le suivant : 1) en matière ci
-      **711** (4.5) Article 711.- L'acheteur qui ne peut restituer la chose ou la restitue détériorée, pour une cause non imputable à son fait ou à sa faute, n'est tenu d'aucune responsabilité. 131 Section III De la vent

**Retrieved by official v1** (top-6, one block per language variant)

- `q032` [fr] hit=False
    -   COC.pdf art 103: Article 103.- Il n'y a pas lieu à responsabilité civile lorsqu'une personne, sans intention de nuire, a fait ce qu'elle avait le droit de faire. Cepen
    -   COC.pdf art 104: Article 104.- Il n'y a pas lieu à responsabilité civile dans le cas de légitime défense, ou lorsque le dommage a été produit par une cause purement fo
    -   COC.pdf art 102: Article 102.- L'état d'ivresse, lorsqu'elle est volontaire, n'empêche point la responsabilité civile dans les obligations dérivant des délits et quasi
    -   COC.pdf art 173: Article 173.- Le créancier solidaire qui, après avoir reçu sa part, ne peut la représenter pour une cause imputable à sa faute, est tenu envers les au
    -   COC.pdf art 107: Article 107.- Les dommages, dans le cas de délits et de quasi- délits, sont la perte effective éprouvée par le demandeur, les dépenses nécessaires qu'
    -   COC.pdf art 1531: Article 1531.- La caution qui a été condamnée à payer, faute de présenter le débiteur, a le droit de faire révoquer la condamnation, si elle prouve qu

**Suggested change:** No change; anchored.

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **82** `Article 82`
        > Article 82.- Tout fait quelconque de l'homme qui, sans l’autorité de la loi, cause sciemment et volontairement à autrui un dommage matériel ou moral, 
    - **83** `Article 83`
        > Article 83.- Chacun est responsable du dommage moral ou matériel qu'il a causé, non seulement par son fait, mais par sa faute, lorsqu’il est établi qu
    - **84** `Article 84`
        > Article 84.- La responsabilité établie aux deux articles ci-dessus s'applique également à l'Etat, même lorsqu'il agit comme puissance publique, aux co

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## coc_force_majeure

- `q033` [fr, obligations_contrats, concept] Qu'est-ce que la force majeure ?
- `q064` [ar, obligations_contrats, concept] ما هي القوة القاهرة؟
- `q083` [en, obligations_contrats, concept] What is force majeure?

**Current gold** (COC.pdf)

- **283** `H` Article 283.- La force majeure est tout fait que l'homme ne peut prévenir, tel que les phénomènes naturels (inondations, sécheresses, 58 orages, incendies, sauterelles), l'invasion ennemie, le fait du prince, et qui rend impossible l'exécution de l'obligation. N'est point considérée comme force maje

**Corpus candidates** (BM25 over COC.pdf headings; query terms: force majeure)

-      **280** (10.2) Article 280.- Le débiteur en demeure répond du cas fortuit et de la force majeure.
-      **1050** (9.6) Article 1050.- Il répond de la force majeure et du cas fortuit, s'il est en demeure de restituer la chose, si, étant partie au procès, il a accepté d'être constitué gardien provisoire, ou si la force 
-      **1022** (9.3) Article 1022.- Le dépositaire ne répond pas : 1) de la perte ou de la détérioration causées par la nature ou le vice des choses déposées ou par la négligence du déposant ; 176 2) des cas de force maje
-      **1207** (9.3) Article 1207.- Le gérant ne peut être chargé des cas fortuits ou de force majeure. Toute stipulation contraire est non avenue.
- gold **283** (9.2) Article 283.- La force majeure est tout fait que l'homme ne peut prévenir, tel que les phénomènes naturels (inondations, sécheresses, 58 orages, incendies, sauterelles), l'invasion ennemie, le fait du
-      **1024** (8.5) Article 1024.- Le dépositaire auquel la chose a été enlevée par une force majeure, et qui a reçu une somme ou quelque chose à la place, doit restituer ce qu’il a reçu.
-      **744** (8.4) Article 744.- Aucune des réparations réputées locatives n’est à la charge du preneur quand elles sont occasionnées par vétusté ou force majeure, par le vice de construction ou par le fait du bailleur.
-      **847** (8.2) Article 847.- Ils ne répondent pas de la détérioration et de la perte provenant d'un cas fortuit ou de force majeure, qui n'a pas été occasionné par leur fait on par leur faute et sauf le cas où ils s

**Retrieved by official v1** (top-6, one block per language variant)

- `q033` [fr] hit=True
    - ✓ COC.pdf art 283: Article 283.- La force majeure est tout fait que l'homme ne peut prévenir, tel que les phénomènes naturels (inondations, sécheresses, 58 orages, incen
    -   COC.pdf art 280: Article 280.- Le débiteur en demeure répond du cas fortuit et de la force majeure.
    -   COC.pdf art 1208: Article 1208.- Le gérant est tenu même des cas fortuits ou de force majeure, s’ils ont été occasionnés par son fait ou sa faute, ou par l’inexécution 
    -   COC.pdf art 847: Article 847.- Ils ne répondent pas de la détérioration et de la perte provenant d'un cas fortuit ou de force majeure, qui n'a pas été occasionné par l
    -   COC.pdf art 1050: Article 1050.- Il répond de la force majeure et du cas fortuit, s'il est en demeure de restituer la chose, si, étant partie au procès, il a accepté d'
    -   COC.pdf art 1207: Article 1207.- Le gérant ne peut être chargé des cas fortuits ou de force majeure. Toute stipulation contraire est non avenue.
- `q064` [ar] hit=True
    - ✓ COC.pdf art 283: Article 283.- La force majeure est tout fait que l'homme ne peut prévenir, tel que les phénomènes naturels (inondations, sécheresses, 58 orages, incen
    -   COC.pdf art 1208: Article 1208.- Le gérant est tenu même des cas fortuits ou de force majeure, s’ils ont été occasionnés par son fait ou sa faute, ou par l’inexécution 
    -   COC.pdf art 280: Article 280.- Le débiteur en demeure répond du cas fortuit et de la force majeure.
    -   COC.pdf art 847: Article 847.- Ils ne répondent pas de la détérioration et de la perte provenant d'un cas fortuit ou de force majeure, qui n'a pas été occasionné par l
    -   COC.pdf art 1050: Article 1050.- Il répond de la force majeure et du cas fortuit, s'il est en demeure de restituer la chose, si, étant partie au procès, il a accepté d'
    -   COC.pdf art 7: Article 7 (Modifié par le décret du 3 août 1956).- Est majeur, aux effets de la présente loi, tout individu de sexe masculin ou féminin âgé de « dix-h
- `q083` [en] hit=True
    - ✓ COC.pdf art 283: Article 283.- La force majeure est tout fait que l'homme ne peut prévenir, tel que les phénomènes naturels (inondations, sécheresses, 58 orages, incen
    -   COC.pdf art 280: Article 280.- Le débiteur en demeure répond du cas fortuit et de la force majeure.
    -   COC.pdf art 1208: Article 1208.- Le gérant est tenu même des cas fortuits ou de force majeure, s’ils ont été occasionnés par son fait ou sa faute, ou par l’inexécution 
    -   COC.pdf art 1024: Article 1024.- Le dépositaire auquel la chose a été enlevée par une force majeure, et qui a reçu une somme ou quelque chose à la place, doit restituer
    -   COC.pdf art 847: Article 847.- Ils ne répondent pas de la détérioration et de la perte provenant d'un cas fortuit ou de force majeure, qui n'a pas été occasionné par l
    -   COC.pdf art 1050: Article 1050.- Il répond de la force majeure et du cas fortuit, s'il est en demeure de restituer la chose, si, étant partie au procès, il a accepté d'

**Suggested change:** Add 280 ('Le débiteur en demeure répond du cas fortuit et de la force majeure').

- add: 280   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - NEW **280** `Article 280`
        > Article 280.- Le débiteur en demeure répond du cas fortuit et de la force majeure.
    - **283** `Article 283`
        > Article 283.- La force majeure est tout fait que l'homme ne peut prévenir, tel que les phénomènes naturels (inondations, sécheresses, 58 orages, incen

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## coc_binding_force

- `q034` [fr, obligations_contrats, concept] Quelle est la force obligatoire du contrat ?

**Current gold** (COC.pdf)

- **242** `H` Article 242.- Les obligations contractuelles valablement formées tiennent lieu de loi à ceux qui les ont faites, et ne peuvent être révoquées que de leur consentement mutuel ou dans les cas prévus par la loi.

**Corpus candidates** (BM25 over COC.pdf headings; query terms: force obligatoire contrat)

-      **1487** (8.2) Article 1487.- Il n'est pas obligatoire pour la validité du cautionnement que le créancier déclare l'avoir accepté; cependant, le cautionnement devient nul si le créancier le récuse.
-      **864** (5.6) Article 864.- Le maître a le droit de résoudre le contrat pour cause de maladie ou autre accident de force majeure survenus à son serviteur ou employé, en payant ce qui est dû à ce dernier proportionn
-      **623** (5.2) Article 623.- Les choses qui se vendent au poids et au nombre et ne présentent pas de variations sensibles dans leur prix, celles qu’on peut diviser sans préjudice, peuvent être vendues pour un prix u
-      **280** (5.0) Article 280.- Le débiteur en demeure répond du cas fortuit et de la force majeure.
-      **1422** (4.9) Article 1422.- Si les plantations périssent, en totalité, par cas fortuit ou force majeure, après avoir atteint l'âge convenu, le colon aura droit de partager le sol dans les proportions établies au c
-      **1050** (4.7) Article 1050.- Il répond de la force majeure et du cas fortuit, s'il est en demeure de restituer la chose, si, étant partie au procès, il a accepté d'être constitué gardien provisoire, ou si la force 
-      **1022** (4.6) Article 1022.- Le dépositaire ne répond pas : 1) de la perte ou de la détérioration causées par la nature ou le vice des choses déposées ou par la négligence du déposant ; 176 2) des cas de force maje
-      **394** (4.5) Article 394.- La prescription n’a pas lieu à l’égard des droits résultant d’un jugement passé en force de chose jugée.

**Retrieved by official v1** (top-6, one block per language variant)

- `q034` [fr] hit=True
    -   COC.pdf art 121: Article 121.- L'obligation est nulle lorsque l'existence même du lien dépend de la nue volonté de l'obligé (condition potestative). Néanmoins, chacune
    -   COC.pdf art 22: Article 22.- Dans les obligations unilatérales, les engagements sont obligatoires dès qu'ils sont parvenus à la connaissance de la partie envers laque
    -   COC.pdf art 177: Article 177.- L'obligation peut être solidaire, encore que l'un des débiteurs soit obligé d'une manière différente des autres, par exemple, si l'un n'
    - ✓ COC.pdf art 242: Article 242.- Les obligations contractuelles valablement formées tiennent lieu de loi à ceux qui les ont faites, et ne peuvent être révoquées que de l
    -   COC.pdf art 998: Article 998.- Pour faire un dépôt et pour l’accepter, il faut avoir la capacité de s’obliger. Néanmoins, si une personne capable de s’obliger accepte 
    -   COC.pdf art 830: Article 830.- Le louage d'ouvrages et celui de services ne sont valables que si les parties contractantes ont la capacité de s'obliger ; l'interdit et

**Suggested change:** No change; anchored.

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **242** `Article 242`
        > Article 242.- Les obligations contractuelles valablement formées tiennent lieu de loi à ceux qui les ont faites, et ne peuvent être révoquées que de l

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## coc_seller_duties

- `q035` [fr, obligations_contrats, concept] Quelles sont les obligations du vendeur ?

**Current gold** (COC.pdf)

- **564** `H` Article 564.- La vente est un contrat par lequel l’une des parties transmet la propriété d’une chose ou d’un droit à l’autre contractant, contre un prix que ce dernier s’oblige à lui payer.
- **611** `H` Article 611.- La vente d’un héritage comprend celle des constructions et des plantations qui s’y trouvent, celle des récoltes qui n’ont pas encore levé, des fruits non noués. Elle ne comprend pas les fruits noués, les récoltes pendantes, les plantes en pots et les pépinières, les arbres secs qui ne 
- **612** `H` Article 612.- La vente d’un édifice comprend celle du sol qui le soutient, et des accessoires fixes et immobilisés, tels que les portes, fenêtres, clefs faisant partie des serrures, moulins, escaliers ou armoires fixes, tuyaux servant à la conduite des eaux, poutres et fourneaux fixés au mur. Elle n

**Corpus candidates** (BM25 over COC.pdf headings; query terms: obligations vendeur)

-      **590** (7.4) Article 590.- En cas de vente de fruits sur l’arbre, des produits d’un potager ou d’une récolte pendante, les fruits ou les légumes sont aux risques du vendeur jusqu’au moment de leur complète maturat
-      **591** (7.3) Article 591.- Le vendeur a deux obligations principales : 1) celle de délivrer la chose vendue ; 2) celle de la garantir. Parag. I. - De la délivrance
-      **800** (5.9) Article 800.- Si le nouvel acquéreur n'exécute pas les obligations imposées par le bail au bailleur, le preneur aura action contre lui et contre son vendeur, solidairement entre eux, pour toutes indem
-      **601** (4.6) Article 601.- Le vendeur n’est pas tenu de délivrer la chose vendue, quand même il aurait accordé un délai pour le paiement : 1) si, depuis la vente, l’acheteur est tombé en déconfiture ; 2) s’il étai
-      **642** (4.5) Article 642.- Les parties peuvent convenir que le vendeur ne sera soumis à aucune garantie. Cette clause n'a cependant pour effet que d’affranchir le vendeur des dommages-intérêts, mais ne peut le lib
-      **576** (4.4) Article 576.- La vente de la chose d’autrui est valable : 1) si le maître la ratifie ; 2) si le vendeur acquiert ensuite la propriété de la chose ; Dans le cas où le maître refuse de ratifier, l’acqué
-      **588** (4.3) Article 588.- La chose vendue voyage aux risques du vendeur jusqu’à sa réception par l’acheteur. 111
-      **651** (4.3) Article 651.- En cas de doute, le dire du vendeur fait foi à charge de serment.

**Retrieved by official v1** (top-6, one block per language variant)

- `q035` [fr] hit=False
    -   COC.pdf art 631: Article 631.- L’obligation de garantir emporte pour le vendeur celle de s’abstenir de tout acte ou réclamation qui tendrait à inquiéter l’acheteur ou 
    -   COC.pdf art 591: Article 591.- Le vendeur a deux obligations principales : 1) celle de délivrer la chose vendue ; 2) celle de la garantir. Parag. I. - De la délivrance
    -   COC.pdf art 675: Article 675.- L'acheteur a deux obligations principales : 1) celle de payer le prix; 2) et celle de prendre livraison de la chose.
    -   COC.pdf art 3: Article 3.- Les dispositions du présent code seront mises en vigueur et appliquées par nos juridictions tunisiennes à dater du 1er juin 1907. Elles n’
    -   COC.pdf art 242: Article 242.- Les obligations contractuelles valablement formées tiennent lieu de loi à ceux qui les ont faites, et ne peuvent être révoquées que de l
    -   COC.pdf art 630: Article 630.- La garantie que le vendeur doit à l’acquéreur à deux objets : a) le premier est la jouissance et la possession paisible de la chose vend

**Suggested change:** Replace: 564 is the definition of sale, 611/612 say what the sale of land/building includes. Art 591: 'Le vendeur a deux obligations principales : 1) délivrer la chose 2) la garantir' is the duties article. Its sub-articles (délivrance, garantie) were not reviewed, so recall is likely understated.

- add: 591   |   remove: 564, 611, 612
- proposed gold (anchor = the text the intended chunk must start with):
    - NEW **591** `Article 591`
        > Article 591.- Le vendeur a deux obligations principales : 1) celle de délivrer la chose vendue ; 2) celle de la garantir. Parag. I. - De la délivrance

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## coc_lease

- `q036` [fr, obligations_contrats, concept] Quelles sont les règles du contrat de louage ?

**Current gold** (COC.pdf)

- **728** `H` Article 728.- Le louage de choses est parfait par le consentement des parties sur la chose, sur le prix et sur les autres clauses dont elles pourraient convenir dans le contrat.

**Corpus candidates** (BM25 over COC.pdf headings; query terms: règles contrat louage)

-      **738** (7.4) Article 738.- La location des mines, minières, carrières et gisements, enfouis dans le sol ou affleurant à la surface, est soumise également aux règlements spéciaux et aux règles de la vente. Section 
-      **724** (7.2) Article 724.- Les règles de la vente s'appliquent à l'échange dans la mesure où le permet la nature de ce contrat. 132
-      **993** (7.1) Article 993.- La naçba est régie par les dispositions relatives au louage de choses dans la mesure où elles sont applicables à ce contrat.
- gold **728** (6.5) Article 728.- Le louage de choses est parfait par le consentement des parties sur la chose, sur le prix et sur les autres clauses dont elles pourraient convenir dans le contrat.
-      **757** (6.4) Article 757.- Les actions du preneur contre le bailleur à raison des articles 748 à 756 inclus se prescrivent par l’expiration du contrat de louage. b) – De la garantie des défauts de la chose louée
-      **777** (6.1) Article 777.- La cession est régie par les dispositions établies au chapitre de la cession des créances (articles 199 et suivants) et emporte la substitution du cessionnaire dans les droits et dans le
-      **766** (6.0) Article 766.- Les actions du preneur contre le bailleur, à raison des articles 758, 764 et 765 ne peuvent plus être utilement intentées à partir du moment où le contrat de louage a pris fin. 139 Parag
-      **828** (6.0) Article 828.- Le louage de services ou de travail est un contrat par lequel l'une des parties s'engage, moyennant un prix que l'autre partie s'oblige à lui payer, à fournir à cette dernière ses servic

**Retrieved by official v1** (top-6, one block per language variant)

- `q036` [fr] hit=False
    -   COC.pdf art 830: Article 830.- Le louage d'ouvrages et celui de services ne sont valables que si les parties contractantes ont la capacité de s'obliger ; l'interdit et
    -   COC.pdf art 726: Article 726.- Il y a deux sortes de contrats de louage : celui des choses (kirâ) ; celui des personnes ou d’ouvrage (idjâra). Chapitre premier Du loua
    -   COC.pdf art 242: Article 242.- Les obligations contractuelles valablement formées tiennent lieu de loi à ceux qui les ont faites, et ne peuvent être révoquées que de l
    -   COC.pdf art 767: Article 767.- Le preneur est tenu de deux obligations principales : a) de payer le prix de louage ; b) de conserver la chose louée et d’en user sans e
    -   COC.pdf art 1531: Article 1531.- La caution qui a été condamnée à payer, faute de présenter le débiteur, a le droit de faire révoquer la condamnation, si elle prouve qu
    -   COC.pdf art 867: Article 867.- L'entreprise de construction et tous autres contrats dans lesquels l'ouvrier ou artisan fournit la matière sont considérés comme louage 

**Suggested change:** No change; anchored.

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **728** `Article 728`
        > Article 728.- Le louage de choses est parfait par le consentement des parties sur la chose, sur le prix et sur les autres clauses dont elles pourraien

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## nat_acquisition

- `q037` [fr, nationalite, concept] Comment acquérir la nationalité tunisienne ?
- `q065` [ar, nationalite, concept] كيف تكتسب الجنسية التونسية؟
- `q084` [en, nationalite, concept] How can someone acquire Tunisian nationality?

**Current gold** (NationaliteFr.pdf)

- **6** `H` Article 6 (Modifié par la loi n° 2010-55 du 1er décembre 2010)(*). - Est tunisien l’enfant né d’un père tunisien ou d’une mère tunisienne. Section II - Attribution en raison de la natalité en Tunisie
- **7** `H` Article 7.- Est Tunisien, l’enfant né en Tunisie et dont le père et le grand-père y sont eux-mêmes nés. L’intéressé peut, sauf s’il est né après l’entrée en vigueur du présent Code, répudier la nationalité tunisienne dans l’année précédant sa majorité; il est libéré de son allégeance à l’égard de la
- **8** `H` Article 8.- Est tunisien, l’enfant né en Tunisie de parents apatrides résidant en Tunisie depuis cinq ans au moins.
- **9** `H` Article 9.- Est Tunisien, l’enfant né en Tunisie de parents inconnus. Toutefois, il sera réputé n’avoir jamais été Tunisien si, au cours de la minorité, sa filiation est établie à l’égard d’un étranger et s’il a, conformément à la loi nationale de cet étranger, la nationalité de celui-ci.

**Corpus candidates** (BM25 over NationaliteFr.pdf headings; query terms: acquérir nationalité tunisienne)

-      **17** (6.2) Article 17.- Lorsque la validité des actes, passés antérieurement à la décision constatant la nullité du mariage ou au décret d’opposition, était subordonnée à l’acquisition par l’intéressé de la nati
-      **29** (2.9) Article 29.- Le mariage ne produit effet, quant à la nationalité, que s’il est célébré en l’une des formes admises, soit par la loi tunisienne, soit par la loi du pays où il a été célébré. Chapitre II
-      **65** (2.7) Article 65 (Modifié par la loi n° 71-12 du 9 mars 1971). -Lorsque le ministre de la justice, les agents diplomatiques et consulaires représentant la Tunisie à l’étranger ou les juges cantonaux refusen
-      **30** (2.6) Article 30 (Modifié par la loi n° 75-79 du 14 novembre 1975). - La perte de la nationalité tunisienne ne peut être prononcée que par décret. (*) Lire : Ministre ou Ministère selon le cas. 13 En cas d’
-      **59** (2.5) Article 59.- La charge de la preuve, en matière de nationalité, incombe à celui qui, par voie d’action ou par voie d’exception, prétend avoir ou non la nationalité tunisienne. Toutefois, cette charge 
-      **14** (2.4) Article 14.- La femme étrangère, qui épouse un tunisien et qui, en vertu de sa loi nationale, conserve sa nationalité d’origine par le mariage avec un étranger, peut réclamer la nationalité tunisienne
-      **62** (2.4) Article 62.- La preuve d’un décret de naturalisation ou d’un décret portant perte, déchéance, retrait de la nationalité tunisienne ou opposition du Président de la République ) 1 ( à l’acquisition de 
-      **13** (2.4) Article 13.- La femme étrangère qui épouse un tunisien acquiert la nationalité tunisienne au moment de la célébration du mariage, lorsque, en vertu de sa loi nationale, elle perd sa nationalité d’orig

**Retrieved by official v1** (top-6, one block per language variant)

- `q037` [fr] hit=False
    -   Nationalit art 65: Article 65 (Modifié par la loi n° 71-12 du 9 mars 1971). -Lorsque le ministre de la justice, les agents diplomatiques et consulaires représentant la T
    -   Nationalit art 4: Article 4.- Les secrétaires d’État à la Présidence, aux affaires étrangères, à la justice, à l’intérieur et au plan et aux finances(*) sont (1) Ratifi
    -   Nationalit art 21: Article 21.- Peut être naturalisé sans la condition de résidence fixée à l’article précédent: 1) l’individu qui justifie que sa nationalité d’origine 
    -   Nationalit art 24: Article 24.- L’individu qui a acquis la nationalité tunisienne jouit, à compter du jour de cette acquisition, de tous les droits attachés à la qualité
    -   Nationalit art 41: article 41 du présent Code, deux ans au plus à partir du jour où la décision judiciaire qui en a admis la validité est passée en force de chose jugée.
    -   Nationalit art 39: article 39 du code de la nationalité tunisienne. L’intéressé acquiert la nationalité tunisienne à la date à laquelle la déclaration est enregistrée, s
- `q065` [ar] hit=False
    -   Nationalit art 2: Article 2.- Les conditions de l’acquisition et de la perte de la nationalité tunisienne, après la naissance, sont régies par la loi en vigueur au mome
    -   Nationalit art 18: Article 18.- L’étranger mineur, adopté par une personne de nationalité tunisienne, acquiert cette nationalité à la date du jugement d’adoption, à cond
    -   Nationalit art 24: Article 24.- L’individu qui a acquis la nationalité tunisienne jouit, à compter du jour de cette acquisition, de tous les droits attachés à la qualité
    -   Nationalit art 39: article 39 du code de la nationalité tunisienne. L’intéressé acquiert la nationalité tunisienne à la date à laquelle la déclaration est enregistrée, s
    -   Nationalit art 13: Article 13.- La femme étrangère qui épouse un tunisien acquiert la nationalité tunisienne au moment de la célébration du mariage, lorsque, en vertu de
    -   Nationalit art 23: Article 23.- Nul ne peut être naturalisé: 1) s’il n’est majeur; 2) s’il ne justifie d’une connaissance suffisante, selon sa condition, de la langue ar
- `q084` [en] hit=False
    -   Nationalit art 39: article 39 du code de la nationalité tunisienne. L’intéressé acquiert la nationalité tunisienne à la date à laquelle la déclaration est enregistrée, s
    -   Nationalit art 65: Article 65 (Modifié par la loi n° 71-12 du 9 mars 1971). -Lorsque le ministre de la justice, les agents diplomatiques et consulaires représentant la T
    -   Nationalit art 41: article 41 du présent Code, deux ans au plus à partir du jour où la décision judiciaire qui en a admis la validité est passée en force de chose jugée.
    -   Nationalit art 18: Article 18.- L’étranger mineur, adopté par une personne de nationalité tunisienne, acquiert cette nationalité à la date du jugement d’adoption, à cond
    -   Nationalit art 24: Article 24.- L’individu qui a acquis la nationalité tunisienne jouit, à compter du jour de cette acquisition, de tous les droits attachés à la qualité
    -   Nationalit art 11: Article 11.- L’enfant qui est tunisien en vertu des dispositions du présent chapitre est réputé avoir été tunisien dès sa naissance même si l’existenc

**Suggested change:** No change; anchored. The question says 'acquérir': the corpus also has acquisition by marriage (13-14) and naturalisation, which lexical search did not surface, so the label may be incomplete.

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **6** `Article 6`
        > Article 6 (Modifié par la loi n° 2010-55 du 1er décembre 2010)(*). - Est tunisien l’enfant né d’un père tunisien ou d’une mère tunisienne. Section II 
    - **7** `Article 7`
        > Article 7.- Est Tunisien, l’enfant né en Tunisie et dont le père et le grand-père y sont eux-mêmes nés. L’intéressé peut, sauf s’il est né après l’ent
    - **8** `Article 8`
        > Article 8.- Est tunisien, l’enfant né en Tunisie de parents apatrides résidant en Tunisie depuis cinq ans au moins.
    - **9** `Article 9`
        > Article 9.- Est Tunisien, l’enfant né en Tunisie de parents inconnus. Toutefois, il sera réputé n’avoir jamais été Tunisien si, au cours de la minorit

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## enfant_at_risk

- `q038` [fr, protection_enfant, concept] Quels sont les droits de l'enfant en danger ?

**Current gold** (EnfantFr.pdf)

- **20** `H` Article 20.- Sont considérés, en particulier, comme des situations difficiles menaçant la santé de l'enfant ou son intégrité physique ou morale : a/ la perte des parents de l'enfant qui demeure sans soutien familial. b/ l'exposition de l'enfant à la négligence et au vagabondage. c/ le manquement not
- **20** `F` article 20 du présent code. Section 2 Le devoir de signalement
- **20** `F` article 20 du présent code. Toute personne peut signaler, au délégué à la protection de l’enfance, tout ce qui lui parait menacer la santé de l’enfant ou son intégrité physique ou morale au sens des autres paragraphes de l’
- **20** `F` article 20 du présent code. Le délégué à la protection de l'enfance est obligatoirement avisé de toutes les situations difficiles prévues par l'
- **20** `F` article 20 du présent code si la personne qui s'est aperçue de l'existence de cette situation fait partie des personnes chargées, et par leurs fonctions, de la protection et de l'assistance des enfants, tels que les éducateurs, le médecins, travailleurs sociaux et toutes autres personnes chargées, à
- **20** `F` article 20 du présent code. 16
- **20** `F` article 20 du présent code. Le délégué à la protection de l'enfance dispose à cet effet des prérogatives qui l'habilitent légalement : a) à convoquer l'enfant et ses parents afin d'écouter leurs déclarations et leurs réponses à propos des faits objets du signalement. b) à se rendre seul en tout lieu
- **20** `H` Article 20.- 1. - Tout enfant qui est temporairement ou définitivement privé de son milieu familial, ou qui dans son propre intérêt ne 60 peut être laissé dans ce milieu, a droit à une protection et une aide spéciales de l'Etat. 2. - Les Etats parties prévoient pour cet enfant une protection de remp
- **20** `H` Article 20.- Les mineurs nouvellement admis sont soumis à un examen médical général, les mineurs malades sont soumis à l'examen médical aussi souvent qu'il est jugé nécessaire, le malade est confié à l'infirmerie du centre, et les médicaments prescrits lui sont fournis gratuitement.
- **20** `H` Article 20.- Les ministres des finances et de la jeunesse, de l'enfance et des sports sont chargés, chacun en ce qui le concerne, de l'exécution du présent décret qui sera publié au Journal Officiel de la République Tunisienne. Tunis, le 14 février 2002. Zine El Abidine Ben Ali 127 Décret n° 2010-30
- **21** `H` Article 21.- La négligence signifie la mise en danger de l'intégrité mentale ou psychologique ou physique de l'enfant soit par son abandon par ses parents, sans motif valable dans un endroit ou dans une institution publique ou privée, soit par l'abandon du foyer familial par les parents pendant une 
- **21** `H` Article 21.- Les Etats parties qui admettent et/ou autorisent l'adoption s'assurent que l'intérêt supérieur de l'enfant est la considération primordiale en la matière, et : a) veillant à ce que l'adoption d'un enfant ne soit autorisée que par les autorités compétentes, qui vérifient, conformément à 
- **21** `H` Article 21.- Le mineur malade bénéficie de la gratuité des soins aux hôpitaux relevant du ministère de la santé publique conformément à la législation en vigueur.
- **22** `H` Article 22.- Est considéré comme étant une des situations nécessitant l'intervention, le vagabondage de l'enfant qui reste sans suivi ni formation, en raison du refus de celui qui est chargé de son éducation ou de sa garde de le confier à une école, en application des dispositions de la loi relative
- **22** `H` Article 22.- 1. - Les Etats parties prennent les mesures appropriées pour qu'un enfant qui cherche à obtenir le statut de réfugié ou qui est considéré comme réfugié en vertu des règles et procédures du droit international ou national applicable, qu'il soit seul ou accompagné de ses père et mère ou d
- **22** `H` Article 22.- Le mineur peut être autorisé par la direction générale des prisons et de la rééducation à être soigné à ses frais dans les cliniques privées selon la volonté de ses parents.
- **22** `F` article 22 de la loi réglementant l'état civil, aviser le procureur de la République que l'acte de naissance de l'enfant ne comporte pas un prénom de père, un prénom de grand-père, un nom patronymique et sa nationalité. Le procureur de la République doit, après l'expiration du délai prévu au premier

**Corpus candidates** (BM25 over EnfantFr.pdf headings; query terms: droits enfant danger)

-      **46** (7.7) Article 46.- Dans les cas de danger imminent, le délégué à la protection de l'enfance peut prendre l'initiative d'éloigner l'enfant de l'endroit du danger en ayant recours même à la force publique, et
-      **19** (6.4) Article 19.- Il est interdit d'exploiter l'enfant dans les différentes formes de criminalité organisée, y compris le fait de lui inculquer le fanatisme et la haine et de l'inciter à commettre des acte
- gold **21** (5.5) Article 21.- La négligence signifie la mise en danger de l'intégrité mentale ou psychologique ou physique de l'enfant soit par son abandon par ses parents, sans motif valable dans un endroit ou dans u
-      **2** (5.5) Article 2.- L'observatoire d'information, de formation, de documentation et d'études pour la protection des droits de l'enfant est chargé des missions suivantes : - observer l'état de la protection de
-      **123** (4.9) Article 123.- Si un incident à la liberté surveillée révèle un défaut de surveillance caractérisé de la part des parents, du tuteur, ou de la personne qui en a la garde, ou des entraves systématiques 
-      **30** (4.8) Article 30.- Le délégué à la protection de l'enfance est chargé d'une mission d'intervention préventive dans tous les cas où il s'avère que la santé de l'enfant ou son intégrité physique ou morale est
-      **15** (4.7) Article 15.- 1. – Les Etats parties reconnaissent les droits de l'enfant à la liberté d'association et à la liberté de réunion pacifique. 2. – L'exercice de ces droits ne peut faire l'objet que des se
-      **4** (4.6) Article 4.- L'observatoire d'information, de formation, de documentation et d'études pour la protection des droits de l'enfant est dirigé par un directeur général. Le directeur général de l'observatoi

**Retrieved by official v1** (top-6, one block per language variant)

- `q038` [fr] hit=False
    -   EnfantFr.p art 2: Article 2.- Ce code garantit à l'enfant le droit de bénéficier des différentes mesures préventives à caractère social, éducatif, sanitaire et des autr
    -   EnfantFr.p art 59: article 59 du code de la protection de l'enfant. La présente loi sera publiée au Journal Officiel de la République Tunisienne et exécutée comme loi de
    -   EnfantFr.p art 14: Article 14.- Le présent code vise à favoriser la procédure de médiation, la correctionnalisation et la non-incrimination, ainsi qu'à faire participer 
    -   EnfantFr.p art 10: article 10 ) et dans les statuts et instruments pertinents des institutions spécialisées et des organisations internationales qui se préoccupent du bi
    -   EnfantFr.p art 6: Article 6.- Les ministres de la justice, de l’intérieur, de la jeunesse, de l’enfance et des sports, des affaires de la femme et 138 de la famille, de
    -   EnfantFr.p art 19: Article 19.- 1. - Les Etats parties prennent toutes les mesures législatives, administratives, sociales et éducatives appropriées pour protéger l'enfa

**Suggested change:** Anchor 20/21/22 to the child-protection code (other chunks numbered 20-22 are CRC treaty articles and prison rules). Add 30 (délégué à la protection de l'enfance, preventive intervention) and 46 (danger imminent: removal of the child).

- add: 30, 46   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **20** `Article 20.- Sont considérés, en particulier, comme des situations difficiles`
        > Article 20.- Sont considérés, en particulier, comme des situations difficiles menaçant la santé de l'enfant ou son intégrité physique ou morale : a/ l
    - **21** `Article 21.- La négligence signifie`
        > Article 21.- La négligence signifie la mise en danger de l'intégrité mentale ou psychologique ou physique de l'enfant soit par son abandon par ses par
    - **22** `Article 22.- Est considéré comme étant une des situations`
        > Article 22.- Est considéré comme étant une des situations nécessitant l'intervention, le vagabondage de l'enfant qui reste sans suivi ni formation, en
    - NEW **30** `Article 30.- Le délégué à la protection de l'enfance est chargé`
        > Article 30.- Le délégué à la protection de l'enfance est chargé d'une mission d'intervention préventive dans tous les cas où il s'avère que la santé d
    - NEW **46** `Article 46.- Dans les cas de danger imminent`
        > Article 46.- Dans les cas de danger imminent, le délégué à la protection de l'enfance peut prendre l'initiative d'éloigner l'enfant de l'endroit du da

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## arb_agreement

- `q039` [fr, arbitrage, concept] Qu'est-ce qu'une convention d'arbitrage ?

**Current gold** (ArbitrageFr.pdf)

- **2** `H` Article 2 Les dispositions du présent code ne dérogent pas aux lois spéciales interdisant le règlement de certains différends par voie d'arbitrage ou prescrivant des procédures spéciales pour le recours à l'arbitrage.
- **2** `H` Article 2 La convention d'arbitrage est l'engagement des parties de régler par l'arbitrage toutes ou certaines contestations nées ou pouvant naître entre elles concernant un rapport de droit déterminé, contractuel ou non contractuel. La convention d'arbitrage revêt la forme d'une clause compromissoi
- **2** `H` Article 2 Les dispositions du numéro 18 de l'
- **2** `H` Art. 2. – Le Premier ministre est chargé de l’exécution du présent décret qui sera publié au Journal Officiel de la République Tunisienne. Tunis, le 23 octobre 1995 Zine El Abidine Ben Ali 48 CONVENTION ENTRE LA RÉPUBLIQUE TUNISIENNE ET LA RÉPUBLIQUE HELLENIQUE RELATIVE A L’ENTRAIDE JUDICIAIRE EN MA
- **2** `H` Article 2. – Entraide judiciaire 1.- Les autorités judiciaires des deux parties contractantes se prêteront réciproquement entraide judiciaire en matière civile et commerciale.
- **2** `H` Art. 2. - Le Premier ministre et les ministres concernés sont chargés, chacun selon ses attributions, de l’exécution du présent décret qui sera publié au Journal Officiel de la République Tunisienne. Tunis, le 5 juillet 2005 Zine El Abidine Ben Ali 1) Le texte de l'accord est publié uniquement en la
- **3** `H` Article 3 Sont abrogées les dispositions des articles 258 à 284 du Code de Procédure Civile et Commerciale promulgué par la loi n° 59-130 datée du 5 octobre 1959. Toutefois les instances arbitrales en cours devant les arbitres ou devant les juridictions, restent soumises aux procédures en (1) Travau
- **3** `H` Article 3 La clause compromissoire est l'engagement des parties à un contrat, de soumettre à l'arbitrage, les contestations qui pourraient naître de ce contrat.
- **3** `H` Article 3. – Mode de transmission 1.- Les autorités judiciaires des parties contractantes communiqueront entre elles, aux fins de l’entraide judiciaire, par l’intermédiaire de leurs organes centraux, à savoir le ministère de la justice des deux pays. 50
- **3** `F` article 3 de la présente convention.
- **3** `F` article 3 de la présente convention.
- **3** `F` article 3 de la présente convention, à la juridiction compétente de l’autre partie contractante. 2.- La demande doit être accompagnée : a- d’une expédition officielle de la décision, ainsi que d’un certificat attestant la force de chose jugée et le caractère exécutoire de la décision, à moins que ce

**Corpus candidates** (BM25 over ArbitrageFr.pdf headings; query terms: convention arbitrage)

-      **51** (2.2) Article 51 Pour les questions objet d'une convention d'arbitrage international, les tribunaux ne peuvent intervenir qu'en vertu des dispositions du présent code. Section II. - Convention d'arbitrage
-      **48** (2.1) Article 48 1- L'arbitrage est international dans l'un des cas suivants : a) Si les parties à une convention d'arbitrage ont, au moment de la conclusion de ladite convention, leur établissement dans de
- gold **2** (2.0) Article 2 La convention d'arbitrage est l'engagement des parties de régler par l'arbitrage toutes ou certaines contestations nées ou pouvant naître entre elles concernant un rapport de droit déterminé
-      **52** (1.8) Article 52 Le tribunal saisi d'un différend sur une question faisant l'objet d'une convention d'arbitrage, renverra les parties à l'arbitrage si l'une d'entre elles le demande au plus tard lorsqu'elle
-      **8** (1.8) Article 8 Les parties à une convention d'arbitrage doivent avoir la capacité de disposer de leurs droits.
-      **6** (1.8) Article 6 La convention d'arbitrage ne peut être établie que par écrit, soit par acte authentique ou sous seing privé, soit par procès- verbal d'audience ou procès-verbal dressé auprès du tribunal arb
-      **42** (1.8) Article 42 Même si les parties en conviennent autrement, le recours en annulation d'une sentence arbitrale définitive, peut être formé dans les cas suivants : 1- si la sentence est rendue en l'absence
-      **9** (1.6) Article 9 Sauf convention contraire des parties, la procédure arbitrale concernant un différend déterminé, débute à la date à laquelle la demande de soumission de ce différend à l'arbitrage, est reçue

**Retrieved by official v1** (top-6, one block per language variant)

- `q039` [fr] hit=True
    -   ArbitrageF art 61: Article 61 1- Le tribunal arbitral statue sur sa propre compétence et sur toute opposition relative à l'existence ou à la validité de la convention d'
    -   ArbitrageF art 39: Article 39 La présente convention pourra être dénoncée par chacun des deux Etats. La dénonciation prendra effet un an après la date à laquelle elle au
    - ✓ ArbitrageF art 3: Article 3 Sont abrogées les dispositions des articles 258 à 284 du Code de Procédure Civile et Commerciale promulgué par la loi n° 59-130 datée du 5 o
    -   ArbitrageF art 6: Article 6 La convention d'arbitrage ne peut être établie que par écrit, soit par acte authentique ou sous seing privé, soit par procès- verbal d'audie
    -   ArbitrageF art 52: article 52 du présent code était frappée d'une incapacité, ou que cette convention n'est pas valable au regard de la loi à laquelle les parties l'ont 
    - ✓ ArbitrageF art 2: Article 2 La convention d'arbitrage est l'engagement des parties de régler par l'arbitrage toutes ou certaines contestations nées ou pouvant naître en

**Suggested change:** Anchor 2 and 3 to the arbitration-agreement/clause articles (6 chunks each carry numbers 2 and 3). Add 6 (form: la convention d'arbitrage ne peut être établie que par écrit).

- add: 6   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - **2** `Article 2 La convention d'arbitrage est l'engagement`
        > Article 2 La convention d'arbitrage est l'engagement des parties de régler par l'arbitrage toutes ou certaines contestations nées ou pouvant naître en
    - **3** `Article 3 La clause compromissoire`
        > Article 3 La clause compromissoire est l'engagement des parties à un contrat, de soumettre à l'arbitrage, les contestations qui pourraient naître de c
    - NEW **6** `Article 6 La convention d'arbitrage ne peut`
        > Article 6 La convention d'arbitrage ne peut être établie que par écrit, soit par acte authentique ou sous seing privé, soit par procès- verbal d'audie

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______

---
## any_art13

- `q040` [fr, unfiltered, cross_domain] Que dit l'article 13 ?
- `q086` [en, unfiltered, cross_domain] What does article 13 say?

**Current gold** (source-ambiguous: any code accepted)

- article 13 (any code)

**Retrieved by official v1** (top-6, one block per language variant)

- `q040` [fr] hit=True
    - ✓ PenalFr.pd art 13: Article 13 (Modifié par la loi n° 99-89 du 2 août 1999).- La peine d'emprisonnement est subie dans l’une des prisons.
    - ✓ CommerceFr art 13: Article 13 Si la partie, aux livres de laquelle on offre de faire foi, refuse de les représenter sans motif valable, le juge admettra le dire de l'aut
    - ✓ EnfantFr.p art 13: Article 13.- 1. – L'enfant a droit à la liberté d'expression. Ce droit comprend la liberté de recherche, de recevoir et de répandre des informations e
    - ✓ ArbitrageF art 13: Article 13 L'arbitrage peut être ad hoc ou institutionnel. En cas d'arbitrage ad hoc, le tribunal arbitral se chargera de l'organiser en fixant la pro
    - ✓ Procedurec art 13: Article 13.- Les déchéances et forclusions sont toutes obligatoires. Le tribunal doit les soulever d'office.
    - ✓ ArbitrageF art 13: Article 13 1.- La signification ne pourra donner lieu à la perception de taxes ou frais de quelque nature que ce soit. 2.- Toutefois, l’Etat requis po
- `q086` [en] hit=True
    - ✓ PenalFr.pd art 13: Article 13 (Modifié par la loi n° 99-89 du 2 août 1999).- La peine d'emprisonnement est subie dans l’une des prisons.
    - ✓ EnfantFr.p art 13: Article 13.- 1. – L'enfant a droit à la liberté d'expression. Ce droit comprend la liberté de recherche, de recevoir et de répandre des informations e
    - ✓ Statutpers art 13: Article 13 .- Toute personne pourra, sauf l'exception prévue à l'
    - ✓ CommerceFr art 13: Article 13 Si la partie, aux livres de laquelle on offre de faire foi, refuse de les représenter sans motif valable, le juge admettra le dire de l'aut
    - ✓ Procedurec art 13: Article 13.- Les déchéances et forclusions sont toutes obligatoires. Le tribunal doit les soulever d'office.
    - ✓ societeFr. art 13: Article 13 quater (Ajouté par l’

**Suggested change:** No change. Source wildcard kept: the question names no code, so an article 13 from any code is an acceptable answer.

- add: none   |   remove: none
- proposed gold (anchor = the text the intended chunk must start with):
    - any code, article 13

**Decision:** [ ] approve  [ ] reject  [ ] edit: ______
