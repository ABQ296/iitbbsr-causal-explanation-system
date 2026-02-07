# def extract_evidence(df, target_outcome, top_terms, max_evidence_per_term=3):
#     evidence_dict = {}

#     relevant_df = df[df["intent"] == target_outcome]

#     for term in top_terms:
#         evidence_dict[term] = []

#         for _, row in relevant_df.iterrows():
#             transcript_id = row["transcript_id"]
#             full_text = row["full_text"]

#             # Split conversation into turns
#             turns = full_text.split("Agent: ")  # basic split

#             for turn in turns:
#                 if term.lower() in turn.lower():
#                     evidence_dict[term].append({
#                         "transcript_id": transcript_id,
#                         "text": turn.strip()
#                     })

#                     if len(evidence_dict[term]) >= max_evidence_per_term:
#                         break

#             if len(evidence_dict[term]) >= max_evidence_per_term:
#                 break

#     return evidence_dict





# def extract_evidence(df, target_outcome, top_terms, max_evidence_per_term=3):
#     evidence_dict = {}

#     relevant_df = df[df["intent"] == target_outcome]

#     for term in top_terms:
#         evidence_dict[term] = []

#         for _, row in relevant_df.iterrows():
#             transcript_id = row["transcript_id"]
#             conversation = row["conversation"]

#             # Look only at early turns (causal zone)
#             for turn in conversation[:6]:
#                 text = turn["text"]

#                 if term.lower() in text.lower():
#                     evidence_dict[term].append({
#                         "transcript_id": transcript_id,
#                         "speaker": turn["speaker"],
#                         "text": text
#                     })

#                     if len(evidence_dict[term]) >= max_evidence_per_term:
#                         break

#             if len(evidence_dict[term]) >= max_evidence_per_term:
#                 break

#     return evidence_dict




# def extract_evidence(df, target_outcome, top_terms, max_evidence_per_term=3):

#     evidence_dict = {}

#     relevant_df = df[df["intent"] == target_outcome]

#     for term in top_terms:
#         evidence_dict[term] = []

#         for _, row in relevant_df.iterrows():
#             transcript_id = row["transcript_id"]
#             conversation = row["conversation"]

#             for turn in conversation[:6]:
#                 text = turn["text"]

#                 if term.lower() in text.lower():
#                     evidence_dict[term].append({
#                         "transcript_id": transcript_id,
#                         "speaker": turn["speaker"],
#                         "text": text
#                     })

#                     if len(evidence_dict[term]) >= max_evidence_per_term:
#                         break

#             if len(evidence_dict[term]) >= max_evidence_per_term:
#                 break

#     return evidence_dict



#FINAL

def extract_evidence(df, target_outcome, top_terms, max_examples=3):

    evidence_dict = {}

    filtered_df = df[df["intent"] == target_outcome]

    for term in top_terms:
        term_lower = term.lower()
        collected = []
        used_ids = set()

        for _, row in filtered_df.iterrows():

            transcript_id = row["transcript_id"]
            conversation = row["conversation"]

            if transcript_id in used_ids:
                continue

            for turn in conversation:
                text = turn["text"]

                if term_lower in text.lower():

                    collected.append({
                        "transcript_id": transcript_id,
                        "speaker": turn["speaker"],
                        "text": text
                    })

                    used_ids.add(transcript_id)
                    break  # Only 1 snippet per transcript

            if len(collected) >= max_examples:
                break

        evidence_dict[term] = collected

    return evidence_dict
