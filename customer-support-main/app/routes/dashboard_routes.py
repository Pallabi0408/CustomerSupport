from flask import Blueprint, render_template, session, redirect, url_for
from app.utils.helpers import login_required
from app.database.models import Ticket

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def index():
    user_id = session.get('user_id')
    tickets = Ticket.get_all_for_user(user_id)
    return render_template('dashboard.html', tickets=tickets, active_page='dashboard')

@dashboard_bp.route('/tickets')
@login_required
def tickets():
    user_id = session.get('user_id')
    tickets = Ticket.get_all_for_user(user_id)
    return render_template('tickets.html', tickets=tickets, active_page='tickets')

@dashboard_bp.route('/analytics')
@login_required
def analytics():
    user_id = session.get('user_id')
    tickets = Ticket.get_all_for_user(user_id)
    
    total = len(tickets)
    categories = {}
    sentiments = {}
    for t in tickets:
        cat = t.get('category') or 'Uncategorized'
        sent = t.get('sentiment') or 'Neutral'
        categories[cat] = categories.get(cat, 0) + 1
        sentiments[sent] = sentiments.get(sent, 0) + 1
        
    stats = {
        'total': total,
        'categories': categories,
        'sentiments': sentiments
    }
    
    return render_template('analytics.html', stats=stats, active_page='analytics')

@dashboard_bp.route('/settings')
@login_required
def settings():
    return render_template('settings.html', active_page='settings')
