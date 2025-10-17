from environs import Env

env = Env()
env.read_env()                         
OLLAMA_API_KEY = env.str("OLLAMA_API_KEY", "")