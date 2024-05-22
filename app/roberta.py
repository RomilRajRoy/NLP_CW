import torch
from transformers import RobertaTokenizer, RobertaForTokenClassification

def load_model():
    model_path = "C:\\Users\\leona\\OneDrive - University of Surrey\\Documents\\University\\Masters\\Semester 2\\NLP COMM061\\Group Coursework\\ROBERTA-finetuned-NER\\checkpoint-4400"
    
    tokenizer = RobertaTokenizer.from_pretrained(model_path)
    model = RobertaForTokenClassification.from_pretrained(model_path)
    
    # Define label map according to your specific label encoding
    label_map = {0: 'B-O', 1: 'B-AC', 2: 'B-LF', 3: 'I-LF'}
    model.config.id2label = label_map
    
    return tokenizer, model

def predict(tokenizer, model, text):
    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    # Model predictions
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get predicted labels
    predictions = torch.argmax(outputs.logits, dim=-1).tolist()[0]
    
    # Convert input IDs to tokens
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
    
    # Map predictions to labels
    labels = [model.config.id2label[p] for p in predictions]
    
    # Filter out special tokens and join subword tokens
    results = []
    current_word = ""
    current_label = ""
    for token, label in zip(tokens, labels):
        if token in tokenizer.all_special_tokens:
            continue  # Skip special tokens
        if token.startswith("Ġ"):  # RoBERTa uses "Ġ" to signify new words
            if current_word:
                results.append((current_word, current_label))
            current_word = token[1:]  # Remove the "Ġ" prefix
            current_label = label
        else:
            current_word += token
            current_label = label
    if current_word:
        results.append((current_word, current_label))
    
    return results

# Only run this block if this file is executed directly
if __name__ == "__main__":
    tokenizer, model = load_model()
    
    text = input("Enter text: ")
    
    results = predict(tokenizer, model, text)
    
    print(results)
