import numpy as np
import matplotlib.pyplot as plt 
from sklearn.metrics import jaccard_score
import pandas as pd 
import seaborn as sns 

# Define the texts 
# Text_1 = prompt-specific AI generated txt 
# Text_2 - Text_4 = AI generated-paraphrased txt (prompt-specific)
# Text_5 = prompt-specific student generated txt 
texts = [
    "The Black Lives Matter (BLM) movement is a social and political movement that advocates for the rights and equality of Black individuals. The movement began in 2013 after the acquittal of Trayvon Martin's killer and gained momentum in the wake of police killings of Black Americans such as Michael Brown, Tamir Rice, and Freddie Gray. BLM protests have taken place across the United States and around the world, calling for an end to systemic racism and police brutality, as well as for economic and political justice for Black people. The movement has also pushed for reforms in areas such as education, housing, and healthcare. In addition to protests and demonstrations, BLM activists have also used social media, art, and other forms of cultural expression to raise awareness about the movement's goals and message.", 
    "The Black Lives Matter movement aims to promote the rights and equality of Black individuals by working to end systemic racism, police brutality and fighting for economic and political justice. It began in 2013 and gained momentum following the acquittal of Trayvon Martin's killer and the deaths of other Black Americans by police. Activists use various methods such as protests, social media, art and cultural expression to bring attention to the cause and also call for reforms in areas such as education, housing, and healthcare.", 
    "The Black Lives Matter movement advocates for the rights and equality of Black people, with a focus on ending systemic racism, police brutality and fighting for economic and political justice. The movement gained traction in 2013, particularly following the acquittal of Trayvon Martin's killer and the deaths of other Black Americans at the hands of police. Activists use various strategies to raise awareness, such as demonstrations, social media, art and cultural expression, and call for reforms in areas like education, housing, and healthcare.", 
    "The Black Lives Matter is a social movement that aims to bring attention to the issue of racial inequality and discrimination faced by Black people. It focuses on ending systemic racism, police brutality, and working towards economic and political justice for Black individuals. The movement gained significant attention in 2013, following the acquittal of Trayvon Martin's killer and the deaths of other Black Americans by police. Activists use various tactics, including protests, social media, art, and cultural expression, to raise awareness and push for reforms in areas such as education, housing, and healthcare.", 
    "The Black Lives Matter movement is a campaign that works to highlight and address the issue of racial inequality and discrimination faced by Black individuals. The movement aims to end systemic racism, police brutality, and push for economic and political justice for Black people. The movement gained significant public attention in 2013, following the acquittal of Trayvon Martin's killer and the deaths of other Black Americans by police. Activists employ a variety of methods, such as demonstrations, social media, art and cultural expression to bring attention to the cause and push for changes in areas like education, housing and healthcare."]

# Tokenize the texts 
texts_tokens = [set(text.split()) for text in texts]

# Initialize an empty matrix to store the Jaccard similarity coefficients 
jaccard_coefficients = np.zeros((5,5))

# Compute the Jaccard similarity coefficient between all pairs of texts 
for i in range(5):
    for j in range(5):
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
ax.set_xticks(np.arange(5))
ax.set_yticks(np.arange(5))
ax.set_xticklabels(['txt1', 'txt2', 'txt3', 'txt4', 'txt5'])
ax.set_yticklabels(['txt1', 'txt2', 'txt3', 'txt4', 'txt5'])

# Add scores to the squares in the heatmap 
for i in range(len(texts)):
    for j in range(len(texts)):
        if i==j:
            score = 1.0
            color = "white"
        else: 
            score = round(jaccard_coefficients[i,j], 5)
            color = "black"
        text = ax.text(j, i, score, ha="center", va="center", color=color)

# Show the plot 
plt.show()


