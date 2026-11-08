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
android.archs = arm64-v8a
android.accept_sdk_license = True
android.skip_update = False
android.minapi = 29
android.ndk_api = 29

# ИСПРАВЛЕНО: Указываем Buildozer точные пути к SDK, NDK и sdkmanager на сервере GitHub Actions
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653

[buildozer]
log_level = 2
warn_on_root = 0
