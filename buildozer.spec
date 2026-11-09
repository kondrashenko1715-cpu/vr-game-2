[app]
title = PicoPythonGame
package.name = picopythongame
package.domain = com.vrgame.cube
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

source.exclude_patterns = **/test/**,**/tests/**,**/unittest/**

# Оставляем только стабильное ядро Kivy
requirements = python3,kivy==2.3.0

orientation = landscape
fullscreen = 1
android.archs = arm64-v8a
android.allow_skip_x86 = True
android.accept_sdk_license = True
android.skip_update = False

# ИСПРАВЛЕНО: Жестко выставляем проверенную связку версий Android SDK/NDK под Kivy 2.3.0
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

[buildozer]
# Включаем полный вывод логов, чтобы компилятор без скрытия показал нам финиш
log_level = 2
warn_on_root = 0
