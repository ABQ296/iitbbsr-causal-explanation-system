# import pandas as pd
# from data_loader import load_transcripts
# from retrieval import detect_outcome_from_query
# from trigger_extractor import extract_trigger_text
# from factor_analysis import extract_top_factors_from_texts
# from evidence_extractor import extract_evidence
# from explanation_generator import generate_structured_explanation


# def print_friendly_output(result):

#     print("\n" + "=" * 90)
#     print(f"Query ID      : {result['query_id']}")
#     print(f"Category      : {result['query_category']}")
#     print(f"User Query    : {result['user_query']}")
#     print("=" * 90)

#     print("\nDetected Outcome Event:")
#     print(f"→ {result['outcome_event']}")

#     print("\nIdentified Causal Factors:\n")

#     if not result["causal_factors"]:
#         print("No strong causal factors identified.")
#     else:
#         for i, factor in enumerate(result["causal_factors"], 1):
#             print(f"{i}) {factor['factor'].replace('_', ' ').title()}")

#             if factor["supporting_evidence"]:
#                 print("   Supporting Evidence:")
#                 for ev in factor["supporting_evidence"]:
#                     print(f"   - (Transcript {ev['transcript_id']})")
#                     print(f"     \"{ev['text']}\"")
#             print()

#     print("Causal Explanation:")
#     print(result["causal_reasoning"])

#     print("=" * 90 + "\n")


# if __name__ == "__main__":

#     df = load_transcripts("../data/transcript.json")

#     queries_df = pd.read_csv("../data/queries.csv")

#     print("\nSystem Ready.")
#     print(f"Loaded {len(queries_df)} queries from CSV.\n")

#     for _, row in queries_df.iterrows():

#         query_id = row["query_id"]
#         query = row["query"]
#         category = row["category"]

#         detected_outcome = detect_outcome_from_query(
#             query,
#             df["intent"].unique()
#         )

#         if detected_outcome is None:
#             print(f"\nQuery ID {query_id}: Could not detect outcome.\n")
#             continue

#         positive_texts, negative_texts = extract_trigger_text(
#             df,
#             detected_outcome,
#             num_turns=6,
#             customer_only=True
#         )

#         top_terms = extract_top_factors_from_texts(
#             positive_texts,
#             negative_texts
#         )

#         evidence = extract_evidence(
#             df,
#             detected_outcome,
#             top_terms
#         )

#         structured_output = generate_structured_explanation(
#             detected_outcome,
#             top_terms,
#             evidence
#         )

#         structured_output["query_id"] = int(query_id)
#         structured_output["query_category"] = category
#         structured_output["user_query"] = query

#         print_friendly_output(structured_output)

#     print("All queries processed successfully.\n")



#FINAL
import os
import pandas as pd

from data_loader import load_transcripts
from retrieval import detect_outcome_from_query
from trigger_extractor import extract_trigger_text
from factor_analysis import extract_top_factors_from_texts
from evidence_extractor import extract_evidence
from explanation_generator import generate_structured_explanation

def infer_category(outcome_event):
    if outcome_event is None:
        return "Unknown"

    if "Fraud" in outcome_event:
        return "Fraud & Security"
    elif "Access" in outcome_event:
        return "Account & Authentication"
    elif "Delivery" in outcome_event:
        return "Logistics & Operations"
    elif "Escalation" in outcome_event:
        return "Customer Escalation"
    elif "Legal" in outcome_event:
        return "Legal & Compliance"
    else:
        return "General Service Issue"

def format_output_text(structured_output):

    lines = []
    lines.append(f"Outcome Event: {structured_output['outcome_event']}")
    lines.append("")

    lines.append("Causal Factors:")

    for factor in structured_output["causal_factors"]:
        lines.append(f"- {factor['factor']}")
        for ev in factor["supporting_evidence"]:
            lines.append(f"   (Transcript {ev['transcript_id']})")

    lines.append("")
    lines.append("Explanation:")
    lines.append(structured_output["causal_reasoning"])

    return "\n".join(lines)

def generate_remarks(outcome_event):

    if outcome_event is None:
        return "No domain Match"

    return (
        "Success"
    )

if __name__ == "__main__":

    print("\nInteractive Submission Mode (Auto-Overwrite Enabled)")
    print("Type 'exit' to stop.\n")

    df = load_transcripts("../data/transcript.json")

    os.makedirs("../outputs", exist_ok=True)

    output_path = "../outputs/submission_output.csv"

    pd.DataFrame(columns=[
        "Query Id",
        "Query",
        "Query Category",
        "System Output",
        "Remarks"
    ]).to_csv(output_path, index=False)

    query_id_counter = 1

    while True:

        query = input("Enter Query: ").strip()

        if query.lower() == "exit":
            print("\nSubmission file generated successfully.")
            print("Location: ../outputs/submission_output.csv\n")
            break

        detected_outcome = detect_outcome_from_query(
            query,
            df["intent"].unique()
        )

        if detected_outcome is None:
            print("This query does not match any known outcome event.\n")
            continue

        positive_texts, negative_texts = extract_trigger_text(
            df,
            detected_outcome,
            num_turns=6,
            customer_only=True
        )

        top_terms = extract_top_factors_from_texts(
            positive_texts,
            negative_texts,
            top_n=3
        )

        evidence = extract_evidence(
            df,
            detected_outcome,
            top_terms
        )

        structured_output = generate_structured_explanation(
            detected_outcome,
            top_terms,
            evidence
        )

        system_output_text = format_output_text(structured_output)

        print("\n" + "=" * 90)
        print(system_output_text)
        print("=" * 90 + "\n")

        category = infer_category(detected_outcome)

        remarks_text = generate_remarks(detected_outcome)

        new_row = {
            "Query Id": query_id_counter,
            "Query": query,
            "Query Category": category,
            "System Output": system_output_text,
            "Remarks": remarks_text
        }

        pd.DataFrame([new_row]).to_csv(
            output_path,
            mode="a",
            header=False,
            index=False
        )

        print(f"Processed Query ID {query_id_counter}\n")

        query_id_counter += 1
