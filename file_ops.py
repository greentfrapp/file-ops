def create_file(filepath: str) -> None:
    """
    Create a file at filepath
    Args:
    - filepath (str): Filepath of file to write (required)
    """
    with open(filepath, "w"):
        pass


def read_file(filepath: str) -> str:
    """
    Create a file at filepath
    Args:
    - filepath (str): Filepath of file to read (required)
    """
    with open(filepath, "r") as file:
        contents = file.read()
    return contents
