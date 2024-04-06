import torch.cuda
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import time
from env.environment_variables import APPCONFIG
from log.cj_logger import cj_logger


class QuestionAddressingGenerator:
    def __init__(self, device="cpu"):

        if not device:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = "cpu"

        cj_logger.info("self.device : {}".format(self.device))
        self.load_models()

    def load_tokenizer(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.tokenizer.pad_token = self.tokenizer.eos_token

    def load_addressing_model(self):
        self.address_model = GPT2LMHeadModel.from_pretrained(APPCONFIG.addressing_generator_model_path).to(self.device)

    def load_models(self):

        cj_logger.info("Loading tokenizer...")
        self.load_tokenizer()
        cj_logger.info("Loaded tokenizer successfully...")

        cj_logger.info("Loading addressing model...")
        self.load_addressing_model()

        cj_logger.info("Loaded addressing model successfully...")

    def get_addressing_statement(self, query):
        cj_logger.info("Addressing model start")
        cj_logger.info("query : {}".format(query))
        input_ids = self.tokenizer.encode(query, return_tensors='pt').to(self.device)

        # Generate the output sequence
        output = self.address_model.generate(input_ids,
                                             max_length=1000,
                                             num_return_sequences=1,
                                             pad_token_id=self.tokenizer.eos_token_id)

        # Decode the generated output
        decoded_output = self.tokenizer.decode(output[0], skip_special_tokens=True)

        is_present, addressing_statement = self.preprocess(decoded_output)

        if not is_present:
            cj_logger.info("Using static addressing statement")
            cj_logger.info("decoded_output : {}".format(decoded_output))
            addressing_statement = "Here is the answer to what you have asked."

        return addressing_statement

    @staticmethod
    def preprocess(arg):
        is_present = "<SOS>" in arg and "<EOS>" in arg

        if is_present:
            arg = arg.split("<SOS>")[-1].split("<EOS>")[0]

        return is_present, arg


if __name__ == "__main__":
    query = "What is machine learning?"

    generator = QuestionAddressingGenerator(device="cuda")

    response = generator.get_addressing_statement(query=query)

    print("response : ", response)
