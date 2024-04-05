import torch.cuda
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import time
from env.environment_variables import APPCONFIG
from log.cj_logger import cj_logger


class AugmentedGenerator:

    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        cj_logger.info("self.device : {}".format(self.device))
        self.load_models()

    def load_models(self):

        cj_logger.info("Loading tokenizer...")
        self.load_tokenizer()
        cj_logger.info("Loaded tokenizer successfully...")

        cj_logger.info("Loading answer model...")
        self.load_rag_model()
        cj_logger.info("Loaded answer model successfully...")


        cj_logger.info("Loading addressing model...")
        self.load_addressing_model()
        cj_logger.info("Loaded addressing model successfully...")

    def load_tokenizer(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.tokenizer.pad_token = self.tokenizer.eos_token

    def load_rag_model(self):
        self.answer_model = GPT2LMHeadModel.from_pretrained(APPCONFIG.answer_generator_model_path).to(self.device)

    def load_addressing_model(self):
        pass

    @staticmethod
    def preprocess(arg):
        is_present = "<SOS>" in arg and "<EOS>" in arg

        if is_present:
            arg = arg.split("<SOS>")[-1].split("<EOS>")[0]

        return is_present, arg

    def predict(self, query, matching_docs):

        context = "\n\n".join(matching_docs[0:3])
        query = "context: " + context + "\nquestion: " + query + "\nAnswer the question based on the provided context"

        input_ids = self.tokenizer.encode(query, return_tensors='pt').to(self.device)

        # Generate the output sequence
        output = self.answer_model.generate(input_ids,
                                     max_length=1000,
                                     num_return_sequences=1,
                                     pad_token_id=self.tokenizer.eos_token_id)

        # Decode the generated output
        decoded_output = self.tokenizer.decode(output[0], skip_special_tokens=True)

        is_present, processed_output = self.preprocess(decoded_output)

        return processed_output


if __name__ == "__main__":

    query = "What is machine learning?"

    matching_docs =  [
        "Machine learning: Machine learning involves the use of algorithms and statistical models to enable computer systems to learn from and make predictions or decisions based on data. It encompasses various techniques, including supervised learning, unsupervised learning, and reinforcement learning.",
        "Machine learning algorithms: Machine learning algorithms are computational procedures used to learn patterns and make predictions from data. They include techniques such as decision trees, support vector machines, neural networks, and clustering algorithms.",
        "Machine Learning Engineer/ ML Engineer: Machine learning engineers develop and deploy machine learning models and systems that enable computers to perform tasks without explicit programming. They work on designing, implementing, and optimizing machine learning algorithms and models, often in collaboration with data scientists and software developers, to create intelligent solutions for various applications."
    ]

    generator = AugmentedGenerator()

    response = generator.predict(query=query,
                                 matching_docs=matching_docs)

    print("response : ",response)
