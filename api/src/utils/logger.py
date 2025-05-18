import logging

class Logger:
    def __init__(self, nivel=logging.INFO):
        """
        Inicializa a classe de log sem criação de diretório.

        Args:
            nivel (int): Nível de log (ex: logging.INFO, logging.DEBUG, etc.).
        """
        self.nivel = nivel

        # Configurar o logger sem salvar em arquivo
        logging.basicConfig(
            level=self.nivel,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.StreamHandler()  # Exibe logs apenas no console
            ]
        )
        self.logger = logging.getLogger(__name__)

    def info(self, mensagem):
        """Registra uma mensagem de nível INFO."""
        self.logger.info(mensagem)

    def warning(self, mensagem):
        """Registra uma mensagem de nível WARNING."""
        self.logger.warning(mensagem)

    def error(self, mensagem):
        """Registra uma mensagem de nível ERROR."""
        self.logger.error(mensagem)

    def debug(self, mensagem):
        """Registra uma mensagem de nível DEBUG."""
        self.logger.debug(mensagem)