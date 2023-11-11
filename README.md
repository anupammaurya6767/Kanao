# Kanao 📚

## Project Overview

Kanao is a project designed to train a GPT (Generative Pre-trained Transformer) model on custom datasets. It provides the capability to train the model using various data sources, including PDFs, Word documents, plain text files, and URLs.

## Features

- **Versatile Training**: Train the GPT model on diverse data types, including PDFs, Word documents, plain text files, and URLs.
- **Conversational AI**: Utilize the trained model for generating responses in a conversational manner.
- **Easy Integration**: Seamlessly integrate Kanao into your projects for natural language understanding and generation.

## Getting Started

To get started with Kanao, follow the installation instructions and examples in the [documentation](https://kanao-documentation.vercel.app/).

## Installation

```bash
pip install Kanao
```

## Usage

```python
from kanao.core.kanao import Kanao
open_ai_api_key = ""

# Initialize Kanao
kanao_instance = Kanao(open_ai_api_key)

# Train the model on custom data
kanao_instance.train_on_pdf('path/to/pdf/file.pdf')

# Generate a response
response_txt = kanao_instance.generate_response("What is in the document?")
```

For more detailed usage, refer to the [documentation](https://kanao-documentation.vercel.app/).

## Contribution

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
