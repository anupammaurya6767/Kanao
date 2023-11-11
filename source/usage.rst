Usage
=====

from Kanao.core.Kanao import Kanao
open_ai_api_key = ""

# Initialize Kanao
Kanao_instance = Kanao(open_ai_api_key)

# Train the model on custom data
Kanao_instance.train_on_pdf('path/to/pdf/file.pdf')

# Generate a response
response_txt = Kanao_instance.generate_response("What is in the document?")