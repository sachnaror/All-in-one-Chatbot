from configparser import ConfigParser

class LoadConfig:
  def __init__(self, config_file='src/ui/config.ini'):
    self.config = ConfigParser()
    self.config.read(config_file)
    
  def get_llm_options(self):
    """
    Get the list of LLM options from the configuration file.
    """
    
    return self.config.get('DEFAULT', 'LLM_options').split(', ')
  
  def get_use_case(self):
    """
    Get the use case from config file.
    """

    return self.config.get('DEFAULT', 'USE_CASE').split(', ')
  
  def get_title(self):
    """
    Get the title from config file.
    """

    return self.config.get('DEFAULT', 'Title')
  
  def get_groq_models(self):
    """
    Get groq models from the config file.
    """

    return self.config.get('DEFAULT', 'GROQ_MODEL').split(', ')

  def get_openai_models(self):
    """
    Get OpenAI models from config file.
    """  

    return self.config.get('DEFAULT', 'OPENAI_MODEL').split(', ')

    