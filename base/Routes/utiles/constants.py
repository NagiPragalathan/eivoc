def login_mail_content(prefix, first_name, surname, registration_number, email, password):
    message = f"""
        Dear {prefix} {first_name} {surname},

        Thank you for your interest in EIVOC 2025.
        Your registration number: {registration_number}
        Log in ID: {email}
        Password: {password}

        You can now log on to our website to know more details about the conference: [website link]

        Conference Registration closes by June 2025.
        Stay tuned! Looking forward to meeting you at the event.

        Regards,
        The Organizing Committee
        EIVOC 2025
        """
    return message