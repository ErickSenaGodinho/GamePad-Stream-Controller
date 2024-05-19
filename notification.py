from plyer import notification
def show_notification(title: str, message: str = ""):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,  
        timeout = 2,
    )