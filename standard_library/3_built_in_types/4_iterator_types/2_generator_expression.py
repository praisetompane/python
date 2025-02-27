"""    
  def generator expression: 
    - formal: expression ↦ Iterator
        - in words: an expression that returns an Iterator.

    - plain english: ???

    - intuition: ???

    - properties:
      - syntax expression for expression_variable in range(number) optional if

    - examples:
        1. without an if:
            i*i for i in range(10)
        2. with an if:  
          j**j for j in range(20) if j%2 == 0
    - use cases: ???
        
    - proof: None. It is a definition.
      
  References: ???

"""

if __name__ == "__main__":
    print(sum(i * i for i in range(10)))
    print(sum(j * j for j in range(10) if j % 2 == 0))

    # More explicit experiment that it is returning an iterator
    itr = (i * i for i in range(10))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
