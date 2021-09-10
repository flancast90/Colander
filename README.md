# Colander
A custom prime algorithm, implementation, and performance code &amp; review

<br />

### Pseudocode Algorithm 
```
1. given a number of primes to find, the following steps are completed: 
2. if number divided by 2 gives a remainder of 0, number is not prime, move to next number
3. If number divided by 3, 5, and 7 does not have a remainder of 0, continue. 
Otherwise number is not prime.
4. If number is less than or equal to 11, add to primes list (primes list already contains 2, 3, 5, 7)
5. If it is greater than 11, check if any of the numbers inside primes list which are less than the
square root of number can go into number with remainder 0. If one or more can, number is composite.
6. If everything is true, number is prime.
```

<br />

### Usage/Install

Using a terminal of your choice, ``cd`` into the ``Colander-main/project`` folder. Assuming you have python installed, you should be able to start the prime-finding process by
```bash
python3 miner.py [numer to iterate (eg. 1000]
```

Your primes will then show up in the ``project/primes.py`` file, and will be used every time you run the ``miner.py`` file to improve performance!

<br />

### Performance
<img src="https://i.imgur.com/BUOz9sV.png" style="background-color:white"/>

<br />

### License
MIT
