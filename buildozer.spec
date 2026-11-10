[app]
title = MyPico3DCube
# ИСПРАВЛЕНО: Дали игре абсолютно уникальное имя, чтобы шлем не путал её с другими приложениями!
package.name = mypico3dcube
package.domain = com.pico.developer

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

source.exclude_patterns = **/test/**,**/tests/**,**/unittest/**

requirements = python3==3.11.11, hostpython3==3.11.11, kivy, android, pyjnius

orientation = landscape
fullscreen = 1
android.archs = arm64-v8a
android.allow_skip_x86 = True
android.accept_sdk_license = True
android.skip_update = False

p4a.bootstrap = sdl2

# Наш защитный щит против сбоя grpmodule
android.meta_data = p4a.no_grp=True

# Стабильные лимиты под Gradle
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24

[buildozer]
log_level = 2
warn_on_root = 0
