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
        temp = line.replace('"', "")
        if(len(temp.split(",")) == 6):
            if(temp.split(",")[5] != " " and temp.split(",")[5] != "No loot, raid was Expired"):
                yield temp.split(",")[2] + temp.split(",")[3], temp.split(",")[4] + temp.split(",")[5]

    def reducer_combine_into_one(self, key, values):
        yield key, list(values)

if __name__ == '__main__':
    MRPreProcess.run()