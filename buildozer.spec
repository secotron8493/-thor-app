[app]
title = THOR
package.name = thor
package.domain = com.tuempresa

source.dir = .
source.include_exts = py,png,jpg

version = 1.0.0

requirements = python3,kivy==2.3.0,kivymd==1.2.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# Cambiado para evitar errores por API incompatible
android.api = 31

# No uses minapi muy alta si usas python3 en buildozer
android.minapi = 21

# Buildozer recomienda NDK 23b en 2024–2025 porque 25b falla
android.ndk = 23b

android.accept_sdk_license = True

# Arquitecturas correctas
android.archs = arm64-v8a,armeabi-v7a


[buildozer]
log_level = 2
warn_on_root = 1

