# encoding:utf-8


class BackendDeveloper(object):
    company = "LPS Ingenieria"
    team = "LPStech"
    job_url = "http://lpsingenieria.com/buscamos-desarrolladores-web/"

    def __init__(self, first_name, last_name, email, knowledges):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.knowledges = knowledges

        self.key_requirements = ('python', 'django', 'motivation', 'software')
        self.other_requirements = ('djangorestframework', 'git', 'teamwork', 'linux', 'REST', 'star wars')

    @property
    def score(self):
        """
            Write the code to match the perfect candidate with the requirements above!
                Output should be 10 or more for perfect matches
                Output should be 0 for candidates that do not fulfill any requirements
        """
        counter = 0
        
        for knowledge in self.knowledges:
            if knowledge in (self.key_requirements[:] + self.other_requirements[:]): #it works without [:] too
                counter += 1
                
        return counter

    def i_am_ready(self):
                
        if self.score > 7:
            print ("Make a pull request with this code, we want you!")
        else:
            print ("Wait, you have created successfully the score method? Then make a pull request, we want you!")

if __name__ == "__main__":
    """
        Write the code to create yourself, a BackendDeveloper, and let us know you are ready!
    """
    my_knowledges = ['python', 'django', 'motivation', 'software', 'git', 'teamwork', 'linux', 'REST', 'star wars', 'lotr']
    Dev = BackendDeveloper("Adrian", "Pizarro", "adrianpizarroserrano@hotmail.com", my_knowledges)
    Dev.i_am_ready()

