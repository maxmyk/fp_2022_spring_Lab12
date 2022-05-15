"""
Lab 12 task 4
simulation.py
"""

# Implementation of the main simulation class.
import random
from modules.arrays import Array
from modules.linkedqueue import LinkedQueue as Queue
from modules.simpeople import TicketAgent, Passenger


class TicketCounterSimulation:
    # Create a simulation object.
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i+1)
        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0
    # Run the simulation using the parameters supplied earlier.

    def run(self):
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)
            pass
    # Print the simulation results.

    def printResults(self):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed
        print("")
        print("Number of passengers served = ", numServed)
        print("Number of passengers remaining in line = %d" %
              len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avgWait)
    # The remaining methods that have yet to be implemented.

    def _handleArrival(self, curTime):
        """
        Handles simulation rule #1.
        Rule 1: If a customer arrives, he is added to the queue.
        At most, one customer can arrive during each time step.
        """
        if random.random() <= self._arriveProb:
            self._numPassengers += 1
            self._passengerQ.add(Passenger(self._numPassengers, curTime))
            print(f'Time\t{curTime}: Passenger {self._numPassengers} arrived.')
        pass

    def _handleBeginService(self, curTime):
        """
        Handles simulation rule #2.
        Rule 2: If there are customers waiting, for each free
        server, the next customer in line begins her transaction.
        """
        for serv in self._theAgents:
            if serv.isFree() and len(self._passengerQ) >= 1:
                psng = self._passengerQ.pop()
                serv.startService(psng, self._serviceTime+curTime)
                self._totalWaitTime += curTime - psng.timeArrived()
                print(
                    f'Time\t{curTime}: Agent {serv.idNum()}' +
                    f' started serving passenger {psng.idNum()}.')
        pass

    def _handleEndService(self, curTime):
        """
        Handles simulation rule #3.
        Rule 3: For each server handling a transaction, if the
        transaction is complete, the customer departs and the
        server becomes free.
        """
        for serv in self._theAgents:
            if serv.isFinished(curTime):
                print(
                    f'Time\t{curTime}: Agent {serv.idNum()}' +
                    f' stopped serving passenger {serv._passenger.idNum()}.')
                serv.stopService()
        pass


if __name__ == "__main__":
    # values = Queue()
    # for i in range(16):
    #     if i % 3 == 0:
    #         values.add(i)
    #     print(values)
    # print()
    # values = Queue()
    # for i in range(16):
    #     if i % 3 == 0:
    #         values.add(i)
    #     elif i % 4 == 0:
    #         values.pop()
    #     print(values)
    random.seed(4500)
    """
    Number of minutes to simulate: 25
    Number of ticket agents: 2
    Average service time per passenger: 3
    Average time between passenger arrival: 2
    """
    sim2 = TicketCounterSimulation(2, 25, 2, 3)
    sim2.run()
    sim2.printResults()
