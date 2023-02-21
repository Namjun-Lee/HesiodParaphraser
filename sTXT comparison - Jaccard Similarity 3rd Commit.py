import numpy as np
import matplotlib.pyplot as plt 
from sklearn.metrics import jaccard_score
import pandas as pd 
import seaborn as sns 

# Define the texts 
# Text_1 = prompt-specific AI generated txt 
# Text_2 - Text_4 = AI generated-paraphrased txt (prompt-specific)
# Text_5 = prompt-specific student generated txt 
texts = ["Series Description: Axial PD-T2 TSE Acquisition Plane: SAGITTAL. As these mind-boggling terms invite me to the world of computational neuroscience, I - once again - prepare to indulge myself with the joy of interdisciplinary learning. From understanding the integrative functions of the nervous system to using technology to investigate theoretical analysis and abstractions of the brain, I strive to further my passion with an unwavering vision: supporting those with neurologic diseases to improve the human condition. And at Boston University, I see myself - alongside other intellectual risk-takers - developing a positive lasting impact on society. Interdisciplinary collaboration. This is what ultimately makes Boston University unique - a school whose community cultivates academic freedom and the pursuit of discovery in motivating ways. A place where students encourage one another to find connections across different topics toward a shared goal. Yet, there is so much more that allows aspiring students to foster independent learning through targeted access to professional skills. Among extensive undergraduate research opportunities that enable students to improve their analytic approaches to problems and gain industry-specific experience, I hope to work with Professor Myriam Abdennadher, whose research team focuses on neuroimaging of epilepsy through MRI data analysis. As her research builds off of my internship experience at BUSM, in which I summarized MRI data from ADNI using neuroimage processing software to build computational models, I hope to expand my understanding of the clinical application of computational neuroscience.At Boston University, those baffling terms will no longer be incomprehensible to me", 
"Series Description: Axial PD-T2 TSE can be restated as The series is described as Axial PD-T2 TSEindicating that the specific type of imaging being referred to is Axial PD-T2 TSE.The author expresses a keen interest in the interdisciplinary study of computational neuroscience with the aim of supporting those with neurologic diseases. They hope to attend Boston University and take advantage of the opportunities for independent learning, academic freedom and research. They view interdisciplinary collaboration as a hallmark of the school, where students work together to find connections across different fields. The author hopes to work with Professor Myriam Abdennadher, whose research team specializes in neuroimaging of epilepsy using MRI data analysis, building on the author's prior experience working with neuroimage processing software during an internship at BUSM. Ultimately, the author hopes to expand their understanding of the clinical applications of computational neuroscience and make sense of the technical terms they previously found incomprehensible.", 
"the text, the statement Series Description: Axial PD-T2 TSE is describing the specific imaging series as Axial PD-T2 TSE. The writer is interested in the interdisciplinary field of computational neuroscience and its role in supporting those with neurological diseases. They plan to attend Boston University, a school that promotes academic freedom, interdisciplinary collaboration and independent learning. They are eager to work with Professor Myriam Abdennadher and her research team, who specialize in neuroimaging of epilepsy using MRI data analysis. The writer hopes to expand their knowledge of the clinical application of computational neuroscience by building on their experience in summarizing MRI data from ADNI using neuroimage processing software during an internship at BUSM. The writer's ultimate goal is to gain a deeper understanding of the complex technical terminology used in the field.", 
"The sentence Series Description: Axial PD-T2 TSE provides a description of the specific type of imaging being used, which is Axial PD-T2 TSE. The writer has a strong interest in the interdisciplinary field of computational neuroscience and hopes to use this field to aid people with neurological diseases. They intend to study at Boston University, which fosters academic freedom, interdisciplinary collaboration, and independent learning. Working with Professor Myriam Abdennadher and her team, who specialize in MRI data analysis for epilepsy neuroimaging, will enable the author to broaden their understanding of the clinical uses of computational neuroscience. Through their previous internship experience, where they utilized neuroimage processing software to analyze MRI data from ADNI, the author hopes to further their comprehension of this complex field. Ultimately, their aim is to make sense of the previously bewildering technical terminology.", 
"The phrase Series Description: Axial PD-T2 TSE refers to the specific type of imaging used, which is Axial PD-T2 TSE. The writer is enthusiastic about the interdisciplinary domain of computational neuroscience and intends to use it to help people with neurological disorders. They have plans to enroll at Boston University, a place that prioritizes academic freedom, collaborative work, and self-directed education. By collaborating with Professor Myriam Abdennadher and her team, who specialize in the use of MRI data analysis for epilepsy neuroimaging, the writer hopes to expand their understanding of the clinical applications of computational neuroscience. They anticipate that their prior internship experience analyzing MRI data from ADNI using neuroimage processing software will be a useful foundation for this work. The writer's ultimate goal is to gain a more comprehensive understanding of the complex technical language used in this field."]

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


