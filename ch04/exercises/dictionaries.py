article = ("Today, President Biden promoted a goal to end hunger in the United States by 2030 as he delivered an address at the first White House conference on hunger since 1969, when President Richard M. Nixon pulled together a similar gathering. Biden said his administration is announcing $8 billion in public- and private-sector commitments to help reach the goal and said the push should be bipartisan and something for “the whole country to work on together.On Capitol Hill, the Senate moved a step closer Tuesday to avoiding a partial government shutdown after removing an energy-project permitting provision pushed by Sen. Joe Manchin III (D-W.Va.). Lawmakers are scrambling to pass a stopgap funding measure by Friday before leaving town")



dictionary = {"President" : "The big guy",
              "White House" : "White castle",
              "Capitol Hill" : "The place on top of the hill",
              "United States" : "Our favorite country",
              "Richard M. Nixon" : "from the Watergate scandal"
        
             }

for key,value in dictionary.items():
  article = article.replace(key, value)



print(article)
             