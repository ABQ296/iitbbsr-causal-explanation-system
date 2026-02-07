# def generate_structured_explanation(outcome, top_terms, evidence):
#     """
#     Generate structured causal explanation from extracted factors and evidence.
#     """

#     explanation = {
#         "outcome_event": outcome,
#         "causal_factors": [],
#         "causal_reasoning": ""
#     }

#     # Add causal factors with supporting evidence
#     for term in top_terms:
#         factor_entry = {
#             "factor": term,
#             "supporting_evidence": []
#         }

#         for ex in evidence.get(term, []):
#             factor_entry["supporting_evidence"].append({
#                 "transcript_id": ex["transcript_id"],
#                 "speaker": ex["speaker"],
#                 "text": ex["text"]
#             })

#         explanation["causal_factors"].append(factor_entry)

#     # Generate reasoning summary (template-based)
#     reasoning_text = (
#         f"The outcome '{outcome}' appears to be triggered by recurring customer-reported "
#         f"issues such as {', '.join(top_terms[:5])}. "
#         "These factors reflect early-stage dissatisfaction, unresolved problems, or repeated failures "
#         "that precede the escalation or business event."
#     )

#     explanation["causal_reasoning"] = reasoning_text

#     return explanation





# def generate_structured_explanation(outcome, top_terms, evidence):

#     explanation = {
#         "outcome_event": outcome,
#         "causal_factors": [],
#         "causal_reasoning": ""
#     }

#     max_factors = 5
#     count = 0

#     for term in top_terms:

#         if count >= max_factors:
#             break

#         # Skip if no supporting evidence
#         if not evidence.get(term):
#             continue

#         # Skip very short fragments
#         if len(term.split()) < 2:
#             continue

#         factor_entry = {
#             "factor": term,
#             "supporting_evidence": evidence[term]
#         }

#         explanation["causal_factors"].append(factor_entry)
#         count += 1

#     key_factors = [f["factor"] for f in explanation["causal_factors"]]

#     reasoning_text = (
#         f"The outcome '{outcome}' is primarily triggered by early-stage customer reports "
#         f"indicating issues such as {', '.join(key_factors)}. "
#         "These statements reflect underlying problems that precede the event. "
#         "The supporting dialogue evidence demonstrates recurring patterns that logically contribute "
#         "to the emergence of this outcome."
#     )

#     explanation["causal_reasoning"] = reasoning_text

#     return explanation



# from factor_cleaner import clean_factor

# def generate_structured_explanation(outcome, top_terms, evidence):

#     explanation = {
#         "outcome_event": outcome,
#         "causal_factors": [],
#         "causal_reasoning": ""
#     }

#     max_factors = 5
#     count = 0

#     for term in top_terms:
#         if count >= max_factors:
#             break

#         if not evidence.get(term):
#             continue

#         cleaned = clean_factor(term)
#         if not cleaned:
#             continue

#         explanation["causal_factors"].append({
#             "factor": cleaned,
#             "supporting_evidence": evidence[term]
#         })

#         count += 1

#     key_factors = [f["factor"] for f in explanation["causal_factors"]]

#     explanation["causal_reasoning"] = (
#         f"The outcome '{outcome}' is primarily triggered by early-stage customer "
#         f"reports indicating issues such as {', '.join(key_factors)}. "
#         "These statements reflect underlying problems that precede the event. "
#         "The supporting dialogue evidence demonstrates recurring patterns that "
#         "logically contribute to the emergence of this outcome."
#     )

#     return explanation


# def generate_structured_explanation(outcome_event, top_terms, evidence):

#     causal_factors = []

#     for factor in top_terms:
#         supporting_evidence = evidence.get(factor, [])

#         if supporting_evidence:
#             causal_factors.append({
#                 "factor": factor,
#                 "supporting_evidence": supporting_evidence
#             })


#     readable_factors = [f["factor"] for f in causal_factors]

