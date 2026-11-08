[app]
title = PicoPythonGame
package.name = picopythongame
package.domain = com.vrgame.cube
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pyopengl
orientation = landscape
osx.kivy_version = 2.1.0
fullscreen = 1

# ИСПРАВЛЕНО: Жестко собираем ТОЛЬКО под мобильный процессор Pico 4, отключая сбойный x86_64
android.archs = arm64-v8a
android.allow_skip_x86 = True

android.accept_sdk_license = True
android.skip_update = False
android.minapi = 29
android.ndk_api = 29

[buildozer]
log_level = 2
warn_on_root = 0
