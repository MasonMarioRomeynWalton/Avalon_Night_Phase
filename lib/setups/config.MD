# Config file docs
The config files for the night phase is built to try to be generic and applicable to many different use casenarios.

The file is a big object that describes the setup.
It is split into three main sections. 

## Meta data
The meta data which for now only consists of the number of people in the setup. For example if there were 10 people to distribute roles to the config file would start with the following coe
```
{
    "people": 10,
    ...
}
```
*Note it does not have to be at the top but it helps readability to adhere to this order*

This is necessary as the number of "cards" or roles being handed out may be a different amount than the actual number of players. Currently the cards are dealt out one by one until they are out. 

*Note the randomization is done by shuffling the players so if multiple roles exist and they are not divided equally by the number of players who gets the extra ones will be random and independent amongst different roles*

## Cards
These can be thought of as the roles handed out that tells each person their own roles or characters. For many use cases only one set of cards is necessary you can use as many as you want. They will each be distributed independently and as discussed above they will be handed out until they are done.

The "cards" attribute of the object consists of a list of sets of cards to be handed out. Each of these is itself an array of roles to be handed out in each set. The layout would look something like
```
{
    ...
    "cards" = [
        [
            { ... },
            { ... },
            ...
        ],
        [
            { ... },
            { ... },
            ...
        ],
        ...
    ]
}
```
As you can see each of the inner lists is a set of cards to be handed out together and each of the elements with curly braces corresponds to one role or card in each set which will be handed out.

Each role consists of multiple parts. These are the text, the properties, and certain attributes. Text is the easiest of them and is what the text of the card saying what card it is says. Properties are things that one can have or not have and attributes a generic tag with a specific answer for this character.

Properties are used for deciding who sees. Attributes are often usefull across different sets of cards. Someone seeing another person can see the attribute of another card the person has.

*Usually it is advisable to use an attribute for cards with equal number of players as cards and to give an attribute to each card. This is as an attribute can only have one answer and should have an answer for all cards for most cases.*

We will look at an example layout. Consider a game with good and evil characters where one player at random gets a "special power". Additionally there is a good character called "Seer" that sees who gets the "special" and their alignment and alignments are tied to characters. For handing out the "special power" we could have a set of cards only containing that
```
{
    ...
    "cards" = [
        [
            {
                "text" : "special power",
                "prop" : ["special power"]
            },
        ]
    ]
}
```
Note that it has the property special power so it can be seen. It is often a good idea to have a property for each card so if you want to add something in the future that sees that card specifically it is easy to add.

Then we can add the characters. We will give each of them the attribute "alignment" which will be "good" or "evil". The "Seer" who will see the person with the property special power and therefore the person who has the card will see what their attribute for alignment is. For the cards this will look like the following
```
{
    ...
    "cards" = [
        [
            {
                "text" : "special power",
                "prop" : ["special power"]
            },
        ],
        [
            {
                "text" : "Seer",
                "prop" : ["Seer", ...],
                "alignment" : "good"
                ...
            },
            ...
        ]
    ]
}
```
Note as seen there could be other properties we want in the array of "prop" and there could be any amount of attributes with different names.


## Knowledge
This secion describes what characters see others. You set up the mechanism to describe different characters in the "cards" section but this section is where you use this to describe the knowledge characters have. The knowledge is a list. Each element describes a some characters seeing others. It has three sections being "needs", "sees", and "info" all of which are lists.
```
{
    ...
    "knowledge" :
    [
        {
            "needs" : [ ... ],
            "sees" : [ ... ],
            "info" : [ ... ]
        }
    ]
}
``` 
Both needs and sees should be a list of properties and info should be a list of attributes. It should be read as all people with all of the properties in "needs" see all people with all of the properties in "sees", and they see what their qualities are for each of the attributes in info. 

*Note "needs" and "sees" are mandatory but "info" can be omitted. If you want everyone to see something simple make the needs list empty*

Let us make the knowledge part of our example above. As a reminder we had a game with good and evil characters, a special power being handed out independently, and one of the good character called "Seer" sees who has the special power and sees their alignment. For this we would add the following entry in the knowledge
```
{
    ...
    "knowledge" :
    [
        {
            "needs" : [ "Seer" ],
            "sees" : [ "special power" ],
            "info" : [ "alignment" ]
        }
    ]
}
``` 
Since we gave the Seer and special power cards the "Seer" and "special power" property the person who draws the Seer sees who has the special power. They also see what their attribute "alignment" is which will be "good" or "evil".
