# import difflib
# def detect_outcome_from_query(query, intent_list):
#     query = query.lower()

#     for intent in intent_list:
#         if intent.lower() in query:
#             return intent

#     best_match = difflib.get_close_matches(query, intent_list, n=1, cutoff=0.3)

#     if best_match:
#         return best_match[0]

#     return None


# import difflib
# def detect_outcome_from_query(query, intent_list):

#     query = query.lower()

#     for intent in intent_list:
#         if intent.lower() in query:
#             return intent

#     best_match = difflib.get_close_matches(query, intent_list, n=1, cutoff=0.3)

#     if best_match:
#         return best_match[0]

#     return None


# import re
# DOMAIN_KEYWORDS = {
#     "Fraud Alert Investigation": [
#         "fraud", "unauthorized", "charge", "transaction",
#         "suspicious", "fraudulent", "alert"
#     ],

#     "Account Access Issues": [
#         "login", "log in", "password", "credentials",
#         "locked", "reset", "access", "authentication"
#     ],

#     "Delivery Investigation": [
#         "delivery", "package", "missing", "not received",
#         "shows delivered", "courier"
#     ],

#     "Escalation - Repeated Service Failures": [
#         "escalation", "complaint", "repeated",
#         "not fixed", "multiple times", "again and again"
#     ],

#     "Escalation - Threat of Legal Action": [
#         "legal", "lawyer", "sue", "court",
#         "complaint authority", "legal action"
#     ],

#     "Service Interruptions": [
#         "outage", "service down", "not working",
#         "interruption", "network issue"
#     ],

#     "Claim Denials": [
#         "claim denied", "insurance denied",
#         "rejected claim", "coverage denied"
#     ]
# }


# def normalize_text(text):
#     text = text.lower()
#     text = re.sub(r"[^a-z0-9\s]", "", text)
#     return text

# def detect_outcome_from_query(query, available_intents):
#     query = normalize_text(query)
#     for intent, keywords in DOMAIN_KEYWORDS.items():
#         for keyword in keywords:
#             if keyword in query:
#                 if intent in available_intents:
#                     return intent


#     for intent in available_intents:
#         if normalize_text(intent) in query:
#             return intent
#     return None



#FINAL
import re
DOMAIN_KEYWORDS = {
    "Fraud Alert Investigation": [
        "fraud",
        "fraudulent",
        "unauthorized",
        "charge",
        "transaction",
        "suspicious",
        "alert",
        "card used",
        "used my card",
        "without permission",
        "stolen card",
        "someone used",
        "unknown charge",
        "did not make this purchase"
    ],

    "Account Access Issues": [
        "login",
        "log in",
        "password",
        "credentials",
        "locked",
        "reset",
        "access",
        "authentication",
        "cannot log",
        "cant log",
        "account locked"
    ],

    "Delivery Investigation": [
        "delivery",
        "package",
        "missing",
        "not received",
        "shows delivered",
        "courier",
        "parcel"
    ],

    "Escalation - Repeated Service Failures": [
        "escalation",
        "complaint",
        "repeated",
        "not fixed",
        "multiple times",
        "again and again",
        "same issue"
    ],

    "Escalation - Threat of Legal Action": [
        "legal",
        "lawyer",
        "sue",
        "court",
        "legal action",
        "complaint authority"
    ],

    "Service Interruptions": [
        "outage",
        "service down",
        "not working",
        "interruption",
        "network issue",
        "no service"
    ],

    "Claim Denials": [
        "claim denied",
        "insurance denied",
        "rejected claim",
        "coverage denied"
    ]
}

def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text


def detect_outcome_from_query(query, available_intents):

    query = normalize_text(query)

    for intent, keywords in DOMAIN_KEYWORDS.items():
        for keyword in keywords:
            if keyword in query:
                if intent in available_intents:
                    return intent

    for intent in available_intents:
        if normalize_text(intent) in query:
            return intent

    return None
