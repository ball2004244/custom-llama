# This file generates code from codellama llm model

curl -X POST http://localhost:10000/api/generate -d '{
    "model": "codellama",
    "prompt": "Write me a function that outputs the fibonacci sequence",
    "stream": false
}'