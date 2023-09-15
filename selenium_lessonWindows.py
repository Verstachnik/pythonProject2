
alert = browser.swith_to.alert# если нужно только подтвердить дествие
alert.accept()
alert_text = alert.text# чтобы взять текст с alert


вариант модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться от него, называется confirm

confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()

Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys():

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()