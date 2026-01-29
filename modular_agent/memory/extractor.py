import re

def extract_user_facts(text: str):
    """
    Extracts explicit user facts from input text.
    Returns a list of (key, value, confidence).
    """
    facts = []

    text = text.lower().strip()
    text = re.sub(r"([.,!])", r"\1", text)
    stop_pattern = r"(?=\s+(?:and|but|i live|i am|i work|located|my name)|$)"
    
    # Pattern: "my name is X"
    match = re.search(r"\b(my name is|i am|call me) ([a-zA-Z ]+?)" + stop_pattern, text)
    if match:
        name = match.group(2).strip().title()
        if name not in ["happy","sad","angry","excited","ready","okay","fine","good"]: 
            facts.append({
                "type": "user_profile",
                "key": "name",
                "value": name,
                "confidence": 0.95,
                "source": "explicit_user_statement"
            })

    # Location
    
    loc_pattern = re.search(r"\b(i live in|i am from|located in) ([a-z ]+?)" + stop_pattern, text)
    if loc_pattern:
        location = loc_pattern.group(2).strip().title()
        facts.append({
            "type": "user_profile",
            "key": "location",
            "value": location,
            "confidence": 0.85,
            "source": "explicit"
        })
    
    #profession
    job_pattern = re.search(r"\b(i work as a|i am a) ([a-z ]+?)" + stop_pattern, text)
    if job_pattern:
        job = job_pattern.group(2).strip().title()
        facts.append({
            "type": "user_profile",
            "key": "job",
            "value": job,
            "confidence": 0.85,
            "source": "explicit"
        })
    
    #preference
    like_pattern = re.search(r"\b(i like|i love|i enjoy) ([a-z0-9 ]+?)" + stop_pattern, text)
    if like_pattern:
        preference = like_pattern.group(2).strip()
        facts.append({
            "type": "user_preferences", # Note the plural type
            "key": "likes",
            "value": preference,
            "confidence": 0.80,
            "source": "explicit"
        })

    return facts