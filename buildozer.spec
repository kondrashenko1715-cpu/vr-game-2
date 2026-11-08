[app]
title = PicoPythonGame
package.name = picopythongame
package.domain = com.vrgame.cube
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ИСПРАВЛЕНО: Собираем строго базовое ядро Python и OpenGL, отсекая сбойные модули звука и буфера
requirements = python3,kivy==2.3.0,pyopengl

orientation = landscape
osx.kivy_version = 2.1.0
fullscreen = 1
android.archs = arm64-v8a
android.accept_sdk_license = True
android.skip_update = False
android.minapi = 29
android.ndk_api = 29

[buildozer]
log_level = 2
warn_on_root = 0
