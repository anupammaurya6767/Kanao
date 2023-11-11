# Kavy 📚

## Why Kavy?

The choice of the name "Kavy" reflects the poetic nature of the project. It aims to bring a sense of creativity and expression, much like the art of poetry. In the world of natural language processing and conversational AI, the goal is to create beautifully coherent and contextually aware responses—akin to the elegance found in poetry.

## Project Overview

Kavy is a project designed to train a GPT (Generative Pre-trained Transformer) model on custom datasets. It provides the capability to train the model using various data sources, including PDFs, Word documents, plain text files, and URLs.

## Features

- **Versatile Training**: Train the GPT model on diverse data types, including PDFs, Word documents, plain text files, and URLs.
- **Conversational AI**: Utilize the trained model for generating responses in a conversational manner.
- **Easy Integration**: Seamlessly integrate Kavy into your projects for natural language understanding and generation.

## Getting Started

To get started with Kavy, follow the installation instructions and examples in the [documentation](link-to-documentation).

## Installation

```bash
pip install Kavy
```

## Usage

```python
from kavy.core.kavy import Kavy
open_ai_api_key = ""

# Initialize Kavy
Kavy_instance = Kavy(open_ai_api_key)

# Train the model on custom data
kavy_instance.train_on_pdf('path/to/pdf/file.pdf')

# Generate a response
response_txt = kavy_instance.generate_response("What is in the document?")
```

For more detailed usage, refer to the [documentation](link-to-documentation).

## Contribution

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
