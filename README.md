# Custom Llama
This project host multiple instace of LLama large language model from Meta. 

We are using LLama 7B in Docker and use Kubernetes to manage the cluster.

We also supply a lightweight web server to communicate with the cluster.

## How to run
### Prerequisite
- Docker
- Kubernetes
- LLama 7B docker image

### Run
1. Build the docker image
```bash
docker run -d -p 11434:11434 -v ollama:/usr/.ollama --name my-ollama ollama:latest
```

2. Run the web server
```bash
python3 main.py
```

3. Write custom CURL
Check Ollama doc/api.md for more information

## Contributors
- Jack Nguyen - @ball2004244