import re 
from collections import Counter 
import math 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 

def get_cosine_similarity(text1, text2):
        # Convert the text to lowercase and remove non-alphabetic characters 
        text1 = text1.lower().strip()
        text2 = text2.lower().strip()


        # Count the frequency of each word in both texts
        word_count1 = Counter(text1.split())
        word_count2 = Counter(text2.split())

        # Calculate the dot product of the two word frequency vectors 
        dot_product = sum(word_count1[word] * word_count2[word] for word in word_count1)

        # Calculate the magnitude of each word frequency vector 
        magnitude1 = math.sqrt(sum(word_count1[word] ** 2 for word in word_count1))
        magnitude2 = math.sqrt(sum(word_count2[word] ** 2 for word in word_count2))

        # Calculate the cosine similarity between the two word frequency vectors 
        cosine_similarity = dot_product / (magnitude1 * magnitude2)

        return cosine_similarity
        
    
# Define the texts 
text1= "The Black Lives Matter (BLM) movement is a social and political movement that advocates for the rights and equality of Black individuals. The movement began in 2013 after the acquittal of Trayvon Martin's killer and gained momentum in the wake of police killings of Black Americans such as Michael Brown, Tamir Rice, and Freddie Gray. BLM protests have taken place across the United States and around the world, calling for an end to systemic racism and police brutality, as well as for economic and political justice for Black people. The movement has also pushed for reforms in areas such as education, housing, and healthcare. In addition to protests and demonstrations, BLM activists have also used social media, art, and other forms of cultural expression to raise awareness about the movement's goals and message."
text2= "The Black Lives Matter movement aims to promote the rights and equality of Black individuals by working to end systemic racism, police brutality and fighting for economic and political justice. It began in 2013 and gained momentum following the acquittal of Trayvon Martin's killer and the deaths of other Black Americans by police. Activists use various methods such as protests, social media, art and cultural expression to bring attention to the cause and also call for reforms in areas such as education, housing, and healthcare."
text3= "The Black Lives Matter movement advocates for the rights and equality of Black people, with a focus on ending systemic racism, police brutality and fighting for economic and political justice. The movement gained traction in 2013, particularly following the acquittal of Trayvon Martin's killer and the deaths of other Black Americans at the hands of police. Activists use various strategies to raise awareness, such as demonstrations, social media, art and cultural expression, and call for reforms in areas like education, housing, and healthcare."
text4= "The Black Lives Matter is a social movement that aims to bring attention to the issue of racial inequality and discrimination faced by Black people. It focuses on ending systemic racism, police brutality, and working towards economic and political justice for Black individuals. The movement gained significant attention in 2013, following the acquittal of Trayvon Martin's killer and the deaths of other Black Americans by police. Activists use various tactics, including protests, social media, art, and cultural expression, to raise awareness and push for reforms in areas such as education, housing, and healthcare."
text5= "The Black Lives Matter movement is a campaign that works to highlight and address the issue of racial inequality and discrimination faced by Black individuals. The movement aims to end systemic racism, police brutality, and push for economic and political justice for Black people. The movement gained significant public attention in 2013, following the acquittal of Trayvon Martin's killer and the deaths of other Black Americans by police. Activists employ a variety of methods, such as demonstrations, social media, art and cultural expression to bring attention to the cause and push for changes in areas like education, housing and healthcare."

# Compute cosine similarity between txt1 and txt1
similarity_1_1 = get_cosine_similarity(text1, text1)

# Compute cosine similarity between txt1 and txt2
similarity_1_2 = get_cosine_similarity(text1, text2)

# Compute cosine similarity between txt1 and txt3
similarity_1_3 = get_cosine_similarity(text1, text3)

# Compute cosine similarity between txt1 and txt4
similarity_1_4 = get_cosine_similarity(text1, text4)

# Compute cosine similarity between txt1 and txt5
similarity_1_5 = get_cosine_similarity(text1, text5)

# Compute cosine similarity between txt2 and txt1
similarity_2_1 = get_cosine_similarity(text2, text1)

# Compute cosine similarity between txt2 and txt2
similarity_2_2 = get_cosine_similarity(text2, text2)

# Compute cosine similarity between txt2 and txt3
similarity_2_3 = get_cosine_similarity(text2, text3)

# Compute cosine similarity between txt2 and txt4
similarity_2_4 = get_cosine_similarity(text2, text4)

# Compute cosine similarity between txt2 and txt5
similarity_2_5 = get_cosine_similarity(text2, text5)

# Compute cosine similarity between txt3 and txt1
similarity_3_1 = get_cosine_similarity(text3, text1)

# Compute cosine similraity between txt3 and txt2
similarity_3_2 = get_cosine_similarity(text3, text2)

# Compute cosine similarity between txt3 and txt3
similarity_3_3 = get_cosine_similarity(text3, text3)

# Compute cosine similarity between txt3 and txt4
similarity_3_4 = get_cosine_similarity(text3, text4)

# Compute cosine similarity between txt3 and txt5
similarity_3_5 = get_cosine_similarity(text3, text5)

# Compute cosine similarity between txt4 and txt4
similarity_4_4 = get_cosine_similarity(text4, text4)

# Compute cosine similarity between txt4 and txt5
similarity_4_5 = get_cosine_similarity(text4, text5)

# Compute cosine similarity between txt5 and txt1
similarity_5_1
# Compute cosine similarity between txt5 and txt5
similarity_5_5 = get_cosine_similarity(text5, text5)

# Print the scores 
print(similarity_1_1, similarity_1_2, similarity_1_3, similarity_1_4, similarity_1_5, similarity_2_2, similarity_2_3, similarity_2_4, similarity_2_5, similarity_3_3, similarity_3_4, similarity_3_5, similarity_4_4, similarity_4_5, similarity_5_5)
