from mrjob.job import MRJob
from mrjob.step import MRStep
import os

class MRProcessSP(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_main),
            MRStep(reducer=self.reducer_main)
        ]
    
    def mapper_main(self, key, line):
        temp = line.split("	")
        temp2 = []
        for elements in temp[1].replace('"', '').split("|"):
            if("Stat Points" in elements):
                temp2.append(elements)
            else:
                temp2.append(elements.split("/")[0].strip() + "/Stat Points: 0")

        temp3 = []
        for lines in temp2:
            temp3.append(lines.split("/")[0].strip() + "/" + filter(lambda element: "Stat Points" in element, lines.split("/"))[0].strip())
        
        yield temp[0].replace('"', ''), temp3

    def reducer_main(self, key, values):
        yield key, "|".join(list(values)[0])

if __name__ == '__main__':
    MRProcessSP.run()
