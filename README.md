# classification-with-evaluation-by-OpenAI-API-MLFlow
Classification with softmax probs output for the specific class you defined

For a detailed demonstration, please go to this link :
https://medium.com/@miltonchan_85581/prompt-engineering-for-classification-with-evaluation-by-openai-api-mlflow-c14b114d2433

# Challenges you will meet
1. LLMs do not provide explicit softmax probabilities for the defined classes
2. Prompt history & versioning problem

# Overcoming challenges with MLOps practice
MLOps tools provide structured ways to manage and track experiments, maintain version control of models and prompts, and offer insights into model confidence and performance.
- Dealing with Random Outputs: Prompt Engineering for Consistent Results

Using a specific prompt template/style which only outputs defined-class label in the response

- Understanding Model Confidence: Incorporating Softmax Probability

Assessing how confident the model is in its predictions with softmax probabilities helps quantify the model’s confidence in its predictions

- Maintaining Prompt History: Establishing an Evaluation Repository

An evaluation repository serves as a centralized place to store and track all prompts and their performance metrics over time. This allows you to maintain a historical record of what works best, ensuring valuable insights are preserved and accessible for future use.

- Tracking Prompt Experiments: Leveraging MLFlow for Experiment Management

 By using MLFlow, you can log and track the performance of different prompts, keep detailed records of experiments, and easily compare results across different versions.




