# AI Health Coach - Streamlit Deployment

This project demonstrates fine-tuning and deployment of an AI health coach model.

## Fine-tuned Model
- Model: [SudhinK/AI-Health-Coach](https://huggingface.co/SudhinK/AI-Health-Coach)

## Deployment
- Built a Streamlit web app to interact with the model.
- Containerized the app using Docker.

## Run Locally
```bash
docker build -t AIHealthCoach .
docker run -p 8501:8501 AIHealthCoach
