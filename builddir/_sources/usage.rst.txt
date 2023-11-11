Usage
=====

from kavy.core.kavy import Kavy
open_ai_api_key = ""

# Initialize Kavy
kavy_instance = Kavy(open_ai_api_key)

# Train the model on custom data
kavy_instance.train_on_pdf('path/to/pdf/file.pdf')

# Generate a response
response_txt = kavy_instance.generate_response("What is in the document?")