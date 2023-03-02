""" Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

ARGS = ['ping', 'yandex.ru']
yandex_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in yandex_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

ARGS = ['ping', 'youtube.com']
youtube_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in youtube_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))