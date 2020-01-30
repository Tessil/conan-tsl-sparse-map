from conans import ConanFile, CMake, tools
import os

class TslSparseMapConan(ConanFile):
    name = "tsl-sparse-map"
    version = "0.6.2"
    license = "MIT"
    description = "C++ implementation of a memory efficient hash map and hash set."
    homepage = "https://github.com/Tessil/sparse-map"
    url = "https://github.com/Tessil/conan-tsl-sparse-map"
    exports = "LICENSE"

    def source(self):
        tools.get("%s/archive/v%s.tar.gz" % (self.homepage, self.version))

    def package(self):
        self.copy("LICENSE", dst="licenses", keep_path=False, ignore_case=True)
        
        cmake = CMake(self)
        cmake.configure(source_folder="sparse-map-%s" % (self.version))
        cmake.install()

    def package_id(self):
        self.info.header_only()
