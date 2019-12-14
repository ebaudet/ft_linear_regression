# ft_linear_regression

## About

`ft_linear_regression` is an introduction project to machine learning at 42 school.

## Installation

Clone the project

```bash
git clone https://github.com/ebaudet/ft_linear_regression.git
```

Install the required libs in the virtual env.

```bash
sh init.sh
```

## Play-it

### Predict

`predict.py` will be used to predict the price of a car for a given mileage. When you launch the program, it should prompt you for a mileage, and then give you back the estimated price for that mileage. The program will use the following hypothesis to predict the price :

```math
estimatePrice(mileage) = θ_0 + (θ_1 ∗ mileage)
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

```math
tmpθ_0 = learningRate ∗ \frac{1}{m}\sum_{i=0}^{m-1}(estimatePrice(mileage[i]) − price[i])
```

```math
tmpθ_1 =learningRate ∗ \frac{1}{m}\sum_{i=0}^{m-1}(estimatePrice(mileage[i]) − price[i]) ∗ mileage[i]
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


