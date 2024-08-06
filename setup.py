from setuptools import setup, find_packages

setup(
    name="Hand2Mouse",
    version="0.1.0",
    description="control mouse with your hand",
    author="Oskar Bartosz",
    packages=find_packages("src"),  # Find packages in src directory
    package_dir={"": "src"},  # Treat "src" directory as the source of packages
    install_requires=[
        'matplotlib',
        'numpy',
        'mouse',
        'pyautogui',
        'mediapipe',
        'pynput',
        'opencv-python==4.6.*'
    ],
    entry_points={
        "console_scripts": []
    },
)