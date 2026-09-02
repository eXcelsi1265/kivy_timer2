[app]

# Название приложения
title = Timer

# Имя пакета (только латиница, без пробелов)
package.name = timerapp

# Домен пакета (можно оставить как есть)
package.domain = org.test

# Папка с исходниками
source.dir = .

# Расширения файлов для включения
source.include_exts = py,png,jpg,kv,atlas

# Версия приложения
version = 0.1

# Версия Python
python.version = 3.11.9

# Зависимости
requirements = python3,kivy

# Зеркало PyPI (для ускорения скачивания)
pypi_mirror = https://pypi.tuna.tsinghua.edu.cn/simple

# Ориентация экрана
orientation = portrait

# Полный экран
fullscreen = 0

# Автоматически принимать лицензию SDK
android.accept_sdk_license = True

# Архитектуры для сборки
android.archs = arm64-v8a, armeabi-v7a

# Версия NDK (рекомендуемая)
android.ndk = 25c

# Минимальная версия Android API
android.ndk_api = 21

# Версия SDK
android.sdk = 33

# Разрешить резервное копирование
android.allow_backup = True

# Использовать стабильную ветку python-for-android
p4a.fork = kivy
p4a.branch = release-2026.05.09
p4a.commit = HEAD

# Уровень логирования
log_level = 2

# Предупреждение при запуске от root
warn_on_root = 1