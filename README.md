# 🎬 AI Video Assistant

An intelligent meeting assistant that transcribes, summarizes, and enables interactive Q&A with your video/audio content using AI.

## ✨ Features

- 🎙️ **Multi-language Transcription** - Supports 23+ Indian languages + English via Sarvam AI
- 📝 **Smart Summarization** - AI-powered meeting summaries using Mistral
- ✅ **Action Item Extraction** - Automatically identifies tasks and action items
- 🔑 **Key Decision Tracking** - Extracts important decisions made
- ❓ **Question Detection** - Identifies open questions and unresolved topics
- 💬 **RAG-powered Chat** - Ask questions about your meeting transcript
- 🌐 **YouTube Support** - Direct transcription from YouTube URLs
- 🎨 **Beautiful Web UI** - Modern Streamlit interface with dark theme

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r Requirements.txt
```

**Note:** FFmpeg must be installed separately:
- **macOS:** `brew install ffmpeg`
- **Ubuntu:** `sudo apt install ffmpeg`
- **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html)

### 2. Configure API Keys

Create/edit `.env` file:

```env
MISTRAL_API_KEY=your_mistral_key_here
SARVAM_API_KEY=your_sarvam_key_here
```

Get your API keys:
- **Mistral AI:** [console.mistral.ai](https://console.mistral.ai/)
- **Sarvam AI:** [sarvam.ai](https://www.sarvam.ai/)

### 3. Test Setup

```bash
python test_sarvam_api.py
```

### 4. Run Application

**Web UI (Recommended):**
```bash
streamlit run app.py
```

**CLI Mode:**
```bash
python main.py
```

## 📖 Usage

### Web Interface

1. Launch: `streamlit run app.py`
2. Open browser at `http://localhost:8501`
3. Enter YouTube URL or local file path
4. Select language (english, hindi, hinglish, etc.)
5. Click "⚡ Analyse"
6. View results and chat with your transcript

### Command Line

```bash
python main.py
```

Follow the prompts:
- Enter YouTube URL or file path
- Choose language
- View generated summary, action items, decisions, and questions
- Chat with your meeting transcript

## 🌍 Supported Languages

### All Languages (23+)
English, Hindi, Hinglish, Bengali, Tamil, Telugu, Kannada, Malayalam, Marathi, Gujarati, Punjabi, Odia, Assamese, Urdu, Nepali, Konkani, Kashmiri, Sindhi, Sanskrit, Santali, Manipuri, Bodo, Maithili, Dogri

### Language Codes
- `english` - English
- `hindi` - Hindi
- `hinglish` - Code-mixed Hindi-English
- `tamil` - Tamil
- `telugu` - Telugu
- `kannada` - Kannada
- `malayalam` - Malayalam
- `bengali` - Bengali
- `marathi` - Marathi
- `gujarati` - Gujarati
- `punjabi` - Punjabi
- `odia` - Odia

See `SARVAM_SETUP.md` for complete language list.

## 🔧 Advanced Configuration

Edit `.env` for advanced options:

```env
# Transcription Model (default: saaras:v3)
SARVAM_MODEL=saaras:v3

# Transcription Mode (default: transcribe)
# Options: transcribe, translate, verbatim, translit, codemix
SARVAM_MODE=transcribe
```

### Transcription Modes

- **transcribe** - Standard transcription with formatting
- **translate** - Translate to English
- **verbatim** - Word-for-word without normalization
- **translit** - Romanization to Latin script
- **codemix** - English in English, Indic in native script

## 📁 Project Structure

```
.
├── app.py                  # Streamlit web interface
├── main.py                 # CLI interface
├── core/
│   ├── transcriber.py      # Sarvam AI transcription
│   ├── summarizer.py       # Mistral summarization
│   ├── extractor.py        # Action items, decisions, questions
│   ├── rag_engine.py       # RAG chat functionality
│   └── vector_store.py     # Vector database
├── utils/
│   └── audio_processor.py  # Audio/video processing
├── Requirements.txt        # Python dependencies
├── .env                    # API keys (create this)
├── README.md              # This file
└── SARVAM_SETUP.md        # Detailed Sarvam AI guide
```

## 🧪 Testing

### Basic Test
```bash
python test_sarvam_api.py
```

### Full Pipeline Test
```bash
# Test with YouTube video
python main.py
# Enter: https://www.youtube.com/watch?v=YOUR_VIDEO_ID
# Language: english

# Test with local file
python main.py
# Enter: /path/to/your/audio.mp3
# Language: hindi
```

See `SARVAM_SETUP.md` for comprehensive testing instructions.

## 🐛 Troubleshooting

### Common Issues

**"SARVAM_API_KEY is not set"**
- Check `.env` file exists in project root
- Verify API key is correct
- No spaces around the `=` sign

**"FFmpeg not found"**
- Install FFmpeg: `brew install ffmpeg` (macOS)
- Verify: `ffmpeg -version`

**"403 Forbidden" from Sarvam API**
- Invalid API key
- Check your Sarvam AI account status

**Poor transcription quality**
- Ensure clear audio (minimal background noise)
- Try different models: `SARVAM_MODEL=saaras:v3`
- Use 16kHz sample rate for best results

See `SARVAM_SETUP.md` for detailed troubleshooting.

## 📊 API Limits

- **Sarvam REST API:** Up to 30 seconds per request
- **Auto-chunking:** Longer audio automatically split into 25s pieces
- **Batch API:** For longer files, see [Sarvam Batch API](https://docs.sarvam.ai/api-reference-docs/api-guides-tutorials/speech-to-text/batch-api)

## 🔗 Resources

- [Sarvam AI Documentation](https://docs.sarvam.ai/)
- [Mistral AI Documentation](https://docs.mistral.ai/)
- [Streamlit Documentation](https://docs.streamlit.io/)

## 📝 License

This project uses:
- **Sarvam AI** for speech-to-text transcription
- **Mistral AI** for summarization and extraction
- **LangChain** for RAG orchestration
- **ChromaDB** for vector storage

## 🎉 Why Sarvam AI?

✅ **No heavy model downloads** (saves 1-3GB)  
✅ **No GPU required** (cloud-based processing)  
✅ **Better Indian language support** (23+ languages)  
✅ **Faster transcription** (parallel cloud processing)  
✅ **Multiple output modes** (translate, translit, codemix)  
✅ **Automatic language detection**  
✅ **Regular model updates**  

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 💡 Tips

1. Use **saaras:v3** model for best accuracy
2. Set language to **"unknown"** for auto-detection
3. Use **"codemix"** mode for Hinglish content
4. **16kHz WAV files** work best
5. Check **pricing** before heavy usage

## 📧 Support

For issues:
1. Check `SARVAM_SETUP.md` for detailed guides
2. Run `python test_sarvam_api.py` to diagnose
3. Review error messages carefully
4. Check API quotas and limits

---

Made with ❤️ using Sarvam AI, Mistral AI, and LangChain
