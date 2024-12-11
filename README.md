# ns-cardfinder

finds the cards of your puppets

python script gets the dbid of your puppets, head to https://ducky4life.pages.dev/cardfinder/ to generate a list of links to your puppets' cards

csv input works with any input as long as the first item is the nation name, i.e. your `nation,password` list should work and the script will only parse the nation part.

## my scripts :D

<a href="https://github.com/ducky4life/ns-detag">
  <img align="center" src="https://ducky4life.vercel.app/api/pin/?username=ducky4life&repo=ns-detag&theme=algolia" />
</a>
<a href="https://github.com/ducky4life/ns-blender">
  <img align="center" src="https://ducky4life.vercel.app/api/pin/?username=ducky4life&repo=ns-blender&theme=algolia" />
</a>
<a href="https://github.com/ducky4life/ns-zombie">
  <img align="center" src="https://ducky4life.vercel.app/api/pin/?username=ducky4life&repo=ns-zombie&theme=algolia" />
</a>
<a href="https://github.com/ducky4life/ns-cardfinder">
  <img align="center" src="https://ducky4life.vercel.app/api/pin/?username=ducky4life&repo=ns-cardfinder&theme=algolia" />
</a>

# Installation

requirement: [pyNationstates](https://github.com/DolphDev/pynationstates), install by using [pip](https://pip.pypa.io/en/stable/installation/)

```
pip install nationstates
```

# Usage

1. download [main.py](https://github.com/ducky4life/ns-cardfinder/blob/main/main.py) and [puppet.csv](https://github.com/ducky4life/ns-cardfinder/blob/main/puppet.csv) (or: [download the repository](https://github.com/ducky4life/ns-cardfinder/archive/refs/heads/main.zip))
2. fill puppet.csv with your puppets
3. enter your nation name in main.py
4. run main.py (`py main.py` in the terminal)
5. choose if you would like to get the id in a text file (press enter), or a csv file in `nation,id` format
6. optionally paste the output in https://ducky4life.pages.dev/cardfinder/ and go through the generated links (or, if you want to host the site yourself: you can find the code [here](https://github.com/ducky4life/ducky4life.github.io/tree/main/cardfinder)

## Having problems/have new ideas?

Contact me on Discord, email: ducky4life@duck.com, or [telegram me on NationStates](https://www.nationstates.net/page=compose_telegram?tgto=ducky)!
