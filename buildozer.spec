[app]
title = PicoPythonGame
package.name = picopythongame
package.domain = com.vrgame.cube
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

source.exclude_patterns = **/test/**,**/tests/**,**/unittest/**

# ИСПРАВЛЕНО: Держим жесткий стабильный Python 3.11, а модули Kivy и Android отдаем на автоподбор сборщику!
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

# Идеальный баланс под Gradle
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24

[buildozer]
log_level = 2
warn_on_root = 0
