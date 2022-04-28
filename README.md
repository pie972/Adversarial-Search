# Table of Content
<!-- toc -->
* [I.	Introduction](##i.-introduction)
* [Options](#options)
  * [template](#template)
* [API](#api)
  * [toc](#toc)
<!-- toc stop -->

## Research Paper ##

### I.	Introduction <br />

Since Artificial Intelligence's early beginnings, two-player games have been a domain of interest, and consistently delivered the following question: will computers ever be able to beat/outperform humans? Numerous researchers over time attempted various strategies/algorithms (search algorithms) to make intelligent agents reach their utility function quicker and in a more effective way than humans, which brought the point of "adversarial search" to the surface. I'm intrigued by this subject to explore to which degree have computers figured out how to outperform humans, and whether or not this domain has become obsolete. <br /><br />

Two-player zero-sum games have been a domain of interest for people even before Artificial Intelligence talks started. The name "two-player zero-sum" refers to games where there are two parties, and each move a party makes builds one party's odds of winning and diminishes the other party's odds of winning. We have seen many games like that such as Chess, Checkers, Go, Shogi, Othello, and so on. The first person to talk about a method to make computers compete with humans was the American mathematician and cryptographer Claude Elwood Shannon who introduced a paper named "Programming a Computer for Playing Chess" on March 9, 1949, at the National Institute for Radio Engineering Convention in New York. This date is 7 years before the authority discusses Artificial Intelligence, which started in 1956 at a meeting at Dartmouth College, in Hanover. Accordingly, after Artificial Intelligence was officially a field in Computer Science, the domain of research that had an interest in two-player zero-sum games got the name of "adversarial search". <br /><br />

Adversarial search refers to a set of search algorithms that are fed to a computer/machine that empowers it to take the most optimal move to win a game. In Shannon's paper in 1949, he proposed an algorithm called minimax, which we will later learn more insights about it, where he gave each chess piece a specific value; 1 point for a pawn, 3 points for a knight or bishop, 5 points for a rook, and 9 focuses for a queen; and the sum of these values is equal to the score of each side; the white pieces versus the dark pieces. Then, the algorithm takes away one score from the other, giving a representation of each board position, and making the objective for one side to maximize/boost its utility function while making the opposite side to minimize its utility function, where the name "minimax" came from: maximizing in one side and minimizing the other side. This methodology was viewed as a breakthrough and gave another new perspective of machines competing with humans; however, it didn't yield positive outcomes. The principal reason was the limited computing abilities computers had in those days, and furthermore, the branching factor (number of potential moves) for chess was considered huge for a computer to handle. Truth be told, Shannon thought of a number which is 10120 potential games that exhibit the lower bound of tree complexity of chess, making "brute force" an impossible methodology. <br /><br />

The Minimax algorithm is only one of numerous algorithms proposed to solve two-player zero-sum games, and chess is only one of the many games this domain is concerned with. Additionally, the various methods that were proposed over time have not only been restricted to board games or two-player games but also, it has extended to reach video games such as multi-player games and for military purposes, as well. All of this makes the domain of adversarial search an intriguing domain of research, and brings up many questions such as: What are the various algorithms proposed consistently and what is the objective behind each one/all of them? With the technological progression we have reached up until this point, has this domain become saturated, or is there still an opportunity to get better and further exploration? <br /><br /><br />


### II.	Linkage <br />

This paper is straightforwardly related to the third unit we have discussed in class, which is problem-solving and search where we have discussed the different search algorithms used in order to reach a solution/goal state. We have primarily discussed two algorithms in class which are the minimax and the alpha-beta pruning, while in this paper, I will be further talking about these two algorithms, alongside some of their variations, and examine the use of reinforcement learning to achieve better results. <br /><br /><br />


### III.	Approaches <br />

As mentioned previously, there are various algorithms that were explained to outperform humans in two-player zero-sum games. In the following, we will partition the approaches into three areas: fully visible case, partially visible case, and use of reinforcement learning. <br /><br />

1.	Fully Visible Case <br />
The fully visible case is when the moves of the computer and the adversary are known, and if there are various moves, then we go through them in a particular order which is the depth-first traversal order. The main algorithm we will talk about in this approach is the minimax algorithm. As we have seen previously in the introduction, the idea of the minimax algorithm was first proposed by Shannon in 1949. This algorithm utilizes straightforward approaches; it is utilized on trees, where each node is a board position, and the children of a node are the possible board positions given the possible arrangement of moves. After the tree is built, the algorithm assigns a value to every node. For that, the algorithm will take as input the board position, the depth of the tree, and the party concerned. For instance, in chess, we should determine it is the dark or the white turn (the party concerned). We will require the depth of the tree on the grounds that the algorithm is written recursively, as we can see below in Figure 1. <br /><br />
```c
function minimax(board, depth, isMaximizingPlayer):

    if current board state is a terminal state :
        return value of the board
    
    if isMaximizingPlayer :
        bestVal = -INFINITY 
        for each move in board :
            value = minimax(board, depth+1, false)
            bestVal = max( bestVal, value) 
        return bestVal

    else :
        bestVal = +INFINITY 
        for each move in board :
            value = minimax(board, depth+1, true)
            bestVal = min( bestVal, value) 
        return bestVal
```
###### Figure 1: minimax function <br />

To show how the algorithm works, we will take the chess example where the root/first move is given to the white pieces, and there are just two possible moves from each position (The branching factor is around 35, which will make the tree too huge to even consider drawing). Since the white pieces are the first pieces to begin, then they will attempt to maximize between the two values in their children’s nodes, these last options are the nodes where it is the black pieces turn to play which implies that they will attempt to minimize between the values of their two children respectively, and it goes like that. This activity of maximizing and minimizing will continue to get called until we arrive at the leaf nodes. At this point, we will have what we call a "static assessment", or in different words, we will assign a value to these board positions. This task is done in various ways, yet in the case of chess, we will utilize the same as what Shannon proposed in his paper in 1949. After that, we will go up in the tree and assign values to the parents' nodes from the maximum/minimum functions related to every single one of them. This model can be better shown in the below tree in Figure 2. <br /><br />
![](minimax%20tree%20picture.PNG)
###### Figure 2: minimax tree <br />

In this model, we are representing the white nodes with circles and the black nodes with squares. We see that the leaf nodes of the left half of the tree (we start from the left because, in this algorithm, we are using a DFS traversal as we mentioned before) have the values 10 and +∞ respectively. Since the node before them is black (black pieces turn) then, at that point, we are going to use a minimum function, thus it will pick the move that will provide the board with a value of 10. A similar logic applies if we look at the white node whose children are black nodes 10 and 5. The white node will attempt to maximize between the two values thus it will pick the move that will prompt the board with value 10. This activity keeps repeating until we arrive at the root node. The algorithm can't run until we realize what each board position in every one of these nodes is. Thus, we can expect that if we take an ordinary chess game with a depth of 10, for example, and a branching factor of 35, calculating [35^(10) – 1] isn't something easily done given the time constraint chess players have; the time varies from a contest to another, for instance, 120 mins for the initial 40 moves, and 30 mins to finish the remainder of the game, and if the time for a player expires, they lose the game as a consequence. From this clarification, we would already be able to see a few issues with the minimax algorithm, which are the depth constraint and the number of computations performed. To take care of this issue, the algorithm has been enhanced and exposed under an alternate name: alpha-beta pruning. The alpha-beta pruning algorithm utilizes a similar minimum/maximum logic but intelligently. <br /><br />
```c
function minimax(node, depth, isMaximizingPlayer, alpha, beta):

    if node is a leaf node :
        return value of the node
    
    if isMaximizingPlayer :
        bestVal = -INFINITY 
        for each child node :
            value = minimax(node, depth+1, false, alpha, beta)
            bestVal = max( bestVal, value) 
            alpha = max( alpha, bestVal)
            if beta <= alpha:
                break
        return bestVal

    else :
        bestVal = +INFINITY 
        for each child node :
            value = minimax(node, depth+1, true, alpha, beta)
            bestVal = min( bestVal, value) 
            beta = min( beta, bestVal)
            if beta <= alpha:
                break
        return bestVal
```
###### Figure 3: minimax function <br />

The code in Figure 3 shows how the algorithm works, and the "cleverness" lives in the fact that prior to computing the value of a board position, it actually looks at what is the parent node and what function is called by it. If, for instance, we have a branching factor of 2 in a chess game, and the parent node is a black node (minimizing) and its first child (white node) has a value of -4, implying that the black node will have a value of -4 or less because it will be trying to minimize and on the opposite side we have a black node that has a value of 3, then, at that point, their parent white node will pick the value of 3, thus no need to evaluate the other nodes (the subtree will be pruned). See Figure 4 below. <br /><br />
![](minimax%20v2%20tree%20picture.PNG)
###### Figure 4: minimax v2 tree <br />

See another example below (Figure 5):<br /><br />
![](minimax%20v2%20tree%20picture%202.PNG)
###### Figure 5: minimax v2 tree 2 <br />

Even after looking at alpha-beta pruning as an enhanced version of minimax, we still can see that we will have an issue assuming the tree is too deep which mainly comes from how DFS works. For that, there was another enhancement done to the alpha-beta pruning algorithm, which is using Iterative Deepening Search IDS. In this approach, it involves having the depth of the tree as a variable that continues to get incremented. Utilizing this approach alongside a Tabulation Table TT which keeps track of the visited states will expand the proficiency of the algorithm if the solution (most optimal choice) is in the shallower levels of the tree. A table that sums up the comparison among minimax and alpha-beta pruning algorithms is below in Figure 6.<br /><br />
![](tabulation%20table%20TT.PNG)
###### Figure 6: tabulation table <br />
- b is the maximum branching factor of the search tree
- d is the number of plies
- m is the maximum depth of the state space <br /><br />


2.	Partially Visible Case <br />
Since we have seen the fully visible case, let us check out the partially visible case with the Monte Carlo algorithm. The way in which this algorithm works is through four different stages as shown in Figure 7. <br />
![](Monte%20Carlo%20algorithm%20stages.PNG)
###### Figure 7: Monte Carlo algorithm stages <br />

A detailed pdf about Improving Monte Carlo Tree Search with Artificial Neural Networks without Heuristics: https://github.com/pie972/Adversarial-Search/blob/main/Improving%20Monte%20Carlo%20Tree%20Search%20with%20Artificial%20Neural%20Networks%20without%20Heuristics.pdf <br />

The first stage is called selection. In this stage, and through a policy function, we pick the following state we will go to in the search tree. The policy function can be deterministic because it gives you precisely what is the following state you ought to go to, or stochastic because it provides you with a percentage of how "good" a state is). After going through the various states and arriving at a leaf node, we move to the subsequent stage which is expansion. In this stage, we see what are the possible moves that could be made from this step and test them. This step is significant for our next stage which is simulation in which we reproduce an "artificial" game from one of the steps we expanded and see what the result from that state might be, either win or lose. In the following step, based on the outcome we got from the game simulated, we update the content of the node which we call backpropagation. In this step, we can update our policy to make it more optimal and pick the best move. Since the Monte Carlo Search MCS can take a long time to be finished, we set a timer and after the timer is finished, we pick the best path which was simulated the most and had the most elevated win rate. Although this algorithm appears to be more complex than the initial two algorithms we have seen and yields better outcomes, it has some issues. The most concerning issue this algorithm has is the decision of policy. A policy is like a heuristic, but it has a component of "randomness" the first time the algorithm runs. The answer for this issue came as the introduction of another approach that is reinforcement learning. <br /><br />


3.	Reinforcement Learning Case <br />
Reinforcement learning is an approach where the agent learns by itself what are the "best practices" based on a reward system as you can see in below Figure 8. <br /><br />
![](reinforcement%20learning%20components.PNG)
###### Figure 8: reinforcement learning components <br />

In the case of adversarial search, this approach is apparent in the MCS especially in the simulation stage and the choice of policy. In the simulation stage, the learning agent plays the game by itself and deduces the result. Additionally, based on the outcomes of the various simulations, the agent updates the policy accordingly so it can go through the optimal path in the quickest way possible. This methodology requests a lot of memory since the agent keeps track of all the board positions in all the paths. Nonetheless, the benefit to this is that at first the agent needs only the basic rules of the game, and it will learn by itself the various strategies. Additionally, the agent doesn't need any supervision, it will continue to process by itself and improve with time. The way in which this approach is described is unrealistic and too good to be true and it is. There are two main issues reinforcement learning brought which are the partial credit problem and the unique reward problem. The first issue can be perceived through this example: assuming that the most optimal path for a game X is made of 32 moves in a specific order. The agent figured out how to go through 31 of these moves in a similar order, however, in the last move it didn't pick the right one and ended up in a losing state. What occurs, for this situation, is that the agent discards all the moves and begins again from the start searching for the optimal path. <br />

This issue of "no partial credits assignment" makes the agent look for quite a long time for a single issue. The second issue we have is when there is one award only, which is by arriving at the objective. In certain games such as video games, there are no rewards for the various moves the player can make, because of the way that the objective can be reached through various ways. Thus, since reinforcement learning's "light in the darkness" is the reward, the agent gathers while picking various moves, the agent feels as if it is blind. One potential solution for this last problem is by manually programming "sub-rewards" based on the game the agent will play; however, this activity can be subjective and challenging to think of and it breaks the idea of automation which is the general purpose of adversarial search. <br /><br />


### IV.	Prospects <br />
The various approaches we have discussed have been carried out, in real life, and we will give two examples to demonstrate that: Deep Blue and AlphaGo Zero. <br />

Deep Blue is a chess computer made by the organization IBM for the sole reason for beating a chess world champion. The computer was first delivered in 1996 and then played its first game with chess world champion Gary Kasparov. Kasparov won the first match by 4 – 2. From that point, IBM updated the computer and played a rematch with the world champion Gary Kasparov in May 1997 and figured out how to beat Kasparov by 3½ – 2½; the ½ is given when the match ends in a draw. This was an enormous shock to the entire world since Deep Blue was the first machine to beat a chess world champion then. So, when IBM talked about Deep Blue at the conference, it referenced that it just used an optimized version of alpha-beta pruning in its subsequent/second match with a better heuristic to beat Gary Kasparov. These days, machines have become more complex, and the standard is for a machine to beat world champions, which can be seen in AlphaGo Zero. <br />

The alpha-beta pruning algorithm demonstrated its productivity by beating the world champion Gary Kasparov in chess, yet in another game, such as Go which has a branching factor of 250 approximately, the algorithm consumed a huge amount of time to produce the results. Rather than utilizing alpha-beta pruning, Google Deep Minds utilized the Monte Carlo Search Tree and strategies of reinforcement learning to figure out its state-of-the-art machine AlphaGo Zero. AlphaGo Zero came as the replacement or successor to AlphaGo which was launched in October 2015 and figured out how to beat a European Champion in Go with a score of 5 - 0. AlphaGo utilized data from past champions matches as a knowledge base to upgrade its search and beat its opponents. However, its replacement AlphaGo Zero was created under the motto "starting from scratch". The machine doesn't need any knowledge base beforehand, but a simple understanding of the basic rules, and in a record period of 21 days, it figured out how to beat its predecessors and some other different machines opponents and arrive at a level no human can accomplish in Go or Chess or even Shogi as shown in the below figures: Figure 9 and Figure 10. <br />

![](chess%20vs%20shogi%20vs%20Go.PNG)
###### Figure 9: Chess/Shogi/Go <br />
![](AlphaGo%20Zero%20vs%20AlphaGo%20Master.PNG)
###### Figure 10: AlphaGo <br />

From the description we gave Deep Blue and AlphaGo Zero, it appears that the domain of adversarial search is “saturated”; however, it isn't. Although the typical zero-sum games have been conquered, there are yet numerous applications where these search algorithms fall short of perfection. The model can be seen in multiplayer games or video games. The organization Open AI, which was established by Elon Musk, figured out how to make an algorithm called Open AI Five to play against Dota 2, known as MOBA videogame, world champions. It was first initialized on June 30, 2018, and after some training (almost a year of training) precisely on April 13, 2019, it figured out how to beat Dota 2 world champions in back-to-back games. This came out as an enormous astonishment since the game of Dota 2 requests collaboration from the players and it might be that a player might pick a terrible move to maximize their group's odds of winning, which was an unfamiliar domain for adversarial search which just knows the most optimal moves. Moreover, Open AI Five is not perfect because it actually loses sometimes (rarely), and there are numerous complex games that AI still can't seem to overcome making this field of exploration rich in chances of a breakthroughs. <br />

The search algorithms of adversarial search have additionally been applied to real-life situations rather than only games, for example, for military purposes. There is continuous research that is attempting to simulate real-life fights that happened before and perceive how the agent will foresee the outcome and the event succession of the way. <br /><br /><br />


### V.	Conclusion <br />

As a conclusion, I will end my research paper with a statement from John McCarthy, a computer scientist, cognitive researcher, and in particular one of the founders of Artificial Intelligence: 
> "What I believe is that if it takes 200 years to achieve artificial intelligence, and finally there is a textbook that explains how it is done; the hardest part of that textbook to write will be the part that explains why people didn’t think of it 200 years ago because we are really talking about how to make machines do things that are on the surface of our minds. It is just that our ability to observe our mental processes is not very good and has not been very good." <br /><br /><br />


### VI.	References <br />

- AlphaGo: The story so far. (n.d.). Retrieved December 08, 2021, from deepmind.com/research/case-studies/alphago-the-story-so-far
- Cercopithecin. (2018, April 20). Algorithms Explained – minimax and alpha-beta pruning. Retrieved December 03, 2021, from youtube.com/watch?v=l-hh51ncgDI
- Claude Shannon. (2021, January 06). Retrieved December 11, 2021, from en.wikipedia.org/wiki/Claude_Shannon
- Kott, A., Budd, R., Ground, L., Rebbarpragada, L., Langston, J. (2016). Decision Aids for Adversarial Planning in Military Operations: Algorithms, Tools, and Turing-test-like Experimental Validation. Cornell University. Retrieved December 09, 2021, from Doi: arxiv.org/abs/1601.06108
- Monte Carlo tree search. (2020, December 17). Retrieved December 11, 2021, from en.wikipedia.org/wiki/Monte_Carlo_tree_search 
- OpenAI. (2020, September 02). OpenAI Five. Retrieved December 10, 2021, from openai.com/projects/five/ <br /><br /><br />


### VII.	Appendices <br />
All the documents (algorithms and pictures) are uploaded on GitHub under this repository: https://github.com/pie972/Adversarial-Search <br /><br /><br />




## WHEN to Contribute? ##
You are ***always welcome*** to contribute.

## HOW to Contribute? ##
- [x] Fork this repository.
- [x] Do your desired changes.
- [x] Make a pull request.

