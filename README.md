# Bitcoin_Analysis

In this project, we focus on a crucial aspect of blockchains operations, i.e., the mining procedure. Miners are the blockchain users that ensure: (i) the validity of the transactions and (ii) the immutability of the data stored in the blockchain. In most cases, including Bitcoin and Ethereum, the security of the mining process relies on the massive amount of energy that is spent to secure the system. Only Bitcoin, each year uses more than the electrical energy consumed by Nations like The Netherlands or Pakistan to keep the data secure, i.e., immutable. This energy is consumed by miners during their mining activity. Miners are paid with rewards in cryptocurrency, so their expected profit depends on three factors:

The market value of the cryptocurrency: when the price of the cryptocurrency increases, more users are pushed to become miners. However, the system reacts to this situation by increasing the difficulty of mining and hence the security of the data.
The cost spent in electricity: if the natural resources' price rises, the profit of mining tends to become smaller and hence less miners will work to secure the network. The system react by decreasing the difficulty of the mining.
The difficulty of mining. For example, Bitcoin blockchain wants to create a block every 10 minutes on average. When there are more miners this time becomes shorter and hence the difficulty level is raised, conversely when miners leave the network, this delay increases and hence the difficulty level is decreased. 
We will study the interests and the profits of the miners in Bitcoin  (BTC) blockchain.

__________________________________________________________

[Part 1 Market Capitalization]

In the first part of the project we to study the market capitalization over the last three years of Bitcoin. Without market capitalization, the BTC would not have values and hence the miners wouldn't receive a concrete reward. Thus the blockchain wouldn't work. 

The file markt-cap.json contains the market capitalization of BTC over the last three years.  The main data you will be interested into is of dictionaries containing the pairs 'x': value, 'y':value that represent the coordinates of the point meaning that at the time corresponding to key 'x' the market capitalization was the value associated with 'y'. 

Steps:

1. Plot the market capitalization placing the time on the x-axis and the values on y-axis
2. Smooth the curve: in order to understand the behavior of the value, we want to remove the noisy fluctuations. We proceed as follows: for each time point x compute the average of the market value in the interval (x-15 days, x+15 days). For the initial/final points that do not have data (on the left and on the right, respectively), we can use only the available data. Plot the curve that we obtain.
3. Discuss the data. Read and interpret the data, convince the reader about your considerations on the capitalization. 

____________________________________________________________

[Part 2 Miners' Rewards] 

The file called miners-revenue.json contains a time serie of the revenue paid by the BTC blockchain to miners in USD (converted according to the value of BTC of the moment in which the block was mined). File called difficulty.json contains the blockchain difficulty during the same time interval. 

Steps:

1. Smooth the curve of the reward on a window of 15 days (7 days before and 7 days after)
2. Plot the curve with the reward and the curve with the difficulty
3. Let us compute the reward per difficulty dividing for each time x the reward by the current. Plot the curve (you may decide if it is better to smooth the curve or not)
4. Find the periods in which it was more convenient to perform the mining by obtaining the 10% of samples which have given the highest profits. 
