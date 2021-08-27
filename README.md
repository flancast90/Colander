# Colander
A custom prime algorithm, implementation, and performance code &amp; review

<br />

### Pseudocode Algorithm 
```
1. given a number of primes to find, the following steps are completed: 
2. if number divided by 2 gives a remainder of 0, number is not prime, move to next number
3. If number divided by 3, 5, and 7 does not have a remainder of 0, continue. 
Otherwise goto next number
4. If number is less than or equal to 11, add to primes list (primes list already contains 2, 3, 5, 7)
5. If it is greater than 11, check if any of the numbers inside primes list can go into number with 
remainder 0. If one or more can, number is composite.
6. Number is prime.
```

<br />

### Usage/Install

Using a terminal of your choice, ``cd`` into ``the Colander-main/src`` folder. Assuming you have python installed, you should be able to start the prime-finding process by
```bash
python colander.py
```

<br />

### Performance
[Imgur](https://i.imgur.com/MYi83Fr.png)

<br />

### License
MIT
