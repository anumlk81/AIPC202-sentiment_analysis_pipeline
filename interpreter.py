# interpreter.py

from textblob import TextBlob
import csv

class Interpreter:
    def __init__(self):
        self.model = None
        self.vector = None
        self.results = []
        self.dataset = []       # holds loaded csv rows

    # --- Load Command ---
    def load(self, target):
        if target == "model":
            self.model = TextBlob
            print("[Interpreter] Model loaded successfully.")

        elif target == "vector":
            self.vector = lambda text: text.lower().split()
            print("[Interpreter] Vectorizer loaded successfully.")

        else:
            print(f"[Interpreter] Unknown target to load: {target}")

    # --- Save Command ---
    def save(self, target):
        if target == "model":
            print("[Interpreter] Model saved.")

        elif target == "results":
            if not self.results:
                print("[Interpreter] No results to save yet.")
                return

            with open("results.txt", "w") as f:
                # write header
                f.write(f"{'TEXT':<45} {'EXPECTED':<12} {'PREDICTED':<12} {'POLARITY':<10} {'MATCH'}\n")
                f.write("-" * 90 + "\n")

                correct = 0
                for r in self.results:
                    match = "YES" if r["expected"] == r["label"].lower() else "NO"
                    if match == "YES":
                        correct += 1
                    f.write(f"{r['text']:<45} {r['expected']:<12} {r['label']:<12} {str(r['polarity']):<10} {match}\n")

                # write summary at bottom
                accuracy = (correct / len(self.results)) * 100
                f.write("-" * 90 + "\n")
                f.write(f"Total: {len(self.results)} | Correct: {correct} | Accuracy: {accuracy:.1f}%\n")

            print(f"[Interpreter] Results saved to results.txt")

        else:
            print(f"[Interpreter] Unknown target to save: {target}")

    # --- Analyse a single piece of text ---
    def analyse_sentiment(self, text, expected=None):
        if self.model is None:
            print("[Interpreter] Error: no model loaded. Run 'load model' first.")
            return
        if self.vector is None:
            print("[Interpreter] Error: no vectorizer loaded. Run 'load vector' first.")
            return

        # step 1: vectorize
        tokens = self.vector(text)

        # step 2: run TextBlob
        blob = self.model(" ".join(tokens))
        polarity = blob.sentiment.polarity

        # step 3: map polarity to label
        if polarity > 0.1:
            label = "POSITIVE"
        elif polarity < -0.1:
            label = "NEGATIVE"
        else:
            label = "NEUTRAL"

        result = {
            "text": text,
            "tokens": tokens,
            "polarity": round(polarity, 4),
            "label": label,
            "expected": expected if expected else "unknown"
        }

        self.results.append(result)

        # print result with match check
        match = ""
        if expected:
            match = "✓" if expected == label.lower() else "✗"

        print(f"  Text     : {text}")
        print(f"  Polarity : {polarity}")
        print(f"  Predicted: {label}  |  Expected: {expected}  {match}")
        print()

        return result

    # --- Analyse entire CSV dataset ---
    def analyse_dataset(self, filepath):
        if self.model is None:
            print("[Interpreter] Error: no model loaded. Run 'load model' first.")
            return
        if self.vector is None:
            print("[Interpreter] Error: no vectorizer loaded. Run 'load vector' first.")
            return

        print(f"[Interpreter] Loading dataset from {filepath}...")
        print()

        try:
            with open(filepath, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)

            print(f"[Interpreter] Found {len(rows)} samples. Running analysis...\n")
            print("-" * 60)

            for row in rows:
                text = row["text"]
                expected = row["expected"]
                self.analyse_sentiment(text, expected)

            # print summary to console
            correct = sum(1 for r in self.results if r["expected"] == r["label"].lower())
            accuracy = (correct / len(self.results)) * 100
            print("-" * 60)
            print(f"[Interpreter] Total   : {len(self.results)}")
            print(f"[Interpreter] Correct : {correct}")
            print(f"[Interpreter] Accuracy: {accuracy:.1f}%")

        except FileNotFoundError:
            print(f"[Interpreter] Error: file '{filepath}' not found.")

    # --- Main Execute ---
    def execute(self, command):
        if command is None:
            print("[Interpreter] No result — check your input syntax.")
            return

        action = command[0]

        if action == "load":
            self.load(command[1])

        elif action == "save":
            self.save(command[1])

        elif action == "sentiment":
            self.analyse_sentiment(command[1])

        elif action == "analyse":
            self.analyse_dataset(command[1])

        else:
            print(f"[Interpreter] Unknown command: {command}")