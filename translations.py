"""All user-facing copy for the site, per language.

Both languages render from the same templates, so adding or changing a
section only needs a template edit plus the matching keys below.
"""

SUPPORTED_LANGUAGES = ("nl", "en")
DEFAULT_LANGUAGE = "en"

TRANSLATIONS = {
    "en": {
        "meta_title": "All Around Service | Heating & Plumbing by Prawesh Bhagwandin",
        "meta_description": (
            "Certified heating, plumbing and CO safety services by Prawesh Bhagwandin. "
            "Boiler installation, repairs, maintenance and CO inspections."
        ),
        "brand_tagline": "Heating & Plumbing",
        "skip_link": "Skip to content",
        "nav": {
            "about": "About",
            "services": "Services",
            "work": "Our work",
            "reviews": "Reviews",
            "contact": "Contact",
            "book": "Book a call",
            "menu": "Menu",
            "language": "Language",
        },
        "hero": {
            "eyebrow": "Reliable home comfort",
            "title": "Professional heating, plumbing and gas safety.",
            "text": (
                "I am a certified installation technician with years of hands-on experience in "
                "boiler systems, plumbing, maintenance and CO safety inspections."
            ),
            "cta_primary": "Book a consultation",
            "cta_secondary": "Send a message",
            "trust": ["Certified technician", "CO inspector", "Local, personal service"],
            "image_alt": "Boiler and hot-water installation completed by All Around Service",
            "badge_title": "Recent installation",
            "badge_text": "Boiler, buffer tank & hot-water cylinder",
            "stat_years": "Years of experience",
            "stat_years_value": "10+",
            "stat_focus": "Certified CO inspections",
            "stat_focus_value": "CO",
        },
        "about": {
            "eyebrow": "About me",
            "title": "Experienced, dependable workmanship.",
            "text": (
                "Whether it is a routine inspection, a sudden breakdown or a complete heating system "
                "replacement, I deliver installation and repair work that keeps your home safe, "
                "comfortable and efficient. You deal with me directly, from first visit to finished job."
            ),
            "features": [
                {"icon": "tool", "title": "Boiler systems",
                 "text": "Installation, maintenance and fault finding for efficient heating."},
                {"icon": "droplet", "title": "Plumbing",
                 "text": "Repairs, upgrades and practical solutions for your water supply."},
                {"icon": "shield", "title": "Safety inspections",
                 "text": "CO safety checks carried out to current standards, for peace of mind."},
            ],
        },
        "services": {
            "eyebrow": "Services",
            "title": "What I can do for you",
            "entries": [
                {"icon": "flame", "title": "Central heating",
                 "text": "Installation, servicing and upgrades for efficient, consistent heating."},
                {"icon": "tool", "title": "Boiler repair",
                 "text": "Fast diagnosis and reliable repairs to restore comfort without delay."},
                {"icon": "clipboard", "title": "CO inspections",
                 "text": "Carbon monoxide safety checks and expert assessments for your household."},
                {"icon": "droplet", "title": "Plumbing & maintenance",
                 "text": "Routine upkeep and problem solving for water and pipe systems."},
            ],
        },
        "work": {
            "eyebrow": "Our work",
            "title": "Recent installations",
            "entries": [
                {"image": "images/work/installation-boiler.jpg",
                 "alt": "Remeha boiler with buffer tank and Masterwatt hot-water cylinder",
                 "caption": "Boiler with buffer tank and hot-water cylinder"},
                {"image": "images/work/installation-heatpump.jpg",
                 "alt": "Heat pump installation with storage cylinder and ventilation unit",
                 "caption": "Heat pump with storage cylinder"},
            ],
        },
        "reviews": {
            "eyebrow": "Client feedback",
            "title": "What clients say",
            "entries": [
                {"quote": "Prawesh fixed our boiler in under an hour. Very professional and efficient!",
                 "name": "Priya"},
                {"quote": "Quick response, honest advice and great service. Highly recommended.",
                 "name": "Johan"},
                {"quote": "He rewired our kitchen and installed new lighting. The work was excellent and tidy.",
                 "name": "Fatima"},
            ],
        },
        "booking": {
            "eyebrow": "Appointment",
            "title": "Schedule a short call to discuss your needs",
            "calendly_url": "https://calendly.com/prawesh-b/30min",
        },
        "contact": {
            "eyebrow": "Contact",
            "title": "Ready to discuss your project?",
            "text": (
                "Whether you need an urgent repair, a maintenance check or a full installation, "
                "I'm happy to help with practical advice and dependable workmanship."
            ),
            "points": ["Fast response times", "Clear communication", "Professional workmanship"],
            "phone_label": "Phone",
            "email_label": "Email",
            "area_label": "Service area",
            "form": {
                "name": "Your name",
                "phone": "Phone number",
                "email": "Email (optional)",
                "message": "Your message",
                "message_placeholder": "Tell me about your project or issue",
                "submit": "Send message",
                "sending": "Sending…",
                "privacy": "Your details are only used to respond to your request.",
            },
            "errors": {
                "name": "Please enter your name.",
                "phone": "Please enter a valid phone number.",
                "email": "Please enter a valid email address.",
                "message": "Please enter a message (max. 2000 characters).",
            },
        },
        "footer": {
            "about": "Certified heating, plumbing and CO safety services for homeowners.",
            "certifications": "Certifications & memberships",
            "rights": "All rights reserved.",
            "kvk": "Chamber of Commerce (KvK)",
        },
        "submitted": {
            "title": "Message received",
            "eyebrow": "Thank you",
            "heading": "Thanks, {name}!",
            "text": "Your message has been received. I'll get back to you as soon as possible.",
            "follow_up": "I'll contact you on",
            "your_message": "Your message",
            "back": "Back to the website",
            "error_heading": "Your message could not be sent",
            "error_text": "Something went wrong on our side. Please try again later, or contact me directly.",
        },
    },
    "nl": {
        "meta_title": "All Around Service | CV & Sanitair door Prawesh Bhagwandin",
        "meta_description": (
            "Gecertificeerde cv-, loodgieters- en CO-veiligheidsdiensten door Prawesh Bhagwandin. "
            "Installatie, reparatie en onderhoud van cv-ketels en CO-keuringen."
        ),
        "brand_tagline": "CV & Sanitair",
        "skip_link": "Direct naar inhoud",
        "nav": {
            "about": "Over mij",
            "services": "Diensten",
            "work": "Projecten",
            "reviews": "Reviews",
            "contact": "Contact",
            "book": "Plan een gesprek",
            "menu": "Menu",
            "language": "Taal",
        },
        "hero": {
            "eyebrow": "Betrouwbaar wooncomfort",
            "title": "Vakkundig cv-, loodgieters- en gasveiligheidswerk.",
            "text": (
                "Ik ben een gecertificeerd installatietechnicus met jarenlange praktijkervaring in "
                "cv-systemen, loodgieterswerk, onderhoud en CO-veiligheidscontroles."
            ),
            "cta_primary": "Plan een consult",
            "cta_secondary": "Stuur een bericht",
            "trust": ["Gecertificeerd technicus", "CO-keurmeester", "Lokale, persoonlijke service"],
            "image_alt": "Cv-ketel en warmwaterinstallatie aangelegd door All Around Service",
            "badge_title": "Recente installatie",
            "badge_text": "Cv-ketel, buffervat & warmwaterboiler",
            "stat_years": "Jaar ervaring",
            "stat_years_value": "10+",
            "stat_focus": "Gecertificeerde CO-keuringen",
            "stat_focus_value": "CO",
        },
        "about": {
            "eyebrow": "Over mij",
            "title": "Ervaren en betrouwbaar vakmanschap.",
            "text": (
                "Of het nu gaat om een routinecontrole, een plotselinge storing of een volledige vervanging "
                "van uw verwarmingssysteem: ik lever installatie- en reparatiewerk dat uw woning veilig, "
                "comfortabel en zuinig houdt. U heeft direct contact met mij, van eerste bezoek tot oplevering."
            ),
            "features": [
                {"icon": "tool", "title": "Cv-systemen",
                 "text": "Installatie, onderhoud en storingsopsporing voor efficiënte verwarming."},
                {"icon": "droplet", "title": "Loodgieterswerk",
                 "text": "Reparaties, verbeteringen en praktische oplossingen voor uw watervoorziening."},
                {"icon": "shield", "title": "Veiligheidscontroles",
                 "text": "CO-controles volgens de geldende normen, voor uw gemoedsrust."},
            ],
        },
        "services": {
            "eyebrow": "Diensten",
            "title": "Wat ik voor u kan doen",
            "entries": [
                {"icon": "flame", "title": "Centrale verwarming",
                 "text": "Installatie, onderhoud en verbeteringen voor efficiënte, constante verwarming."},
                {"icon": "tool", "title": "Ketelreparatie",
                 "text": "Snelle diagnose en betrouwbare reparaties, zodat uw comfort snel terug is."},
                {"icon": "clipboard", "title": "CO-keuringen",
                 "text": "Koolmonoxide-veiligheidscontroles en deskundige beoordelingen voor uw huishouden."},
                {"icon": "droplet", "title": "Loodgieterswerk & onderhoud",
                 "text": "Routineonderhoud en probleemoplossing voor water- en leidingwerk."},
            ],
        },
        "work": {
            "eyebrow": "Projecten",
            "title": "Recente installaties",
            "entries": [
                {"image": "images/work/installation-boiler.jpg",
                 "alt": "Remeha cv-ketel met buffervat en Masterwatt warmwaterboiler",
                 "caption": "Cv-ketel met buffervat en warmwaterboiler"},
                {"image": "images/work/installation-heatpump.jpg",
                 "alt": "Warmtepompinstallatie met boilervat en ventilatie-unit",
                 "caption": "Warmtepomp met boilervat"},
            ],
        },
        "reviews": {
            "eyebrow": "Klantervaringen",
            "title": "Wat klanten zeggen",
            "entries": [
                {"quote": "Prawesh repareerde onze cv-ketel binnen een uur. Super professioneel en efficiënt!",
                 "name": "Priya"},
                {"quote": "Snelle reactie, eerlijk advies en geweldige service. Zeker een aanrader.",
                 "name": "Johan"},
                {"quote": "Hij heeft onze keuken opnieuw bedraad en nieuwe verlichting geïnstalleerd. "
                          "Het werk was uitstekend en netjes.",
                 "name": "Fatima"},
            ],
        },
        "booking": {
            "eyebrow": "Afspraak",
            "title": "Plan een kort gesprek om uw wensen te bespreken",
            "calendly_url": "https://calendly.com/prawesh-b/new-meeting",
        },
        "contact": {
            "eyebrow": "Contact",
            "title": "Klaar om uw project te bespreken?",
            "text": (
                "Of u nu een dringende reparatie, een onderhoudsbeurt of een complete installatie nodig heeft, "
                "ik help u graag met praktisch advies en betrouwbaar vakwerk."
            ),
            "points": ["Snelle reactie", "Duidelijke communicatie", "Professioneel vakwerk"],
            "phone_label": "Telefoon",
            "email_label": "E-mail",
            "area_label": "Werkgebied",
            "form": {
                "name": "Uw naam",
                "phone": "Telefoonnummer",
                "email": "E-mailadres (optioneel)",
                "message": "Uw bericht",
                "message_placeholder": "Vertel mij over uw project of probleem",
                "submit": "Verstuur bericht",
                "sending": "Bezig met versturen…",
                "privacy": "Uw gegevens worden alleen gebruikt om op uw aanvraag te reageren.",
            },
            "errors": {
                "name": "Vul uw naam in.",
                "phone": "Vul een geldig telefoonnummer in.",
                "email": "Vul een geldig e-mailadres in.",
                "message": "Vul een bericht in (max. 2000 tekens).",
            },
        },
        "footer": {
            "about": "Gecertificeerde cv-, loodgieters- en CO-veiligheidsdiensten voor particulieren.",
            "certifications": "Certificeringen & lidmaatschappen",
            "rights": "Alle rechten voorbehouden.",
            "kvk": "KvK-nummer",
        },
        "submitted": {
            "title": "Bericht ontvangen",
            "eyebrow": "Bedankt",
            "heading": "Bedankt, {name}!",
            "text": "Uw bericht is ontvangen. Ik neem zo snel mogelijk contact met u op.",
            "follow_up": "Ik neem contact met u op via",
            "your_message": "Uw bericht",
            "back": "Terug naar de website",
            "error_heading": "Uw bericht kon niet worden verzonden",
            "error_text": "Er ging iets mis aan onze kant. Probeer het later opnieuw of neem direct contact met mij op.",
        },
    },
}
