# Hands Off Coding 🎙️💻

A minimal, browser-based Speech-to-Text interface designed to support voice-driven development workflows. This project provides a clean dual-panel UI where spoken input is captured via microphone and sent to a backend API for transcription and further processing (e.g., speech-to-code pipelines).

# Overview
Hands Off Coding demonstrates the foundation of a modern AI-assisted coding interface:
Frontend captures live audio using the Web MediaRecorder API
Audio is sent to a backend endpoint (/transcribe)
Transcribed text is displayed instantly in the UI
Architecture is compatible with AI models such as OpenAI Whisper
This makes it suitable for experimentation with:
Voice-based coding assistants
AI-powered productivity tools
Accessibility-driven developer interfaces
NLP and speech-processing projects

# Features

- Real-time microphone recording (browser-native MediaRecorder)
- Automatic audio upload to backend (POST /transcribe)
- Dual-panel editor layout
- Left: Speech-to-text output
- Right: Generated code output (extendable)
- Responsive UI built with Bootstrap 5
- Flask/Jinja-ready template structure
- Clean, minimal, extensible architecture

Tech Stack
# Frontend
HTML5
CSS
Bootstrap 5.3
Vanilla JavaScript
MediaRecorder API
# Backend (Expected Integration)
Python (Flask)
Whisper or any Speech-to-Text model
REST API endpoint: /transcribe
