#!/usr/bin/python3

from os import remove
import json

group_file = "construction_groups"
recipe_file = "construction_recipes"
modinfo_file = "modinfo"
not_in_bn = ["t_thconc_r", "t_zebra"]

with open("./" + group_file + ".json", "r") as read_gfile:
    groups = json.load(read_gfile)

with open("./" + recipe_file + ".json", "r") as read_rfile:
    recipes = json.load(read_rfile)

with open("./" + modinfo_file + ".json", "r") as read_mfile:
    modinfo = json.load(read_mfile)

bn_recipe_file = recipe_file + ".BN"
bn_modinfo_file = modinfo_file + ".BN"

ident = modinfo[0]["id"]
del modinfo[0]["id"]
modinfo[0]["ident"] = ident

with open(bn_modinfo_file, "w") as data_mfile:
    json.dump(modinfo, data_mfile, indent=4)

for recipe in recipes:
    con_group = recipe["group"]
    del recipe["group"]
    for group in groups:
        if (con_group == group["id"]):
            description = group["name"]
        recipe["description"] = description

for recipe in recipes:
    kill_recipe = 0
    for remove_me in not_in_bn:
        if (recipe["pre_terrain"] == remove_me):
            kill_recipe = 1
    if (kill_recipe):
        recipes.remove(recipe)
            


with open(bn_recipe_file, "w") as data_rfile:
    json.dump(recipes, data_rfile, indent=4)

#print ( json.dumps(modinfo, indent=4) )
#print ( json.dumps(groups, indent=4) )
#print ( json.dumps(recipes, indent=4) )

quit()
