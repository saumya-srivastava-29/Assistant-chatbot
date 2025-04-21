import importlib.util
import subprocess
import spacy

def get_nlp():
    # Auto-download the model if not available
    if not importlib.util.find_spec("en_core_web_sm"):
        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    return spacy.load("en_core_web_sm")
