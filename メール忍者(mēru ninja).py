import requests
import smtplib
from email.message import EmailMessage
import time

def get_pwned_data(email, api_key): #This function collect data from the I Have Been Pwned API for moredetails consult their documentation
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

def send_email_report(report_data, to_email):#stamp the date and the hour of the execution in the object of the email
    date = time.strftime("%d/%m/%Y")
    hours = time.strftime("%H:%M:%S")

    fromadd = 'youremail@example.com'#the email that will send the report i used an outlook 
    subject = f'Report of {date} {hours}'
    username = 'youremail@exemple.com' # I used the Microsoft mail services like email provider. Because is really simple to implement
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
        send_email_report(pwned_emails_data, 'receveremail@example.com') #write here the email where you want to receve the report
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

if __name__ == "__main__":
    main()

# Disclaimer: Usage and Responsibility
#The メール忍者 (Mēru Ninja) script provided here is intended for educational and demonstration purposes only. It is designed to showcase the capabilities of checking email addresses against the "Have I Been Pwned" API and sending reports via the Outlook email service. I, [Your Name], would like to emphasize the following points:
#External Service Usage: This script utilizes external services such as "Have I Been Pwned" and Microsoft Outlook to provide its functionality. I want to clarify that I do not have any ownership or control over these services. Any rights, terms, and conditions associated with these external services are solely governed by their respective service providers.
#Usage Restrictions: Using this script for commercial, business, or other purposes beyond personal use may potentially violate the terms and conditions of the services integrated. It is crucial to thoroughly review and comply with the terms of use, privacy policies, and service agreements of "Have I Been Pwned" and Microsoft Outlook before implementing this script in your system.
#User Responsibility: I want to make it clear that I am not responsible for any misuse of this script that might lead to a violation of the terms and conditions of the external services involved. Users are solely responsible for ensuring their compliance with the policies of the services used.
#Consultation Recommended: Before integrating this script into your system, especially for business or commercial use, I strongly recommend consulting the terms and conditions of the services mentioned earlier. This will help you make informed decisions and avoid any unintended breaches of service agreements 

