from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# ================== КЛИЕНТ ==================
def get_client_keyboard():
    keyboard = [
        [KeyboardButton("📱 Мой QR")],
        [KeyboardButton("🎁 Акции")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_client_keyboard_with_back():
    """Клавиатура клиента с кнопкой Назад (для админа)"""
    keyboard = [
        [KeyboardButton("📱 Мой QR")],
        [KeyboardButton("🎁 Акции")],
        [KeyboardButton("🔙 Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ================== БАРИСТА ==================
# ================== БАРИСТА ==================
def get_barista_keyboard():
    """Клавиатура баристы ДО сканирования"""
    keyboard = [
        [KeyboardButton("📷 Скан QR"), KeyboardButton("ℹ️ Акции")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_barista_keyboard_with_back():
    """Клавиатура баристы ДО сканирования (для админа)"""
    keyboard = [
        [KeyboardButton("📷 Скан QR"), KeyboardButton("ℹ️ Акции")],
        [KeyboardButton("🔙 Назад")]  # Возврат в настройки админа
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_barista_action_keyboard():
    """Клавиатура после сканирования QR"""
    keyboard = [
        [KeyboardButton("✅ Засчитать покупку")],
        [KeyboardButton("❌ Отменить")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ================== АДМИН - ГЛАВНОЕ МЕНЮ ==================
def get_admin_main_keyboard():
    keyboard = [
        [KeyboardButton("👥 Баристы"), KeyboardButton("👤 Посетители")],
        [KeyboardButton("⚙️ Настройки")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ================== АДМИН - УПРАВЛЕНИЕ БАРИСТАМИ ==================
def get_admin_barista_keyboard():
    keyboard = [
        [KeyboardButton("➕ Добавить"), KeyboardButton("➖ Удалить")],
        [KeyboardButton("📋 Список"), KeyboardButton("🔙 Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ================== АДМИН - УПРАВЛЕНИЕ ПОСЕТИТЕЛЯМИ ==================
def get_admin_customers_keyboard_after_list():
    return ReplyKeyboardMarkup(
        [[KeyboardButton("🔍 Найти пользователя")],
         [KeyboardButton("🔙 Назад")]],
        resize_keyboard=True
    )

# ================== АДМИН - НАСТРОЙКИ ==================
def get_admin_settings_keyboard():
    keyboard = [
        [KeyboardButton("📝 Изменить акции")],
        [KeyboardButton("👤 Режим клиента"), KeyboardButton("👨‍💼 Режим бариста")],
        [KeyboardButton("🔙 Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ================== АДМИН - УПРАВЛЕНИЕ АКЦИЯМИ ==================
def get_admin_promotion_keyboard():
    keyboard = [
        [KeyboardButton("📝 Название"), KeyboardButton("7️⃣ Условие")],
        [KeyboardButton("📖 Описание")],
        [KeyboardButton("🔙 Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ================== ПЕРЕКЛЮЧЕНИЕ РОЛЕЙ ==================
def get_role_switcher_keyboard():
    keyboard = [
        [KeyboardButton("👑 Режим админа")],
        [KeyboardButton("👨‍💼 Режим бариста"), KeyboardButton("👤 Режим клиента")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_admin_customers_keyboard():
    return ReplyKeyboardMarkup(
        [[KeyboardButton("🔍 Найти пользователя")],
         [KeyboardButton("🔙 Назад")]],
        resize_keyboard=True
    )

