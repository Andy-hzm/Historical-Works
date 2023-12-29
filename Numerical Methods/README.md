# Numerical Methods
This part of the repository stores some computational projects. Here are some explanations.
## 1. Video Background Extraction
**Key Techniques:** *SVD, Power Iterations, OOP, Python*

Extract a fixed background picture from a moving video using SVD and Power Iteration
## 2. Single Server Priority Queue System
**Key Techniques:** *Stochastic Simulation, OOP, Python*

Simulation of a stochastic process.
  
For the single-server queuing system, suppose that each customer has a priority level, 1 or 2, which is known upon their arrivals. Upon completing
service for a customer, the server chooses from the queue with the following non-preemptive order:

  1. choosing a priority level 1 customer with the earliest arrival time if there is any;
  2. choosing a priority level 2 customer with the earliest arrival time if there is no priority level 1 customer.
     
Once a customer is served, the service will not be interrupted until finished, even when there is a customer with higher priority waiting in the queue. Suppose the customer with priority level 1 and 2 arrives according to a Poisson process with rate λ1 = 0.1 and λ2 = 0.2, respectively. The service time is a constant time, for level-1 customer t1 = 0.2 and for level-2 customer t2 = 3. Design a discrete-event simulation algorithm to simulate this priority queue and implement it in Python. Estimate the average delay of two types of customers in long run. 
