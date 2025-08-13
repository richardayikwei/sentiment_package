# Sentiment 
A package for analysing swap related messages.

## wsentiment subpackage
This subpackage analyses WhatsApp related messages for sentiment.

## Using wsentiment

import by using
```
from sentiment.wsentiment import wsentiment_score
```
wsentiment_score takes only string inputs.

-example

```
wsentiment_score('kofi has lights out')
>> -2
```