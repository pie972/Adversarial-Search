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

As mentioned previously, there are various algorithms that were explained to outperform humans in two-player zero-sum games. In the following, we will partition the approaches into three areas: fully visible case, partially visible case, and use of reinforcement learning.<br /><br />

1.	Fully Visible Case <br />


<br /><br /><br />

2.	Partially Visible Case <br />


<br /><br /><br />

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

