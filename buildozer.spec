[app]
title = PicoPythonGame
package.name = picopythongame
package.domain = com.vrgame.cube
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 1. ИСПРАВЛЕНО: Вырезаем сбойные тестовые папки Python, на которых загорался крестик
source.exclude_patterns = **/test/**,**/tests/**,**/unittest/**

requirements = python3,kivy==2.3.0

orientation = landscape
fullscreen = 1
android.archs = arm64-v8a
android.allow_skip_x86 = True
android.accept_sdk_license = True
android.skip_update = False
android.minapi = 29
android.ndk_api = 29

[buildozer]
# Оставляем двойку для перехвата ошибок, но...
log_level = 2
warn_on_root = 0

# 2. ИСПРАВЛЕНО: Принудительно глушим пулеметный спам компилятора Clang внутри Android NDK
android.meta_data = "p4a.extra_args=--quiet"
