from app.database.db import get_db
import logging

class User:
    @staticmethod
    def create(username, password_hash):
        try:
            db = get_db()
            with db.cursor() as cursor:
                sql = "INSERT INTO Users (username, password_hash) VALUES (%s, %s)"
                cursor.execute(sql, (username, password_hash))
            db.commit()
            return cursor.lastrowid
        except Exception as e:
            logging.error(f"Error creating user: {e}")
            return None

    @staticmethod
    def find_by_username(username):
        db = get_db()
        with db.cursor() as cursor:
            sql = "SELECT * FROM Users WHERE username=%s"
            cursor.execute(sql, (username,))
            return cursor.fetchone()

    @staticmethod
    def find_by_id(user_id):
        db = get_db()
        with db.cursor() as cursor:
            sql = "SELECT * FROM Users WHERE id=%s"
            cursor.execute(sql, (user_id,))
            return cursor.fetchone()

class Ticket:
    @staticmethod
    def create(user_id, text):
        db = get_db()
        with db.cursor() as cursor:
            sql = "INSERT INTO Tickets (user_id, text) VALUES (%s, %s)"
            cursor.execute(sql, (user_id, text))
            ticket_id = cursor.lastrowid
        db.commit()
        return ticket_id

    @staticmethod
    def get_all_for_user(user_id):
        db = get_db()
        with db.cursor() as cursor:
            sql = """
                SELECT t.*, p.category, p.sentiment, p.summary, p.auto_reply
                FROM Tickets t
                LEFT JOIN Predictions p ON t.id = p.ticket_id
                WHERE t.user_id=%s
                ORDER BY t.created_at DESC
            """
            cursor.execute(sql, (user_id,))
            return cursor.fetchall()

class Prediction:
    @staticmethod
    def create(ticket_id, category, sentiment, summary, auto_reply):
        db = get_db()
        with db.cursor() as cursor:
            sql = """
                INSERT INTO Predictions (ticket_id, category, sentiment, summary, auto_reply) 
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (ticket_id, category, sentiment, summary, auto_reply))
        db.commit()
