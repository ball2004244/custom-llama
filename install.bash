# This file installs codellama llm model

curl -X POST -H "Content-Type: application/json" -d '{
    "name": "codellama"
}' http://localhost:10000/api/pull
