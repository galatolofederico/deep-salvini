from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline, GPT2Tokenizer
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--model", type=str, required=True)

args = parser.parse_args()

tokenizer = AutoTokenizer.from_pretrained(args.model)
model = AutoModelWithLMHead.from_pretrained(args.model)

text_generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
prompts = [
    "Buongiorno amici,",
    "Io credo che",
    "VERGOGNOSO gli italiani",
    "INCREDIBILE, la sinistra ha",
]


samples_outputs = text_generator(
    prompts,
    do_sample=True,
    max_length=50,
    top_k=50,
    top_p=0.95,
    num_return_sequences=3
)


for i, sample_outputs in enumerate(samples_outputs):
    print(100 * '-')
    print("Prompt:", prompts[i])
    for sample_output in sample_outputs:
        print("Sample:", sample_output['generated_text'].split("\n")[0])
        print()
