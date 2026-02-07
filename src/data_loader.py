# import json
# import pandas as pd
# def load_transcripts(json_path):
#     with open(json_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     records = []

#     for transcript in data["transcripts"]:
#         transcript_id = transcript["transcript_id"]
#         domain = transcript["domain"]
#         intent = transcript["intent"]

#         conversation_text = ""
#         for turn in transcript["conversation"]:
#             speaker = turn["speaker"]
#             text = turn["text"]
#             conversation_text += f"{speaker}: {text} "

#         records.append({
#             "transcript_id": transcript_id,
#             "domain": domain,
#             "intent": intent,
#             "full_text": conversation_text.strip()
#         })

#     df = pd.DataFrame(records)
#     return df


# import json
# import pandas as pd
# def load_transcripts(json_path):
#     with open(json_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     records = []

#     for transcript in data["transcripts"]:
#         transcript_id = transcript["transcript_id"]
#         domain = transcript["domain"]
#         intent = transcript["intent"]

#         conversation = transcript["conversation"]

#         records.append({
#             "transcript_id": transcript_id,
#             "domain": domain,
#             "intent": intent,
#             "conversation": conversation  # keep structured
#         })

#     df = pd.DataFrame(records)
#     return df



#FINAL
import json
import pandas as pd


def load_transcripts(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    records = []

    for transcript in data["transcripts"]:
        records.append({
            "transcript_id": transcript["transcript_id"],
            "domain": transcript["domain"],
            "intent": transcript["intent"],
            "conversation": transcript["conversation"]
        })

    df = pd.DataFrame(records)
    return df
