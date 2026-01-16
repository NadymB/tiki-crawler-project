import requests 
from config.runtime import DISCORD_WEBHOOK_URL

def notify_discord(context):
    task_instance = context.get("task_instance")
    dag_id = context.get("dag").dag_id
    task_id = task_instance.task_id
    execution_date = context.get("execution_date")
    log_url = task_instance.log_url

    message = {
        "content": (
            f"🚨 **Airflow Task Failed**\n"
            f"**DAG:** {dag_id}\n"
            f"**Task:** {task_id}\n"
            f"**Execution Date:** {execution_date}\n"
            f"🔗 [View Logs]({log_url})"
        )
    }

    requests.post(DISCORD_WEBHOOK_URL, json=message)
