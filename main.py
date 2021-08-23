import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pyfiglet import Figlet
from printy import printy, inputy
from random import choice
from getpass import getpass
import os
import tempfile
from pathlib import Path
import time
import license

print(chr(27) + "[2J")

fonts = [
    "big",
    "graffiti",
    "bigchief",
    "colossal",
    "computer",
    "doom",
    "doh",
    "dotmatrix",
    "epic",
    "avatar",
    "drpepper",
    "isometric1",
    "isometric2",
    "isometric3",
    "isometric4",
    "larry3d",
    "pawp",
    "slant",
    "small",
    "speed",
    "standard",
    "stellar",
    "stop",
]

colors = [
    "g",
    "w",
    "<r",
    "r",
    "r>",
    "<n",
    "n",
    "n>",
    "<y",
    "y",
    "y>",
    "<b",
    "b",
    "b>",
    "<m",
    "m",
    "m>",
    "<c",
    "c",
    "c>",
    "<o",
    "o",
    "o>",
    "<p",
    "p",
    "p>",
]

formats = ["B", "D", "I", "U", "H"]

providers = [
    "Office 365 (e.g. example@office365.com)",
    "Microsoft (e.g. example@outlook.com, example@hotmail.com)",
    "Google (e.g. example@gmail.com, example@googlemail.com)",
    "Other (e.g. example@yoursite.com, example@yandex.ru)",
]

banner_fig = Figlet(font=choice(fonts))
printy((banner_fig.renderText("mailer")), f"{choice(colors)}B")

printy(
    "Coded by Ege Akman <egeakmanegeakman@hotmail.com>",
    f"{choice(colors)}{choice(formats)}",
)

printy("https://github.com/egeakman", f"{choice(colors)}{choice(formats)}")

time.sleep(2)

if str(os.path.exists(f"{tempfile.gettempdir()}/mailer_no_first")) == "False":

    printy(license.license, "wB")

    printy(
        "\nYou can also find this license at https://github.com/egeakman/mailer/blob/master/LICENSE\n",
        "wB",
    )

    yes_no = str(inputy("Do you accept this license? (y/N)\n", "wB") or " ")

    while True:
        if yes_no.lower() == "y" or yes_no.lower() == "yes":
            break

        elif yes_no.lower() == "n" or yes_no.lower() == "no":
            printy("\nOK, your decision.\n", "wB")
            time.sleep(3)
            exit()

        else:
            printy("\nOnly answer with yes(y) or no(n).\n", "rB")
            time.sleep(2)
            yes_no = str(inputy("Do you accept this license? (y/N)\n", "wB") or " ")

    os.mkdir(f"{tempfile.gettempdir()}/mailer_no_first")
    Path(f"{tempfile.gettempdir()}/mailer_no_first/no_first.txt").touch()
    with open(
        f"{tempfile.gettempdir()}/mailer_no_first/no_first.txt", "w", encoding="utf-8"
    ) as f:
        f.write(
            "This is a file created to check if the mailer ever ran on the device.\n    Coded by Ege Akman <egeakmanegeakman@hotmail.com>\n    https://github.com/egeakman"
        )

printy(
    "Hello I am the Mailer, your mailer. We'll send your e-mails interactively.\nDon't hesitate to contact my developer in any condition.\nPlease report bugs and etc. at https://github.com/egeakman/mailer/issues.\n",
    f"{choice(colors)}B",
)
time.sleep(2)

printy(
    "First we have to connect to your SMTP server. So I will need to get some information about the provider.\n",
    f"{choice(colors)}B",
)

provider = str(
    inputy(
        "Which mail provider do you use?\n\n", f"{choice(colors)}B", options=providers
    )
)

if provider.lower() == "office 365 (e.g. example@office365.com)":
    smtp_server = "smtp.office365.com"
    smtp_port = "587"

if provider.lower() == "microsoft (e.g. example@outlook.com, example@hotmail.com)":
    smtp_server = "smtp-mail.outlook.com"
    smtp_port = "587"

if provider.lower() == "google (e.g. example@gmail.com, example@googlemail.com)":
    smtp_server = "smtp.gmail.com"
    smtp_port = "587"

if provider.lower() == "other (e.g. example@yoursite.com, example@yandex.ru)":
    while True:
        smtp_server = str(
            inputy(
                "\nWhat is your provider's SMTP server address? (e.g. mail.yoursite.com)\n",
                f"{choice(colors)}B",
            )
        )
        if not smtp_server.strip(" "):
            printy("\nDo not leave it blank.\n", "rB")
            time.sleep(1)

        elif smtp_server.strip(" "):
            break

    smtp_port = str(
        inputy(
            "What is your provider's SMTP port? (default:587)\n",
            f"{choice(colors)}B",
            type="int",
            default="587",
        )
    )

