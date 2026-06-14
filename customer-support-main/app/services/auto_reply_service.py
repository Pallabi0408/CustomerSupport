from app.utils.faq_reply import get_best_faq_match

class AutoReplyService:
    @staticmethod
    def get_reply(text):
        return get_best_faq_match(text)
