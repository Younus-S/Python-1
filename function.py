def my_function(country, province, city):
    print("My country is", country, "My province,", province, "and my city is", city+".")

my_function(country = "Afghanistan", province= "Balkh", city= "Dehdadi")

def my_function2(**google_map_project):
    print("Project name is,", google_map_project["projectName"])
    print("Project start date is,", google_map_project["startDate"])
    print("project budget is,", google_map_project["budget"])
    print("staff included,", google_map_project["staff"])
    print("and the country implemented in is", google_map_project["country"]+".")

my_function2(projectName="Python", startDate = "09/04/2067", budget= "$54,6546,543", staff= 54555, country= "Georgia")