class User:
    def __init__(self, user_id, username, app_action, offset, page_limit, lang, autorizated):
        self.user_id = user_id
        self.username = username
        self.app_action = app_action
        self.offset = offset
        self.page_limit = page_limit
        self.lang = lang
        self.autorizated = autorizated