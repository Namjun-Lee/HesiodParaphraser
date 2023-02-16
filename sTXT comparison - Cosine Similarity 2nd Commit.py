import numpy as np
import matplotlib.pyplot as plt

# Define five sample texts
texts = [
    "The Black Lives Matter (BLM) movement is a social and political movement that advocates for the rights and equality of Black individuals. The movement began in 2013 after the acquittal of Trayvon Martin's killer and gained momentum in the wake of police killings of Black Americans such as Michael Brown, Tamir Rice, and Freddie Gray. BLM protests have taken place across the United States and around the world, calling for an end to systemic racism and police brutality, as well as for economic and political justice for Black people. The movement has also pushed for reforms in areas such as education, housing, and healthcare. In addition to protests and demonstrations, BLM activists have also used social media, art, and other forms of cultural expression to raise awareness about the movement's goals and message.", 
    "The Black Lives Matter movement aims to promote the rights and equality of Black individuals by working to end systemic racism, police brutality and fighting for economic and political justice. It began in 2013 and gained momentum following the acquittal of Trayvon Martin's killer and the deaths of other Black Americans by police. Activists use various methods such as protests, social media, art and cultural expression to bring attention to the cause and also call for reforms in areas such as education, housing, and healthcare.", 
    "The Black Lives Matter movement advocates for the rights and equality of Black people, with a focus on ending systemic racism, police brutality and fighting for economic and political justice. The movement gained traction in 2013, particularly following the acquittal of Trayvon Martin's killer and the deaths of other Black Americans at the hands of police. Activists use various strategies to raise awareness, such as demonstrations, social media, art and cultural expression, and call for reforms in areas like education, housing, and healthcare.", 
    "The Black Lives Matter is a social movement that aims to bring attention to the issue of racial inequality and discrimination faced by Black people. It focuses on ending systemic racism, police brutality, and working towards economic and political justice for Black individuals. The movement gained significant attention in 2013, following the acquittal of Trayvon Martin's killer and the deaths of other Black Americans by police. Activists use various tactics, including protests, social media, art, and cultural expression, to raise awareness and push for reforms in areas such as education, housing, and healthcare.", 
    "The Black Lives Matter movement is a campaign that works to highlight and address the issue of racial inequality and discrimination faced by Black individuals. The movement aims to end systemic racism, police brutality, and push for economic and political justice for Black people. The movement gained significant public attention in 2013, following the acquittal of Trayvon Martin's killer and the deaths of other Black Americans by police. Activists employ a variety of methods, such as demonstrations, social media, art and cultural expression to bring attention to the cause and push for changes in areas like education, housing and healthcare."]

# Define a function to compute the cosine similarity between two vectors
def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

# Define a function to convert a text into a vector of word frequencies
def text_to_vector(text):
    words = text.split()
    vector = np.zeros(len(vocab))
    for word in words:
        if word in vocab:
            vector[vocab.index(word)] += 1
    return vector

# Create a vocabulary of all unique words in the texts
vocab = set(" ".join(texts).split())
vocab = list(vocab)

# Convert each text into a vector of word frequencies
vectors = [text_to_vector(text) for text in texts]

# Calculate the cosine similarity score between each pair of vectors
cos_sim_matrix = np.zeros((len(texts), len(texts)))
for i in range(len(texts)):
    for j in range(i, len(texts)):
        cos_sim = cosine_similarity(vectors[i], vectors[j])
        cos_sim_matrix[i,j] = cos_sim
        cos_sim_matrix[j,i] = cos_sim

# Plot the cosine similarity matrix as a heatmap
fig, ax = plt.subplots()
im = ax.imshow(cos_sim_matrix, cmap="YlGnBu")

# Add labels and a colorbar to the plot
ax.set_xticks(np.arange(len(texts)))
ax.set_yticks(np.arange(len(texts)))
ax.set_xticklabels(['txt1', 'txt2', 'txt3', 'txt4', 'txt5'])
ax.set_yticklabels(['txt1', 'txt2', 'txt3', 'txt4', 'txt5'])
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
cbar = ax.figure.colorbar(im, ax=ax)

# Add scores to the squares in the heatmap --> same texts == white; diff texts == black
for i in range(len(texts)):
    for j in range(len(texts)):
        if i == j:
            score = 1.0
            color = "white"
        else:
            score = round(cos_sim_matrix[i,j], 5)
            color = "black"
        text = ax.text(j, i, score, ha="center", va="center", color=color)
                     
# Show the plot
plt.show()