#     if not readable_factors:
#         reasoning = (
#             f"The outcome '{outcome_event}' is associated with conversational patterns "
#             f"observed in the dataset, but no strong distinguishing early-stage factors "
#             f"were identified under the current extraction constraints."
#         )
#     else:

#         if "Fraud" in outcome_event:
#             reasoning = (
#                 f"In conversations labeled '{outcome_event}', customers frequently report "
#                 f"unauthorized charges, deny recent purchases, or reference fraud alerts. "
#                 f"These anomalies suggest suspicious account activity, which logically "
#                 f"triggers automated fraud detection mechanisms and initiates a formal investigation."
#             )

#         elif "Delivery" in outcome_event:
#             reasoning = (
#                 f"For '{outcome_event}', customers consistently report discrepancies "
#                 f"between tracking status and physical receipt of items (e.g., marked delivered "
#                 f"but not received). Such inconsistencies prompt verification procedures, "
#                 f"leading to delivery investigations."
#             )

#         elif "Account Access" in outcome_event:
#             reasoning = (
#                 f"In '{outcome_event}' cases, customers describe login failures, security holds, "
#                 f"or access restrictions often triggered after credential resets. These "
#                 f"protective security mechanisms restrict account access, resulting in reported issues."
#             )

#         elif "Escalation" in outcome_event:
#             reasoning = (
#                 f"The outcome '{outcome_event}' emerges when customers describe repeated "
#                 f"service failures, unresolved complaints, or threats of legal action. "
#                 f"Persistent dissatisfaction increases severity, ultimately leading to escalation."
#             )

#         else:
#             reasoning = (
#                 f"The outcome '{outcome_event}' is consistently preceded by conversational "
#                 f"signals such as {', '.join(readable_factors)}. These patterns indicate "
#                 f"underlying operational or service disruptions that logically contribute "
#                 f"to the emergence of this event."
#             )

#     return {
#         "outcome_event": outcome_event,
#         "causal_factors": causal_factors,
#         "causal_reasoning": reasoning
#     }


#FINAL
def generate_structured_explanation(outcome_event, top_terms, evidence):

    causal_factors = []

    for factor in top_terms:
        supporting_evidence = evidence.get(factor, [])
        if supporting_evidence:
            causal_factors.append({
                "factor": factor,
                "supporting_evidence": supporting_evidence
            })

    if not causal_factors:
        reasoning = (
            f"The outcome '{outcome_event}' is associated with conversational "
            f"patterns observed in the dataset, but no strong distinguishing "
            f"early-stage factors were identified."
        )
    else:

        if "Fraud" in outcome_event:
            reasoning = (
                f"In conversations labeled '{outcome_event}', customers report "
                f"suspicious charges or deny recent transactions. These conversational "
                f"signals correspond to cases categorized under fraud investigation "
                f"within the dataset."
            )

        elif "Delivery" in outcome_event:
            reasoning = (
                f"For '{outcome_event}', customers describe orders marked as delivered "
                f"but not physically received. This reported discrepancy leads to "
                f"classification as a delivery investigation."
            )

        elif "Account Access" in outcome_event:
            reasoning = (
                f"In '{outcome_event}' cases, customers describe login failures or "
                f"security holds following credential resets. These access restrictions "
                f"correspond to account access issue categorization."
            )

        elif "Escalation" in outcome_event:
            reasoning = (
                f"The outcome '{outcome_event}' is associated with repeated service "
                f"complaints or unresolved issues expressed in conversations, "
                f"leading to escalation classification."
            )

        else:
            readable_factors = [f["factor"] for f in causal_factors]
            reasoning = (
                f"The outcome '{outcome_event}' is preceded by conversational "
                f"signals such as {', '.join(readable_factors)}, which are "
                f"consistently observed in the dataset."
            )

    return {
        "outcome_event": outcome_event,
        "causal_factors": causal_factors,
        "causal_reasoning": reasoning
    }
