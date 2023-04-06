from parrot import Parrot 
import torch 
import warnings 
warnings.filterwarnings("ignore")

def random_state(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

random_state(1234)

parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

phrases = [""]

for phrase in phrases:
    print("-"*100)
    print("Input_phrase", phrase)
    print("-"*100)
    para_phrases = parrot.augment(input_paraphrase=phrase, 
                                  use_gpu=False, 
                                  do_diverse=True, 
                                  max_return_phrases=1, 
                                  max_length=2048,
                                  adequacy_threshold=0.5,
                                  fluency_threshold=0.5)
    
    if para_phrases is not None: 
        for para_phrase in para_phrases:
            print(para_phrase)
    else:
        print("No paraphrases found:", para_phrases)