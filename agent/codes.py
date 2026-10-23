CODE_DESCRIPTIONS = {
    "arbitrage": "Domestic and international arbitration; bundles annexed laws, decrees and judicial-assistance conventions.",
    "obligations_contrats": "General law of obligations and named contracts: sale, lease, loan, mandate, surety.",
    "commerce": "Merchants, business goodwill, bills of exchange, cheques, bankruptcy, commercial contracts.",
    "droit_international_prive": "Cross-border cases: international jurisdiction, recognition of foreign judgments, immunity, applicable law.",
    "droits_reels": "Property, usufruct, servitudes, real securities, land registration; bundles annexed land laws.",
    "protection_enfant": "Children in danger and juvenile offenders; bundles UN convention and other texts.",
    "nationalite": "Tunisian nationality: by origin, acquisition, loss, administrative procedure, nationality litigation.",
    "penal": "General criminal rules, penalties, offences against public order and individuals, contraventions.",
    "procedure_civile": "Civil and commercial court procedure: jurisdiction, proceedings, appeals, summary relief, enforcement.",
    "procedure_penale": "Criminal procedure: prosecution, investigation, trial courts, appeals, sentence enforcement; bundles annexed laws.",
    "societes": "Commercial companies: partnerships, limited-liability, joint-stock companies, mergers; bundles commercial register law.",
    "statut_personnel": "Marriage, divorce, custody, maintenance, filiation, inheritance; bundles civil-status, adoption, marital-property laws.",
    "travail": "Employment contracts, collective agreements, working conditions, wages, safety, labour inspection, disputes, unions.",
    "constitution": "2022 Constitution: general principles, rights and freedoms, state powers, constitutional revision.",
}

def codes_block() -> str:
    lines = [f"- {k}: {v}" for k, v in CODE_DESCRIPTIONS.items()]
    return "Codes and what they cover:\n" + "\n".join(lines)