[app]
title = PicoPythonGame
package.name = picopythongame
package.domain = com.vrgame.cube
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Собираем только чистое 3D-ядро без сбойных аудио-модулей
requirements = python3,kivy==2.3.0,pyopengl

orientation = landscape
fullscreen = 1

# Собираем исключительно под мобильный 64-битный процессор шлема Pico 4
android.archs = arm64-v8a
android.allow_skip_x86 = True

android.accept_sdk_license = True
android.skip_update = False
android.minapi = 29
android.ndk_api = 29

[buildozer]
# ИСПРАВЛЕНО: Уровень 1 отключает бесконечный спам логов компилятора, спасая сервер от вылета
log_level = 1
warn_on_root = 0
