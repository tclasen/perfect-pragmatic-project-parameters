python_library()

pex_binary(name="bin", entry_point="greeter.main:greet", dependencies=[":greeter"])

python_tests(name="test")

python_distribution(
    name = "dist",
    provides = setup_py(
        name="greeter",
        version="0.1.0",
        description="A simple program that greets people",
    ),
    setup_py_commands=["sdist", "bdist_wheel"]

)

