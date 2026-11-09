[app]
title = PicoPythonGame
package.name = picopythongame
package.domain = com.vrgame.cube
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ИСПРАВЛЕНО: Полностью вырезаем папки тестов, на которых компилятор спотыкался
source.exclude_patterns = **/test/**,**/tests/**,**/unittest/**

# ГИБРИДНОЕ ИСПРАВЛЕНИЕ: Жестко требуем стабильный Python 3.11.11 и мобильный движок Kivy
requirements = python3==3.11.11,kivy

orientation = landscape
fullscreen = 1
android.archs = arm64-v8a
android.allow_skip_x86 = True
android.accept_sdk_license = True
android.skip_update = False

# Используем надежный мобильный Bootstrap sdl2
p4a.bootstrap = sdl2

# Сбалансированный современный стандарт Android API под Java 11
android.api = 34
android.minapi = 24
android.ndk_api = 24

[buildozer]
log_level = 2
warn_on_root = 0
