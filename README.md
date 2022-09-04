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
| Left Click   | Touch your index finger to your thumb's tip |
| Right Click   | Touch your middle finger to your thumb's tip |
| Double Left Click   | Touch your ring finger to your thumb's tip |
| Do nothing      | Touch your thumb to your rigth side of palm |
| Drag something | Touch tour index, middle, and ring finger with your pinkie pointing up |
| Scroll up and down | Touch your thumb, ring, and pinkie, with your index and middle pointing up|

To simulate depth vision of single camera, it's recomended to turn your hand slightly while doing gestures for better cursor response.
Soon I'll add photos of gestures with descriptions ;)
