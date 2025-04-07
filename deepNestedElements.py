import argparse
from wonderwords import RandomWord

def generate_paragraph(word_count=400):
    rw = RandomWord()
    words = [rw.word(include_parts_of_speech=["nouns", "verbs", "adjectives"]) for _ in range(word_count)]
    # Capitalize first word and add periods every 10-15 words
    sentences = []
    i = 0
    while i < len(words):
        sentence_length = min(len(words) - i, 10 + i % 5)  # vary sentence length
        sentence = " ".join(words[i:i + sentence_length]).capitalize() + "."
        sentences.append(sentence)
        i += sentence_length
    return " ".join(sentences)

def generate_deep_nesting(depth=10, indent_size=2):
    lines = []
    indent = lambda level: " " * (level * indent_size)

    lines.append("<html>")
    lines.append(indent(1) + "<body>")

    for i in range(depth):
        lines.append(indent(2 + i) + f"<p id='nested-{i}'>")
        paragraph = generate_paragraph()
        paragraph_lines = paragraph.split(". ")
        for line in paragraph_lines:
            if line.strip():
                lines.append(indent(3 + i) + line.strip() + ('.' if not line.endswith('.') else ''))
        lines.append(indent(2 + i) + "</p>")

    lines.append(indent(1) + "</body>")
    lines.append("</html>")

    return "\n".join(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate deeply nested HTML with random 400-word paragraphs using <p> tags.")
    parser.add_argument(
        "--depth",
        type=int,
        default=3,
        help="Number of nested <p> levels (default: 3)"
    )
    args = parser.parse_args()

    html_output = generate_deep_nesting(depth=args.depth)
    print(html_output)
