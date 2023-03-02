import openai 
import random 
from sklearn.metrics import jaccard_score 
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
from api_key import api_key
# Personalized API key 
openai.api_key = api_key

# Input definition 
input_text = "The Black Lives Matter (BLM) movement is a social and political movement that advocates for the rights and equality of Black individuals. The movement began in 2013 after the acquittal of Trayvon Martin's killer and gained momentum in the wake of police killings of Black Americans such as Michael Brown, Tamir Rice, and Freddie Gray. BLM protests have taken place across the United States and around the world, calling for an end to systemic racism and police brutality, as well as for economic and political justice for Black people. The movement has also pushed for reforms in areas such as education, housing, and healthcare. In addition to protests and demonstrations, BLM activists have also used social media, art, and other forms of cultural expression to raise awareness about the movements goals and message."

#GPT-3 Engine & Parameters 
model_engine = "text-curie-001"
max_tokens = 1000
temperature = 0.5
top_p = 0.75
n = 4
    # Number of paraphrased texts generated 

# Paraphrased texts generation
paraphrased_texts = []
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


# Paraphrased texts generation
paraphrased_texts = []
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
    
    # Save the paraphrased text
    paraphrased_text = response.choices[0].text.strip()
    paraphrased_texts.append(paraphrased_text)
    print(f"Paraphrased text{i+1}: {paraphrased_text}")


# Tokenize the texts 
texts_tokens = [set(text.split()) for text in paraphrased_texts]

# Initialize an empty matrix to store the Jaccard similarity coefficients 
jaccard_coefficients = np.zeros((4,4))

# Compute the Jaccard similarity coefficient between all pairs of texts 
for i in range(4):
    for j in range(4):
        # Calculate the union of the sets of tokens 
        union = texts_tokens[i].union(texts_tokens[i])
       
        # Calculate the intersection of the sets of tokens 
        intersection = texts_tokens[i].intersection(texts_tokens[j])
        
        # Calculate the Jaccard similariy coefficients 
        jaccard_coefficients[i,j] = len(intersection)/len(union)
        

        jaccard_coefficients[i,j] = len(intersection)/len(union)

print(jaccard_coefficients)


# create a figure and axis 
fig, ax = plt.subplots()

# use the imshow function to display the matrix as an image 
cax = ax.imshow(jaccard_coefficients, cmap='YlGnBu', 
interpolation='nearest')

# add a colorbar 
fig.colorbar(cax)
 
# add x and y labels
ax.set_xticks(np.arange(4))
ax.set_yticks(np.arange(4))
ax.set_xticklabels(['txt1', 'txt2', 'txt3', 'txt4'])
ax.set_yticklabels(['txt1', 'txt2', 'txt3', 'txt4'])

# Add scores to the squares in the heatmap 
for i in range(len(paraphrased_texts)):
    for j in range(len(paraphrased_texts)):
        if i==j:
            score = 1.0  
            color = "white"
        else: 
            score = round(jaccard_coefficients[i,j], 4)
            color = "black"
        text = ax.text(j, i, score, ha="center", va="center", color=color)

# Show the plot 
plt.show()
