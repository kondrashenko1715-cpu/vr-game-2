[app]
title = PicoPythonGame
package.name = picopythongame
package.domain = com.vrgame.cube
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

source.exclude_patterns = **/test/**,**/tests/**,**/unittest/**
requirements = python3,kivy==2.3.0

orientation = landscape
fullscreen = 1
android.archs = arm64-v8a
android.allow_skip_x86 = True
android.accept_sdk_license = True
android.skip_update = False
android.minapi = 29

# ИСПРАВЛЕНО: Жестко требуем стабильную версию NDK r25b, чтобы убрать ошибку упаковки на финише
android.ndk = 25b
android.ndk_api = 29

[buildozer]
log_level = 2
warn_on_root = 0
