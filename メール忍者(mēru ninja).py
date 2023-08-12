import requests
import smtplib
from email.message import EmailMessage
import time

def get_pwned_data(email, api_key):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "hibp-api-key": api_key
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return None
    else:
        raise Exception(f"Failed to get data for email: {email}. Status code: {response.status_code}")

def send_email_report(report_data, to_email):
    date = time.strftime("%d/%m/%Y")
    hours = time.strftime("%H:%M:%S")

    fromadd = 'pwned.checker@outlook.com'
    subject = f'Report of {date} {hours}'
    username = 'youremail.exemple.com' # I used the Microsoft mail services like email provider. Because is really simple to implement
    app_password = 'your_app_password' # I used the microsoft outlook app password

    email_msg = EmailMessage()
    email_msg['Subject'] = subject
    email_msg['From'] = fromadd
    email_msg['To'] = to_email

    email_body = []

    for email, sites in report_data.items():
        if sites:
            email_body.append(f"{email}: {', '.join(sites)}")
        else:
            email_body.append(f"{email}: not pwned")

    msg = "\n".join(email_body)
    email_msg.set_content(msg)

    server = smtplib.SMTP('smtp-mail.outlook.com', 587)  # here is set for the outlook SMTP and port but you can customize if have a favourite one
    server.starttls()
    server.login(username, app_password)
    try:
        server.send_message(email_msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
    finally:
        server.quit()

def main():
    api_key = "Your_i_have_been_powned_api_key"
    email_list = ["email@exemple.com", "email@exemple.com", "email@exemple.com", "email@exemple.com", "email@exemple.com", "email@exemple.com"]

    pwned_emails_data = {}

    for email in email_list:
        try:
            data = get_pwned_data(email, api_key)
            if data:
                pwned_emails_data[email] = [item['Name'] for item in data]
            else:
                pwned_emails_data[email] = []  # Mark email as not pwned
        except Exception as e:
            print(f"Error processing {email}: {str(e)}")

        # Introduce a delay of 10 seconds between requests to avoid rate-limiting
        time.sleep(10)

    print(f"Number of emails given: {len(email_list)}")
    print("Pwned Emails Data:")
    for email, sites in pwned_emails_data.items():
        print(f"{email}: {', '.join(sites)}")

    try:
        send_email_report(pwned_emails_data, 'black18t@icloud.com')
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

if __name__ == "__main__":
    main()
