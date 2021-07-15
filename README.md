# Deconstruction_plus
Mod for Cataclysm-DDA that adds more deconstruction options and a power tool.

I got fed up that the only way to make changes to established houses was to BREAK ALL THE THINGS, when we 
have a suite of power tools and plenty of time (this was causing roof collapse ~80% of the time), so I made 
this mod to stop myself jumping into debug mode to fix the issue.

Fair warning, deconstruction of buildings is aimed to be a mid-game activity, while modifying existing 
buildings to suit base needs, and as such, most recipes require more tools to deconstruct than you'd use to 
construct them and a decent whack of time. The trade off is that you don't risk roof collapse and the 
floor tile is more or less preserved.

## Currently allows deconstruction of (most)
- empty window frames
- floors
- linoleum tiles
- concrete floors
- walls
- wooden walls
- brick walls
- concrete walls
- roads / pavement / zebra crossings
- metal doors
- rebar cages
- concrete columns
- half complete walls

## Adds this powertool
- Masonry Saw (and an easy recipe to create it)

## For Cataclysm Bright Nights
Download the mod as per normal, then... 

DELETE the following files:
- construction_recipes.json
- construction_groups.json
- modinfo.json

RENAME the files with .BN in the filename by replacing .BN with .json.
- construction_recipes.BN -> construction_recipes.json
- modinfo.BN -> modinfo.json 

Please note, until the process for making BN stuff is automated, the files WILL be behind the CDDA variants.