class InvalidMenuId(Exception):
    def __init__(self, id: str):
        super().__init__(400, f'Invalid id: {id}')
