# ML_spacerat

#### Dataset:
The dataset for the training the model contain data from 1000 simulations, summing up to a total of 132462 data records for training the model.
    data.csv -> 4 cols: 
    1. input:
        - belief : 30*30,
        - ship : 30*30,
        - steps : int
    2. output:
        - remain : int


#### Hyper parameter optimization conducted for the model:
    1. No. of linear layers : 
        - Tested with 1,2,3 layers 
        - all layers has 128 nodes .
        here , least loss was found when using 2 linear layer with 128 nodes

    2. No. of nodes in the layers: 
        - 3 combinations of nodes was tested:
            - 256, 128; 
            - 128,128; 
            - 128, 64
        - the linear combination of 256, 128 nodes was found to give the minimum loss

    3. No. of convolution layers:
        - implemented using 1, 2 convolution layers 
        - the loss were comparitively same, with 2 convolution layers giving lesser loss.
        - we have chosen 1 convolution layer for our model as a fair trade of b/w complexity and loss

    4. Other parameters:
        - filters: 2,4,8,16 
            - filter of size 16 in convoultion layer gave the best results
        - learning rate: 1e-1, 1e-2,1e-3,1e-4
            - learning rate of 1e-3 gave the least loss
        - batch size : 16,32
            - batch size of 16 give the best results
 
#### Requirements:
run "pip install requirements.txt"

    libraries:
        matplotlib
        matplotlib-inline
        numpy
        pandas
        pygame
        scikit-learn
        scipy
        torch
        torchvision

#### Running the model:
- To run the model: python main.py
- The loss function curve corresponding to the executed run will be stored as "loss_curve.png"