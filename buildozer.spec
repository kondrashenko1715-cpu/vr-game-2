[app]
title = PicoPythonGame
package.name = picopythongame
package.domain = com.vrgame.cube
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Вырезаем сбойный тестовый мусор Python
source.exclude_patterns = **/test/**,**/tests/**,**/unittest/**

requirements = python3,kivy

orientation = landscape
fullscreen = 1
android.archs = arm64-v8a
android.allow_skip_x86 = True
android.accept_sdk_license = True
android.skip_update = False

p4a.bootstrap = sdl2

# ИСПРАВЛЕНО: Сбалансировали версии API для стабильной упаковки Gradle
android.api = 34
android.minapi = 24
android.ndk_api = 24

[buildozer]
log_level = 2
warn_on_root = 0
