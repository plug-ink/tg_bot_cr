@echo off
:loop
py bot.py
echo Бот остановлен, перезапуск через 5 сек...
timeout /t 5 >nul
goto loop