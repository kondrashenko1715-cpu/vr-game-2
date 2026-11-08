[app]
title = PicoPythonGame
package.name = picopythongame
package.domain = com.vrgame.cube
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ИСПРАВЛЕНО: Убрали ПК-версию pyopengl, заменив на легкий мобильный pyopengl_headless
requirements = python3,kivy==2.3.0,pyopengl_headless

orientation = landscape
fullscreen = 1
android.archs = arm64-v8a
android.allow_skip_x86 = True

android.accept_sdk_license = True
android.skip_update = False
android.minapi = 29
android.ndk_api = 29

[buildozer]
log_level = 1
warn_on_root = 0
