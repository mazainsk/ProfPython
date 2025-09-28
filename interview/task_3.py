"""
Домашнее задание к лекции 7. «Подготовка к собеседованию»
Задача 3. Рефакторинг кода.
"""

import email
import os
import smtplib
import imaplib
import configparser

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Gmail:
    """
    Класс для работы с почтой.
    """
    @classmethod
    def load_constants(cls, ini_path):
        """
        Загрузка констант (атрибутов класса) из ini-файла.
        :param ini_path: имя ini-файла в текущем каталоге;
        :return: None
        """
        assert os.path.exists(ini_path), f'Settings file "{ini_path}" was not found'
        config = configparser.ConfigParser(allow_no_value=True)
        config.read(ini_path)

        cls.GMAIL_SMTP = config['common']['GMAIL_SMTP']
        cls.GMAIL_IMAP = config['common']['GMAIL_IMAP']
        cls.PORT = int(config['common']['PORT'])
        cls.INI_PATH = ini_path

    def __init__(self, subject:str=None, recipients:str=None, message:str=None, header:str=None):
        config = configparser.ConfigParser(allow_no_value=True)
        config.read(Gmail.INI_PATH)

        self.__login = config['authorization']['login']
        self.__password = config['authorization']['password']
        self.folder = config['mail_settings']['folder']
        self.uid = config['mail_settings']['uid']

        if subject is None:
            self.subject = config['mail_settings']['subject']
        else:
            self.subject = subject

        if recipients is None:
            recipients = config['mail_settings']['recipients']
            split_char = '\n'
        else:
            split_char = ','
        self.recipients = [i.strip() for i in recipients.split(split_char)]

        if message is None:
            self.message = config['mail_settings']['message']
        else:
            self.message = message

        if header is None:
            self.header = config['mail_settings']['header']
        else:
            self.header = header

    def __str__(self):
        result = f'subject: {self.subject}\n'
        result += f'recipients: {self.recipients}\n'
        result += f'message: {self.message}\n'
        result += f'header: {self.header}\n'
        result += f'folder: {self.folder}\n'
        result += f'uid: {self.uid}\n'
        return result

    def send_message(self):
        """
        Метод для отправки писем.
        :return: None
        """
        msg = MIMEMultipart()
        msg['From'] = self.__login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))

        ms = smtplib.SMTP(Gmail.GMAIL_SMTP, Gmail.PORT)
        ms.ehlo()       # Identify ourselves to smtp gmail client.
        ms.starttls()   # secure our email with tls encryption
        ms.ehlo()       # re-identify ourselves as an encrypted connection

        ms.login(self.__login, self.__password)
        ms.sendmail(self.__login, ms, msg.as_string())
        ms.quit()

    def receive_message(self):
        """
        Метод для получения писем.
        :return: email_message
        """
        mail = imaplib.IMAP4_SSL(Gmail.GMAIL_IMAP)
        mail.login(self.__login, self.__password)
        mail.list()
        mail.select(self.folder)

        criterion = f'(HEADER Subject "{self.header}")' if self.header else 'ALL'
        _, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'

        latest_email_uid = data[0].split()[-1]
        _, data = mail.uid('fetch', latest_email_uid, self.uid)

        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)

        mail.logout()
        return email_message


if __name__ == '__main__':
    Gmail.load_constants('task_3_config.ini')
    test_mail = Gmail()
    print(test_mail)
