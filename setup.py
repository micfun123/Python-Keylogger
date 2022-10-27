import os
try:
    import pynput
except:
    os.system('python -m pip install pynput')

email = str(input("Enter the email to send to: "))
app_password = str(input("Enter the app password: "))

with open(".env", "a") as f:
            f.write(f"EMAIL = {email}")
            f.write("\n")
            f.write(f"APP_PASSWORD = {app_password}")
