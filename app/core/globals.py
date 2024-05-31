from dotenv import load_dotenv
import os

load_dotenv()

class Globals():
  IP: str = os.getenv('IP')
  PORT: str = os.getenv('PORT')
  DATABASE_URL: str = os.getenv('DATABASE_URL')

globals = Globals()