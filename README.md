# ft_linear_regression

## About

`ft_linear_regression` is an introduction project to machine learning at 42 school.

## Installation

Clone the project

```shell
git clone https://github.com/ebaudet/ft_linear_regression.git
```

Install the required libs in the virtual env.

```sh
sh init.sh
```

## Play-it

### Predict

`predict.py` will be used to predict the price of a car for a given mileage. When you launch the program, it should prompt you for a mileage, and then give you back the estimated price for that mileage. The program will use the following hypothesis to predict the price :

![estimatePrice(mileage) = θ_0 + (θ_1 ∗ mileage)](https://latex.codecogs.com/gif.latex?estimatePrice(mileage)%20=%20%CE%B8_0%20+%20(%CE%B8_1%20%E2%88%97%20mileage))
```math
https://latex.codecogs.com/gif.latex?estimatePrice(mileage) = θ_0 + (θ_1 ∗ mileage)
```

Before the run of the training program, theta0 and theta1 will be set to 0.

Run it with :
```bash
./predict
```

To get usage :
```bash
./predict -h
```

```
usage: predict.py [-h] [-f FILE] [-t0 T0] [-t1 T1] [-v]

Predict the price for a given mileage

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Data file (default:data.csv)
  -t0 T0                θ0: if not specified, take the one found by train.py.
  -t1 T1                θ1: if not specified, take the one found by train.py.
  -v, --verbose         Verbose mode
```

### Train

`train.py` will be used to train your model. It will read the dataset file and perform a linear regression on the data.<br>
Once the linear regression has completed, it will save the variables theta0 and theta1 for use in the first program.<br>
It will be using the following formulas:

```mathematica
tmpθ_0 = learningRate ∗ \frac{1}{m}\sum_{i=0}^{m-1}(estimatePrice(mileage[i]) − price[i])
```

<img src="https://latex.codecogs.com/gif.latex?tmpθ_0 = learningRate ∗ \frac{1}{m}\sum_{i=0}^{m-1}(estimatePrice(mileage[i]) − price[i]) " />
- <img src="https://latex.codecogs.com/gif.latex?s=\text { sensor reading }  " />
- <img src="https://latex.codecogs.com/gif.latex?P(s | O_t )=\text { Probability of a sensor reading value when sleep onset is observed at a time bin } t " />

![equation](http://latex.codecogs.com/gif.latex?O_t%3D%5Ctext%20%7B%20Onset%20event%20at%20time%20bin%20%7D%20t)

```mma
https://latex.codecogs.com/gif.latex?tmpθ_1 =learningRate ∗ \frac{1}{m}\sum_{i=0}^{m-1}(estimatePrice(mileage[i]) − price[i]) ∗ mileage[i]
```

Run it with :
```bash
./train
```

To get usage :
```bash
./train -h
```

```
usage: train.py [-h] [-g] [-f FILE] [-l LEARNING_RATE] [-i ITERATIONS]
                [-t0 T0] [-t1 T1] [-v]

Train the model to found the best θ0 and θ1 to fit f(x) = θ0 + θ1x

optional arguments:
  -h, --help            show this help message and exit
  -g, --graph           Show the graph
  -f FILE, --file FILE  Data file (default:data.csv)
  -l LEARNING_RATE, --learning_rate LEARNING_RATE
                        Learning Rate (default:0.1)
  -i ITERATIONS, --iterations ITERATIONS
                        How many iterations (default:5000)
  -t0 T0                Starting θ0 (default:0)
  -t1 T1                Starting θ1 (default:0)
  -v, --verbose         Verbose mode
```


