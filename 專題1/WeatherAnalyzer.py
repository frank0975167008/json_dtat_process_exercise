import json



class data_processing:

    def __init__(self,original_data):
        self.original=open(original_data,"r")
        self.data=json.load(self.original)
        self.newdata={}

    def __del__(self):
        self.original.close()


    def display_site_name(self):
        index=0
        for site in self.data:
            print("index:",index,site["site_id"]) 
            index+=1 

    def display_site_name_and_birth_total(self):
        index=0
        for site in self.data:
            print("index:",index,site["site_id"])
            print("index:",index,site["birth_total"])  
            index+=1 

    def Decision_city_index(self,city_fist_three_name):
        fist_loop=True
        index=0
        fist_index=0
        end_index=0
        for site in self.data:
            if city_fist_three_name == site["site_id"][:3]:
                if(fist_loop):
                    fist_index=index
                    fist_loop=False
                end_index=index
            index+=1
        return fist_index,end_index
    
    def city_birth_total(self,city_fist_three_name):
        fistindex,endindex=self.Decision_city_index(city_fist_three_name)
        birth_total=0
        index=0
        for site in self.data:
            if index>=fistindex and index<=endindex:
                birth_total+=int(site["birth_total"])
            index+=1
        return birth_total
    
    def city_birth_total_boy(self,city_fist_three_name):
        fistindex,endindex=self.Decision_city_index(city_fist_three_name)
        birth_total=0
        index=0
        for site in self.data:
            if index>=fistindex and index<=endindex:
                birth_total+=int(site["birth_total_m"])
            index+=1
        return birth_total

    def city_birth_total_girl(self,city_fist_three_name):
        fistindex,endindex=self.Decision_city_index(city_fist_three_name)
        birth_total=0
        index=0
        for site in self.data:
            if index>=fistindex and index<=endindex:
                birth_total+=int(site["birth_total_f"])
            index+=1
        return birth_total

    def create_newdata(self,cityname):
        fist_three_city_name = cityname
        if fist_three_city_name[0] == "台":
            fist_three_city_name=fist_three_city_name.replace('台','臺')
        self.newdata[cityname]=self.city_birth_total(fist_three_city_name)
        self.newdata[cityname +'_boy']=self.city_birth_total_boy(fist_three_city_name)
        self.newdata[cityname +'_girl']=self.city_birth_total_girl(fist_three_city_name)