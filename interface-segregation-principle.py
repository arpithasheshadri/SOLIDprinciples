# Interface Segregation principle states that client should not be forced to implement an interface that it doesn't use
# or clients should not be forcec to depend on methods they do not use


# Violation of Interface Segregation Principle

# class WorkerInterface:
#     def work(self):
#         pass

#     def manage(self):
#         pass

# class Worker(WorkerInterface):
#     def work(self):
#         print("Worker is working")

#     def manage(self):
#         raise NotImplementedError("Worker can't manage!")
    
# class Manager(WorkerInterface):
#     def work(self):
#         print("Manager is working")

#     def manage(self):
#         print("Manager is managing")

# worker = Worker()
# worker.work()
# worker.manage()


# Fixed

class Workable:
    def work(self):
        pass

class Manageable:
    def manage(self):
        pass

class Worker(Workable):
    def work(self):
        print("Worker is working")

class Manager(Manageable, Workable):
    def work(self):
        print("Manager is working")

    def manage(self):
        print("Manager is managing")

worker = Worker()
worker.work()

manager = Manager()
manager.work()
manager.manage()