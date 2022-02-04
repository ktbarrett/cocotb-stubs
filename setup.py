import pathlib

from setuptools import setup

root = pathlib.Path(__file__).parent.resolve()


if __name__ == "__main__":
    setup(
        name="cocotb-stubs",
        version="0.dev1",
        description="Python typing stubs for cocotb, pygpi, cocotb_bus, and related packages",
        long_description=(root / "README.md").read_text(encoding="utf-8"),
        long_description_content_type="text/markdown",
        url="https://github.com/ktbarrett/cocotb-stubs",
        author="Kaleb Barrett",
        author_email="dev.ktbarrett@gmail.com",
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
            "Programming Language :: Python :: 3",
        ],
        package_dir={"": "src"},
        packages=["cocotb-stubs"],
        package_data={
            "cocotb-stubs": [
                path.as_posix()
                for path in (root / "src" / "cocotb-stubs").glob("**/*.pyi")
            ]
        },
        install_requires=["cocotb>=1.6<1.7"],
    )
