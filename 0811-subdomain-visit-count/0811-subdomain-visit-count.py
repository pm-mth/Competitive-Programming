class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_paired_domain = defaultdict(int)
        
        for ch in cpdomains:
            number_of_visits, domain_name = ch.split()
            sub_domains = domain_name.split(".")
            for i in range(len(sub_domains)):
                count_paired_domain[domain_name.split(".", i)[i]] += int(number_of_visits)
                
        res = []        
        for key, val in count_paired_domain.items():
            res.append(str(val) +  " " + key)
        return res
            
        
            
            