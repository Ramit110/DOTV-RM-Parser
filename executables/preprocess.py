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
        temp = line.replace('"', "").split(",")
        for lines in temp:
            lines.strip()
        if(len(temp) == 6):
            if(temp[5] != " " and temp[5] != "No loot, raid was Expired"):
                yield (temp[2].strip() + " " + temp[3]).strip(), temp[4].replace(" ", "") + " /" + temp[5]

    def reducer_combine_into_one(self, key, values):
        yield key, "|".join(values)

if __name__ == '__main__':
    MRPreProcess.run()