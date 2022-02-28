import numpy as np

def sigmoid(z):
    return 1/(1+np.exp(-z))

def sigmoid_prime(z):
    return sigmoid(z)*(1-sigmoid(z))


def reset_climber(climber):
    climber.position_index =np.random.randint(climber.step,climber.terrain.shape[1]-climber.n_input-climber.step-1)#i%975 + 3 #
    climber.old_input = climber.terrain[0,climber.position_index:climber.position_index + climber.n_input].reshape(climber.n_input,1)
    climber.input = climber.terrain[0,climber.position_index:climber.position_index + climber.n_input].reshape(climber.n_input,1)
    climber.output = None
    climber.y = 0
    
    climber.position_switch_counter = climber.position_switch_counter + 1
    #print("-------NEW POSITION-------")
    
    
    
def linear_equation_solver(x,y,climber,weight):
    w = weight
    ws = []
    while(True):
        #can make this make efficient.to calculate just one new cost
        costs = get_costs(w,climber.n_input,x,y)
        #1.calculate 1 cost
        output = climber.get_output(costs)
        #2.forward propagation
        #3.No back brop.Direct gradient descent
        if output>0.5:
            w = w + 1
        else:
            w = w - 1
            
        ws.append(w)
        
        
        if(len(ws)>10):
            #Can make this more efficient    
            p = np.mean(ws[-10:]) + np.std(ws[-10:])
            n = np.mean(ws[-10:]) - np.std(ws[-10:])
                
            if (n<=ws[-1]<=p):
                print("Correct weight is :",(w+climber.n_input/2 -1))
                
                return ws

def get_costs(index,n_input,x,y):
    
    start = index
    end = index + n_input
    
    x = x[10:1000]
    y = y[10:1000]
    
    weights = np.arange(start,end,1).reshape(-1,1)
    x = x.reshape(1,-1)
    m = np.matmul(x.T,weights.T) - y.reshape(-1,1)
    sqr = np.square(m)
    costs = np.sum(sqr,axis = 0)
    #print(costs)
    #plt.scatter(np.arange(costs.shape[0]),cost)
    return costs.reshape(-1,1)