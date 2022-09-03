# Hand2Mouse
Change your hand movements an gestures into cursor movements and actions!

## Instalation

### Windows 
```
git clone https://github.com/Ardiegon/Hand2Mouse.git
cd Hand2Mouse
conda env create -f env.yml
conda activate Hand2Mouse
python configure.py
python Hand2Mouse.py
```
### Linux
```
git clone https://github.com/Ardiegon/Hand2Mouse.git
cd Hand2Mouse
conda env create -f env.yml
conda activate Hand2Mouse
export PYTHONPATH=$(pwd):$(pwd)/src:$(PYTHONPATH)
python Hand2Mouse.py
```

## About

### Instruction
The moment you start the application, it will start to recording your hand.
Control your mouse with:

| Mouse       | Hand        |
| ----------- | ----------- |
| Move cursor      | Move Hand       |
| Left Click   | Touch Your index finger to your thumb's tip |
| Right Click   | Touch Your middle finger to your thumb's tip |
| Double Left Click   | Touch Your ring finger to your thumb's tip |

### In future
There are a lot of possibilities of upgrading hand gestures to controll more stuff.
Planned activities are

| Mouse       | Hand        |
| ----------- | ----------- |
| Do nothing      | Touch Your pinkie to your thumb's tip       |
| Drag something | Do Italian gesture |
| Scroll down | Point with index finger and slide down |
| Scroll up | Point with index finger and slide up |

