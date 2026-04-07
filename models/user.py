class User:
    def __init__(self, user_id, username, menu_status, offset, page_limit, lang, autorizated):
        self.user_id = user_id
        self.username = username
        self.menu_status = menu_status
        self.offset = offset
        self.page_limit = page_limit
        self.lang = lang
        self.autorizated = autorizated