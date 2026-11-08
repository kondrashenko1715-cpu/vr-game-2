[app]
title = PicoPythonGame
package.name = picopythongame
package.domain = com.vrgame.cube
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 1.requirements: берем только базовую графику без тяжелых медиа-хвостов
requirements = python3,kivy==2.3.0,pyopengl

orientation = landscape
fullscreen = 1

# 2. РАДИКАЛЬНОЕ СОКРАЩЕНИЕ: собираем ТОЛЬКО под процессор Pico 4 (arm64-v8a)
# Отключаем сборку под старые телефоны и Intel-архитектуры, убирая 70% времени загрузки!
android.archs = arm64-v8a
android.allow_skip_x86 = True

android.accept_sdk_license = True
android.skip_update = False
android.minapi = 29
android.ndk_api = 29

[buildozer]
log_level = 2
warn_on_root = 0
