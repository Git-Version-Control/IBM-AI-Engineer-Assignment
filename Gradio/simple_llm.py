# Import the necessary packages
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai import Credentials
from langchain_ibm import WatsonxLLM
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

# Specify the model and project settings 
# (make sure the model you wish to use is commented out, and other models are commented)
#model_id = 'mistralai/mixtral-8x7b-instruct-v01' # Specify the Mixtral 8x7B model
model_id = 'ibm/granite-3-3-8b-instruct' # Specify IBM's Granite 3.3 8B model

# Set the necessary parameters
parameters = {
    GenParams.MAX_NEW_TOKENS: 256,  # Specify the max tokens you want to generate
    GenParams.TEMPERATURE: 0.5, # This randomness or creativity of the model's responses
}

# Wrap up the model into WatsonxLLM inference

project_id = "skills-network"
apikey = os.getenv("WATSONX_APIKEY")
print(apikey)
# Wrap up the model into WatsonxLLM inference
watsonx_llm = WatsonxLLM(
    model_id=model_id,
    url="https://us-south.ml.cloud.ibm.com",
    project_id=project_id,
    params=parameters,
    apikey=apikey
)

# Get the query from the user input
query = input("Please enter your query: ")

# Print the generated response
print(watsonx_llm.invoke(query))