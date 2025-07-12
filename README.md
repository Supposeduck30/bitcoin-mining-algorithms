# Two Mock Bitcoin Mining Algorithms
## Two fully functional mock bitcoin mining algorithms built only using python with no external libraries which replicates actual bitcoin mining algorithms  
This project is meant to imitate the bitcoin mining process by replicating essential components of the process and eventually finding and outputting a hash. This project:
- Incorporates Double SHA-256 hashing (as used in actual Bitcoin mining)
- Converts difficulty bits into a full target number
- Builds a fake block header with version, previous hash, Merkle root, timestamp, bits, and nonce
- Tries different nonces until the hash is below the target
- Shows the mining process and prints the valid hash

#### 🔐 The realistic algorithm:
- Incorporates the actual Bitcoin difficulty bits (as of June 2025)
  - This means you will most likely never find a hash with the realistic algorithm, since the difficulty is very high
  - The average time to find a vald hash in this algorithm with a regular CPU is ~300 million years
    - That's why real mining algorithms employ networks with other bitcoin miners who share the result, and they have very powerful computers which use a lot of energy
  - If by a miracle you find an actual hash within a short amount of time (the chances are astronomically low to find one), thats actually a valid bitcoin hash
    - Sadly, it would have no value since it wasn't produced with a legitimate mining network, but it would match a valid hash that would be worth money if found by real mining algorithms
    
#### ⚡️ The simplified algorithm:
- Incorporates a much lower difficulty than the actual bitcoin one
  - This means that it will eventually find a hash within 1-40s
- It technically finds a valid hash which may even be a real hash
  - However, that hash will never be found by miners because the minng network has a requirement of a higher difficulty, but it could still technically be a valid hash

## 🕓 Version History
### 1.0.0
- Terminal based
- Every 1,000,000 attempts it hasnt found a hash, it prints ("Still mining")
- Once found, it prints ("Found hash") and prints the hash with the nonce

## 🚀 How to run 

1. Make sure python is installed on your device

2. Download the script
   - If you have git installed, run: "git clone https://github.com/Supposeduck30/bitcoin-mining-algorithms.git"
   - Or, click the green code button and press "downoad zip", and then extract it

3. Inside of the directory, open the file "simplified-crypto-mining-algorithm.py" or "realistic-crypto-mining-algorithm.py" (whichever one you want to run)

4. Run it by inputting into command prompt/terminal "python file name"

5. ALTERNATIVE - Paste the code into an online python compiler

## 🔧 How to tweak this project for your own use 
1. Fork the repository
   
2. Clone the fork
   
3. Make your changes to the code
   
4. Commit and push your changes to the fork
   
5. OPTIONAL - Create a pull request if you want the main repository to change the code with what you changed 


## ⛏️ How it works 
#### 1. Sets up the block data 
- The algorithm creates a fake block header with fixed parts like version, previous hash, Merkle root, and timestamp, essentially replicating the bitcoin mining network
  
Version - Block format version number, which tells the network what rules to use
  Previous hash - The hash of the previous block in the chain
  Merkle root - A single hash representing all the transactions in this block
  Timestamp - The time the block was created, as a timestamp

#### 2. Picks a difficulty 
- It decides how hard it should be to find a valid hash (The actual bitcoin difficulty is in the realistic algorithim, while a very easy difficulty is in the simplified version)

#### 3. Tries a random nonces 
- It picks random numbers called nonces and adds them to the block header (random 32-bit number that is used a sort of random seed which helps find the hash)

#### 4. Hash the header twice 
- It runs the block headertwice through the hash function

#### 5. Check the hash
- It looks at the hash to see if it meets the difficulty

#### 6. Repeat until success
- It goes through millions of attempts 

## Screenshot 
### ![image](https://github.com/user-attachments/assets/db74480e-9c2f-4585-ba7e-755c3a73413a)


## ⚠️ Warnings/Known Issues
- Does not use real bitcoin transactions
- Nonces are randomly chosen instead of incremented
- For the simplified one, the difficulty is too low to represent real mining difficulty
- For the realistic one, the difficulty is normal which makes it near impossible for a normal computer to find a hash
- Has fake block data
