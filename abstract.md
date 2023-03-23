abstrakcia oop,
 v kotorom cozdaetsya obstraknyi klass pustyshka,
kot ukaz nazvanija metodov, kot obiazatelno nujno realizovat 
 pri sozdaniii dochernego klassa.

 chtoby realizovat abstrakciju 
 nujno importirovat abs, a nujnuje metody dekoriruem 
 v astractmethod 
 ```py
 from abc import ABC, abstractmethod 
 class AbstractAnimal(ABC):
    def speak(self):
        pass
```
    
