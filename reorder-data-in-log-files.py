class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let = []
        dig = []
        
        for log in logs:
            if log.split()[1].isdigit():
                dig.append(log)
            else:
                let.append(log)
        
        let = sorted(let, key=lambda x: (x.split()[1:], x.split()[0]))
        
        return let + dig