[app]
title = PicoPythonGame
package.name = picopythongame
package.domain = com.vrgame.cube
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ИСПРАВЛЕНО: Убрали pyopengl, оставив только Kivy, который сам умеет рисовать 3D на Android
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
# ИСПРАВЛЕНО: Вернули детальные логи, чтобы в случае чего сразу увидеть точную причину
log_level = 2
warn_on_root = 0
