import os
import requests
from pydub import AudioSegment

# Sarvam's REST API rejects audio longer than 30s.
# We slice each chunk into 25s pieces (with a 5s safety margin) before sending.
SARVAM_PIECE_SECONDS = 25

# Sarvam AI Configuration
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")
SARVAM_STT_URL = "https://api.sarvam.ai/speech-to-text"
SARVAM_MODEL = os.getenv("SARVAM_MODEL", "saaras:v3")
SARVAM_MODE = os.getenv("SARVAM_MODE", "transcribe")


def _send_to_sarvam(piece_path: str, language_code: str = "en-IN", mode: str = "transcribe") -> str:
    """
    Send one ≤30s audio file to Sarvam AI and return the transcript.
    
    Args:
        piece_path: Path to audio file
        language_code: BCP-47 language code (e.g., 'en-IN', 'hi-IN', 'unknown')
        mode: Operation mode - 'transcribe', 'translate', 'verbatim', 'translit', 'codemix'
    
    Returns:
        Transcribed text
    """
    if not SARVAM_API_KEY:
        raise RuntimeError("SARVAM_API_KEY is not set in environment / .env")

    headers = {"api-subscription-key": SARVAM_API_KEY}

    with open(piece_path, "rb") as f:
        files = {"file": (os.path.basename(piece_path), f, "audio/wav")}
        data = {
            "model": SARVAM_MODEL,
            "language_code": language_code,
            "mode": mode
        }
        response = requests.post(
            SARVAM_STT_URL,
            headers=headers,
            files=files,
            data=data,
            timeout=120,
        )

    if not response.ok:
        print(f"\n❌ Sarvam AI returned {response.status_code}")
        print(f"Response body: {response.text}\n")
        response.raise_for_status()

    result = response.json()
    return result.get("transcript", "")


def transcribe_chunk_sarvam(chunk_path: str, language: str = "english") -> str:
    """
    Transcribe audio chunk using Sarvam AI.
    Sarvam REST API only accepts ≤30s audio. We split this chunk into
    25-second pieces, send each separately, and join the transcripts.
    
    Args:
        chunk_path: Path to audio chunk
        language: 'english', 'hindi', 'hinglish', or other supported languages
    
    Returns:
        Full transcribed text
    """
    # Map language to Sarvam language codes and modes
    language_map = {
        "english": ("en-IN", "transcribe"),
        "hindi": ("hi-IN", "transcribe"),
        "hinglish": ("unknown", "codemix"),  # Auto-detect with code-mixed output
        "tamil": ("ta-IN", "transcribe"),
        "telugu": ("te-IN", "transcribe"),
        "kannada": ("kn-IN", "transcribe"),
        "malayalam": ("ml-IN", "transcribe"),
        "bengali": ("bn-IN", "transcribe"),
        "marathi": ("mr-IN", "transcribe"),
        "gujarati": ("gu-IN", "transcribe"),
        "punjabi": ("pa-IN", "transcribe"),
        "odia": ("od-IN", "transcribe"),
    }
    
    language_code, mode = language_map.get(language.lower(), ("unknown", "transcribe"))
    
    # Override with env variable if set
    if SARVAM_MODE:
        mode = SARVAM_MODE

    audio = AudioSegment.from_wav(chunk_path)
    piece_ms = SARVAM_PIECE_SECONDS * 1000

    full_text = ""
    total_pieces = (len(audio) + piece_ms - 1) // piece_ms

    for i, start in enumerate(range(0, len(audio), piece_ms)):
        piece = audio[start: start + piece_ms]
        piece_path = f"{chunk_path}_sv_{i}.wav"
        piece.export(piece_path, format="wav")

        try:
            print(f"  → Sarvam AI piece {i + 1}/{total_pieces} ({language_code}, {mode})...")
            full_text += _send_to_sarvam(piece_path, language_code, mode) + " "
        finally:
            if os.path.exists(piece_path):
                os.remove(piece_path)

    return full_text.strip()


def transcribe_chunk(chunk_path: str, language: str = "english") -> str:
    """
    Transcribe one audio chunk using Sarvam AI.
    
    Args:
        chunk_path: Path to audio chunk
        language: Language of the audio
    
    Returns:
        Transcribed text
    """
    return transcribe_chunk_sarvam(chunk_path, language)


def transcribe_all(chunks: list, language: str = "english") -> str:
    """
    Transcribe all audio chunks using Sarvam AI.
    
    Args:
        chunks: List of audio chunk file paths
        language: Language of the audio
    
    Returns:
        Complete transcript
    """
    full_transcript = ""
    
    print(f"Using Sarvam AI for transcription (Language: {language}).")

    for i, chunk in enumerate(chunks):
        print(f"Transcribing chunk {i + 1}/{len(chunks)}...")
        text = transcribe_chunk(chunk, language=language)
        full_transcript += text + " "

    print("Transcription complete.")
    return full_transcript.strip()  
