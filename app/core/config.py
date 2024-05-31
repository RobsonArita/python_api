from ..core.globals import globals

class Settings():
  app_name: str = 'Robson API'
  admin_email: str
  items_per_user: int = 50
  mongodb_url: str = globals.DATABASE_URL
  mongodb_database: str = 'Robson Database'

settings = Settings()