Бот работает на TimeWeb Cloud (Ubuntu)
Деплой через: systemd + git_update.sh + check_bot.sh
Репозиторий: https://github.com/plug-ink/tg_bot_cr
SSH ключ настроен для беcпарольного доступа

# Статус бота
sudo systemctl status mybot

# Перезапуск бота  
sudo systemctl restart mybot

# Логи бота
sudo journalctl -u mybot -f

# Ручное обновление с GitHub
cd /root/tg_bot_cr && git pull && sudo systemctl restart mybot


Бот запускается через systemd службу mybot

Авто-обновление через cron каждые 10 минут

.env файлы защищены .gitignore

SSH ключ настроен для GitHub

Режим разработки (тестовый бот):
powershell
# Переключаемся на тестового бота
Copy-Item .env.test .env -Force

# Проверяем что переключилось
Get-Content .env

Режим продакшн (основной бот):
powershell
# Переключаемся на основного бота
Copy-Item .env.prod .env -Force

# Пушим изменения на GitHub
git add .
git commit -m "Описание изменений"
git push origin main

# На сервере автоматически обновится через 10 минут