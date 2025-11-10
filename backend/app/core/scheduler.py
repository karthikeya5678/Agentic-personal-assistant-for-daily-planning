# app/core/scheduler.py

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from ..core.database import task_collection, exam_collection
from ..services.notification_service import send_whatsapp_message
import logging
from datetime import datetime, timedelta

# --- Import your AI agents ---
from ..agents.study_agent import get_study_materials
from ..agents.recommendation_agent import get_recommendation

# Configure logging
logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.INFO)

# Initialize the scheduler with the correct timezone
scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")

# --- 1. Your Existing Task Notification Job ---
def send_task_notification(task_name: str):
    """This function now sends a real WhatsApp notification."""
    message_body = f"🔔 Reminder: It's time for '{task_name}'!"
    send_whatsapp_message(message_body)

# --- 2. UPGRADED: Proactive Exam Check Job ---
async def check_for_upcoming_exams():
    """
    Runs once per day. Checks all exams in the database and sends
    a WhatsApp reminder if an exam is exactly 3 days away.
    """
    print("Checking for upcoming exams...")
    today = datetime.now().date()
    three_days_later = today + timedelta(days=3)
    
    exams = await exam_collection.find().to_list(1000)
    
    for exam in exams:
        try:
            # Convert the date string from the database into a date object
            exam_date = datetime.strptime(exam["date"], "%Y-%m-%d").date()
            
            if exam_date == three_days_later:
                subject = exam["subject"]
                print(f"Exam found for {subject}. Running Study Buddy agent...")
                
                # --- THIS IS THE AGENTIC PART ---
                # 1. Run the Study Buddy agent automatically
                study_links = get_study_materials(subject)
                
                # 2. Create a rich, combined message
                message_body = (
                    f"🎓 *Proactive Exam Alert!* 🎓\n\n"
                    f"Your exam for **{subject}** is in 3 days on {exam_date.strftime('%d-%b-%Y')}.\n\n"
                    f"I've automatically found some study materials for you:\n\n"
                    f"{study_links}"
                )
                
                # 3. Send the proactive notification
                send_whatsapp_message(message_body)
                print(f"Sent proactive 3-day reminder for {subject} exam.")
                
        except ValueError:
            print(f"Could not parse date for exam: {exam['subject']}")
        except Exception as e:
            print(f"Error processing exam {exam.get('subject')}: {e}")


# --- 3. NEW: Proactive Sunday Recommendation Job ---
async def send_sunday_recommendations():
    """
    Runs every Sunday morning. Runs the recommendation agent
    and sends movie suggestions via WhatsApp.
    """
    print("It's Sunday! Running movie recommender...")
    try:
        # 1. Run the recommendation agent automatically
        movie_ideas = get_recommendation("movie")
        
        # 2. Create the message
        message_body = (
            f"☀️ *Happy Sunday!* ☀️\n\n"
            f"Here are a few movie ideas for you and your family to watch today:\n\n"
            f"{movie_ideas}"
        )
        
        # 3. Send the proactive notification
        send_whatsapp_message(message_body)
        print("Sent Sunday movie recommendations.")
        
    except Exception as e:
        print(f"Failed to send Sunday recommendations: {e}")


# --- 4. The Main Setup Function (Updated) ---
async def setup_scheduler():
    """
    Sets up all scheduled jobs for the assistant.
    """
    print("Setting up scheduler jobs...")
    
    # --- Job 1: Daily Exam Check (runs at 8:00 AM) ---
    scheduler.add_job(
        check_for_upcoming_exams,
        'cron',
        hour=8,
        minute=0,
        id="daily_exam_check"
    )
    print("✅ Scheduled daily exam check at 8:00 AM.")
    
    # --- Job 2: Sunday Recommender (runs on Sun at 9:00 AM) ---
    scheduler.add_job(
        send_sunday_recommendations,
        'cron',
        day_of_week='sun', # 'sun' means Sunday
        hour=9,
        minute=0,
        id="sunday_recommendations"
    )
    print("✅ Scheduled Sunday movie recommendations at 9:00 AM.")

    # --- Job 3: Your existing logic for daily tasks ---
    day_mapping = {"weekday": "mon-sat", "sunday": "sun"}
    tasks = await task_collection.find().to_list(1000)

    for task in tasks:
        task_name = task.get("task_name")
        task_time = task.get("time")
        day_type = task.get("day_type")
        
        if task_name and task_time and day_type:
            try:
                hour, minute = map(int, task_time.split(':'))
                day_of_week = day_mapping.get(day_type)
                
                scheduler.add_job(
                    send_task_notification,
                    'cron',
                    day_of_week=day_of_week,
                    hour=hour,
                    minute=minute,
                    args=[task_name],
                    id=f"task_{task['_id']}",
                    replace_existing=True
                )
            except Exception as e:
                print(f"❌ Could not schedule task '{task_name}'. Error: {e}")