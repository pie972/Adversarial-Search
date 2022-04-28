# Adversarial-Search #
## Research Paper ##

COMING SOON!

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
![image](https://user-images.githubusercontent.com/78828566/165815870-3365e791-23cb-4ab0-9ce5-a088be5d25fb.png)

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
![image](https://user-images.githubusercontent.com/78828566/165815947-47f8bdc3-5d42-4c98-bc94-369e5fbc82d8.png)
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

A detailed pdf about Improving Monte Carlo Tree Search with Artificial Neural Networks without Heuristics: github.com/pie972/Adversarial-Search/blob/main/Improving%20Monte%20Carlo%20Tree%20Search%20with%20Artificial%20Neural%20Networks%20without%20Heuristics.pdf


<br /><br />

3.	Reinforcement Learning Case <br />


<br /><br /><br />


### IV.	Prospects ### <br />

<br /><br /><br />


### V.	Conclusion <br />

As a conclusion, I will end my research paper with a statement from John McCarthy, a computer scientist, cognitive researcher, and in particular one of the founders of Artificial Intelligence: "What I believe is that if it takes 200 years to achieve artificial intelligence, and finally there is a textbook that explains how it is done; the hardest part of that textbook to write will be the part that explains why people didn’t think of it 200 years ago because we are really talking about how to make machines do things that are on the surface of our minds. It is just that our ability to observe our mental processes is not very good and has not been very good." <br /><br /><br />


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