printy(
    "\nOK, I got the provider information.\nNow we need to login. So I'll need your login credentials. (Don't worry I'll not steal them, you can check my code I'm open-source ;) )\n",
    f"{choice(colors)}B",
)

while True:
    sender_email = str(
        inputy(
            "What is your e-mail address?\n",
            f"{choice(colors)}B",
        )
    )
    if not sender_email.strip(" "):
        printy("\nDo not leave it blank.\n", "rB")
        time.sleep(1)

    elif sender_email.strip(" "):
        break

password = getpass(
    prompt="\nWhat is your password? (Don't worry it will not be prompted.)\n",
    stream=None,
)

context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)

except Exception as error:
    printy(
        "\nI can't login. You probably gave me wrong credentials :|\nRestart the app and try again.\nOh by the way I can't login to accounts which has 2 factor authentication, maybe in the future...",
        "rB",
    )
    print(error)
    exit()

printy(
    "\nWe logged in! Next, we are going to choose the receiver.\n",
    f"{choice(colors)}B",
)

while True:
    receiver_email = str(
        inputy(
            "\nWhat is the e-mail address of this lucky human?\n",
            f"{choice(colors)}B",
        )
    )
    if not receiver_email.strip(" "):
        printy("\nDo not leave it blank.\n", "rB")
        time.sleep(1)

    elif receiver_email.strip(" "):
        break

printy(
    "\nOK, I know who are we going to send this. Now the subject and the message.\n",
    f"{choice(colors)}B",
)
confirmation = "no"
while True:
    subject = str(
        inputy(
            "\nWhat is the subject?\n",
            f"{choice(colors)}B",
        )
    )
    if not subject or subject.isspace():
        if confirmation == "n" or confirmation == "no":
            confirmation = str(
                inputy("\nAre you sure you want to leave it blank?\n", "rB") or " "
            )
            while True:
                if confirmation.lower() == "y" or confirmation.lower() == "yes":
                    printy("\nOK, got it.\n", f"{choice(colors)}B")
                    confirmation = "yes"
                    break

                elif confirmation.lower() == "n" or confirmation.lower() == "no":
                    confirmation = "no"
                    break

                else:
                    printy("\nOnly answer with yes(y) or no(n).\n", "rB")
                    time.sleep(1)
                    confirmation = str(
                        inputy("\nAre you sure you want to leave it blank?\n", "wB")
                        or " "
                    )

    elif (
        subject or not subject.isspace() or confirmation == "y" or confirmation == "yes"
    ):
        break


confirmation_m = "no"
while True:
    raw_text = str(
        inputy(
            "\nWhat is your message?\n",
            f"{choice(colors)}B",
        )
    )
    if not raw_text or raw_text.isspace():
        if confirmation_m == "n" or confirmation_m == "no":
            confirmation_m = str(
                inputy("\nAre you sure you want to leave it blank?\n", "rB") or " "
            )
            while True:
                if confirmation_m.lower() == "y" or confirmation_m.lower() == "yes":
                    printy("\nOK, got it.\n", f"{choice(colors)}B")
                    confirmation_m = "yes"
                    break

                elif confirmation_m.lower() == "n" or confirmation_m.lower() == "no":
                    confirmation_m = "no"
                    break

                else:
                    printy("\nOnly answer with yes(y) or no(n).\n", "rB")
                    time.sleep(1)
                    confirmation_m = str(
                        inputy("\nAre you sure you want to leave it blank?\n", "wB")
                        or " "
                    )

    elif (
        raw_text
        or not raw_text.isspace()
        or confirmation_m == "y"
        or confirmation_m == "yes"
    ):
        break


message = MIMEMultipart()
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email
text = f"""\
{raw_text}
"""
mtext = MIMEText(text, "plain")
message.attach(mtext)

try:
    server.sendmail(sender_email, receiver_email, message.as_string())

except Exception as error_m:
    printy(
        "\nI can't send the e-mail. Check if there is anything unusual in the message.\nRestart the app as the last resort.\n",
        "rB",
    )
    print(error_m)
    exit()

printy(
    "\nYes we did it, we sent the e-mail! We should celebrate this sometime :D\nSee you until your next use.\n",
    "nB",
)

try:
    server.quit()

except:
    exit()
