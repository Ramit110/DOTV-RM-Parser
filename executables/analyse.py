from mrjob.job import MRJob
from mrjob.step import MRStep
import os

class MRPreProcess(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_remove_errors),
            MRStep(reducer=self.reducer_combine_into_one)
        ]
    
    def mapper_remove_errors(self, _, line):
        yield "rest", line

    def reducer_combine_into_one(self, key, values):
        yield key, list(values)

if __name__ == '__main__':
    MRPreProcess.run()