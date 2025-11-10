import logging
import pytest
import os

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.
    ...
    """
    logging.basicConfig(
        filename= 'login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        filemode='w',
        force=True
        )
    logger = logging.getLogger("log_event")

    log_message = f"Login event - Username: {username}, Status: {status}"

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

def status_cheker(log_file):
    """
    Читає останнє слово з лог-файлу.
    """
    with open(log_file, 'r') as f:
        data = f.read().strip()

    if not data:
        return None
    status = data.split()[-1]
    return status

def test_logger_case_success():
    #Перевірка логування успішного входу (success)
    log_event("Den", "success")
    assert status_cheker(log_file="login_system.log") == "success"

def test_logger_case_expired():
    #Перевірка логування застарілого паролю (expired)
    log_event("Alex", "expired")
    assert status_cheker(log_file="login_system.log") == "expired"

def test_logger_case_failed():
    #Доданий тест для невдалого входу (failed)
    log_event("Hacker", "failed")
    assert status_cheker(log_file="login_system.log") == "failed"
    
def test_logger_case_unknown_error():
    #Доданий тест для невідомого статусу (повинен логуватися як error)
    log_event("UnknownUser", "unknown_status")
    assert status_cheker(log_file="login_system.log") == "unknown_status"