from flask import Blueprint, request, jsonify, session
from app.services.classification_service import ClassificationService
from app.services.sentiment_service import SentimentService
from app.services.summarization_service import SummarizationService
from app.services.auto_reply_service import AutoReplyService
from app.database.models import Ticket, Prediction
from app.utils.helpers import login_required

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/api/predict', methods=['POST'])
@login_required
def predict():
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
        
    user_id = session.get('user_id')
    
    category = ClassificationService.classify_ticket(text)
    sentiment = SentimentService.analyze(text)
    summary = SummarizationService.summarize(text)
    auto_reply = AutoReplyService.get_reply(text)
    
    ticket_id = Ticket.create(user_id, text)
    Prediction.create(ticket_id, category, sentiment, summary, auto_reply)
    
    return jsonify({
        'success': True,
        'ticket_id': ticket_id,
        'category': category,
        'sentiment': sentiment,
        'summary': summary,
        'auto_reply': auto_reply
    })
