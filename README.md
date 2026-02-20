# voice_assisatance
Speech recognition is the process of turning spoken words into text. It is a key part of any voice assistant. In Python the SpeechRecognition module helps us do this by capturing audio and converting it to text. In this guide we’ll create a basic voice assistant using Python.
# 🎙️ Python Voice Assistant

> A lightweight, command-based Voice Assistant built using Python that performs automation tasks like Wikipedia search, opening websites, telling time, and generating jokes.

---

## 📌 Table of Contents

- [About The Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Installation Guide](#installation-guide)
- [Usage Instructions](#usage-instructions)
- [Supported Commands](#supported-commands)
- [Code Structure](#code-structure)
- [Error Handling](#error-handling)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

---

## 📖 About The Project

This project is a Python-based Voice Assistant that interacts with users through typed commands (simulating voice input).

It integrates multiple Python modules to provide features like:

- Wikipedia search
- Web browser automation
- Time reporting
- Joke generation
- Smart greeting system

The assistant is modular and beginner-friendly, making it easy to extend with new features.

---

## ✨ Features

✔ Time-based Greeting  
✔ Wikipedia Search (2 sentence summary)  
✔ Open YouTube  
✔ Open Google  
✔ Tell Current Time  
✔ Generate Random Jokes  
✔ Clean Exit Command  
✔ Exception Handling for Stability  

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python 3 | Core Programming Language |
| speech_recognition | Voice input handling (for future expansion) |
| pyttsx3 | Text-to-Speech Engine |
| wikipedia | Fetch Wikipedia summaries |
| webbrowser | Open URLs |
| datetime | Time-based greeting |
| pyjokes | Random joke generation |

---

## 🏗 Project Architecture

```
User Input
   ↓
Command Processing
   ↓
Condition Matching
   ↓
Task Execution
   ↓
Text-to-Speech Response
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install SpeechRecognition pyttsx3 wikipedia pyjokes
```

If you're using Windows and face audio issues:

```bash
pip install pypiwin32
```

---

## ▶️ Usage Instructions

Run the assistant:

```bash
python assistant.py
```

You will see:

```
Good Morning!
I am your voice assistant. How can I help you today?
```

Then type your command.

---

## 💬 Supported Commands

| Command Example | Action |
|-----------------|--------|
| wikipedia python | Searches Wikipedia |
| open youtube | Opens YouTube |
| open google | Opens Google |
| time | Tells current system time |
| joke | Tells a random joke |
| exit / bye | Stops the assistant |

---

## 📂 Code Structure

```
voice-assistant/
│
├── assistant.py
├── README.md
└── requirements.txt (optional)
```

### Core Functions

- `speak()` → Converts text to speech
- `wish_user()` → Greets based on current time
- `take_command()` → Accepts user input
- `run_assistant()` → Main program loop

---

## 🛡 Error Handling

The assistant includes:

- Wikipedia page error handling
- Disambiguation handling
- Empty input handling
- Safe joke fetching
- Graceful exit handling

---

## ⚠ Limitations

- Uses typed input instead of real microphone
- `pyttsx3` may not work in cloud environments like Google Colab
- Limited command recognition (basic string matching)

---

## 🚀 Future Enhancements

- 🎤 Real microphone input
- 🌦 Weather API integration
- 📁 Open local applications
- 🖥 System automation (shutdown, restart)
- 🧠 AI conversational capability
- 🪟 GUI using Tkinter or PyQt
- 🌐 Deployment as desktop application

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to branch
5. Open a Pull Request

---

## 👨‍💻 Author

**Harsh Thakur**  
Computer Engineering Student  
Jawaharlal Nehru Government Engineering College, Sundernagar  
Himachal Pradesh Technical University  

---

## 📜 License

This project is open-source and available under the MIT License.
