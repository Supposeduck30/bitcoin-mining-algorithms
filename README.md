# Two Mock Bitcoin Mining Algorithms
## Two fully functional mock bitcoin mining algorithms built only using python with no external libraries. 
This project is meant to imitate the bitcoin mining process by replicating essential components of the process and eventually finding and outputting a hash. This project:
- Incorporates Double SHA-256 hashing (as used in actual Bitcoin mining)
- Converts difficulty bits into a full target number
- Builds a fake block header with version, previous hash, Merkle root, timestamp, bits, and nonce
- Tries different nonces until the hash is below the target
- Shows the mining process abd prints the valid hash
#### The realistic algorithm:
- Incorporates the actual Bitcoin difficulty bits (as of June 2025)
  - This means you will most likely never find a hash with the realistic algorithm, since the diffulty is very high
  - The average time to find a vald hash in this algorithm with a regular CPU is ~300 million years
    - That's why real mining algorithms employ networks with other bitcoin miners who share the result, and they have very powerful computers which use a lot of energy
  - If by a miracle you find an actual hash within a short amount of time (the chances are astronomically high), thats actually a valid bitcoin hash
    - Sadly, it would have no value since it wasn't produced with a legitimate mining network, but it would match a valid hash that would be worth money if found by real mining algorithms
    
#### The simplified algorithm:
- Incorporates a much lower difficulty than the actual bitcoin one
  - This means that it will eventually find a hash within 1-40s
- It technically finds a valid hash which may even be valid 
  - However, that hash will never be found by miners because the minng network has a requirement of a higher difficulty, but it could still technically be a valid hash
 
## How to run 

1. Make sure python is installed on your device

2. Download the script
   - If you have git installed, run: "git clone https://github.com/Supposeduck30/bitcoin-mining-algorithms.git"
   - Or, click the green code button and press "downoad zip", and then extract it

3. Inside of the directory, open the file "simplified-crypto-mining-algorithm.py" or "realistic-crypto-mining-algorithm.py" (whichever one you want to run)

4. Run it by inputting into command prompt/terminal "python "file name")

5. ALTERNATIVE - Paste the code into an online python compiler

## How it works 
#### 1. Sets up the block data 
- The algorithm creates a fake block header with fixed parts like version, previous hash, Merkle root, and timestamp, essentially replicating the bitcoin mining network
