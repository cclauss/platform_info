# Original is at https://github.com/cclauss/Ten-lines-or-less

import inspect
import platform


def info(name, value):
    if name[0] != '_' and callable(value):
        try:
            value = value()
            if str(value).strip("( ,')"):
                return ('{:>21}() = {}'.format(name, value))
        except TypeError:
            pass

    return ''


def get_platform_info():
    lines = (info(name, value) for name, value in inspect.getmembers(platform))
    return '\n'.join(line for line in lines if line)


if __name__ == '__main__':
    print(get_platform_info())
    import sys
    print(sys.platform, sys.version)
