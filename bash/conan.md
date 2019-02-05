# Documentation

* https://docs.conan.io
* https://docs.conan.io/en/latest/reference.html
* https://docs.conan.io/en/latest/reference/commands.html

# Installation with vagrant

## From Host

```sh
$ mkdir vagrant_conan && cd $_
$ vagrant init debian/stretch64
$ vagrant up
$ vagrant ssh
```

## From Vagrant Box

```sh
$ sudo aptitude update && sudo aptitude upgrade -y
$ sudo aptitude install python3-pip python3-wheel
$ pip3 install conan
$ sudo ln -s ~/.local/bin/conan /usr/local/bin/conan
$ conan --version
WARN: Remotes registry file missing, creating default one in /home/vagrant/.conan/registry.json
Conan version 1.11.2
```

# Manipulate Conan from Vagrant Box

```sh
$ sudo aptitude install cmake g++ git
```

```sh
$ git clone https://github.com/memsharded/hello.git && cd hello
$ conan new Hello/0.1
File saved: conanfile.py
```
Then adapt conanfile.py :
```py
$ cat conanfile.py
from conans import ConanFile, CMake, tools


class HelloConan(ConanFile):
    name = "Hello"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = [
            "CMakeLists.txt",
            "*.cpp",
            "*.h",
            ]

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
```

Build package with conan :
```sh
$ conan create . Hello/testing
```
