import openai 
import random 
from sklearn.metrics import jaccard_score 

# Personalized API key 
openai.api_key = "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"

# Input definition 
input_text = "The Black Lives Matter (BLM) movement is a social and political movement that advocates for the rights and equality of Black individuals. The movement began in 2013 after the acquittal of Trayvon Martin's killer and gained momentum in the wake of police killings of Black Americans such as Michael Brown, Tamir Rice, and Freddie Gray. BLM protests have taken place across the United States and around the world, calling for an end to systemic racism and police brutality, as well as for economic and political justice for Black people. The movement has also pushed for reforms in areas such as education, housing, and healthcare. In addition to protests and demonstrations, BLM activists have also used social media, art, and other forms of cultural expression to raise awareness about the movements goals and message."

#GPT-3 Engine & Parameters 
model_engine = "text-davinci-003"
max_tokens = 1000
temperature = 0.5
top_p = 1.0
n = 4
    # Number of paraphrased texts generated 

# Paraphrased texts generation
for i in range (n):
     # Set up the prompt for the GPT-3 engine
    prompt = "Paraphrase the following sentence:\n\n" + input_text + "\n\nParaphrased sentence:"
    
    # Generate the paraphrased text
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Print the paraphrased text
    print(f"Paraphrased text{i+1}: {response.choices[0].text.strip()}")

