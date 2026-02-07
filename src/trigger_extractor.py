# def extract_trigger_text(df, target_outcome, num_turns=6, customer_only=True):
#     positive_texts = []
#     negative_texts = []

#     for _, row in df.iterrows():
#         transcript_intent = row["intent"]
#         conversation = row["conversation"]

#         selected_turns = conversation[:num_turns]

#         combined_text = ""

#         for turn in selected_turns:
#             if customer_only:
#                 if turn["speaker"] == "Customer":
#                     combined_text += turn["text"] + " "
#             else:
#                 combined_text += turn["text"] + " "

#         if transcript_intent == target_outcome:
#             positive_texts.append(combined_text.strip())
#         else:
#             negative_texts.append(combined_text.strip())

#     return positive_texts, negative_texts



#FINAL

def extract_trigger_text(df, target_outcome, num_turns=6, customer_only=True):

    positive_texts = []
    negative_texts = []

    for _, row in df.iterrows():
        transcript_intent = row["intent"]
        conversation = row["conversation"]

        selected_turns = conversation[:num_turns]

        combined_text = ""

        for turn in selected_turns:
            if customer_only:
                if turn["speaker"] == "Customer":
                    combined_text += turn["text"] + " "
            else:
                combined_text += turn["text"] + " "

        if transcript_intent == target_outcome:
            positive_texts.append(combined_text.strip())
        else:
            negative_texts.append(combined_text.strip())

    return positive_texts, negative_texts
