def magart():
    return r"""

                       .

                        .
              /^\     .
         /\   "V"
        /__\   I      O  o
       //..\\  I     .
       \].`[/  I
       /l\/j\  (]    .  O
      /. ~~ ,\/I          .
      \\L__j^\/I       o
       \/--v}  I     o   .
       |    |  I   _________
       |    |  I c(`       ')o
       |    l  I   \.     ,/
     _/j  L l\_!  _//^---^\\_
~~~~~~~~~~~Mage~~~~~~~~~~~~~~~
"""


def jesterart(score):
    return r"""
        ______________________     Q
        |                    |  ___|\_.-,
        |                    S\ Q~\___ \|
        |     SCORE:         |(   )o 5) Q
        |    NOT WORKING     |\\  \_ ()
        |                    | \'. _'/'.
        |                   .-. '-(  x< \
        |       ,o         /\, '.  )  /'\\
        |______ \'.__.----/ .'\  '.-'/   \\
                 '---'q__/.'__ ;    /     \\_
                      '---'     '--'       `"'
"""


def warart():
    return r'''
                          ,dM
                         dMMP
                        dMMM'
                        \MM/
                        dMMm.
                       dMMP'_\---.
                      _| _  p ;88;`.
                    ,db; p >  ;8P|  `.
                   (``T8b,__,'dP |   |
                   |   `Y8b..dP  ;_  |
                   |    |`T88P_ /  `\;
                   :_.-~|d8P'`Y/    /
                    \_   TP    ;   7`\
         ,,__        >   `._  /'  /   `\_
         `._ """"~~~~------|`\;' ;     ,'
            """~~~-----~~~'\__[|;' _.-'  `\
                    ;--..._     .-'-._     ;
                   /      /`~~"'   ,'`\_ ,/
                  ;_    /'        /    ,/
                  | `~-l         ;    /
                  `\    ;       /\.._|
                    \    \      \     \
                    /`---';      `----'
                   (     /
                    `---'
                    Warrior
'''


def manart():
    return r"""
     O
    /|\
    / \
"""


def map():

    return r"""
  |   |
  |   | Entrance
 _\___\___________      _______________    _______________
|               |    |               |    |               |
|  Start Room   |----|   Treasure     |---|   Trap Room   |
|      X        |    |      💰        |   |     ☠️ Trap  |
|_______________|    |_______________|    |_______________|
      |                     /---/
      |                    /---/            |||
      |                    /---/            |||
 _____|__________      ____/___/_____      _______________
|               |    |               |    |               |
|   Goblin Room |----|  Corridor      |---| Phantom Phrase|
|     👹        |    |               |   |      💀      |
|_______________|    |_______________|    |_______________|
                                              zzzz
      |                                |       zzzz
      |                                |        zzzz
 _______________      ___cccc___________   ______zzzz______
|               |    |               |    |               |
|   Git Golem   |----|   Empty Room  |----|   Boss Room  |
|     🐉        |    |               |    |     👑 Boss  |
|_______________|    |_______________|    |_______________|
"""


def side_by_side_hero(art1, art2):
    lines1 = art1.splitlines()
    lines2 = art2.splitlines()
    max_lines = max(len(lines1), len(lines2))
    for i in range(max_lines):
        line1 = lines1[i] if i < len(lines1) else ""
        line2 = lines2[i] if i < len(lines2) else ""
        print(f"{line1:<60} {line2}")
