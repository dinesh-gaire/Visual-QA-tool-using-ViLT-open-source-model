# Visual Question Answering Tool

This project implements a Visual Question Answering (VQA) tool using the Visual Language Transformer (ViLT) model. It provides both a Streamlit web application and a FastAPI backend to allow users to upload images and ask questions about them.

## Features

- Upload images and ask questions to receive answers.
- Utilizes the ViLT model for processing both visual and textual inputs.
- Built with FastAPI for the backend and Streamlit for the frontend.

## Installation

To get started, clone this repository and install the required dependencies.

### Requirements

Create a `requirements.txt` file with the following content:

```plaintext
transformers==4.45.2
torch==2.5.0
requests==2.32.3
pillow==10.4.0
fastapi==0.115.2
uvicorn==0.32.0
streamlit==1.39.0
python-multipart==0.0.13
```

## Setup
1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
2. **Create and activate a Conda virtual environment:**
    ```bash
    conda create --name vqa-env python=3.8
    conda activate vqa-env
3. **Install the requirements:**
    ```bash
    pip install -r requirements.txt

## Running the Application

### FastAPI Backend

To start the FastAPI server, run:

    uvicorn api:app --reload
    
The API will be available at ``http://127.0.0.1:8000``.

### Streamlit Frontend

To run the Streamlit application, execute:

    streamlit run app.py

The Streamlit app will be available at ``http://localhost:8501``.

## Usage

1. **Upload an Image:** Use the Streamlit app to upload an image.
2. **Ask a Question:** Enter a question related to the uploaded image.
3. **Get Answer:** Click the "Ask Question" button to receive an answer.

### Example Output

## API Endpoint
You can also interact with the VQA model via the FastAPI endpoint:

### POST /answer
* **Request Body:**
    
    * **image:** Image file (required)
    * **text:** Question text (optional)

* **Response:** A JSON object containing the answer.

### Example cURL Request

    curl -X POST "http://127.0.0.1:8000/answer" -F "image=@path/to/image.jpg" -F "text=What is in this image?"
    
## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
* Hugging Face Transformers
* FastAPI
* Streamlit