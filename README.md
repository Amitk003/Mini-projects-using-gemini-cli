# Made small projects using Gemini-CLI

This repository contains a collection of small Python projects developed with the assistance of the Gemini CLI. Each project demonstrates different functionalities and uses various libraries.

## Table of Contents
1.  [Currency Converter](#currency-converter)
2.  [Image to Sketch Converter](#image-to-sketch-converter)
3.  [Mystery Game](#mystery-game)
4.  [QR Generator](#qr-generator)
5.  [Quiz Game](#quiz-game)

---

## 1. Currency Converter

### Description
A simple web-based application that allows users to convert currency amounts between different denominations. It fetches real-time exchange rates to provide accurate conversions.

### How it was Made
This project was developed interactively with the Gemini CLI, which helped in setting up the Streamlit application structure and integrating the `forex-python` library for currency exchange rates.

### How to Run
1.  Navigate to the `Currency converter` directory:
    ```bash
    cd "Currency converter"
    ```
2.  Install the required Python packages:
    ```bash
    pip install -r currency_converter_requirements.txt
    ```
3.  Run the Streamlit application:
    ```bash
    streamlit run currency_converter_app.py
    ```
    This will open the application in your web browser.

---

## 2. Image to Sketch Converter

### Description
This project provides a web interface to convert any uploaded image into a pencil sketch effect. It uses image processing techniques to achieve the artistic transformation.

### How it was Made
The Gemini CLI assisted in building this application, particularly in integrating the Gradio library for the user interface and OpenCV for the image processing logic to create the sketch effect.

### How to Run
1.  Navigate to the `Image to Sketch Converter` directory:
    ```bash
    cd "Image to Sketch Converter"
    ```
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    python app.py
    ```
    This will start a local server and provide a URL to access the web interface in your browser.

---

## 3. Mystery Game

### Description
A classic text-based adventure game where players make choices that determine their path and outcome within a mysterious cave. It's a simple command-line interactive story.

### How it was Made
This game was crafted with the guidance of the Gemini CLI, focusing on Python's basic input/output functionalities to create a branching narrative experience.

### How to Run
1.  Navigate to the `Mystery game` directory:
    ```bash
    cd "Mystery game"
    ```
2.  Run the Python script directly:
    ```bash
    python mysterious_cave_corrected.py
    ```
    The game will run in your terminal.

---

## 4. QR Generator

### Description
A web-based tool that allows users to input text or a URL and instantly generate a QR code. The generated QR code can also be downloaded as an image.

### How it was Made
The Gemini CLI helped in setting up this Streamlit application, integrating the `qrcode` library for QR code generation and Pillow for image handling.

### How to Run
1.  Navigate to the `QR Generator` directory:
    ```bash
    cd "QR Generator"
    ```
2.  Install the required Python packages:
    ```bash
    pip install -r qr_code_generator_requirements.txt
    ```
3.  Run the Streamlit application:
    ```bash
    streamlit run qr_code_generator_app.py
    ```
    This will open the application in your web browser.

---

## 5. Quiz Game

### Description
A command-line quiz game that tests your knowledge with a set of multiple-choice questions. It also includes a basic leaderboard to track scores.

### How it was Made
This console application was developed with the assistance of the Gemini CLI, focusing on core Python concepts for game logic and file handling for the leaderboard.

### How to Run
1.  Navigate to the `Quiz game` directory:
    ```bash
    cd "Quiz game"
    ```
2.  Run the Python script directly:
    ```bash
    python quiz_game.py
    ```
    The quiz will run in your terminal.

---

## Getting Started with the Projects

To run any of these projects, you'll need Python installed on your system. It's recommended to use a virtual environment for each project to manage dependencies.

### General Setup Steps:

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd "small projects"
    ```
2.  **Navigate to the desired project directory** (e.g., `cd "Currency converter"`).
3.  **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
4.  **Install dependencies** (if a `requirements.txt` file exists in the project directory):
    ```bash
    pip install -r requirements.txt
    ```
5.  **Run the project** using the specific command mentioned in each project's section above.

Enjoy exploring these small projects!
