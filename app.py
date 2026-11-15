import logging
import os
import re
from datetime import date

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, session, url_for
from flask_mail import Mail, Message

from translations import DEFAULT_LANGUAGE, SUPPORTED_LANGUAGES, TRANSLATIONS

load_dotenv()

app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY", "dev-only-change-me"),
    MAIL_SERVER=os.environ.get("MAIL_SERVER"),
    MAIL_PORT=int(os.environ.get("MAIL_PORT", 587)),
    MAIL_USE_TLS=os.environ.get("MAIL_USE_TLS", "true").lower() == "true",
    MAIL_USE_SSL=os.environ.get("MAIL_USE_SSL", "false").lower() == "true",
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD"),
    MAIL_DEFAULT_SENDER=os.environ.get("MAIL_DEFAULT_SENDER") or os.environ.get("MAIL_USERNAME"),
    SESSION_COOKIE_SAMESITE="Lax",
)
mail = Mail(app)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
if not os.environ.get("SECRET_KEY"):
    log.warning("SECRET_KEY is not set; using an insecure development key.")

# Business details shown on the site. Leave a value empty to hide it.
BUSINESS = {
    "name": "All Around Service",
    "owner": "Prawesh Bhagwandin",
    "phone": os.environ.get("BUSINESS_PHONE", ""),
    "email": os.environ.get("BUSINESS_EMAIL", ""),
    "area": os.environ.get("BUSINESS_AREA", ""),
    "kvk": os.environ.get("BUSINESS_KVK", ""),
}
CONTACT_RECIPIENT = os.environ.get("CONTACT_RECIPIENT") or BUSINESS["email"]

PHONE_RE = re.compile(r"^[+()\d\s-]{6,20}$")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def get_language():
    lang = request.args.get("lang") or request.form.get("lang")
    if lang in SUPPORTED_LANGUAGES:
        return lang
    return request.accept_languages.best_match(SUPPORTED_LANGUAGES) or DEFAULT_LANGUAGE


def render_page(template, lang, **context):
    return render_template(
        template,
        lang=lang,
        t=TRANSLATIONS[lang],
        business=BUSINESS,
        year=date.today().year,
        **context,
    )


def validate_contact(form):
    data = {
        "name": form.get("name", "").strip(),
        "phone": form.get("phone", "").strip(),
        "email": form.get("email", "").strip(),
        "message": form.get("message", "").strip(),
    }
    errors = []
    if not data["name"] or len(data["name"]) > 100:
        errors.append("name")
    if not PHONE_RE.match(data["phone"]):
        errors.append("phone")
    if data["email"] and (len(data["email"]) > 254 or not EMAIL_RE.match(data["email"])):
        errors.append("email")
    if not data["message"] or len(data["message"]) > 2000:
        errors.append("message")
    return data, errors


def send_contact_email(data):
    """Email the enquiry to the business. Returns True on success."""
    if not (app.config["MAIL_SERVER"] and CONTACT_RECIPIENT):
        # Mail is not configured (e.g. local development): log instead of losing the message.
        log.warning("Mail not configured; contact request: %s", data)
        return True

    msg = Message(
        subject=f"New website enquiry from {data['name']}",
        recipients=[CONTACT_RECIPIENT],
        reply_to=data["email"] or None,
        body=(
            f"Name:    {data['name']}\n"
            f"Phone:   {data['phone']}\n"
            f"Email:   {data['email'] or '-'}\n\n"
            f"{data['message']}\n"
        ),
    )
    try:
        mail.send(msg)
        return True
    except Exception:
        log.exception("Failed to send contact email")
        return False


@app.route("/")
def home():
    return render_page("index.html", get_language())


@app.route("/contact", methods=["POST"])
def contact():
    lang = get_language()

    # Honeypot: real visitors never fill in this hidden field; bots usually do.
    if request.form.get("website"):
        return redirect(url_for("submitted", lang=lang))

    data, errors = validate_contact(request.form)
    if errors:
        return render_page("index.html", lang, form=data, errors=errors), 400

    sent = send_contact_email(data)
    session["contact"] = {"name": data["name"], "phone": data["phone"],
                          "message": data["message"], "sent": sent}
    return redirect(url_for("submitted", lang=lang))


@app.route("/submitted")
def submitted():
    lang = get_language()
    contact_data = session.pop("contact", None)
    if contact_data is None:
        return redirect(url_for("home", lang=lang))
    return render_page("submitted.html", lang, contact=contact_data)


# Keep the old form endpoint working for any cached pages.
app.add_url_rule("/submitted", "submitted_legacy", contact, methods=["POST"])


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
