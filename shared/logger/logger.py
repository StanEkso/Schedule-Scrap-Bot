class Logger:
    prefix: str

    def __init__(self, prefix: str = "") -> None:
        self.prefix = prefix

    def info(self, msg: str) -> None:
        print("[INFO] " + msg)

    def error(self, msg: str) -> None:
        print("[ERROR] " + msg)

    def debug(self, msg: str) -> None:
        print("[DEBUG] " + msg)

    def init(self, msg: str) -> None:
        print("[INIT] " + msg)

    def warning(self, msg: str) -> None:
        print("[WARNING] " + msg)

    def custom(self, msg: str, tag: str = "LOG") -> None:
        print("["+tag+"] " + msg)


logger = Logger()
