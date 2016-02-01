Uneven Coins
============

You are given three pairs of coins: A and A', B and B', and C and C'. Within each pair, one coin is fair, and one coin is counterfeit and slightly lighter. (So, there are 3 light and 3 heavy coins in total.) Your goal is to determine which coin in each pair is the light one, with only two uses of a balancing scale.

You may put any set of coins on one side of the scale, and any other set of coins on the other side, and the scale will tip one way or the other or stay perfectly balanced if both sides are equal. Doing this only twice, how can you determine all three light coins?

>!1. weigh A and B vs B' and C'

>!If A and B were heavier, then there are three possibilities:
>!i) A and B both heavy; B' and C' both light
>!ii) A and B both heavy; B' light and C' heavy
>!iii) A light and B heavy; B' and C' both light

>!We need some test to differentiate between these possibilities in this case.

>!2a. If A and B were heavier: ;wip: finish this

>!If it was equal, there are two possibilities:
>!i) A heavy and B light; B' heavy and C' light
>!ii) A light and B heavy; B' light and C' heavy

>!If B' and C' were heavier, then there are three possibilities (note that these are the mirror image of the first case above)
>!i) A and B both light; B' and C' both heavy
>!ii) A heavy and B light; B' and C' both heavy
>!iii) A and B both light; B' heavy, C' light

