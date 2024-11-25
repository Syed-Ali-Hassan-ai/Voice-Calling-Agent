
# AI Calling Agent using Twilio and OpenAI

The **AI Calling Agent** is an innovative solution designed to automate both inbound and outbound calling processes, currently tailored as a mental health consultant. This project leverages cutting-edge technologies including Twilio for call handling, OpenAI for intelligent conversations, Pinecone for vector database services, and MongoDB for data persistence.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Features

- **Inbound and Outbound Calls:** Efficiently handles both incoming and outgoing calls using Twilio.
- **AI-Powered Conversations:** Integrates OpenAI to provide responsive and context-aware interactions.
- **Data Handling:** Utilizes MongoDB for robust data management and Pinecone for advanced querying capabilities.
- **Real-Time Response:** Employs Text-to-Speech (TTS) and Speech-to-Text (STT) technologies for real-time communication.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.x** installed on your machine.
- **Twilio Account:** Sign up for a Twilio account to obtain necessary API keys.
- **OpenAI API Key:** Obtain an API key from OpenAI.
- **Pinecone API Key:** Sign up for Pinecone to get an API key.
- **MongoDB:** Set up a MongoDB instance (local or cloud-based).
- **Environment Variables:** Create a `.env` file and fill it with your configuration details (API keys, database URIs, etc.).

## Installation

Follow these steps to get the project up and running on your local machine:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/ai-calling-agent.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd ai-calling-agent
   ```

3. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   - Create a `.env` file in the project's root directory.
   - Add your configuration details (API keys, database URIs) to the `.env` file.

5. **Run the application:**

   ```bash
   python app.py
   ```

## Usage

After starting the server, the application will be available at `http://localhost:5000/`. Use the following endpoints to interact with the AI Calling Agent:

- **GET /** - Test the connection and retrieve API status.
- **POST /voice** - Handle incoming calls.
- **GET /make_call?phone_number=+1234567890** - Initiate an outbound call to the specified number.
- **POST /handle_speech** - Process user speech from an ongoing call.

## Project Structure

```
ai-calling-agent/
├── app.py                # Flask application entry point
├── modules/              # Modular functionalities
│   ├── agent_tools.py
│   ├── chatbot.py
│   ├── mongodb.py
│   ├── sender.py
│   ├── tts.py
│   └── twilio_api.py
└── static/               # Static files directory
```

## Contributing

We welcome contributions from the community. To contribute:

1. **Fork the repository.**

2. **Create a feature branch:**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit your changes:**

   ```bash
   git commit -m 'Add your feature'
   ```

4. **Push to the branch:**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a pull request.**

## Contact

- **Syed Ali Hassan**
  - [LinkedIn](https://www.linkedin.com/in/ali-hassan-b71b2a245/)

## Acknowledgments

- Thanks to [Twilio](https://www.twilio.com/), [OpenAI](https://openai.com/), [Pinecone](https://www.pinecone.io/), and [MongoDB](https://www.mongodb.com/) for providing the technologies that power this project.
