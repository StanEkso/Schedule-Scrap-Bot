class Logger:
    def info(self, msg: str) -> None:
        self.__output("[INFO] " + msg)

    def error(self, msg: str) -> None:
        self.__output("[ERROR] " + msg)

    def debug(self, msg: str) -> None:
        self.__output("[DEBUG] " + msg)

    def init(self, msg: str) -> None:
        self.__output("[INIT] " + msg)

    def warning(self, msg: str) -> None:
        self.__output("[WARNING] " + msg)

    def custom(self, msg: str, tag: str = "LOG") -> None:
        self.__output("[" + tag + "] " + msg)

    def __output(self, msg: str) -> None:
        print(msg.replace("  ", " "))


logger = Logger()
