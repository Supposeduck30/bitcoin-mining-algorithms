# Two Mock Bitcoin Mining Algorithms
## Two fully functional mock bitcoin mining algorithms built only using python with no external libraries. This project is meant to imitate the bitcoin mining process by replicating essential components of the process and eventually finding and outputting a hash. This project:
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


